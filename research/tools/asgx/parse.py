#!/usr/bin/env python3
"""Parse the Apple Style Guide PDF text into entries with page numbers."""
import re, json, sys, os

SRC = "/Users/hajunbae/dev/Skills/research/apple-style-guide.txt"

def load_pages():
    t = open(SRC, encoding="utf-8").read()
    parts = re.split(r"^===== PAGE (\d+) =====$", t, flags=re.M)
    pages = {}
    # parts[0] is preamble
    for i in range(1, len(parts), 2):
        pages[int(parts[i])] = parts[i+1]
    return pages

ENTRY_START = re.compile(r"^([A-Z0-9][^\n]{0,80}?)\s{2,}(\S.*)$")
# Continuation lines are wrapped text; an entry start line has >=2 spaces after headword.

def parse_entries(pages, lo=11, hi=222):
    entries = []
    cur = None
    for pno in range(lo, hi + 1):
        raw = pages.get(pno, "")
        lines = raw.split("\n")
        for ln in lines:
            s = ln.rstrip()
            if not s.strip():
                continue
            # skip running heads / page numbers
            if s.strip() == str(pno):
                continue
            if s.startswith("Apple Style Guide"):
                s = s[len("Apple Style Guide"):]
                if not s.strip():
                    continue
            m = ENTRY_START.match(s)
            if m and not re.match(r"^(See also|See|Correct|Incorrect|Avoid|Preferable|Example|Examples|Note|Notes|Before|After|Abbreviation|Acronym|Verb|Noun|Adjective|Fig|Figure|Table|Style|Usage|First reference|Subsequent|Plural|Singular|Don’t|Do not|Use|Not)\b", m.group(1)):
                if cur:
                    entries.append(cur)
                cur = {"head": m.group(1).strip(), "text": m.group(2).strip(),
                       "page": pno, "parts": [m.group(2).strip()]}
            else:
                if cur is None:
                    cur = {"head": "", "text": "", "page": pno, "parts": []}
                cur["parts"].append(s.strip())
                cur["text"] = (cur["text"] + " " + s.strip()).strip()
    if cur:
        entries.append(cur)
    for e in entries:
        e["text"] = " ".join(e["parts"])
    return entries

if __name__ == "__main__":
    pages = load_pages()
    ents = parse_entries(pages)
    json.dump(ents, open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json", "w"), indent=1)
    print("entries:", len(ents))
    for e in ents[:15]:
        print(e["page"], "|", e["head"], "||", e["text"][:90])
