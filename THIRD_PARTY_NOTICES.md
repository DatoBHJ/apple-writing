# Third-party notices

## Apple

This repository is **not affiliated with, endorsed by, or sponsored by Apple Inc.**
Apple, iPhone, iPad, Mac, MacBook, Apple Watch, AirPods, Siri, App Store and the
Apple logo are trademarks of Apple Inc.

The `apple-writing` skill explains and quotes Apple’s publicly published writing
guidance so that a writer or an agent can follow it:

- *Apple Style Guide* — <https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf>
  and <https://support.apple.com/guide/applestyleguide/>
- *Human Interface Guidelines* — <https://developer.apple.com/design/human-interface-guidelines/>
- Apple product and support pages — <https://www.apple.com/>, <https://support.apple.com/>

**What is quoted:** short excerpts, each attributed to its page or section, used
to state a rule accurately rather than paraphrase it. The substitution tables in
`references/apple-style-guide-rules.md` are derived from the guide’s own
“Don’t use X; use Y” entries, with the source condition quoted where the guide
gives one.

**What is not redistributed:** Apple’s documents themselves. The full style guide
(PDF and extracted text), the mirrored web sections, and the bulk machine
extracts produced during research (1,700 A–Z entries, rule dumps and draft tables
under `research/tools/asgx/`) are excluded by `.gitignore` and are **not** part of
this repository. The scripts that generate them are tracked, so anyone can
rebuild them from Apple’s own source. To get the corpus locally, fetch it from
Apple with:

```bash
skills/apple-writing/tools/fetch-style-guide.sh
```

That script downloads from Apple directly and writes the corpus into your own
checkout. Review Apple’s terms before redistributing anything it retrieves.

**Marketing copy** quoted in `references/marketing-register.md` is Apple’s
advertising copy, reproduced in short excerpts for analysis and instruction,
each with the URL it came from.

If you are Apple and would like a quotation changed or removed, open an issue.

## Rulings, filings and journalism

The `research/` reports cite regulatory and legal documents and news reporting,
each with a URL and an evidence grade — `(V)` verified, `(M)` measured by us,
`(R)` reported elsewhere and not verified, `(X)` excluded. Nothing graded `(R)`
or `(X)` is used as a rule in the skill. See `research/03-voice-systems-and-corpus.md` §B9.

## Fonts, images, binaries

None. This repository contains no fonts, no images and no compiled binaries.

## Dependencies

The skill’s own tooling uses only the Python standard library. Optional extras
referenced in the docs: `pypdf` (to extract the style guide text),
`beautifulsoup4` (used by the research scripts), and [Vale](https://vale.sh)
if you want to run the prose linter. The Vale style in
`skills/apple-writing/tools/vale/` is original to this repository.
