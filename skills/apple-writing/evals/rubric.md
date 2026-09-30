# Rubric — judging text the checker cannot judge

`tools/check-apple-style.py` catches what a machine can catch: banned words, first person, Latin abbreviations, exclamation marks, unhedged claims, superlative density. **Passing it means the text is not obviously wrong. It does not mean the text is good.**

Grade with this rubric after the checker is clean, and grade one dimension at a time.

---

## 0. Before you grade

1. **Run the mechanical checker** with the right surface: `python3 tools/check-apple-style.py TEXT --surface editorial|interface|marketing|policy`. Errors must be zero.
2. **Confirm the register was routed** (`SKILL.md` §1). Grading a correct sentence in the wrong register as “good” is the most common failure of a style review.
3. **Check that meaning survived.** Compare fact by fact with the source: every number, name, date, condition and hedge. A beautiful rewrite that changed a number scores zero on everything.

---

## 1. The dimensions

Score each 0–2. Anchors are written so two reviewers reading the same text reach the same score.

### D1. Register fit — *is this the right voice for this surface?*
- **2** — Unmistakably right: a verb-first label in the UI, a documented, hedged claim in marketing, plain editorial prose in a README, accountability language in a failure notice.
- **1** — Right register, wrong intensity: marketing rhythm leaking into helper text; an error message that is technically plain but reads like a brochure.
- **0** — Wrong register. Cuteness in an error, a joke in a legal notice, a superlative in a postmortem.

### D2. Word choice — *would Apple have picked this word?*
- **2** — Concrete, short, in the reader’s own vocabulary. No word is doing decoration. Substitutions applied.
- **1** — Understandable but abstract or corporate in places (`utilize`, `leverage`, `facilitate`, nominalisations like “the implementation of”).
- **0** — Jargon the reader must decode; a banned term; a metaphorical use of violence or a colour-coded value judgement.

### D3. Sentence shape — *does each sentence do one job?*
- **2** — One claim per sentence; actor and action first; active voice; the sentence ends when the meaning ends.
- **1** — Correct but flabby, or two ideas sharing one sentence without a reason.
- **0** — Nominalised, passive, or a sentence the reader must re-read to parse.

### D4. Evidence and honesty — *is every claim defensible as written?*
- **2** — Every number, comparison and superlative carries its hedge and its qualification, in the same block. Nothing is claimed that the source cannot support.
- **1** — Hedge present but the qualification is separated from the claim, or the disclosure is too thin to be informative.
- **0** — An unqualified comparative, an absolute (`never`, `guaranteed`), or a claim whose evidence does not exist.

### D5. Rhythm without caricature — *does it sound confident rather than imitated?*
- **2** — Deliberate cadence; at most one stylistic device per paragraph; the short sentences land because the long ones set them up.
- **1** — Rhythm present but repetitive, or one device too many.
- **0** — Parody: stacked fragments, three superlatives in a paragraph, a punchline with no substance behind it.

### D6. Meaning preserved — *is anything lost, added, or softened?*
- **2** — Same facts, same strength, same conditions. Nothing invented to complete a rhythm.
- **1** — A nuance dropped (a condition implied rather than stated), or a hedge quietly weakened.
- **0** — A number, name, condition or legal term changed; a protected string paraphrased.

**Total: 12.** Interpretation: **10–12** ship it · **7–9** fix the 1s and re-grade · **≤6** rewrite, do not patch.

---

## 2. Automatic fails

Regardless of score:

- Protected text altered (product name, code, URL, quoted UI string, legal wording).
- A number, date or condition changed from the source.
- A claim published without the evidence its hedge promises.
- Marketing register in a regulated, adversarial or apologetic surface (`references/guardrails.md`).

---

## 3. Blind comparison — when you are choosing between rewrites

Do not trust your own sense of “more Apple-like” without controls. Rank two candidates this way:

1. **Same model, same effort, fresh context** for each candidate. No candidate sees the other.
2. **Swap the order** and re-judge. If the preference flips, the judgement was positional, not textual.
3. **Length-match** the candidates before comparing. Judges systematically prefer the longer text, and the shorter text systematically loses.
4. **Judge dimension by dimension** (D1–D6), not holistically. Holistic judgement collapses to “which do I like”.
5. Keep the loser. A rewrite that scores worse should be reverted, not shipped because it was newer.

---

## 4. What this rubric cannot do — stated plainly

- **No automatic style metric is trustworthy here.** Published style-transfer work finds that classifier scores of “style match” correlate only weakly with human judgement (reported around ρ≈0.38 for the GYAFC benchmark), and that BLEU **anti-correlates** with human preference for style transfer. Do not report a number as evidence of voice.
- **LLM judges have a known bias toward low-perplexity text.** A judge asked “which sounds more like Apple?” will often prefer whichever candidate reads more like a generic assistant. That is why D1–D6 are anchored and why the mechanical checker exists: it is not impressed by anything.
- **“Sounds like Claude” is not “sounds like Apple.”** If a sentence would fit in any assistant’s reply, it has no voice in it.
- **Nobody has published a corpus-linguistic study of Apple’s register.** The counts in this skill are measurements of small samples, not sitewide findings. Treat them as calibration, not as law.

When you cannot decide, **prefer the plainer text.** Every regime that constrains writing — accessibility, localization, regulation, plain-language law — rewards the same choice.
