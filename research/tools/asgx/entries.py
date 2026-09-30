#!/usr/bin/env python3
"""Robust A–Z entry parser for the Apple Style Guide PDF text.

Idea: headword lines in the PDF text are `Headword<2+ spaces>body`.  Some
continuation lines also contain a 2-space run (where the source had bold/italic),
so we pick the maximum-weight chain of candidates whose headwords are in
non-decreasing alphabetical order (the A–Z is sorted).
"""
import re, json, bisect

SRC = "/Users/hajunbae/dev/Skills/research/apple-style-guide.txt"

STOP = set("""It It's You If When To For The This These That There Avoid Correct Incorrect
Preferable See Use Don't Do Note Also In On After Before Then But And Or However Make
Click Choose Select Tap Press Type Enter Drag Open While Because As At By From With An A
All Some Most Their Its His Her They We Your My Our Not Only Just Even Once First Next
Last Finally More Less Listen Watch Read Go Get Set Turn Add Delete Move Copy Paste Hold
Swipe Say Ask Tell Show Hide Write Run Start Stop Wait Check Verify Find Learn Visit
Contact Call Send Receive Share Save Print Scan Record Play Pause Zoom Lock Unlock Connect
Disconnect Install Remove Update Upgrade Restart Relaunch Quit Exit Close Minimize Maximize
Resize Increase Decrease Adjust Change Modify Edit Create Build Test Debug Deploy Publish
Post Import Export Backup Restore Sync Refresh Reload Yes No Neither Either Each Both
Another Other Others Such Same Different Many Few Several Every Any None Nothing Something
Anything Everything One Two Three Four Five Six Seven Eight Nine Ten Here Where What Which
Who Whom Whose Why How Whether Although Though Unless Until Since So Thus Therefore Also
Instead Rather Similarly Likewise Conversely Meanwhile Otherwise Besides Finally Indeed
Of Off Out Up Down Over Under Again Further Then Now Today Currently Generally Usually
Typically Often Sometimes Never Always Usually Provide Provided Providing Using Used
Make Makes Making Take Takes Taking Give Gives Giving Keep Keeps Keeping Let Lets Letting
Help Helps Helping Avoid Avoids Avoiding Consider Considers Considering Note Notes Noting
Remember Ensure Be Being Been Is Are Was Were Will Would Can Could May Might Must Should
Have Has Had Having""".split())

def load_pages():
    t = open(SRC, encoding="utf-8").read()
    parts = re.split(r"^===== PAGE (\d+) =====$", t, flags=re.M)
    return {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}

CAND = re.compile(r"^(?P<head>\S[^\n]{0,58}?)\s{2,}(?P<body>\S.*)$")

def norm(h):
    h = h.strip().strip('“”"').strip()
    h = re.sub(r"\s*\((?:n|v|adj|pred\. adj|pl|sing|abbr)\.?[^)]*\)\s*$", "", h).strip()
    return h

def sortkey(h):
    h = norm(h).lower()
    h = h.lstrip("(“\"'")
    first = h[:1]
    cls = 0 if first.isdigit() else 1
    return (cls, h)

def plausible(head, body):
    h = head.strip()
    if not h or len(h) > 58:
        return 0.0
    if h[-1] in ",;:":
        return 0.0
    w = h.split()
    if len(w) > 9:
        return 0.0
    score = 1.0
    if w[0].strip("’'") in STOP:
        score = 0.02          # sentence starter: likely wrapped continuation
    if re.match(r"^(Don’t|Do not|Avoid|Correct|Incorrect|Preferable|See also|See|Example|Examples|Note|When to|How to|Style|Usage)\b", h):
        return 0.0
    if h[0].islower() and score == 1.0:
        score = 0.6           # lowercase headwords exist (e.g. "access") but risky
    if len(w) == 1 and h.islower():
        score = 0.5
    return score

def candidates(pages, lo=11, hi=222):
    out = []
    for pno in range(lo, hi + 1):
        for ln in pages.get(pno, "").split("\n"):
            s = ln.strip()
            if not s or s == str(pno) or s.startswith("Apple Style Guide"):
                continue
            m = CAND.match(s)
            if not m:
                continue
            sc = plausible(m.group("head"), m.group("body"))
            if sc > 0:
                out.append({"head": norm(m.group("head")), "body": m.group("body").strip(),
                            "page": pno, "score": sc, "raw": s})
    return out

def lis_chain(cands):
    """Max-weight non-decreasing-subsequence by sortkey."""
    n = len(cands)
    keys = [sortkey(c["head"]) for c in cands]
    best = [c["score"] for c in cands]
    prev = [-1] * n
    order = sorted(range(n), key=lambda i: (keys[i], i))
    # Fenwick over sorted positions for max prefix
    size = n + 1
    tree = [(-1.0, -1)] * (size + 1)
    def upd(i, val, idx):
        i += 1
        while i <= size:
            if val > tree[i][0]:
                tree[i] = (val, idx)
            i += i & -i
    def qry(i):
        r = (-1.0, -1)
        i += 1
        while i > 0:
            if tree[i][0] > r[0]:
                r = tree[i]
            i -= i & -i
        return r
    pos = {i: k for k, i in enumerate(order)}
    for i in range(n):
        p = pos[i]
        v, j = qry(p)
        if v > 0:
            best[i] += v
            prev[i] = j
        upd(p, best[i], i)
    end = max(range(n), key=lambda i: best[i])
    chain = []
    while end != -1:
        chain.append(cands[end])
        end = prev[end]
    return chain[::-1]

if __name__ == "__main__":
    pages = load_pages()
    c = candidates(pages)
    ch = lis_chain(c)
    json.dump(ch, open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json", "w"), indent=1)
    print("candidates:", len(c), "chain:", len(ch))
    dropped = [x for x in c if x not in ch]
    print("dropped:", len(dropped))
    for d in dropped[:40]:
        print("  DROP", d["page"], "|", d["head"][:50], "|", d["raw"][:70])
