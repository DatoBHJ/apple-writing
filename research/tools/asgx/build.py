#!/usr/bin/env python3
"""Build the A–Z entry list (head, page, full body) from the ASG PDF text."""
import re, json, bisect

SRC = "/Users/hajunbae/dev/Skills/research/apple-style-guide.txt"

STOP = set("""It It’s You If When To For The This These That There Avoid Correct Incorrect
Preferable See Use Don’t Do Note Also In On After Before Then But And Or However Make
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
Instead Rather Similarly Likewise Conversely Meanwhile Otherwise Besides Indeed Further
Of Off Out Up Down Over Under Again Now Today Currently Generally Usually Typically Often
Sometimes Never Always Provide Provided Providing Using Used Give Gives Keep Keeps Let Lets
Help Helps Consider Considers Remember Ensure Be Being Been Is Are Was Were Will Would Can
Could May Might Must Should Have Has Had Having""".split())

def load_pages():
    t = open(SRC, encoding="utf-8").read()
    parts = re.split(r"^===== PAGE (\d+) =====$", t, flags=re.M)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}

DANGLING = set("""don’t use don’t use; use use and or the a an to of in for with by on at from as is are be been that than when such your you it them not but if see like into about over including as: and/or""".split())

CAND = re.compile(r"^(?P<head>\S[^\n]{0,58}?)\s{2,}(?P<body>\S.*)$")

def norm(h):
    h = h.strip().strip("“”\"'").strip()
    return h

def sortkey(h):
    h = re.sub(r"\((?:n|v|adj|pred\. adj|pl|sing|abbr)[^)]*\)", "", norm(h).lower())
    alnum = re.sub(r"[^a-z0-9]", "", h)
    return (0 if alnum[:1].isdigit() else 1, alnum)

def plausible(head):
    h = norm(head)
    if not h or len(h) > 58 or h[-1] in ";:-" or h[0] == "•":
        return 0.0
    if re.match(r"^(Don’t|Do not|Avoid|Correct|Incorrect|Preferable|See also|See|Example|Examples|Note|When to|How to|Style|Usage)\b", h):
        return 0.0
    w = h.split()
    if len(w) > 9:
        return 0.0
    if w[0].strip("’'") in STOP:
        return 0.3
    if h[0].islower():
        return 0.7
    return 1.0

def scan(pages, lo=11, hi=222):
    """Return ordered list of (pageno, lineno, head, body, score)."""
    out = []
    for pno in range(lo, hi + 1):
        for i, ln in enumerate(pages.get(pno, "").split("\n")):
            s = ln.strip()
            if s.startswith("Apple Style Guide"):
                s = s[len("Apple Style Guide"):].strip()
            if not s or s == str(pno) or len(s) <= 2:
                continue
            if re.match(r"^(Style and usage A–Z|Numbers|Writing inclusively|Units of measure|Technical notation|International style|Copyright and trademarks|About this guide|Changes to the guide|Contents|Welcome|Intro to|General guidelines|Inclusive representation|Gender identity|Writing about disability|Prefixes for|Names and unit symbols|Code$|Syntax descriptions|Code font in text|Placeholder names in text|Countries|Currency|Dates and times|Decimals|Languages|Telephone numbers)\b", s):
                continue
            m = CAND.match(s)
            if not m:
                continue
            sc = plausible(m.group("head"))
            if sc:
                out.append({"page": pno, "line": i, "head": norm(m.group("head")),
                            "body": m.group("body").strip(), "score": sc})
    return out

