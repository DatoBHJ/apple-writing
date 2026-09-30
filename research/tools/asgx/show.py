import json, sys, re
ents = json.load(open("/Users/hajunbae/dev/Skills/.research-tools/asgx/entries.json"))
pat = sys.argv[1]
rx = re.compile(pat, re.I)
for e in ents:
    if rx.search(e["head"]):
        print(f"### {e['head']}  (p.{e['page']})")
        print(e["body"])
        print()
