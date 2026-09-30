# Surfaces — the full map of where text lives

Every surface that carries text is in scope, down to a single string. Find your surface here, take its register, apply that register’s rulebook.

**Registers:** **M** = Marketing (`marketing-register.md`) · **I** = Interface / HIG (`ui-strings.md`) · **E** = Editorial / Apple Style Guide (`apple-style-guide-rules.md`).
**When a surface is not listed:** pick the register of the nearest listed surface; if it is genuinely ambiguous, use **E** and say so.

Rules quoted below are from Apple’s published guidance; examples marked *(Apple)* are real copy, examples marked *(shape)* are illustrations of the rule, not Apple’s words.

---

## 1. Marketing surfaces

| Surface | Reg. | What matters most | Example |
|---|---|---|---|
| Hero headline | M | One idea. A fragment may end in a period. Withhold second person. | `Ultra Retina XDR. The world’s most advanced display.` *(Apple)* |
| Hero subhead | M | Deliver the “you” the headline withheld; add the number. | `Fly through demanding AI tasks up to 6x faster.` *(Apple)* |
| Feature blurb (tile) | M | Two beats: label, then the payoff in plain words. | `Dual-battery system. All-day power.` *(Apple)* |
| Section header | M | Name the benefit, not the component. | `Longest battery life ever in a Mac.` *(Apple)* |
| Three-beat escalation | M | Label. Plain meaning. What you get. Use sparingly. | `Apple Intelligence. Works hard. You take it easy.` *(Apple)* |
| Tagline / campaign line | M | Short, memorable, no exclamation marks. Keep the period if the cadence needs it. | `Passkeys. Simple. Secure. So not a password.` *(Apple)* |
| CTA | M | Verb. No cuteness. | `Buy`, `Learn more`, `Compare` *(Apple)* |
| Footnote / disclaimer | M | Mandatory partner of any claim with a number or superlative. Opens with the method, closes with the scope. | `Testing conducted by Apple in September 2025 using preproduction…` *(Apple)* |
| Comparison-table cell | M | One dimension, one value, no sentence. | `Up to 24 hours` |
| App Store name | M | ≤30 characters. The product name only. | — |
| App Store subtitle | M | ≤30 characters. One benefit, not a sentence. | — |
| App Store promotional text | M | ≤170 characters. Changeable without review — use it for news. | — |
| App Store description / What’s New | M | ≤4,000 characters. First two lines are what everyone reads. | — |
| App Store keywords | M | ≤100 bytes total; each keyword longer than two characters, comma-separated, no spaces. | — |
| Launch email — subject | M | ≤ ~6 words; the benefit, not the announcement. | — |
| Launch email — preheader | M | Completes the subject, never repeats it. | — |
| Ad copy | M | One claim, evidence attached, hedge if the claim is comparative. | — |
| Press release | E | Apple’s newsroom register: factual, third person, quotes attributed. Not marketing rhythm. | — |
| Packaging copy | M | Space is the constraint; the benefit is the content. | — |
| Retail / signage | M | Verb or noun, no sentence. | — |
| Video script / voiceover | M | Written to be heard: shorter clauses than prose, no nested subordinate clauses. | — |
| SEO title / meta description | M | The benefit, then the differentiator. No keyword stuffing — it reads as spam, which is off-voice. | — |

*App Store limits above are verified field by field against App Store Connect Help (see `sources.md` §4.2). They are the only citable source for these numbers — the App Store Connect API specification does not carry them.*

---

## 2. Interface surfaces

All of these are governed by HIG. The three that decide most of them: **verb-first labels**, **no cuteness**, **no blame**.

