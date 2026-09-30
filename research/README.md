# research — how the skill was built

This directory is the evidence behind `skills/apple-writing/`. It exists so that every rule in the skill can be traced to something retrieved, and so that the parts that could **not** be established stay visible instead of quietly becoming folklore.

## Read in this order

| File | What it is |
|---|---|
| [`00-recon-findings.md`](00-recon-findings.md) | What was verified first-hand: retrieval routes that work, tool failures, extraction traps |
| [`01-prior-art-agent-skills.md`](01-prior-art-agent-skills.md) | What already existed, and the exact gap this project fills |
| [`02-apple-primary-sources.md`](02-apple-primary-sources.md) | The primary-source map: 70 numbered rules with URLs, plus failed URLs and route notes |
| [`03-voice-systems-and-corpus.md`](03-voice-systems-and-corpus.md) | The evidence base: a sourced 52-sentence corpus, 22 measured rules with counts, failure modes F1–F11, third-party voice systems, and the browser verification pass (B10) |
| [`04-synthesis-and-direction.md`](04-synthesis-and-direction.md) | The decision record: options considered, what was chosen, and why |
| [`_parts/`](_parts/) | Supporting quote sets collected during research (App Store, developer docs, marketing and localization, Marcom) |
| [`tools/`](tools/) | The scripts used for research when the search tooling was degraded, plus the Apple Style Guide extraction pipeline |

## The evidence grade

`03` marks every claim with one of four grades, and they are not interchangeable:

- **`(M)` measured** — our own count on a stated sample. Most of the numbers in the skill.
- **`(V)` verified** — retrieved and quoted verbatim from the source itself.
- **`(R)` reported** — someone else said it; we could not retrieve the original.
- **`(X)` excluded** — could not be retrieved at all. **Nothing in the skill is built on an `(X)`.**

## What this work does not establish

Stated plainly, because the alternative is a repository that sounds more certain than it is:

- **No readability score for Apple’s copy exists in this record.** Two academic studies of Apple’s advertising language were located and cited, but neither measures readability.
- **No diachronic or sitewide claim.** Everything is one era of copy (fetched 2026-09-30), from sampled pages — not a census.
- **Two popular regulator stories are unusable.** The 2008 UK ASA ruling and the 2012 Australian 4G penalty survive only in secondary sources. The ASA’s own searchable archive covers 2021–2026, returns **no ruling naming Apple** in any of those years, and does not reach back to 2008.
- **Apple’s Korean register is out of scope for the skill** (it is English-only by decision), though three distinct Korean registers were measured and recorded in `03` §B10.4 for whoever builds that layer.

## Not in this repository

Apple’s own documents — the *Apple Style Guide* PDF, its extracted text, and the mirrored web sections — are **excluded by `.gitignore`** and are not redistributed here. Rebuild them locally from Apple:

```bash
skills/apple-writing/tools/fetch-style-guide.sh
```

Short attributed quotations from Apple’s published guidance appear throughout the skill and these reports. See [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).
