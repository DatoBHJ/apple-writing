# AGENTS.md

Instructions for any agent working **on this repository**. (The skill that ships here is for agents writing *text*; this file is for agents editing *this repo*.)

## What this repository is

A public Agent Skill repository. The product is `skills/apple-writing/` — a skill that teaches an agent to write English text in Apple’s voice across three registers. `research/` is the evidence record behind it.

## Hard rules

1. **Never redistribute Apple’s documents.** `research/apple-style-guide.pdf`, `research/apple-style-guide.txt` and `research/asg/` are excluded by `.gitignore` for copyright reasons, as are the bulk machine extracts in `research/tools/asgx/` (`*.json`, `*.tsv`, `*.txt`, draft tables). Do not commit them, do not paste their full text into tracked files, and do not remove those `.gitignore` lines. Short attributed quotations are fine — that is the entire point of the references. If you regenerate the corpus locally, it stays local.
2. **Never invent a citation.** Every rule in `references/` carries a verbatim quote and a source. If you cannot find the quote, delete the rule. `references/sources.md` §3 lists sources that *do not exist* — read it before adding a citation.
3. **Keep the evidence grades.** `research/03-voice-systems-and-corpus.md` marks claims `(M)` measured, `(V)` verified, `(R)` reported, `(X)` excluded. Do not upgrade `(R)` to fact, and do not build a rule on an `(X)`.
4. **Route before you write.** Any change to wording in the skill must respect the three registers (`SKILL.md` §1). Marketing rhythm in an interface rule is a bug.
5. **Samples, not census.** Counts are from small corpora. Never reword them as sitewide claims.

## Layout

```
README.md                      public face: the idea, install for every harness
LICENSE · THIRD_PARTY_NOTICES.md
.claude-plugin/marketplace.json   Claude Code plugin marketplace manifest
skills/apple-writing/          the skill (SKILL.md + references/ + tools/ + evals/)
research/                      evidence: reports, corpora, extraction tools
```

The `skills/<name>/SKILL.md` layout is what `npx skills add <owner>/<repo>` discovers, so keep skills under `skills/` and keep the frontmatter to `name` + `description`.

## Before you commit

```bash
# the skill's own tests must pass
cd skills/apple-writing/evals && ./run.py --selftest        # expect: 14 passed · 0 failed

# no broken relative links, no missing SKILL.md targets
python3 - <<'PY'
import os, re
root = "."
bad = []
for base, _, files in os.walk(root):
    if any(x in base for x in (".git", "__pycache__")): continue
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(base, f)
            for t in re.findall(r"\]\((?!https?:)([^)#]+)", open(p).read()):
                if not os.path.exists(os.path.normpath(os.path.join(base, t))):
                    bad.append(f"{p} -> {t}")
print("broken links:", bad or "none")
PY

# the mechanical checker still runs
python3 skills/apple-writing/tools/check-apple-style.py README.md --surface editorial
```

## Editing the skill

- `SKILL.md` is the entry point and must stay small (roughly 150–200 lines). Detail goes in `references/`, which are loaded on demand — say *when* to load each one.
- Long reference files (>500 lines) start with a loading note telling the agent to grep to the section it needs rather than read end to end.
- Adding a rule means: imperative statement → verbatim quote → citation. No quote, no rule.
- Adding an eval case: put the prompt, mechanical assertions and a reference answer in `evals/cases.json`, then run `--selftest`. **If your reference answer fails its own assertions, the case is wrong, not the answer.**

## Style of the writing in this repo

The skill’s own advice applies to the skill: active voice, no first person (`we`), no Latin abbreviations, serial commas, contractions, no exclamation marks. The root README and the skill’s README are user-facing prose and should be written that way.