| Surface | What matters most | Example |
|---|---|---|
| Button | Verb first. The action, not the outcome. | `Send` beats `Let’s do it!` *(Apple)* |
| Link | Describe the destination. Never `Click here`. | `Learn more about UX Writing` *(Apple)* |
| Tab / segmented control | Noun, parallel grammatical form across all tabs. | — |
| Menu item | Verb for actions, noun for destinations; parallel form. | — |
| Navigation title | The place, not the brand. | — |
| Field label | The thing being asked for, no sentence. | `Email` |
| Placeholder | An example of the expected format, never a label substitute. | `name@example.com` |
| Helper text | One line, states the constraint before the error. | `At least 8 characters.` |
| Error message | What happened + what to do. No blame, no interjection. | `"That password is too short"` → `"Choose a password with at least 8 characters."` *(Apple)* |
| Alert title / body | Title states the situation; body states the consequence; buttons are verbs. | — |
| Destructive confirmation | Name the thing being destroyed and the loss. No jokes. | — |
| Onboarding step | One decision per screen; label the way forward consistently. | `Get Started` … `Continue` … `Done` *(Apple)* |
| Permission prompt (pre-prompt) | State exactly what is requested and why, before the system asks. | — |
| Settings row | Label is a noun; value is the current state; description only if the label is ambiguous. | — |
| Toggle label | The state it enables, not `On`/`Off` as the label. | — |
| Empty state | What this place is for + the first action. Never a joke. | — |
| Loading / progress | Say what is happening, not that something is happening. | `Checking your library…` |
| Toast / banner | One sentence, result first. | — |
| Push notification | The value in the first 6 words; the app name is already shown. | — |
| Tooltip | The one fact the control cannot show. No repetition of the label. | — |
| Coach mark | Why this matters, in one line, skippable. | — |
| Search placeholder / no results | No results offers a next step, never just `No results`. | — |
| Column header | Shortest unambiguous noun. | — |
| Badge / chip / status | One word, a state not a feeling. | `New`, `Beta`, `Synced` |
| Alt text | What the image conveys, not “image of”. | — |
| Accessibility label / hint | Label = what it is; hint = what happens. Never duplicate the visible label. | — |
| VoiceOver announcement | A sentence a person can act on, in the order the change happened. | — |
| Siri / voice response | Written for the ear: no lists, no parentheses, no URLs read aloud. | — |
| Localization string + comment | Comment explains the context and the variables, not the meaning of the words. | — |

---

## 3. Editorial surfaces

| Surface | What matters most | Example |
|---|---|---|
| README title | The product name, exactly as capitalized. | — |
| README one-line description | One sentence, what it is and who it is for, no marketing adjectives. | — |
| Section headings | Sentence-style capitalization, parallel form, noun phrases. | — |
| API reference entry | Present tense, third person, product as subject: “Returns the…”, not “This will return…”. | — |
| Parameter / return description | State the type, the constraint, and the failure. | — |
| Code comment | Why, not what. The code already says what. | — |
| Docstring | Contract: what it does, what it takes, what it throws, what it guarantees. | — |
| Log / error message (in code) | What failed, in the log’s own vocabulary, with the identifiers a person can search. | — |
| CLI help text | One line per flag, imperative or noun phrase, no trailing period on fragments. | — |
| CLI flag description | The effect, then the default. | — |
| Changelog entry | Tense and voice consistent across the file; the user-visible change first. | — |
| Commit subject | Imperative, ≤ ~50 characters, no period. | `Add retry for idempotent requests` |
| Commit body | Why, and what it affects. Not a restatement of the diff. | — |
| PR title / description | The change and its risk; the verification steps. | — |
| Release notes | Benefit first, then the mechanism, then the known limits. | — |
| Support article title | The reader’s own words for the problem. | `Is my Apple Watch waterproof?` *(Apple)* |
| Support article body | Steps in order, one action each, condition before action. | — |
| Troubleshooting entry | Symptom → cause → fix. Cause is never the reader. | — |
| FAQ | The real question, answered in the first sentence. | — |
| Tutorial step | Imperative opener, one action, expected result shown. | — |
| Architecture doc / ADR | The decision, the alternatives rejected, and the consequence. | — |
| Runbook step | Copy-pasteable command + what success looks like. | — |
| Incident report / postmortem | Timeline in past tense, causes without blame, actions with owners. | — |
| Test name | The behaviour asserted, in the reader’s language. | `rejects a token from another tenant` |
| Schema / field description | What it holds, its units, its nullability. | — |
| Data dictionary entry | Definition, source, unit, known limits. | — |
| Config file comment | What to change and what breaks if you don’t. | — |

---

## 4. Business and general prose

