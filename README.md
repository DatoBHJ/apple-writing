# Apple Writing — an agent skill

An [Agent Skill](https://agentskills.io/specification) that teaches any coding agent to write **English text in Apple’s own voice** — on any surface where text appears, down to a single word.

Works with Claude Code, Codex, Cursor, OpenCode, Gemini CLI, GitHub Copilot, Windsurf, Zed, DSH and [75+ other harnesses](#install) — the format is the open `SKILL.md` standard, not a vendor plugin.

---

## The idea

Apple does not have one voice. It has **three registers**, and Apple says so itself. The public *Apple Style Guide* covers “instructional materials, technical documentation, reference information, training programs, and user interfaces” — and notes that *“Some departments at Apple (Marcom, for example) have supplemental style guides.”* Marketing is a **documented departure** from Apple’s own baseline, not an application of it.

| Register | Surfaces | Governed by |
|---|---|---|
| **Marketing** | product pages, app-store listings, launch emails, ads | Marcom — internal, reverse-engineered from live copy |
| **Interface** | buttons, labels, alerts, errors, onboarding, permissions, alt text | HIG — *Writing*, *Inclusion* |
| **Editorial** | docs, READMEs, API references, support articles, reports, emails, commits | Apple Style Guide (June 2026) |

The two rulebooks genuinely conflict. The Style Guide says a sentence fragment takes no ending punctuation; **92% of Apple’s marketing headlines are fragments that end in a period anyway**. A “write like Apple” tool that does not route by surface produces marketing pastiche inside error messages — which Apple’s own guidelines explicitly forbid. Routing first is the whole point.

## Install

### Any supported agent — one command

```bash
npx skills add DatoBHJ/apple-writing
```

The [skills CLI](https://github.com/vercel-labs/skills) detects your harness and installs to the right place. Add `--agent claude-code` (or `codex`, `cursor`, `opencode`, …) to target one explicitly, or `-g` for a global install.

### Claude Code — as a plugin marketplace

```
/plugin marketplace add DatoBHJ/apple-writing
/plugin install apple-writing@apple-writing-skills
```

### Manual — copy the folder into your harness

The skill is a directory with a `SKILL.md` in it. Copy `skills/apple-writing/` to any of these:

| Harness | Project | Global |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.codex/skills/` |
| Cursor | `.agents/skills/` | `~/.cursor/skills/` |
| OpenCode | `.agents/skills/` | `~/.config/opencode/skills/` |
| Gemini CLI | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `.agents/skills/` | `~/.copilot/skills/` |
| Cline, Zed, Amp, Warp, Kimi CLI, Roo Code, Droid, Kilo | `.agents/skills/` | `~/.agents/skills/` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| Continue | `.continue/skills/` | `~/.continue/skills/` |
| Kiro CLI | `.kiro/skills/` | `~/.kiro/skills/` |
| Goose | `.goose/skills/` | `~/.config/goose/skills/` |
| DSH | `.dsh/skills/` | `~/.dsh/skills/` |

There is also a small helper that does the copy for you:

```bash
./skills/apple-writing/install.sh claude     # or: dsh, codex, cursor, agents, /custom/path
```

Claude.ai / Claude Desktop: zip the `skills/apple-writing/` folder and upload it under **Settings → Capabilities → Skills**.

## Use

Once installed, the skill activates on writing requests — *“make this sound like Apple”*, *“tighten this copy”*, *“write the error message”*, *“name this feature”*, *“de-jargon this README”*. It defers to Apple’s **interface design** work to a different skill (`apple-design`), so the two do not collide.

You can also drive its tools directly:

```bash
# mechanical style check, at the right register
python3 skills/apple-writing/tools/check-apple-style.py draft.md --surface interface

# grade the suite (14 cases, reference answers included)
cd skills/apple-writing/evals && ./run.py --selftest

# re-read Apple's live copy instead of trusting memory
skills/apple-writing/tools/fetch-apple-copy.sh page https://www.apple.com/macbook-pro/
skills/apple-writing/tools/fetch-apple-copy.sh hig writing
skills/apple-writing/tools/fetch-apple-copy.sh grep "serial comma"
```

If you clone this and start committing, point your git identity at a noreply
address first — commits carry whatever `user.email` said when they were made,
forever, and GitHub's "keep my email private" setting only covers web-based
operations, not commits made from a machine. On a fresh machine git guesses
`user@hostname`, which leaks more than an email does:

```bash
tools/setup-git-identity.sh        # see what it would do: --dry-run
```

## What’s in the skill

```
skills/apple-writing/
  SKILL.md                      the router + the rules an agent reads first (179 lines)
  references/
    surfaces.md                 ~150 text surfaces → their register (incl. one-word surfaces)
    apple-style-guide-rules.md  the editorial rulebook: 599-row substitution table, 600 verified quotes
    ui-strings.md               the interface rulebook: 264 HIG quotes across 214 rules
    marketing-register.md       12 named patterns, the footnote system, measured counts, before/after
    guardrails.md               where Apple's style is illegal or irresponsible, and what to write instead
    sources.md                  how to re-read Apple's own sources, and what does not exist
  tools/
    check-apple-style.py        dependency-free mechanical checker (surface-aware)
    fetch-apple-copy.sh         pull live Apple copy / HIG text / style guide sections
    fetch-style-guide.sh        rebuild Apple's style guide corpus locally
    vale/                       the same rules as a Vale style
  evals/
    cases.json · run.py · rubric.md    14 cases with reference answers, and the judgement layer
```

**Not vibes — measurements.** The rules are drawn from Apple’s published documents and from counted samples of live copy: zero exclamation marks across 4,638 sentences; 92% of headlines ending in a period; em dashes absent from all 83 headlines but present in 5.6% of body sentences; semicolons the exact inverse. Where a common belief did not survive measurement, it is recorded as wrong rather than repeated.

The skill also knows when **not** to sound like Apple: pharmaceutical claims (where a hero line plus a small-print footnote is structurally illegal), litigation, outages, and privacy promises. `references/guardrails.md` is the part that keeps the rest safe to use.

## The research behind it

`research/` is the full record — prior-art analysis, the primary-source map (70 numbered rules with URLs), a sourced 52-sentence corpus, 22 measured rules with counts and honest verdicts, and eleven documented failure modes with an evidence grade for every claim.

It includes what the work could **not** establish, which is the part most repositories leave out: no readability score for Apple’s copy exists, two widely repeated regulator stories survive only in secondary sources, and the ASA’s own searchable archive (2021–2026) contains no ruling naming Apple at all. See [`research/README.md`](research/README.md).

Apple’s own documents are **not** redistributed here — `tools/fetch-style-guide.sh` downloads them from Apple into your own checkout. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT — see [LICENSE](LICENSE). Quotations from Apple’s published guidance remain Apple’s; this project is **not affiliated with Apple Inc.**
