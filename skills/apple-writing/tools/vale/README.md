# vale/ — the rules as a standard Vale style

For teams that already run [Vale](https://vale.sh) in CI. **Vale is not required by this skill** — `tools/check-apple-style.py` implements the same mechanical layer with no dependencies and is the version that has been tested here.

## Use it

```bash
vale --config=tools/vale/.vale.ini path/to/text.md
```

```bash
# or install the style into an existing Vale setup
cp -r tools/vale/styles/apple-writing ~/.local/share/vale/styles/
```

## Rules

| Rule | Type | Source |
|---|---|---|
| `Substitutions` | substitution | Apple Style Guide — wordy phrases and Latin abbreviations |
| `Banned` | substitution | Apple Style Guide — *Writing inclusively* and A–Z entries |
| `Cuteness` | existence | HIG *Writing* / *Feedback* — cuteness, blame, interjections |
| `FirstPerson` | existence | Apple Style Guide — “Don't use we, us, or I” |
| `Exclamation` | existence | Apple Style Guide — “Avoid in documentation” |
| `UnhedgedClaim` | existence | FTC *.com Disclosures* — qualify the claim itself |

## Status — read this before trusting it

- **Not run against a Vale binary.** Vale is not installed in the environment where this skill was built. The YAML files were validated for structure (valid YAML, required `extends`/`message`/`level` keys, valid levels, non-empty payloads) and the `.vale.ini` was validated to parse as a Vale-style config, but **no rule has been executed by Vale**. Verify on your first run and report a mismatch rather than assuming the rule works.
- **The `FirstPerson` rule has a real exception the linter cannot detect**: in a privacy notice, policy or leadership letter, “we” is the company speaking as itself and is correct. The `.vale.ini` here scopes that rule off for `**/policy/**` paths; if your layout differs, adjust the scope.
- **`UnhedgedClaim` is a heuristic.** It looks for a comparative number without a hedge within the same sentence. It will miss claims phrased unusually and it cannot see whether the evidence exists — only a human can decide that.
- **Never treat a clean Vale run as “this is Apple style.”** It means the text avoids known errors. Grade with `evals/rubric.md`.
