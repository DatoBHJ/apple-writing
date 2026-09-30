#!/usr/bin/env python3
"""Make every table quote verifiably verbatim: drop or elide unverifiable sentences."""
import re, glob, sys

DOC = "apple-writing/references/apple-style-guide-rules.md"
src = open("research/apple-style-guide.txt").read()
for f in glob.glob("research/asg/*.txt"):
    src += "\n" + open(f).read()

def norm(s):
    s = s.replace("\u00a0", " ").replace("\u2011", "-").replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"[^A-Za-z0-9]+", " ", s)
    return " " + re.sub(r"\s+", " ", s).strip().lower() + " "

NS = norm(src)

def verify(text):
    parts = [p.strip() for p in text.split("\u2026") if p.strip()]
    return all(len(norm(p)) < 8 or norm(p) in NS for p in parts)

def sents(t):
    tmp = t.replace("e.g.", "e\u0001g\u0001").replace("i.e.", "i\u0001e\u0001").replace("etc.", "e\u0001t\u0001")
    tmp = tmp.replace("Inc.", "I\u0001").replace("in.", "i\u0001").replace("vs.", "v\u0001")
    out = re.split(r"(?<=[.!?;])\s+(?=[A-Z\u201c(])", tmp)
    return [s.replace("\u0001", ".") for s in out]

lines = open(DOC).read().split("\n")
out, fixed, dropped = [], 0, 0
for ln in lines:
    m = re.match(r"^\| \*\*(.+?)\*\* \| (.*?) \| \u201c(.+)\u201d \| (p\..+) \|$", ln)
    if not m:
        out.append(ln); continue
    avoid, use, note, cite = m.groups()
    if verify(note):
        out.append(ln); continue
    good = [s.strip() for s in sents(note) if verify(s.strip())]
    if good:
        new = " \u2026 ".join(good)
        out.append("| **" + avoid + "** | " + use + " | \u201c" + new + "\u201d | " + cite + " |")
        fixed += 1
    else:
        out.append("| **" + avoid + "** | " + use + " | \u2014 (see " + cite + ") | " + cite + " |")
        dropped += 1
open(DOC, "w").write("\n".join(out))
print("fixed:", fixed, "note dropped:", dropped)
