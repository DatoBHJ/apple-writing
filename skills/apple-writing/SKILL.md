---
name: apple-writing
description: Write or rewrite English text in Apple’s own voice — the wording Apple uses on product pages, in interface strings, in developer documentation and support articles. Covers word choice, sentence shape, rhythm, and tying a claim to its evidence, on any surface where text appears — a hero line or feature blurb, a button label, an error message, an onboarding step, a README or API doc, a changelog, a commit message, a report, an email, alt text, or a single word. Use when asked to write like Apple, to make copy sound Apple-like, to tighten or de-jargon prose, to pick the right word or name, to write UI strings and error messages, or to review text for tone, clarity and word choice. For Apple’s interface design, motion and visual craft, use apple-design instead.
---

# Apple Writing

Apple writes in **three registers**, and using the wrong one is the most common way “Apple style” fails. A hero line is not a button label; an error message is not a product page. **Route first, then write.** All three registers share one core (§2).

Apple’s own documentation proves the split: the Apple Style Guide covers “instructional materials, technical documentation, reference information, training programs, and user interfaces” and states that “Some departments at Apple (Marcom, for example) have supplemental style guides.” Marketing is a *documented departure*, not an application of the editorial rules.

---

## 1. Route the text to a register

| The text is… | Register | Rulebook | Load |
|---|---|---|---|
| Product page, landing hero, app-store listing, launch email, ad, tagline | **Marketing** | Marcom (not public — reverse-engineered from live copy) | `references/marketing-register.md` |
| Anything inside a product: button, label, tab, menu item, alert, error, onboarding step, settings row, permission prompt, tooltip, notification, empty state, alt text, accessibility label | **Interface** | HIG — *Writing*, *Inclusion* | `references/ui-strings.md` |
| Docs, README, API reference, guide, tutorial, support article, changelog, commit message, PR description, code comment, report, memo, email, slides | **Editorial** | Apple Style Guide (June 2026) | `references/apple-style-guide-rules.md` |
| A single word or a 2–3 word string (a name, status, badge, category, CLI flag, chart label) | the register of the surface it sits on | as above | `references/surfaces.md` §6 |

**If you are unsure, use Editorial.** It is the only register Apple publishes, and everything else is a deliberate departure from it.

**Precedence when rules collide — apply in this order:**
1. **Meaning and facts are untouchable.** Never change a number, name, date, condition, hedge, or the strength of a claim.
2. **Protected text is copied verbatim:** product and feature names, code, identifiers, file paths, URLs, CLI flags, placeholders, quoted interface strings, legal wording, and anything marked “do not change”.
3. **The register’s rulebook beats the other two.** Never apply marketing rhythm to an error message.
4. **Clarity beats style.** If a rule makes the sentence harder to understand, the rule loses.
5. A user’s explicit instruction beats all of the above.

The surface list is far longer than this table — see `references/surfaces.md` for the full map, including one-word surfaces. **Anything that carries text is in scope**, down to a single string.

---

## 2. Non-negotiables — true in every register

| Rule | Why it is Apple’s rule |
|---|---|
| **No first person.** Don’t write `we`, `us`, `our`, or `I`. Rewrite with the reader or the product as the subject. **One exception:** a policy, privacy notice or leadership letter, where `we` means the company speaking as itself. Never in documentation or interface text, where the reader cannot tell who “we” is. | Apple Style Guide, `we`: “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.” Example: `We recommend that the image be at least 600 x 600 pixels.` → `For best results, the image should be at least 600 x 600 pixels.` HIG: “Avoid using we altogether because it may be unclear who the 'we' in question refers to.” |
| **Address the reader as `you`.** | HIG, *Inclusion*: “It typically works well to use you and your to address people directly. Referring to people indirectly as **the user** or **the player** can make your experience feel distant and unwelcoming.” |
| **Active voice, named actor.** | Apple Style Guide: “Avoid [passive voice] when possible and use active voice.” Passive stays legal only when the actor is unknown or genuinely irrelevant. |
| **Use contractions.** `don’t`, `isn’t`, `you’ll`, `can’t`. | Apple Style Guide, *contractions*: “As part of Apple’s informal voice, contractions are used and recommended throughout most documentation, interface text, and marketing copy.” |
| **No jargon.** Define a technical term the first time it appears. | Apple Style Guide, *jargon*: “Avoid jargon whenever possible. Define technical terminology on first occurrence.” |
| **Fewer words — but never at clarity’s expense.** If you can say it in fewer, do. If cutting costs the reader the thing they need, don’t. | HIG: “Check each word to be sure it needs to be there. If you can use fewer words, do so.” Swift API Design Guidelines: “Clarity at the point of use is your most important goal” and “Clarity is more important than brevity.” WWDC 2025: “UX writing is all about economy of language. Resist the urge to fill all available space with repeated information.” |
| **Read it aloud.** If it trips, rewrite it. | HIG: “When in doubt, read your writing out loud.” |
| **Serial comma** before `and`/`or` in a list of three or more. | Apple Style Guide: “Use a serial comma before and or or in a list of three or more items.” |
| **No Latin abbreviations.** Write `for example`, `and so on`, `that is`. Never `e.g.`, `i.e.`, `etc.`, `et al.` | Apple Style Guide, *Latin*: “Avoid using Latin abbreviations.” Entries: `e.g.` → “use for example or such as”; `etc.` → “use and so forth or and so on”. |
| **Inclusive language is mandatory, not a nicety.** | Apple Style Guide, *Writing inclusively* — see §3. |
| **Nothing in the text blames the reader.** | HIG, *Feedback*: error messages must “avoid blame, and be clear about what someone can do to fix it.” |

