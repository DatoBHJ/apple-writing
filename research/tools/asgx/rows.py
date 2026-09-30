#!/usr/bin/env python3
"""Produce substitution rows (avoid / use / note) from ASG entries."""
import json, re, sys

ENTS = json.load(open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json"))

FUNC = set("a an the as in on at by for from with when that this these those such any more it them us me if to of and or but".split())
POS = re.compile(r"\s*\((?:n|v|adj|pred\. adj|adv|pl|sing|abbr)\.?[^)]*\)\s*$")

def bare(head):
    return POS.sub("", head).strip()

def sents(body):
    # split keeping it simple; protect common abbreviations
    tmp = body.replace("e.g.", "e<g>").replace("i.e.", "i<i>").replace("etc.", "e<t>")
    tmp = tmp.replace("Inc.", "I<n>").replace("in.", "i<n>").replace("vs.", "v<s>")
    out = re.split(r"(?<=[.!?])\s+(?=[A-Z“\[])", tmp)
    return [s.replace("e<g>", "e.g.").replace("i<i>", "i.e.").replace("e<t>", "etc.")
             .replace("I<n>", "Inc.").replace("i<n>", "in.").replace("v<s>", "vs.") for s in out]

def directive_sents(body):
    out = []
    for s in sents(body):
        if re.search(r"Don’t use|don’t use|\bAvoid\b|\bavoid\b|Don’t say|Don’t abbreviate|Don’t write|Don’t call|Don’t refer|Don’t precede|Don’t shorten|Don’t include|Don’t form|Not ", s):
            out.append(s)
    return out

rows = []
for e in ENTS:
    head, body, page = e["head"], re.sub(r"\s+", " ", e["body"]).strip(), e["page"]
    ds = directive_sents(body)
    if not ds:
        continue
    # avoid column
    avoid = bare(head)
    # "Not X." pattern at start -> X is wrong, head is right
    m = re.match(r"^Not (.+?)\.", body)
    if m:
        rows.append({"avoid": m.group(1).strip(), "use": bare(head),
                     "note": "Not " + m.group(1).strip() + ".", "page": page,
                     "head": head, "kind": "spelling"})
        continue
    if not re.match(r"(Don’t use|Avoid|Don’t say|Don’t abbreviate|Don’t write|Don’t call|Don’t refer|Don’t precede|Don’t shorten)", body):
        # in-body directive: try to pull the banned phrase
        mm = re.search(r"(?:Don’t use|don’t use|\bavoid\b|\bAvoid\b)\s+(?:the word\s+|the term\s+)?([^.]{2,60}?)\s*\.", body)
        if mm:
            cand = mm.group(1).strip()
            first = cand.split()[0].lower().strip("’'")
            hw = set(re.findall(r"[a-z]+", bare(head).lower()))
            cw = set(re.findall(r"[a-z]+", cand.lower()))
            if (first not in FUNC and len(cand.split()) <= 6 and not (cw & hw)
                    and not re.match(r"^(as|to|when|that|this|these|such|any|more|it|them|us|me|them)\b", cand)):
                avoid = cand
    # use column
    use = ""
    for s in ds:
        m = re.search(r"(?:^|[,;]\s*)(?:instead,?\s*)?use (.+?)\.?$", s)
        if m and len(m.group(1)) < 120:
            use = m.group(1).strip().rstrip("."); break
        m = re.search(r"\buse (.+?) (?:instead|rather than)\b", s)
        if m:
            use = m.group(1).strip(); break
    note = " ".join(ds)
    if len(note) > 300:
        note = note[:297].rsplit(" ", 1)[0] + "…"
    rows.append({"avoid": avoid, "use": use, "note": note, "page": page,
                 "head": head, "kind": "term"})

seen, out = set(), []
for r in sorted(rows, key=lambda r: (r["avoid"].lower(), r["page"])):
    k = (r["avoid"].lower(), r["note"][:60])
    if k in seen:
        continue
    seen.add(k); out.append(r)

with open("/Users/hajunbae/dev/Skills/.research-tools/asgx/rows.tsv", "w") as f:
    for r in out:
        f.write(f"{r['avoid']}\t{r['use']}\t{r['note']}\t{r['page']}\t{r['head']}\n")
print("rows:", len(out))
