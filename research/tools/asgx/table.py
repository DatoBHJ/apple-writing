#!/usr/bin/env python3
"""Draft the 'avoid -> use' substitution table from parsed ASG entries."""
import json, re

ENTS = json.load(open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json"))

def clean(s):
    s = re.sub(r"\s+", " ", s).strip()
    return s

def esc(s):
    return s.replace("|", "\\|")

def first_sentence(s):
    m = re.match(r"(.+?\.)(?:\s|$)", s)
    return m.group(1) if m else s

rows = []
for e in ENTS:
    head, body, page = e["head"], clean(e["body"]), e["page"]
    kind = use = None
    m = re.match(r"Don’t use;\s*(?:instead,\s*)?use (.+?)\.", body)
    if m: kind, use = "head", m.group(1).strip()
    if not kind:
        m = re.match(r"Don’t use\.\s*Use (.+?)\.", body)
        if m: kind, use = "head", m.group(1).strip()
    if not kind:
        m = re.match(r"(?:Avoid|Don’t use)\.\s*Use (.+?)\.", body)
        if m: kind, use = "head", m.group(1).strip()
    if not kind:
        m = re.match(r"Avoid;\s*instead,\s*use (.+?)\.", body)
        if m: kind, use = "head", m.group(1).strip()
    if not kind:
        m = re.match(r"Not (.+?)\.", body)
        if m: kind, use = "not", head
    if not kind:
        m = re.match(r"(?:Don’t use|Avoid)\b(.*)", body)
        if m:
            kind = "head"
            rest = m.group(1)
            u = re.search(r"(?:,|;)\s*(?:instead,?\s*)?use (.+?)\.", rest)
            if u: use = u.group(1).strip()
    if kind == "head":
        rows.append({"avoid": head, "use": use or "", "quote": body, "page": page})
    elif kind == "not":
        rows.append({"avoid": use, "use": head, "quote": body, "page": page})

# in-body prohibitions naming other terms
for e in ENTS:
    head, body, page = e["head"], clean(e["body"]), e["page"]
    if re.match(r"(?:Don’t use|Avoid|Not )", body):
        continue
    found = []
    for m in re.finditer(r"(?:Don’t use|don’t use|avoid|Avoid)\s+(?:the word\s+|the term\s+)?([A-Za-z][\w’'./+-]*(?:\s+[A-Za-z][\w’'./+-]*){0,3})", body):
        if m.group(1).lower() in ("when", "in", "as", "to", "the", "this", "it", "them", "these", "such", "for"):
            continue
        found.append(m.group(1).strip())
    for m in re.finditer(r"(?:Don’t use|don’t use|avoid|Avoid)\s+([a-z][\w-]*(?:\s+[a-z][\w-]*){0,2})\s+as (?:a|an) (verb|noun|adjective)", body):
        found.append(m.group(1).strip() + f" (as a {m.group(2)})")
    if found:
        rows.append({"avoid": "; ".join(dict.fromkeys(found)), "use": "", "quote": body, "page": page})

# dedupe by avoid+page
seen, out = set(), []
for r in rows:
    k = (r["avoid"], r["page"])
    if k in seen: continue
    seen.add(k); out.append(r)
out.sort(key=lambda r: (r["page"]))
with open("/Users/hajunbae/dev/Skills/.research-tools/asgx/table-draft.md", "w") as f:
    for r in out:
        f.write(f"{r['avoid']}\t{r['use']}\t{r['quote']}\t{r['page']}\n")
print("rows:", len(out))