---

## 3. Word choice — this is where the style actually lives

Style is 90% picking the right word. Before writing a sentence, check the word.

**Substitute on sight** (full table with exceptions in `references/apple-style-guide-rules.md`):

| Don’t write | Write |
|---|---|
| `e.g.` / `i.e.` / `etc.` | `for example` / `that is` / `and so on` |
| `prior to` / `subsequent to` | `before` / `after` |
| `in order to` / `due to the fact that` | `to` / `because` |
| `utilize` / `leverage` / `make use of` | `use` |
| `in the event that` | `if` |
| `has the ability to` | `can` |
| `click on` / `click the mouse` | `click` |
| `allows you to` | `lets you` |
| `in close proximity to` | `near` |

**Never write** — banned outright by Apple’s guide:

- **People as objects or stereotypes:** `master`/`slave`, `blacklist`/`whitelist`, `grandfathered`, `sanity check`, `man-in-the-middle`, `he/she`, `s/he`, `dummy`, `crippled`, `handicapped`, `suffers from`, `victim of`, `normal user`.
- **Violence as metaphor:** `kill`, `hang`, `abort` for a process, `hit`/`nuke` for an action. Apple: “Don’t describe technology using terms that are inherently violent.”
- **Human or biological traits for software:** Apple: “avoid describing software or hardware using human or biological attributes.”
- **Colour as a value judgement:** `black hat`, `white hat`, `red team`.
- **Reader-blaming and cuteness:** `oops!`, `uh-oh`, `simply`, `just`, `obviously`, `easy`, `Let’s do it!`, `Click here`, `blame the user`.
- **Idioms and colloquialisms** (`on the same page`, `fall through the cracks`, `backseat driver`). Apple: hard to understand for people learning the language, and hard to translate.

**One word is a decision, not a placeholder.** For a name, status, badge, flag or label, the register still applies: prefer a concrete verb or noun over an abstraction, avoid cuteness, keep product names exactly as Apple capitalizes them, and never trade precision for brevity. `Favorites`, not `Your Favorites` — HIG: “Possessive pronouns like my and your are often unnecessary to establish context… 'Favorites' conveys the same message as 'Your Favorites', and is more succinct.” See `references/surfaces.md`.

---

## 4. Sentence shape

**Editing pass — Editorial and Interface:** one claim per sentence → actor and action first → cut every word that does not carry meaning or rhythm → define the one term that needs it → read it aloud.

**Interface text** follows three hard rules (all quoted from HIG):
1. **An action label starts with a verb.** “When labeling buttons and links, it’s almost always best to use a verb.”
2. **No cuteness.** “Avoid the temptation to be too cute or clever with your labels. For example, just saying 'Send' often works better than 'Let’s do it!'”
3. **Say the fix, not the fault.** `"That password is too short"` → `"Choose a password with at least 8 characters."` Errors “avoid blame” and “Interjections like 'oops!' or 'uh-oh' are typically unnecessary and can sound insincere.”

Also: **capitalization is a per-element decision, applied consistently** — “Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently.”

**Marketing copy** inverts several of these on purpose — fragments end in periods, second person is withheld from the headline and delivered in the paragraph, one idea per line. That is a different register with its own rules and its own liabilities: read `references/marketing-register.md` before writing any.

---

## 5. A claim is never alone — it travels with its evidence

This is the rule that separates Apple’s copy from imitation of it. Apple’s confident lines are defensible because the footnote exists, and the two are one unit:

> `Fly through demanding AI tasks up to 6x faster.` **+** the footnote disclosing the preproduction hardware, the build, the file and the framework version.

If the text makes a number, a comparison or a superlative claim, it needs the hedge (`up to`, `as much as`, `varies by use and configuration`) and its evidence attached. **Never write the punchline and leave the disclosure out.** If you lack the evidence, write the weaker sentence you can defend.

Where the qualification goes, in order of preference — the FTC’s own guidance for advertisers is to put it *inside* the claim rather than in a separate disclosure, “when practical”:

1. **In the sentence:** `Up to 24 hours of battery life, depending on how you use it.`
2. **In the same visual block**, not below the fold.
3. A numbered footnote — Apple’s practice, and the weakest of the three legally. A footnote under three screens of layout is not “clear and conspicuous”.

