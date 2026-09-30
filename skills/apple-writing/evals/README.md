# evals — how to tell whether the skill worked

Three layers, in order of trustworthiness: **mechanical checks** (a machine decides), **rubric** (a human or a careful judge decides), **blind comparison** (controls for your own bias).

## Run it

```bash
# 1. Prove the suite is coherent: the reference answers pass their own assertions.
cd evals && ./run.py --selftest

# 2. Grade real outputs: put <case-id>.txt files in a directory, one per case.
./run.py path/to/outputs

# 3. List the cases and their surfaces.
./run.py --list
```

```bash
# 4. Mechanical check on anything, at any time.
python3 tools/check-apple-style.py your-text.md --surface interface
python3 tools/check-apple-style.py your-text.md --surface marketing --json
cat draft.md | python3 tools/check-apple-style.py - --surface editorial
```
Exit code is 1 when an error-level finding exists, so it drops straight into CI or a pre-commit hook.

## Files

| File | What it is |
|---|---|
| `cases.json` | 14 cases across editorial, interface, marketing and policy surfaces. Each has a prompt, mechanical assertions, and a **reference answer** written to pass its own assertions. Includes a `requires` field for checks a regex cannot make. |
| `run.py` | The runner. `--selftest` grades the reference answers; a directory argument grades real outputs. Also runs the mechanical checker per case with the correct surface. |
| `rubric.md` | The judgement layer: six dimensions with anchors, automatic fails, the blind-comparison protocol, and an honest account of what cannot be measured. |

## What is deliberately *not* here

- **No “style score”.** No published automatic metric for voice is trustworthy: benchmark style classifiers correlate only weakly with human judgement, and BLEU anti-correlates with human preference in style transfer. A number would create false confidence.
- **No LLM-judge script.** Judges systematically prefer low-perplexity text, which would reward “sounds like a generic assistant” over “sounds like Apple”. If you use one, follow the controls in `rubric.md` §3.
- **No sitewide claims.** The counts in this skill come from small samples (10 English pages, 4,638 sentences, 83 headlines, 59 footnotes, plus Korean pages for comparison). They are calibration, not census.

## Adding a case

Add an object to `cases.json`:

```json
{
  "id": "ui-04-settings-row",
  "surface": "interface",
  "prompt": "…",
  "why": "which rule this case exists to protect",
  "assert": {
    "must_match": ["regex"],
    "must_not_match": ["regex"],
    "max_words": 12,
    "max_words_line1": 8,
    "max_chars": 40,
    "max_sentences": 2,
    "requires": "a judgement a regex cannot make"
  },
  "reference": "an answer that passes the above"
}
```

Then run `./run.py --selftest` — if your reference answer fails its own assertions, the case is wrong, not the answer.