| Surface | Reg. | What matters most |
|---|---|---|
| Report / findings sentence | E | Conclusion first, in plain words; method and limits in the caveat, not the sentence. |
| Metric line on a screen | E | The number in the reader’s vocabulary. No model or source words in the conclusion: `About 42% of his passes get past a defender.` — method goes in the small print. |
| Methodology / caveat note | E | State what the number is *not*. Apple’s own pattern: `This shows where the defending happens, not how hard anyone presses.` |
| Chart title | E | What is plotted, not “Chart of…”. |
| Axis label | E | Quantity + unit. Numbers on the axis stay numerals. |
| Legend / series name | E | Shortest unambiguous noun; consistent capitalization across the legend. |
| Chart caption | E | The one thing the reader should notice. |
| Dashboard empty state | I | What will appear here and how to make it appear. |
| Slide title | E | The claim, not the topic. `Pass rates fell after the rule change`, not `Pass rates`. |
| Slide bullets | E | Parallel form, one idea each, no full sentences unless the sentence is the point. |
| Internal email | E | The ask in the first two lines; the context after. |
| Chat / Slack message | E | Front-load the decision needed; no “hey team”. |
| Meeting notes | E | Decisions and owners, not a transcript. |
| Memo / proposal | E | Recommendation first, then the reasoning, then the cost. |
| Job posting | E | The work, concretely. No “rockstar”, no “ninja” — those are idioms and clichés. |
| Performance review | E | Observable behaviour, not adjectives; no absolutes (`always`, `never`). |
| Announcement | E | What changes for the reader, first. |
| Support reply | I | Acknowledge the state, give the next action, no blame, no canned cheer. |
| Postmortem | E | As above; the language must survive being read by the person who caused it. |

**Apple’s own caution here:** press releases and support articles are *editorial*, not marketing — Apple’s Korean releases even switch to a different sentence-ending register from its marketing. Do not import marketing rhythm into these surfaces.

---

## 5. Legal, policy and trust surfaces

| Surface | Reg. | What matters most |
|---|---|---|
| Terms / policy summary | E | Plain language for the summary; the operative wording is protected text and is never reworded. |
| Privacy notice | E | Specific and falsifiable. Never `we never`, `we always` unless it can be defended line by line. |
| Privacy label (data types) | E | A noun, exactly the category’s official name. |
| Consent / cookie banner | I | The choice, then the consequence. Never a dark pattern; never pre-checked language. |
| Security advisory | E | Affected versions, impact, action, credit. No euphemism: “an attacker can read the file”, not “a security situation”. |
| Account / data deletion flow | I | What will be lost, what is kept, how long it takes. No jokes. |
| Billing / invoice line item | E | The charge in the customer’s words, not the internal SKU. |
| Eligibility / age notice | E | The condition, then the alternative. |
| Refund / cancellation policy | E | The rule, the exception, the time limit — in that order. |

**In these surfaces the style is a liability, not an asset.** Apple’s confident register is defensible only because Apple footnotes it; here, prefer the hedge Apple itself uses in footnotes (`Not all devices are eligible`) over the absolutism it uses in heroes. See `marketing-register.md` §Guardrails.

---

## 6. One word, and other micro-surfaces

A single string is still a writing decision, and the register of the surface still applies.

| Surface | Reg. | The decision |
|---|---|---|
| Product / feature name | M | Capitalize exactly as the owner does. Never shorten, never pluralize into a common noun, never use a trademark as a verb. |
| Status word | I | A state the user recognizes: `Synced`, `Offline`, `Waiting`. Never `Oops` or `Uh-oh`. |
| Badge text | I | One word, factual: `New`, `Beta`, `Updated`. |
| Category name | E | The noun a user would search for, not the internal taxonomy. |
| CLI subcommand | E | A verb: `deploy`, `verify`, `rollback`. |
| CLI flag | E | Consistent convention across the tool; description states effect + default. |
| Error code + short description | E | Code is protected text; the description is one line stating the cause. |
| Enum value shown in UI | I | A label, not `STATUS_PENDING`; keep the serialized value untouched. |
| Email subject (2–3 words) | M | The benefit or the news, never both. |
| File / folder name in a UI | I | What it holds, in the user’s vocabulary. |
| Toggle on/off label | I | The thing being switched, not `On`/`Off`. |
| Chart series label | E | ≤ 3 words, unambiguous, parallel with its siblings. |
| Keyboard shortcut description | E | The verb, matching the menu item it triggers exactly. |
| Hashtag / handle | M | Readable as words; no forced camelCase that hides meaning. |
| Placeholder / sample name | E | Obviously fictional, culturally neutral, never a real person’s name. |

**Micro-surface checklist:** is this word the one the reader already uses? Is it a noun when it names a thing and a verb when it does a thing? Would it survive being translated? Does it stay correct at 30% of its allotted width, or in a language twice as long as English? Apple’s guide: “Keep localization in mind” — assume every string you write will be translated, because it will.
