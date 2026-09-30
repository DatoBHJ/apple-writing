# apple-writing

An [Agent Skill](https://agentskills.io/specification) for writing **English** text in Apple’s voice — on any surface where text appears, down to a single word.

This is the prose counterpart to the `apple-design` skill, which covers Apple’s *interface* design, motion and visual craft. This one covers the words. The two split cleanly: if the question is what a control looks like or how it moves, use `apple-design`; if it is what the text says, use this.

## Install

```bash
npx skills add DatoBHJ/Skills            # detects your harness
./skills/apple-writing/install.sh claude # or: dsh, codex, cursor, agents, /custom/path
```

The skill is a directory containing `SKILL.md`, so it works by copying it into any harness’s skill folder — `.claude/skills/`, `.agents/skills/`, `~/.codex/skills/`, `~/.dsh/skills/` and so on. The repository README has the [full path table](../../README.md#manual--copy-the-folder-into-your-harness).

## Why it exists

Apple writes in **three registers**, and using the wrong one is the most common way “Apple style” fails:

| Register | Surfaces | Rulebook |
|---|---|---|
| **Marketing** | product pages, app-store listings, launch emails, ads | Marcom — **not public**; reverse-engineered from live copy |
| **Interface** | buttons, labels, alerts, errors, onboarding, permissions, alt text | HIG — *Writing*, *Inclusion* |
| **Editorial** | docs, READMEs, API references, support articles, reports, emails, commits | Apple Style Guide (June 2026) |

Apple’s own guide proves the split: it covers “instructional materials, technical documentation, reference information, training programs, and user interfaces” and states that *“Some departments at Apple (Marcom, for example) have supplemental style guides.”* Marketing is a documented **departure** from Apple’s baseline — a hero line follows rules an error message is forbidden to follow.

## What was checked before writing any of it

Every rule in this skill traces to a source that was retrieved, not remembered:

- **Apple Style Guide, June 2026** — 244 pages, downloaded and text-extracted
- **The same guide as 52 web sections** — 507 K characters
- **HIG Writing / Inclusion / Feedback** — via Apple’s documentation JSON endpoint
- **Live apple.com copy** — measured, not eyeballed: 0 exclamation marks across 4,638 sentences; 92% of headlines end in a period; **em dashes never appear in headlines** (0/83) — the popular idea that the em dash is a signature Apple device is unsupported, and the fresh sample locates them where they actually live: 5.6% of feature body sentences, **zero** in 240 footnotes. Semicolons are the exact inverse (142 footnote sentences, 3 in body prose). Each punctuation mark belongs to its own surface.

Where a rule could not be sourced, it is labelled as inference. Where a widely repeated “fact” turned out to be wrong — the Markkula memo’s authorship, the “Apple never punctuates taglines” claim, the em-dash folklore, two regulator stories — it is recorded as wrong in `references/sources.md` rather than quietly repeated.

## Layout

```
SKILL.md                        the router + the rules an agent reads first (179 lines)
references/
  surfaces.md                   every surface that carries text → its register (marketing, UI, docs, legal, one-word)
  apple-style-guide-rules.md    the editorial rulebook: 599-row substitution table, 600 verified quotes
  ui-strings.md                 the interface rulebook: 264 HIG quotes across 214 rules
  marketing-register.md         the pattern catalogue, the footnote system, measured counts, transformations
  guardrails.md                 where Apple's style is illegal or irresponsible, and what to write instead
  sources.md                    what Apple published, how to re-read it, and what does not exist
tools/
  check-apple-style.py          mechanical checker (no dependencies) — the tested one
  fetch-apple-copy.sh           pull live Apple copy / HIG text / style guide sections
  fetch-style-guide.sh          rebuild Apple's style guide text locally, from Apple
  vale/                         the same rules as a Vale style (see its README for status)
evals/
  cases.json · run.py           14 cases with reference answers; `./run.py --selftest` proves the suite is coherent
  rubric.md                     the judgement layer, and an honest account of what cannot be measured
```

## Use

```bash
# Mechanical pass over your text, at the right register
python3 tools/check-apple-style.py draft.md --surface interface

# Grade an output
cd evals && ./run.py --selftest

# Re-read the source instead of trusting memory
./tools/fetch-apple-copy.sh page https://www.apple.com/macbook-pro/
./tools/fetch-apple-copy.sh hig writing
./tools/fetch-apple-copy.sh grep "serial comma"
```

The corpus commands need Apple’s style guide text locally. It is not shipped with the skill — download it from Apple once:

```bash
./tools/fetch-style-guide.sh
```

## Known limits

- **English only.** Apple’s non-English copy is *transcreated*, not translated, and the register is chosen by content type. That is measured on Apple’s own pages: Korean **marketing** runs 합니다체 + 해요체 with `당신`; Korean **support and user guides** run 하십시오체 with no `당신` at all; Korean **press releases** switch to 한다체. Three registers in one language. A language layer is a separate piece of work; the skill says so rather than pretending.
- **The marketing register is reverse-engineered.** No public Marcom guide exists. The patterns are measured from live copy, so they age as the site changes — which is why `tools/fetch-apple-copy.sh` exists.
- **Counts are samples, not a census.** They come from small corpora and are labelled as such throughout.
- **No readability score exists for Apple’s copy.** Two academic studies of Apple’s advertising language were located and are cited as corroboration, but neither measures readability, so any “Apple writes at grade N” claim would be invented.
- **Vale rules are structurally validated but never executed** — Vale was not installed in the environment where this was built.
- **Two widely repeated regulator stories are not usable.** The ASA’s own searchable archive covers 2021–2026, returns **no ruling naming Apple** in any of those years, and does not reach back to 2008 — where the famous story lives. The 2012 Australian 4G penalty survives only in secondary sources.

## Verification passes

The skill was built in two rounds. The first used HTTP only; the second re-checked every claim HTTP could not settle in a real browser, which is how the ASA question, the App Store character limits, the academic literature and the Korean support register were closed. Where a claim could not be verified, it was removed rather than softened — the “does not exist, do not cite it” list in `references/sources.md` §3 exists for exactly that reason.

## Where the research lives

`../../research/` holds everything the skill was built from: the prior-art analysis, the primary-source map (70 numbered rules with URLs), a sourced 52-sentence corpus, 22 measured rules with counts and honest verdicts, and eleven documented failure modes — each claim carrying an evidence grade. See [`research/README.md`](../../research/README.md).

Apple’s own documents are not redistributed here. Quotations remain Apple’s; this project is **not affiliated with Apple Inc.** See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).