Some surfaces make this pattern **unavailable rather than merely risky**. Read `references/guardrails.md` before writing anything in a regulated, adversarial or apologetic surface: in pharmaceutical claims the qualification must be as prominent as the claim, so a hero line with a small-print footnote is structurally illegal; in litigation and outages, confidence is quoted against you.

---

## 6. Do not

- **Do not blend registers.** Marketing rhythm in an error message is not Apple style; it is the thing Apple’s guidelines explicitly forbid.
- **Do not caricature.** Superlatives and one-line fragments work at Apple’s dose and Apple’s scale — 16% of headlines, each footnoted. Three or four in a paragraph destroys all of them. **At most one stylistic device per paragraph**, and never a superlative you cannot evidence.
- **Do not stack absolutes.** `never`, `always`, `the only`, `the best` are falsifiable public commitments. In privacy, security, health, finance or legal text, prefer the hedge Apple itself uses in its footnotes.
- **Do not paraphrase protected text** to sound nicer. Product names, code, URLs, legal wording and quoted UI strings are copied exactly.
- **Do not imitate Apple under criticism.** Apple has no apology register: its iPhone 4 letter normalised the defect, reframed it, and reasserted the superlative. In an outage, a defect or a dispute, write the accountability register instead — what happened, who it affected, what is being done, by when. No reframing, no excellence, no jokes.
- **Do not carry wordplay across a language, and do not write in a language this skill does not cover.** English only: if the text is not English, stop and say so. Apple’s non-English copy is *transcreated*, not translated — `Label. Payoff.` survives translation, a pun does not, and Apple rebuilds its jokes per language rather than carrying them across.
- **Do not invent facts, numbers, or capabilities** to complete a rhythm. A missing beat is better than a false one.

---

## 7. Verify — before you deliver

Run this against your own output. Each item is checkable; if you cannot check it, you have not finished.

**Run the checker first.** It automates most of the list below and cites the source for every finding:

```bash
python3 tools/check-apple-style.py YOUR_FILE --surface editorial   # or interface | marketing | policy
```

Then confirm by hand what a machine cannot: the substantive list. Grade with `evals/rubric.md` when the text matters.

**Mechanical**
- [ ] Zero `we`, `us`, `our`, `I` as the writer (quoted text excepted).
- [ ] Zero `e.g.`, `i.e.`, `etc.`, `et al.`
- [ ] Zero banned words from §3 (grep them).
- [ ] Zero `oops`, `uh-oh`, `Click here`, `simply`, `just`, `obviously`, `easy`.
- [ ] Every action label starts with a verb.
- [ ] Serial commas present in every list of three or more.
- [ ] Curly apostrophes (`’`), not straight ones, outside code font.
- [ ] Exclamation marks: **zero** — unless the text is promotional, where Apple’s rule permits them “occasionally”. Zero is what Apple actually ships.
- [ ] No paragraph contains two stylistic devices (fragment + superlative + rule of three = caricature).

**Substantive**
- [ ] Every number, name, date, condition and hedge unchanged from the source.
- [ ] Every claim that carries a number, comparison or superlative has its evidence or its hedge attached.
- [ ] Protected text copied verbatim; nothing silently “improved”.
- [ ] The register matches the surface (§1) — you did not write marketing into an error message.
- [ ] Read aloud: no sentence that trips.
- [ ] A reader who knows nothing about the subject understands each sentence on the first pass.

**If any box fails, fix it and run the list again.** Deliver the text with a short note of what you changed and why, and say explicitly what you could not verify.

---

## 8. References — load on demand

| File | Load it when |
|---|---|
| `references/surfaces.md` | The text is a single word / short string, or you need the surface → register map for something not in the §1 table |
| `references/apple-style-guide-rules.md` | Editorial register: full rulebook, the complete substitution table, punctuation, capitalization, numbers, units, terminology, inclusive language |
| `references/ui-strings.md` | Interface register: labels, errors, alerts, onboarding, settings, empty states, permissions, alt text — with the quotes behind each rule |
| `references/marketing-register.md` | Marketing register: the pattern catalogue, the footnote system, rhythm and mechanics, guardrails, before/after transformations |
| `references/guardrails.md` | **Anything regulated, adversarial, or apologetic** — where the marketing register is illegal or irresponsible, and what to write instead |
| `references/sources.md` | You need the primary source, want to check a rule, or need to re-read Apple’s live copy |
| `tools/fetch-apple-copy.sh` | You want fresh Apple copy or HIG guidance to calibrate against — run it instead of trusting memory |
| `tools/check-apple-style.py` | Mechanical pass over your text (`--surface editorial\|interface\|marketing\|policy`). Run it before you deliver |
| `evals/rubric.md` · `evals/run.py` | You are judging output, or you want to know what “passing” means |

**The sources move.** Apple’s live copy is the calibration target, not this file’s memory of it. When a rule matters and you have network access, re-read the source: run `tools/fetch-apple-copy.sh`, or fetch the Apple Style Guide page for the rule. Cite what you checked.