def select(cands):
    keys = [sortkey(c["head"]) for c in cands]
    n = len(cands)
    best = [c["score"] for c in cands]
    prev = [-1] * n
    order = sorted(range(n), key=lambda i: (keys[i], i))
    pos = {i: k for k, i in enumerate(order)}
    tree = [(-1.0, -1)] * (n + 2)
    def upd(i, val, idx):
        i += 1
        while i <= n + 1:
            if val > tree[i][0]:
                tree[i] = (val, idx)
            i += i & -i
    def qry(i):
        r = (-1.0, -1); i += 1
        while i > 0:
            if tree[i][0] > r[0]:
                r = tree[i]
            i -= i & -i
        return r
    for i in range(n):
        v, j = qry(pos[i])
        if v > 0:
            best[i] += v; prev[i] = j
        upd(pos[i], best[i], i)
    end = max(range(n), key=lambda i: best[i])
    chain = []
    while end != -1:
        chain.append(end); end = prev[end]
    chain = chain[::-1]
    # recover high-score stragglers if they fit positionally
    chosen = list(chain)
    for i, c in enumerate(cands):
        if i in set(chosen) or c["score"] < 0.7:
            continue
        k = sortkey(c["head"])
        ks = [sortkey(cands[j]["head"]) for j in chosen]
        p = bisect.bisect_left(ks, k)
        prevp = cands[chosen[p - 1]]["page"] if p > 0 else 0
        nextp = cands[chosen[p]]["page"] if p < len(chosen) else 999
        if prevp <= c["page"] <= nextp:
            chosen.insert(p, i)
    return [cands[i] for i in chosen]

def build():
    pages = load_pages()
    cands = scan(pages)
    sel = select(cands)
    starts = {(c["page"], c["line"]): c for c in sel}
    entries, cur = [], None
    for pno in range(11, 223):
        for i, ln in enumerate(pages.get(pno, "").split("\n")):
            s = ln.strip()
            if s.startswith("Apple Style Guide"):
                s = s[len("Apple Style Guide"):].strip()
            if not s or s == str(pno) or len(s) <= 2:
                continue
            if re.match(r"^(Style and usage A–Z|Numbers|Writing inclusively|Units of measure|Technical notation|International style|Copyright and trademarks|About this guide|Changes to the guide|Contents|Welcome|Intro to|General guidelines|Inclusive representation|Gender identity|Writing about disability|Prefixes for|Names and unit symbols|Code$|Syntax descriptions|Code font in text|Placeholder names in text|Countries|Currency|Dates and times|Decimals|Languages|Telephone numbers)\b", s):
                continue
            if (pno, i) in starts:
                if cur:
                    entries.append(cur)
                c = starts[(pno, i)]
                cur = {"head": c["head"], "page": pno, "body": c["body"], "lines": [s]}
            elif cur is not None:
                cur["body"] += " " + s
                cur["lines"].append(s)
    if cur:
        entries.append(cur)
    # Merge entries that are really continuations of the previous entry:
    # an entry body that stops mid-sentence means the next "entry" is its tail.
    merged = []
    for e in entries:
        if merged:
            prev = merged[-1]
            tail = prev["body"].rstrip().split()[-1].strip("“”()").lower() if prev["body"].strip() else ""
            if tail in DANGLING:
                prev["body"] = (prev["body"] + " " + e["head"] + " " + e["body"]).strip()
                prev["lines"].extend(e["lines"])
                continue
        merged.append(e)
    for e in merged:
        e["body"] = re.sub(r"\s+", " ", e["body"]).strip()
    return merged

if __name__ == "__main__":
    ents = build()
    json.dump(ents, open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json", "w"), indent=1)
    print("entries:", len(ents))
    # coverage of Don't use / Avoid
    miss = 0
    for e in ents:
        if re.search(r"Don’t use|Avoid", e["body"]):
            pass
    import collections
    print("with Don’t use:", sum(1 for e in ents if "Don’t use" in e["body"]))
    print("with Avoid:", sum(1 for e in ents if "Avoid" in e["body"]))
    for h in ["serial comma", "comma", "em dash", "accessibility", "passive voice", "contractions", "numbers", "colon"]:
        print(h, "->", [e["head"] for e in ents if h in e["head"].lower()][:3])
