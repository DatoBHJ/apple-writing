# The marketing register

Apple’s marketing copy is the one register Apple does **not** publish a rulebook for. The Apple Style Guide covers “instructional materials, technical documentation, reference information, training programs, and user interfaces” and then says, in Apple’s own words: “Some departments at Apple (Marcom, for example) have supplemental style guides.” Marcom’s guide is not public. Everything below is reverse-engineered from live copy that was fetched and quote-checked, sentence by sentence.

**This register is a documented departure from Apple’s published rules, not an application of them.** The Style Guide says a sentence fragment takes “no ending punctuation”; 92% of Apple’s own marketing headlines are fragments that end in a period. Read this file as the Marcom supplement, and read `apple-style-guide-rules.md` as the baseline it departs from.

> **Two things are true at once, and this file teaches both.** The patterns below are why Apple’s copy works. The same patterns, used without the evidence apparatus that surrounds them on apple.com, are how companies get fined. The `Do not` section below is not optional reading — a hero line written from §1 without §3 and the `Do not` section is a liability with good rhythm.

---

## 0. Samples — what every number in this file counts

There is no sitewide claim anywhere in this file. Apple publishes thousands of pages; these are the ones measured.

| Sample | Definition | n | Where it comes from |
|---|---|---|---|
| **A-hero** | Hero, section and card headlines, five EN product pages, deduplicated | **83** | Corpus A (prior session) |
| **A-two** | Subset of a headline pool matching `X. Y.` | **38** | Corpus A |
| **A-body** | `<p>` elements ≥8 words, ten EN pages, deduplicated | **568** | Corpus A |
| **A-sent** | Sentence-split of `<h1>`–`<h4>`, `<p>`, `<li>` ≥3 words, same ten pages | **4,638 sentences / 80,882 words** | Corpus A |
| **A-fn** | Every `<li id="footnote-*">` on `/macbook-pro/` | **59** | Corpus A |
| **B-head** | Headline-class strings, **17 marketing pages**, deduplicated | **790** | Corpus B (this file) |
| **B-para** | `<p>` elements ≥8 words, same 17 pages | **841** | Corpus B |
| **B-sent** | Sentence-split of B-head + B-para + B-fn, ≥3 words, **excluding App Store customer reviews** | **2,062 sentences / 25,916 words** | Corpus B |
| **B-fn** | Every `<li id="footnote-*">` across those 17 pages | **240** (239 with text) | Corpus B |
| **B-5page** | Headline strings on the same five product pages A-hero used | **332** | Corpus B |

**Corpus A** = the measurement set in `research/03-voice-systems-and-corpus.md`. **Corpus B** = 20 URLs fetched for this file on 2026-09-30 with `curl` + a desktop User-Agent (19 carried usable copy; `apple.com/newsroom/` served an index shell with no body prose). Corpus B pages: `/macbook-pro/`, `/ipad-pro/`, `/airpods-pro/`, `/apple-vision-pro/`, `/apple-intelligence/`, `/privacy/`, `/iphone/`, `/mac/`, `/watch/`, `/accessibility/`, `/environment/`, `/shop/trade-in`, `/support/products/`, `/apple-card/`, `/apple-one/`, `/icloud/`, the Apple Music App Store listing, plus two support articles.

**How to read a count.** `76/83` means 76 of the 83 headlines in that sample. It does not mean 92% of apple.com. Where Corpus A and Corpus B disagree, both numbers are given and the disagreement is named.

**Retrieval hazard — read this before you scrape.** Apple’s HTML emits a start-frame and an end-frame copy of scroll-animated text. Naive extraction produces `track track you.` and `Read Read, , delete, delete , and reply with peace of mind.` Those are extraction artifacts, **not Apple typos**. The real strings are `Decide which apps are allowed to track you.` and `Read, delete, and reply with peace of mind.` Deduplicate before quoting. `web_fetch` returns nav chrome only on these pages; `curl` works.

---

## 1. The core pattern

### 1.1 One idea per line

Everything in this register follows from one constraint: **each line carries exactly one idea, and the line ends when the idea does.** A line is not a sentence in the grammatical sense — it is a beat. `Ultra Retina XDR.` is a beat with no verb. `The world’s most advanced display.` is the next beat. They are two lines that happen to be set on one row.

The consequence for a writer: you stop asking “how do I fit this into a sentence” and start asking “how many ideas do I have.” Two ideas → two beats. Three ideas → three beats, and the third is where the reader’s benefit lives.

The other consequence: **beats are separated by periods, even when a beat is a fragment.** This is the register’s single most visible departure from the Apple Style Guide, which says fragments take no ending punctuation. Marketing headlines take the period anyway, because the period is what makes the beat a beat.

### 1.2 The two-beat: `Label. Payoff.`

The base pattern. Name the thing, then say what it buys the reader.

| | Headline | Source |
|---|---|---|
| 1 | `Ultra Retina XDR. The world’s most advanced display.` | <https://www.apple.com/ipad-pro/> |
| 2 | `Magic Keyboard. Precision at your fingertips.` | <https://www.apple.com/ipad-pro/> |
| 3 | `Built for AI. From the silicon up.` | <https://www.apple.com/macbook-pro/> |
| 4 | `All-day battery life. Think outside the outlet.` | <https://www.apple.com/macbook-pro/> |
| 5 | `A workspace with infinite space.` | <https://www.apple.com/apple-vision-pro/> |
| 6 | `The ultimate theater. Wherever you are.` | <https://www.apple.com/apple-vision-pro/> |

**Measured.** 38 headlines in A-hero match the two-part shape, and **30 of those 38 lead with a product or technology noun followed by a period** — the `Label. Payoff.` form specifically, not just “any two sentences.” In Corpus B, **83 of 790 headline strings (11%) are exactly two period-terminated beats** and **19 are exactly three**. Two-beat is the base rate; three-beat is the variation.

The label in beat one is usually a **noun the reader already half-knows** — a feature name, a technology, a category. Beat two is the payoff, and it is usually where the second person or the human detail goes.

### 1.3 The three-beat: `Label. Plain meaning. What you get.`

The form that does the most work, and the one worth teaching explicitly. Three beats, three jobs:

1. **Label** — the thing, in the reader’s vocabulary, not engineering’s.
2. **Plain meaning** — the label translated into ordinary words, with the number in it if there is a number.
3. **What you get** — the human consequence, often short, often funny, often in second person.

| | Headline | Beats | Source |
|---|---|---|---|
| 1 | `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` | label / number / human close | <https://www.apple.com/macbook-pro/> |
| 2 | `Apple Intelligence. Works hard. You take it easy.` | label / function / benefit | <https://www.apple.com/ipad-pro/> |
| 3 | `M5 chip. Furiously fast. The next giant leap for AI on iPad.` | label / plain meaning / what you get | <https://www.apple.com/ipad-pro/> |
| 4 | `iPadOS. Powerfully redesigned. Game-changing capabilities.` | label / meaning / payoff | <https://www.apple.com/ipad-pro/> |
| 5 | `Introducing Siri AI. Truly helpful. Truly yours.` | label / function / reassurance | <https://www.apple.com/apple-intelligence/> |
| 6 | `Design. A powerhouse of portability.` | label / payoff (two-beat minimum) | <https://www.apple.com/ipad-pro/> |

**Measured.** Roughly a fifth of the two-part headlines in A-two extend to three or four beats. In Corpus B, 19/790 are exactly three period-terminated beats. **Treat the tricolon as a spice, not a base** — a page where every headline has three beats reads as a metronome.

Beat three is the beat that gets cut first when a writer is unsure, and it is usually the beat that should stay. `Longest battery life ever in a Mac. Up to 24 hours.` is a spec. `Hit the road, Mac.` is the reason anyone cares.

### 1.4 The blurb is the same pattern, one size down

A feature blurb — the paragraph under a tile — is the three-beat pattern with the beats run together:

> `Sound quality. A new multiport acoustic architecture for deeper bass, a wider soundstage so you hear every note, and stunningly vivid vocal clarity.`
> — <https://www.apple.com/airpods-pro/>

> `Fit and feel. The ear tips are now rotated inward for a more secure fit, and a new layer of foam-infused microspheres increases noise cancellation.`
> — <https://www.apple.com/airpods-pro/>

> `Heart rate sensing. Our smallest heart rate sensor ever pulses invisible light to give you accurate workout metrics from the gym to the track.`
> — <https://www.apple.com/airpods-pro/>

Label (a noun phrase, period). Then one sentence of plain meaning. Note what is **absent**: no “Introducing,” no “Our revolutionary new,” no adjective before the noun in beat one. The label is bare and the adjectives are spent in beat two, where they are attached to something the reader can picture — `deeper bass`, `a wider soundstage`, `from the gym to the track`.

### 1.5 The assembly order

Write in this order. It is the order the evidence supports, and it prevents the most common failure (a punchy line with nothing behind it).

1. **Decide the surface.** Marketing register is for surfaces whose job is desire: product page, landing hero, app-store listing, launch email, ad, tagline. If the text is a button, an alert, a setting or legal notice, you are in the wrong file — see `ui-strings.md` and `apple-style-guide-rules.md`.
2. **Write the claim as a fact first, in flat prose, with its number.** `Battery lasts up to 24 hours.` No rhythm yet.
3. **Find the evidence.** What test, what conditions, what sample, what caveats? If you cannot produce it, **change the claim** — do not add a hedge. An `up to` with no test behind it is an unsubstantiated claim wearing a cautious costume. See §3 and the `Do not` section.
4. **Write beat one as the bare label.** Strip every adjective. `Longest battery life ever in a Mac.`
5. **Write beat two as the number or the plain meaning.** `Up to 24 hours.`
6. **Write beat three as the human consequence.** Short. Concrete. This is the only beat allowed to be funny. `Hit the road, Mac.`
7. **Write the footnote to the same claim**, using the skeleton in §3.4. A claim and its footnote are one unit of work, not two.
8. **Read it aloud.** If beat three is doing work beat two already did, cut it.

---

## 2. Pattern catalogue

Twelve named patterns. Each one: the shape, two real examples with their URLs, when it earns its place, and when it backfires.

Two of the names below describe devices also catalogued elsewhere under other names (a two-part boast, a three-item rhythm, a turn on a contrast). The names here are this file’s own, and the examples are all drawn directly from the pages cited.

---

### P1 · Two-Beat Close

**Shape.** `[Bare label]. [Payoff].` — a noun or feature name, period, then what it does for the reader.

| Example | Source |
|---|---|
| `Nano-texture glass. Brilliant in any light.` | <https://www.apple.com/ipad-pro/> |
| `Carry one thing. Everything.` | <https://www.apple.com/apple-card/> |
| `Fast that lasts.` | <https://www.apple.com/iphone/> |
| `Sleek profile. Chic protection.` | <https://www.apple.com/ipad-pro/> |

**Use when** the thing has a name the reader will meet again — a feature, a material, a mode — and you need one row of copy. This is the highest-yield pattern in the register and the one to reach for first.

**Backfires when** beat one is not a real label. `Innovation. Reimagined.` has the shape and none of the content: the reader learns nothing and the period on `Innovation` reads as a drumbeat with no drum. If beat one could be deleted without loss, it was never a label.

---

### P2 · Three-Beat Ladder

**Shape.** `[Label]. [Plain meaning]. [What you get].` — the third beat is the human one.

| Example | Source |
|---|---|
| `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` | <https://www.apple.com/macbook-pro/> |
| `Apple Intelligence. Works hard. You take it easy.` | <https://www.apple.com/ipad-pro/> |
| `M5 chip. Furiously fast. The next giant leap for AI on iPad.` | <https://www.apple.com/ipad-pro/> |

**Use when** a hero or section opener has to carry a technology, a number and a feeling, and you have one row to do it in. Use it **once or twice per page**, not on every tile.

**Backfires when** the ladder is used as a default. Three beats on every headline makes the page sound like a chant, and the reader stops hearing beat three — which is the whole point of the pattern. It also backfires when beat three is another spec rather than a consequence (`Faster. Better. More efficient.`).

---

### P3 · Named Number

**Shape.** `[Claim] [up to] [numeral]x [more|faster|longer] [than the thing being compared].` The number is the content of the sentence, not decoration on it.

| Example | Source |
|---|---|
| `Fly through demanding AI tasks up to 6x faster.` | <https://www.apple.com/macbook-pro/> |
| `Up to 2x more than AirPods Pro 2.` | <https://www.apple.com/airpods-pro/> |
| `Get up to $1200 in credit on a new iPhone after trade-in.` | <https://www.apple.com/iphone/> |
| `Made with 40% recycled material by weight.` | <https://www.apple.com/airpods-pro/> |

**Use when** you have a real measurement and a real comparison baseline. `6x faster` is only meaningful against a stated predecessor, and Apple always states it — in the footnote if not in the line.

**Backfires when** the number has no baseline, no test, or no footnote. `10x faster` with nothing behind it is the single most common way a company turns a defensible claim into a deceptive one. See `Do not`, F1. A number is not evidence; a number is a claim that requires evidence.

---

### P4 · Human Close

**Shape.** `[Spec or fact]. [Short human sentence].` The second beat drops the register on purpose.

| Example | Source |
|---|---|
| `Easily share what you’re watching or listening to with a friend. Just bring their AirPods near the iPhone, iPad, or Apple TV you’re connected to. And voilà.` | <https://www.apple.com/airpods-pro/> |
| `Trade in. Upgrade. Save. Or recycle it for free.` | <https://www.apple.com/shop/trade-in> |
| `MacBook Pro has the longest battery life ever in a Mac — up to 24 hours — so you can work, create, and play all day.` | <https://www.apple.com/macbook-pro/> |

**Use when** the preceding sentence is technical, numeric or long. The close works because of the contrast; it is a *release*, and a release needs tension before it.

**Backfires when** it is used without the setup. `And voilà.` after a short plain sentence is just a shrug. It also backfires in a language or market where the casual particle has no equivalent — this beat is the one that localizes worst, and it must be rebuilt rather than translated.

---

### P5 · Hedge-and-Evidence Pair

**Shape.** Hedged claim in the headline → methodology footnote in the small print. **The two are one object.** The hedge is only honest when the evidence ships with it.

| Example | Source |
|---|---|
| `Fly through demanding AI tasks up to 7.8x faster.` + footnote 8 | <https://www.apple.com/macbook-pro/> |
| `Get up to 8 hours of listening time with Active Noise Cancellation on a single charge.` + footnote 3 | <https://www.apple.com/airpods-pro/> |

The matching footnote, verbatim, from the same page:

> `Testing conducted by Apple in September 2025 using preproduction 14-inch MacBook Pro systems with Apple M5, 10-core CPU, 10-core GPU, 32GB of unified memory, and 4TB SSD… Time to first token measured with a 16K-token prompt using an 8-billion parameter model with 4-bit weights and FP16 activations, mlx-lm, and prerelease MLX framework. Performance tests are conducted using specific computer systems and reflect the approximate performance of MacBook Pro.`
> — <https://www.apple.com/macbook-pro/>

**Use when** the claim involves a measurement, a comparison, a conditional, or a number that varies by configuration. `Up to` is the register’s standard hedge and it appears on `6x`, `7.8x`, `1.5x`, `24 hours`, `8 hours`, `$1200`, `2x`, `3x`, `4 more hours` — always with a footnote marker.

**Backfires when** the hedge is copied and the evidence is not. `Up to 3x faster` with no test conditions is not a cautious claim; it is an unsubstantiated one wearing a cautious costume, and the `up to` makes it *look* more defensible than it is. That is worse than the unhedged version, because it is a claim about evidence you do not have. See `Do not`, F2.

---

### P6 · Reassurance by Negation

**Shape.** `[Subject] [does the helpful thing]. Not [the invasive thing].` Or, compressed: `[Product] [verb]s your [thing], not your [other thing].`

| Example | Source |
|---|---|
| `Siri learns what you need. Not who you are.` | <https://www.apple.com/privacy/> |
| `Maps knows your route, not your profile.` | <https://www.apple.com/privacy/> |
| `Our apps mind their business. Not yours.` | <https://www.apple.com/privacy/> |
| `Your business is nobody else’s.` | <https://www.apple.com/mac/> |

**Use when** the product’s virtue is an *absence* — no tracking, no fee, no account required, no data leaving the device. Negation is the only grammatical shape that states an absence, which is why privacy copy is the one place this voice is allowed to be negative.

**Backfires when** the negation is absolute and you cannot defend every word. `Siri learns what you need. Not who you are.` is a beautiful sentence and a falsifiable public commitment. In a regulated domain — health, finance, children’s data, anything under GDPR — an absolute `never`, `not` or `nobody` is a promise the company can be held to and, in most organisations, cannot actually keep. Write the negation only for a property you can demonstrate end to end, and put the boundary in the footnote. When in doubt, use the hedge Apple itself uses in its small print (`Not all devices are eligible`, `varies by use and configuration`) rather than the absolutism it uses in its heroes.

---

### P7 · Second-Beat Swerve

**Shape.** `[Straight setup]. [Turn].` Beat one reads like a normal product claim; beat two reveals it was a joke, a pun, or a withheld verb, and the joke restates the benefit.

| Example | Source |
|---|---|
| `Happily ever faster.` | <https://www.apple.com/macbook-pro/> |
| `OLED it shine.` | <https://www.apple.com/ipad-pro/> |
| `The best thing you’ve never heard.` | <https://www.apple.com/airpods-pro/> |
| `They’re workin' 9 to 5.` | <https://www.apple.com/airpods-pro/> |
| `Fast runs in the family.` | <https://www.apple.com/macbook-pro/> |
| `Magic to your ears.` | <https://www.apple.com/airpods-pro/> |

**Use when** the claim itself is unremarkable and the *memorability* is the deliverable — a tagline, a section opener, an ad. The pun must restate the benefit; every example above does. `OLED it shine.` is about a display that shines. `Fast runs in the family.` is about a chip family that is fast.

**Backfires when** the pun is doing the work the claim should be doing, or when the audience is not the audience for wordplay. This is the highest-variance pattern in the register: it is the reason people quote Apple’s copy, and it is the reason almost every imitation of Apple’s copy reads as parody. **One swerve per page.** Two is a comedy routine.

---

### P8 · Plain-Language Gloss

**Shape.** `[Technical term] — [everyday list of what that means].` Em dash, then the translation, closed up with no surrounding spaces.

| Example | Source |
|---|---|
| `Do more with Apple Intelligence — from Image Wand to Live Translation.` | <https://www.apple.com/ipad-pro/> |
| `Perform hundreds of actions — from sending a message to taking down a note — all within Spotlight.` | <https://www.apple.com/macbook-pro/> |
| `iPad Pro comes in two great finishes — Silver and Space Black.` | <https://www.apple.com/ipad-pro/> |

**Use when** the sentence has to contain a term of art that the reader does not own. The gloss is not a definition; it is a *list of instances* the reader recognises. `Live Translation` and `Image Wand` are not explanations of Apple Intelligence — they are proof that it does something.

**Backfires when** the gloss is a restatement instead of an instance (`Machine learning — the power of AI.`), or when the dash is doing work a period should do. Apple’s rule for the punctuation is explicit: “Use the em dash (—) to set off a word or phrase that interrupts or changes the direction of a sentence… Don’t overuse em dashes.” (Apple Style Guide.) Closed up on both sides.

---

### P9 · Fact, Not Fault

**Shape.** `[State the true situation]. [Name the exception or limit].` No blame, no apology, no interjection, no explanation of what the reader did wrong.

This is the pattern that sits **on the boundary of the marketing register**. It is Apple’s dominant shape in support copy and error messages, and it is the shape to use when marketing copy has to deliver bad news (a limit, an expiry, a regional restriction).

| Example | Source |
|---|---|
| `Your Apple Watch is water resistant, but not waterproof.` | <https://support.apple.com/en-us/109522> |
| `You might’ve bought the subscription from another company.` | <https://support.apple.com/en-us/118428> |
| `Siri AI is rolling out in English. Usage limits may apply.` | <https://www.apple.com/privacy/> |
| `Available in select languages and regions. For more information, see Feature Availability.` | <https://www.apple.com/airpods-pro/> |

**Use when** the reader will be disappointed or confused and you need them to keep reading. The first sentence grants the true fact; the second names the limit without implying the reader is at fault. Note `You might’ve bought the subscription from another company.` — the correction is delivered as a *possibility about the world*, not a judgement about the reader.

**Backfires when** it is written in the marketing register instead. Apple’s own published UI guidance forbids it: “avoid blame,” no “oops!” or “uh-oh,” and “avoid the temptation to be too cute or clever.” A cheerful line on a failed payment is not Apple style — it is the opposite of Apple’s documented style for that surface. See `Do not`, F6.

---

### P10 · Condition Up Front

**Shape.** `[Requires|Available|Varies by|Subject to] [the condition].` A subject-less, terse caveat sentence, usually in the footnote — occasionally in the body when the condition is the actual news.

| Example | Source |
|---|---|
| `Requires that your iPhone and Mac are signed in with the same Apple Account using two-factor authentication…` | <https://www.apple.com/macbook-pro/> |
| `Battery life varies by use and configuration; see apple.com/batteries for more information.` | <https://www.apple.com/macbook-pro/> |
| `Wi-Fi 7 available in countries and regions where supported.` | <https://www.apple.com/macbook-pro/> |
| `Port configuration varies by model.` | <https://www.apple.com/macbook-pro/> |
| `In temperatures less than 25° C.` | <https://www.apple.com/macbook-pro/> |

**Use when** a claim is true only under conditions. Put the condition where the claim is, not in a general disclaimer at the bottom of the page.

**Backfires when** the condition is buried far from the claim, or when the condition contradicts the hero. `Up to 24 hours` in the hero and `In temperatures less than 25° C` fourteen footnotes away is defensible only because both are on the same page and numbered. The condition belongs to the claim; separate them and you have a headline that says one thing and small print that says another.

**Measured.** In B-fn (240 footnotes across 17 pages), the caveat markers are: `subject to` 45, `for more information` 27, `see ` 26, `Available` 20, `Requires` 13, `up to`/`Up to` 16, `varies by` 11, `Not all` 9. In A-fn (59 footnotes): `for more information` 7, `varies by` 5, `subject to` 4.

---

### P11 · Escalating Tercet

**Shape.** `[One]. [Two]. [Three].` Three short fragments, each a step up in specificity or commitment, often imperatives.

| Example | Source |
|---|---|
| `M5. Creator. Accelerator.` | <https://www.apple.com/ipad-pro/> |
| `Trade in. Upgrade. Save. Or recycle it for free.` | <https://www.apple.com/shop/trade-in> |
| `Go fast. Go far.` | <https://www.apple.com/mac/> |
| `Mmmmm. Power.` | <https://www.apple.com/ipad-pro/> |

**Use when** the page needs one line that a reader could repeat from memory, and the three items form a real progression. `Trade in. Upgrade. Save.` works because it is the actual sequence of the transaction — and then the fourth beat (`Or recycle it for free.`) breaks the rhythm to include the reader who is not buying.

**Backfires when** the items do not escalate. `Fast. Powerful. Beautiful.` is an adjective list with periods, and it is the shape most often mistaken for Apple’s voice by writers who have noticed the periods and not the progression. Note that Apple’s own style guide says “Don’t overuse” this effect — a tercet loses its force on the second appearance in a row.

---

### P12 · Values Close

**Shape.** `[A short, calm sentence about principles or consequences].` No product name, no number, no benefit. Used as an end-of-page or end-of-section beat.

| Example | Source |
|---|---|
| `Our values lead the way.` | <https://www.apple.com/airpods-pro/> |
| `Privacy. That’s Apple.` | <https://www.apple.com/privacy/> |
| `A plan as innovative as our products.` | <https://www.apple.com/airpods-pro/> |
| `Our planet deserves our best thinking.` | <https://www.apple.com/environment/> |
| `Innovation that’s accessible by design.` | <https://www.apple.com/accessibility/> |

**Use when** a section has been dense with specification and needs to return to why any of it matters. Placed at the end, it functions as a cadence.

**Backfires when** it is used as a substitute for evidence. `Our values lead the way.` on apple.com sits above an environment section containing specific numbers. As a *section closer* it is a cadence; as a *claim* it is empty. If your organisation cannot show the numbers, do not write the cadence — a values line with nothing under it reads as an admission.

---

## 3. The footnote system

**This section is mandatory, never optional.** Apple’s headline patterns are lawful *because* of the footnote apparatus around them. The FTC’s advertising guidance states the obligation plainly: “Advertising must be truthful and non-deceptive; Advertisers must have evidence to back up their claims; and Advertisements cannot be unfair” (<https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business>). The footnote is where the evidence lives. A skill that teaches the headline without the footnote teaches the half that gets companies fined.

### 3.1 Claim and footnote are ONE unit

Write them together or not at all. Every performance headline in the corpus carries a marker, and the marker resolves to a methodology disclosure:

> `Fly through demanding AI tasks up to 6x faster.¹` — headline, <https://www.apple.com/macbook-pro/>
> `¹ Testing conducted by Apple in September 2025 using preproduction 14-inch MacBook Pro systems with Apple M5… Time to first token measured with a 16K-token prompt using an 8-billion parameter model with 4-bit weights and FP16 activations, mlx-lm, and prerelease MLX framework. Performance tests are conducted using specific computer systems and reflect the approximate performance of MacBook Pro.` — footnote 1, same page

The words `preproduction`, `(Beta)` and `prerelease` appear in the small print and never in the hero. That is the point of the apparatus: the hero makes the promise legible, the footnote makes it checkable.

### 3.2 Measured footnote statistics

| Measure | Corpus A (n=59, `/macbook-pro/`) | Corpus B (n=240, 17 pages) |
|---|---|---|
| Footnotes on the page | 59 | 240 across 15 pages (5–59 per page) |
| **Opening template**: `Testing conducted by Apple in…` | **40/59 (68%)** | **53/240 (22%)** |
| **Closing template**: `Performance tests are conducted using specific computer systems and reflect the approximate performance of…` | **36/59 (61%)** | **36/240** — all 36 are on `/macbook-pro/` |
| Shortest | **5 words** (`In temperatures less than 25° C.`) | **3 words** (`Accessories sold separately.`) |
| Median length | **100 words** | **66 words** (101 on `/macbook-pro/`, re-counted) |
| Longest | **694 words** (the Apple Upgrade lease footnote) | **710 words** re-counted on the same page; **8,909 words** for `footnote-13` on `/apple.com/iphone/` (a carrier installment block) |
| Footnotes containing digits | 51/59 | — |

The two samples measure the same `/macbook-pro/` page at different times and with different tokenizers, which is why the median reads 100 in one and 101 in the other and the lease footnote reads 694 and 710. **Treat those as the same measurement, not two findings.** The distribution is what matters, and it is not bell-shaped:

| Length band | Footnotes in B-fn (n=239 with text) |
|---|---|
| < 20 words | 47 |
| 20–49 | 58 |
| 50–99 | 54 |
| 100–199 | 59 |
| 200–399 | 9 |
| 400+ | 13 |

**Bimodal, not short.** The same page carries `In temperatures less than 25° C.` (6 words) and a 710-word consumer lease. A skill that says “keep footnotes short” is wrong about this register. The rule is: **the footnote is exactly as long as the obligation it discharges** — no shorter, and no longer than the claim requires.

### 3.3 The two dominant sentence templates

**Opening — the methodology sentence.** 40/59 on `/macbook-pro/`; 53/240 across Corpus B. Skeleton:

```
Testing conducted by Apple in [Month(s) Year] using [preproduction|production]
[device description] with [chip], [core counts], [memory], and [storage],
as well as [comparison device], all configured with [shared config].
```

Real instance (<https://www.apple.com/macbook-pro/>):

> `Testing conducted by Apple in September 2025 using preproduction 14-inch MacBook Pro systems with Apple M5, 10-core CPU, 10-core GPU, 32GB of unified memory, and 4TB SSD, as well as production 14-inch MacBook Pro systems with Apple M4, 10-core CPU, 10-core GPU, and 32GB of unified memory, and production 13-inch MacBook Pro systems with Apple M1, 8-core CPU, 8-core GPU, and 16GB of unified memory, all configured with 2TB SSD.`

**Closing — the approximation sentence.** 36/59 on `/macbook-pro/` (and nowhere else in Corpus B). It is one fixed sentence with one slot:

```
Performance tests are conducted using specific computer systems and
reflect the approximate performance of [Product Name].
```

Note the shape of both: **subject-less or impersonal, past tense, no adjectives, full device configuration, and the comparison device named.** The section between them carries the actual test conditions — the prompt size, the model, the framework version. That middle section is the part that makes the claim checkable, and it is the part imitators always drop.

### 3.4 Reusable footnote skeleton

Fill every slot you can. **Leave a slot empty only when the answer genuinely does not apply — and never leave `What was measured` or `Conditions` empty, because those two are the disclosure.**

```
[Marker] [What was measured] — [the number and its unit].
Tested by [who ran the test] in [Month(s) Year] using
[preproduction | production] [exact device/model], [chip or engine],
[memory / capacity], running [software + version, + "(Beta)" if applicable],
compared with [exact comparison device or baseline], configured identically except where noted.
Measured as [the precise procedure: input size, dataset, method, repetitions].
[What varies and how] — for example: "Battery life varies by use and configuration."
[Eligibility or availability limit], e.g. "Available in countries and regions where supported."
[Where to read more], e.g. "See apple.com/batteries for more information."
[The approximation sentence, if the claim is a performance comparison.]
```

Worked example of the skeleton filled in for a claim a company could actually defend:

```
* Latency measured as median time to first response over 200 requests
from a 16K-token prompt on a 2024 laptop with 16GB unified memory
and a 1TB SSD, running version 3.2 (Beta) of the client, compared with
version 3.0 of the same client on identical hardware and network conditions.
Network latency varies by connection. Available in regions where the
service is offered; see example.com/regions for more information.
Performance tests are conducted using specific devices and reflect the
approximate performance of Example App.
```

### 3.5 Three footnote failure modes

1. **The hedge without the evidence.** `up to 3x faster` and no test conditions. This is not a cautious claim; it is an unsubstantiated one, and it is worse than the unhedged version because it implies a test exists.
2. **The footnote as decoration.** Copying `Performance tests are conducted using specific computer systems and reflect the approximate performance of…` into a document that has no performance tests converts a disclosure into a false statement. The template is not a style; it is a factual assertion with slots.
3. **The disclosure nobody can read.** A 710-word lease footnote and an 8,909-word carrier footnote are legally careful and communicatively useless. If your obligation is 700 words long, the honest move is not to bury it — it is to **change the claim** so the obligation is short enough for the reader to act on. See `Do not`, F4.

---

## 4. Rhythm and mechanics

Measured facts only. Where Corpus A and Corpus B disagree, both are given.

### 4.1 Headlines end with a period

**Measured.** 76/83 = **92%** of headlines in A-hero end with a period. In Corpus B’s re-fetch of the same five pages, **63%** of all 332 headline strings on those same pages end with a period, rising to **74%** when the sample is restricted to headline strings of three words or more.

The two numbers describe the same rule. Stated properly:

> **If the headline is a sentence or a clause, it takes a period. If it is a noun phrase used as a label, it does not.**

The no-period minority in the fresh sample is almost entirely: product names (`MacBook Pro`, `iPad Air`, `iPhone 17`), navigation and eyebrow labels (`Recycled Material`, `Renewable Electricity`, `Ways to Buy`), and card titles (`Sound quality.` — which does take a period — alongside `Hearing Health`).

This is the register’s clearest break with Apple’s published baseline. The Apple Style Guide’s rule for callouts and captions is “Use sentence-style capitalization. Use a period for a complete sentence and no ending punctuation for a sentence fragment.” Marketing takes the period on the fragment anyway.

### 4.2 Zero exclamation marks

**Measured. 0 / 4,638 sentences** in A-sent. The only two `!` characters on all ten pages are inside the film title `Deaf President Now!` (Apple accessibility page). Corpus B reproduces this exactly: of **2,062 marketing sentences**, the only `!` characters are the same two, inside the same film title. Every other `!` in the fetched HTML was in **customer reviews** on the App Store listing — user-generated content, not Apple copy.

Apple’s own rule permits them: “OK to use exclamation points occasionally in promotional text and dialogue. Avoid in documentation.” (Apple Style Guide.) Apple permits and does not use. **Write zero.** This is one of the few near-absolute rules available in this register, and it is worth more than it looks: an exclamation mark is the cheapest way to make confident copy sound desperate.

### 4.3 Second person: in the paragraph, not the headline

**Measured.**

| Sample | `you`/`your` present |
|---|---|
| A-body (568 paragraphs) | **344 = 61%** |
| A-hero (83 headlines) | **18 = 22%** |
| B-para (841 paragraphs) | **464 = 55%** |
| B-head (790 headline strings) | **107 = 14%** |

The asymmetry is the rule, and it is not “always say you.” It is: **name the thing in the headline, and hand it to the reader in the paragraph.**

> `Magic Keyboard. Precision at your fingertips.` — headline names the product, beat two addresses the hand. <https://www.apple.com/ipad-pro/>
> `Apple Intelligence. Works hard. You take it easy.` — three beats, and `you` appears only in the third. <https://www.apple.com/ipad-pro/>

Contrast with Apple’s *published* UI guidance, which pulls the other way: “Use possessive pronouns sparingly… 'Favorites' conveys the same message as 'Your Favorites,' and is more succinct.” Both are correct for their surface. The marketing register wants the reader in the second sentence; the interface register wants them out of the label.

### 4.4 Sentence length

**Measured.** A-sent: mean **17.4** words, median **14**. Corpus B: mean **12.6**, median **11** (marketing surfaces, excluding App Store reviews).

Both numbers are honest and they measure different corpora. A-sent includes legal boilerplate, which pulls the mean up; Corpus B’s B-sent is marketing surfaces only. The defensible statement: **Apple’s marketing prose sits in the low-to-mid teens, with a median around 11–14 words, and the mean is inflated wherever legal text is included in the sample.** The distribution is right-skewed — B-sent has a p90 of 23 words and a maximum of 94.

The teaching point is not the average. It is the **variance within a single unit**: a 40-word methodology footnote next to a 3-word headline is normal here, and a page of uniformly 12-word sentences reads like a metronome.

### 4.5 Numerals

Apple’s documented rules, from the Apple Style Guide (<https://support.apple.com/guide/applestyleguide/welcome/web>; PDF: <https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf>):

| Rule | Apple’s wording / example |
|---|---|
| Small cardinals | `Spell out the following numbers: Cardinal numbers from one through nine. (However, use a numeral, no matter how small, to express numbers as numbers and as units of measure.)` |
| Mixed sizes in one paragraph | `For numbers of the same category within a paragraph, if any number is larger than nine.` Example: `We have 25 computers and 4 printers on the network.` |
| Sentence-initial numbers | Spell out — but Apple marks the restructure as preferable. Correct: `Two hundred fifty functions are available in the Function Browser.` **Preferable:** `The Function Browser gives you access to 250 functions.` |
| Battery life | `Use numerals when referring to battery life (up to 8 hours of battery life, up to an 8-hour battery life).` |
| Percent | `Always preceded by a numeral, no matter how small the value. 1 percent` — with `%` reserved for `technical appendixes, specification lists, and tables`. |
| `24/7` | `Not 24x7. To spell out, use the form 24 hours a day, 7 days a week.` |

The sentence-initial rule is the one that matters most for this register, because “one-word opener + period” is the register’s signature move. Apple’s documented preference is to **restructure so the number is not first** — which is exactly what the three-beat ladder does: `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` The numeral arrives in beat two.

**Measured.** 51/59 footnotes in A-fn contain digits. Headline examples in the corpus use `6x`, `7.8x`, `1600 nits`, `24 hours`, `80 percent`, `5.1 mm`, `100 million`, `40%`, `$1200`. Apple mixes `80 percent` (word, per the rule) and `40%` (symbol, in recycled-material claims) — the rule resolves the inconsistency: word by default, symbol in spec lists.

### 4.6 `up to Nx` — the performance form

**Measured.** Every performance claim in the corpus uses `up to` plus a numeral plus a lowercase, closed-up `x`:

`up to 6x faster` · `up to 7.8x faster` · `up to 8x faster AI performance than the M1 family` · `up to 1.6x faster GPU performance than M4` · `up to 2x more than AirPods Pro 2` · `1.5x increase` · `up to 3x more Active Noise Cancellation`

Sources: <https://www.apple.com/macbook-pro/>, <https://www.apple.com/ipad-pro/>, <https://www.apple.com/airpods-pro/>.

Apple’s style guide fixes the form: `For the speed of optical drives, use a lowercase x—for example, 24x speed. Note that there’s no space between the numeral and the x.` So: **`7.8x`, never `7.8X`, never `7.8 x`, never `×`.** And `up to` is part of the unit, not a softening word you can drop — `6x faster` unhedged is a different, much stronger claim than `up to 6x faster`.

**A live defect worth knowing about.** As of this fetch, `/macbook-pro/` carries three sibling bento tiles reading `up to 6x faster`, `up to 7.8x faster` and `up to 86x faster`. The `86x` tile is an artifact — most likely a footnote-marker problem in a revised figure. It is in the served HTML, it is not a stylistic rule, and it is a useful reminder that a performance-claim pipeline can ship a wrong number. **Do not imitate it.**

### 4.7 Em dashes — what is actually true

The popular claim is that the em dash is a signature of Apple’s marketing voice. **It is not supported in headlines.** 0/83 headlines in A-hero contain an em dash. Corpus B finds 5 em dashes across 790 headline strings, and those five are subhead-style lines that join a clause to its gloss, not hero lines.

**A correction to the record, from the fresh sample.** A-hero’s companion finding characterised the em dash as concentrated in legal and footnote text. Corpus B does not reproduce that. In the 17-page fresh sample:

- **115 / 2,062 marketing sentences (5.6%)** contain an em dash.
- **0 / 59** footnotes on `/macbook-pro/` contain one. Across all 240 footnotes in Corpus B: zero.
- The em dash appears in ordinary feature body copy — `MacBook Pro has the longest battery life ever in a Mac — up to 24 hours — so you can work, create, and play all day.` (<https://www.apple.com/macbook-pro/>) and `Apple Pencil sets the standard for how drawing, painting, handwriting, and note-taking should feel — intuitive, precise, and magical.` (<https://www.apple.com/ipad-pro/>).

So the honest three-part statement is: **headlines almost never; footnotes on these pages never; feature paragraphs often, as a device for appending a gloss or a consequence.** Apple’s rule governs the form: “Don’t overuse em dashes,” and “Close up the em dash with the word before it and the word after it.” Semicolons are the exact inverse, and the fresh sample makes the split unusually clean: **334** semicolons in A-sent, but only **3** in the 2,062 sentences of Corpus B’s marketing prose, against **142 semicolon-bearing sentences in the footnotes**. The semicolon is the footnote’s punctuation — it chains parallel conditions in legal prose — and the em dash is the body paragraph’s. Using either in the other’s place is the most visible way imitation copy gives itself away.

**When the em dash is right in this register:** appending a concrete instance or a consequence to a general claim (P8). **When it is wrong:** as a rhythm device in a headline, where a period is the register’s separator.

### 4.8 Other mechanics that carry over

- **Serial comma, always.** `Use a serial comma before and or or in a list of three or more items.` (Apple Style Guide.) Corpus example: `HDMI, Thunderbolt 5, SDXC, MagSafe, Wi-Fi 7, and Bluetooth 6.` (<https://www.apple.com/macbook-pro/>). Apple’s comma is the Oxford comma, not a style choice.
- **`And` and `But` open sentences freely.** 15/83 A-hero headlines contain `and`; body paragraphs open with `And` routinely, especially in privacy copy, where it chains guarantees. Corpus B: `And voilà.` (<https://www.apple.com/airpods-pro/>).
- **Contractions, including in headlines.** `They’re workin' 9 to 5.` · `The best thing you’ve never heard.` · `Your business is nobody else’s.` The register is informal by design.
- **Sentence case is not reliably the rule in marketing.** Among 83 A-hero headlines, 41 look title-cased, inflated by 2–3 word headlines where the cases are indistinguishable. Apple’s value-prop modules use title case (`Recycled Material`, `Renewable Electricity`, `Same-day service`). **Do not build a rule on this** — the sample is inconclusive.
- **No `we` in the headline, occasional `we` in the body.** `Give us the old. Save on the new.` (<https://www.apple.com/mac/>) is a rare headline use. The body uses it: `we’ll ship it to you`. Apple’s *interface* guidance says “Avoid using we altogether” — the marketing register does not follow that rule, which is why the two must not be mixed.
- **Plural headline labels are normal.** `Mics and speakers.` · `Mics. Cameras. Action.` (<https://www.apple.com/ipad-pro/>).

---

## Do not

Each item states the failure, the documented basis where there is one, and the rule. This section is the reason the rest of the file is safe to use.

**F1 — Do not ship a punchy claim without its evidentiary footnote.**
The failure is not stylistic, and the load-bearing cases here were each verified:

- **Which?, 2019** tested nine iPhone models and found every one fell short of Apple’s battery-time claims — the iPhone XR lasted 16 hours 32 minutes against a claimed 25 hours. Apple disputes the method, so treat the study as contested; the point that survives is that `up to N hours` carries an evidence obligation, not a flourish.
- **CFPB, 2024** ordered Apple and Goldman Sachs to pay over $89 million over Apple Card, finding that customers were misled about interest-free payment options. Note the shape: not a false sentence, but one **true of one path and silently false of another**.
- Apple’s own iPhone 18 Pro specs page runs hero `Up to 45 hours` against a footnote in which `preproduction` and `actual results may vary` appear **only** in the small print.
- A US class action over advertised-but-undelivered features turns on precisely this structure, alleging that no disclaimer contradicted the “prominent Challenged Representations” (*Landsheft v. Apple Inc.*, N.D. Cal. 5:25-cv-02668 ¶30).

The FTC’s rule is the general form: qualifications belong **inside** the claim “when practical”, not only in a separate disclosure. *Two commonly repeated regulator stories are not usable: the 2008 UK ASA ruling and the 2012 Australian 4G penalty survive only in secondary sources. The ASA’s own searchable archive covers 2021–2026 and returns **zero** rulings for Apple Inc or Apple Distribution International — and it does not reach back far enough to check 2008. See `sources.md` §4.1.* **Rule: the claim and its footnote are one unit of work. If you cannot write the footnote, rewrite the claim.**

**F2 — Do not stack superlatives.**
13/83 headlines (**16%**) in A-hero contain a superlative or absoluteness marker (`best`, `fastest`, `most`, `world’s`, `ultimate`, `ever`, `never`). At 16%, spread across a long page, with each one footnoted, they still land. **Four superlatives in a paragraph destroy all four** — the reader discounts the whole set, including the ones that were true. There is no measured safe density for a short document; the safe move is one superlative per surface, reserved for the claim you can actually prove. Note also that Apple stops short of the strongest words: across 83 headlines there are **zero** instances of `magical` used as a product claim. The word that survives is the milder `Magic` as a product name (`Magic Keyboard`) and the pun `Magic to your ears.`

**F3 — Do not make absolute privacy promises.**
The negation pattern (P6) is the register at its most beautiful and its most dangerous, because every negation is a falsifiable public commitment. Apple’s own record shows the gap: Face ID was announced as private because data was stored locally and never uploaded to the cloud, and was later the subject of reporting about an internal testing tool. In a regulated domain — health, finance, children’s data, anything under GDPR or equivalent — **do not generate an absolute `never`, `not`, `nobody` or `none` unless you can demonstrate it end to end and will maintain it.** Use the hedge Apple itself uses in its small print (`Not all devices are eligible`, `varies by use and configuration`) rather than the absolutism it uses in its heroes. GDPR Article 12 requires information in “a concise, transparent, intelligible and easily accessible form, using clear and plain language” — a comprehensibility standard, which ornamental ambiguity in a privacy claim fails.

**F4 — Do not treat the footnote as a place to hide.**
Median footnote 100 words; the lease footnote on `/macbook-pro/` runs **694 words** (710 re-counted); a carrier footnote on `/apple.com/iphone/` runs **8,909 words**. The 694-word footnote is a single block covering eligibility, credit checks, damage fees, upgrade mechanics, termination charges and excluded storefronts. Whatever its legal status, **it is not communicatively sufficient**, and copied into a domain with real consumer harm — credit, insurance, health — it is a liability rather than a style. **Rule: if the obligation needs 700 words, change the claim until it does not.** Also: a disclosure is a factual assertion. Never paste a methodology sentence into a document that has no methodology.

**F5 — Do not use unqualified superlatives or absolutes.**
`The world’s best in-ear Active Noise Cancellation.` is defensible for Apple because Apple has the tests and names the comparison. `The world’s best analytics platform.` is not a claim; it is an invitation to a regulator. Every superlative in this register is bounded by a comparison class, a date, or a footnote. If you cannot name what you were measured against and when, the superlative is not available to you. **The unhedged comparative is the single highest-risk sentence in marketing copy.**

**F6 — Do not apply the register where it does not belong.**
The most common way an “Apple-style” piece of writing fails is not bad rhythm — it is using the marketing register on a surface whose job is clarity. Apple’s own published guidance for interface text says the opposite of this file: “avoid the temptation to be too cute or clever”; “Avoid using `we` altogether”; “Use possessive pronouns sparingly”; error messages should “avoid blame”; interjections like “oops!” are “unnecessary and can sound insincere.” Writing `Happily ever faster.` on a failed-payment screen is not Apple style. **Rule: route first. Product page, landing hero, app-store listing, launch email, ad, tagline → this file. Button, alert, error, setting, legal notice, support article → `ui-strings.md` or `apple-style-guide-rules.md`.** Never blend.

**F7 — Do not write in this register for someone else’s culture, craft or loss.**
In 2024 Apple released an ad filmed in Bangkok that was criticised for portraying Thailand as an underdeveloped “third-world” state, and apologised and removed the film. In the same year the *Crush!* iPad Pro advertisement was widely criticised; Apple’s VP of marketing communications apologised: “We missed the mark with this video, and we’re sorry.” **The register is confident. Confidence reads as arrogance when the writer has not earned the audience’s trust, and as tone-deaf when the subject is someone else’s culture, craft or grief.** Before applying P7 (the swerve) or P11 (the tercet), ask whose experience the joke depends on.

**F8 — The anti-caricature rule.**
Parody is what this register becomes when its surface features are copied without its constraints. The tells, in order of frequency:

1. **Three-beat everywhere.** The tricolon is roughly a fifth of two-part headlines (19/790 in Corpus B). A page where every headline has three beats is a caricature.
2. **Puns without a claim underneath.** P7 always restates a real benefit. A swerve that only amuses is a joke, not a headline.
3. **Adjectives in beat one.** Real beat one is a bare label (`Ultra Retina XDR.`). `Revolutionary new Ultra Retina XDR.` is the imitation.
4. **Superlatives as filler.** See F2.
5. **Borrowed rhythm, borrowed claim.** If the sentence would still be true with a competitor’s name in it, it says nothing.
6. **Periods as decoration.** The period marks a real beat boundary, not a pause for effect.

**Apple’s own published instruction for adjacent surfaces is the right test for the whole file**: “Check each word to be sure it needs to be there. If you can use fewer words, do so.” If a pattern from this catalogue can be removed without loss, remove it. The register is a compression device, and compression that adds nothing is just noise with better typography.

**One more boundary, stated as a boundary rather than a cited finding.** Nothing here says the Apple voice is unusable in a regulated domain. The honest constraint is narrower and harder: **no ambiguity where ambiguity creates liability, and no absolute claim you cannot footnote.** That is a judgement call about your own evidence, and it is the writer’s to make — not the style guide’s.

---

## Transformations

Twelve before/after pairs. The “Before” text is ordinary corporate or technical prose of the kind that actually gets written. The “After” is the register applied — or, where marked, **deliberately not applied**, because the correct move on that surface is a different register. Each pair names what was deleted and why.

### T1 · Product page hero

**Before.** `Introducing our all-new flagship laptop, now featuring the latest generation processor for dramatically improved performance and a battery that lasts significantly longer than before.`

**After.** `New flagship laptop. Faster than the last one. All-day battery.` + footnote on the battery claim.

**Register call:** marketing.
**Deleted:** `Introducing` (announces the announcement, not the product); `our` (the reader knows whose page it is); `all-new` and `latest generation` (unfalsifiable, and `latest` is a fact about the calendar); `dramatically` and `significantly` (adverbs standing in for the number that should be there); `than before` (unstated baseline).
**Why:** the sentence had one idea (a new laptop) carrying five unsupported intensifiers. The rewrite has three ideas, each a beat, and the one that carries a number gets a footnote.

### T2 · Feature blurb + its footnote

**Before.** `Our proprietary AdaptiveFlow™ engine leverages advanced machine learning to intelligently optimise resource allocation across your workloads, delivering industry-leading efficiency improvements.`

**After.** `AdaptiveFlow. Puts the busy work where it costs least. 40% fewer wasted CPU cycles on mixed workloads.*`
`* Measured as idle and retry cycles as a share of total cycles over a 24-hour replay of the standard mixed-workload trace, on a 16-core instance running version 3.2, compared with version 3.0 on identical hardware. Results vary by workload.`

**Register call:** marketing, with the evidence apparatus attached.
**Deleted:** `proprietary` (every vendor’s engine is proprietary — it is not a benefit); `leverages advanced machine learning` (a mechanism, not an outcome, and the reader cannot act on it); `intelligently` (the software is not intelligent; it is deterministic); `industry-leading` (an unqualified superlative with no named industry and no named competitor — see F5); `delivering` (a participle that lets the sentence avoid stating who does what).
**Why:** three beats — label, plain meaning, what you get with a number. The footnote carries the method, the baseline, the conditions and the variance, and the claim would be indefensible without it.

### T3 · Pricing page

**Before.** `Flexible pricing options designed to scale with your business, so you only pay for what you need. Contact our team to learn more.`

**After.** `Pay for what you use. Nothing else.` / `Starter $19 a month, up to 5 people. Team $49 a month, up to 25. Everything above that is a conversation.`

**Register call:** marketing for the headline; the price table itself stays factual.
**Deleted:** `Flexible` (self-congratulation — the number is the flexibility); `designed to scale with your business` (a promise with no mechanism); `Contact our team to learn more` (a call to action that withholds the information the reader came for).
**Why:** the reader’s question is “what will this cost me.” The two-beat answers with a negation that is literally true — you pay for usage, nothing else — and then the table does the work. `Everything above that is a conversation.` is a human close, and it is honest about where self-serve ends.

### T4 · App-store listing

**Before.** `Our award-winning app delivers a comprehensive suite of productivity features designed to help you stay organised and get more done, wherever you are.`

**After.** Subtitle: `Notes, tasks, and files in one place.` Description opener: `Everything you wrote down this week. In one place, on every device. Offline by default, so it works on a plane.`

**Register call:** marketing for subtitle and description; the release notes below stay in the editorial register.
**Deleted:** `award-winning` (an adjective doing a claim’s job, with no award named); `comprehensive suite of productivity features` (a category description, not a product — the reader cannot picture a single thing in it); `stay organised and get more done` (the universal verb phrase of the category, true of every competitor — see F8.5); `wherever you are` (a cliché that replaces the concrete `on a plane`).
**Why:** Apple’s own App Store subtitles are the model: `Over 100 million songs.` (<https://apps.apple.com/us/app/apple-music/id1108187390>) and `Shopping designed around you` (<https://apps.apple.com/us/app/apple-store/id375380948> — subtitle, no terminal period). Concrete nouns, one idea, the platform benefit named.

### T5 · Launch email

**Before.** `We’re thrilled to announce that our new analytics dashboard is now live! Built with you in mind, it brings together powerful new capabilities that will transform the way you understand your data.`

**After.** Subject: `Your dashboard is live.` Body: `Open it and the first chart is already built from your data. Nothing to configure. If a number looks wrong, the definition is one click away.`

**Register call:** marketing, but a *low-pressure* variant — the reader already bought.
**Deleted:** `We’re thrilled to announce` (the reader’s reaction is not a feature); the exclamation mark (see §4.2); `Built with you in mind` (unfalsifiable and unfelt); `powerful new capabilities` (no reader can picture a capability); `transform the way you understand your data` (hyperbole aimed at a person who is about to open a dashboard).
**Why:** two-beat lines, no exclamation mark, second person, and one line that pre-empts the reader’s real doubt. `If a number looks wrong, the definition is one click away.` is a Fact-Not-Fault move (P9) inside marketing copy, and it is the line that builds trust.

### T6 · Landing hero

**Before.** `The leading platform for teams who want to move faster, work smarter, and unlock their full potential.`

**After.** `Ship on Friday.` / `Deploys that finish before your coffee does, and roll back in one command.`

**Register call:** marketing.
**Deleted:** `The leading` (a ranking claim with no ranking); `platform` (a category the reader already knows they are shopping in); `teams who want to move faster, work smarter` (three abstractions, no image, and `unlock their full potential` is closer to a horoscope than a product claim).
**Why:** one concrete, slightly provocative claim (`Ship on Friday.`) in beat one, then what you get. `before your coffee does` is a human close; `in one command` is the checkable part. Two beats, one idea each.

### T7 · Data / analytics finding

**Before.** `The model’s projected defensive contribution metric indicates a statistically significant positive deviation relative to the positional baseline, suggesting the player’s underlying performance exceeds observed output.`

**After.** `He wins the ball back more often than a typical player in his position — about 3 times a game more.` Footnote: `Counted from where each possession ended, using only challenges the cameras could see. Pressure on the ball isn’t recorded, so this is a floor, not a measure of effort.`

**Register call:** the *rhythm* is marketing; the *hedging discipline* is editorial. This is the domain where the register transfers best to non-marketing writing, and it is where the footnote does the most work.
**Deleted:** `projected … metric indicates` (nominalisation that hides the actor); `statistically significant positive deviation` (a fact about a test, not about a player — the reader cannot picture a deviation); `relative to the positional baseline` (the baseline belongs in the footnote, and it belongs there explicitly); `underlying performance exceeds observed output` (a distinction only the analyst cares about, and it is the *finding*, so it should have been the first sentence).
**Why:** the finding goes in the headline, the method and its limits go in the footnote, and the footnote names the direction of the error (`a floor, not a measure of effort`). This is the single most valuable transfer in the file: **conclusion in the sentence, method and limitation in the footnote.**

### T8 · Changelog entry

**Before.** `v4.2 — Various bug fixes and performance improvements. We’ve also made some exciting updates to the settings experience.`

**After.** `v4.2 — Settings load without the delay on first open. Fixed a crash when exporting more than 10,000 rows. The export limit is now 50,000; above that, use the API.`

**Register call:** **not marketing.** Changelogs are editorial. Beat structure is fine; hedges, puns and superlatives are not.
**Deleted:** `Various bug fixes` (the phrase that tells a reader nothing — Apple’s own App Store release notes use the equally empty `Various improvements and performance enhancements.`, which appears **22 times in the rendered text** of one App Store page — 44 in the served HTML, which emits each entry twice); `performance improvements` (which performance, improved how much); `exciting updates` (the reader decides what is exciting); `experience` (a word that lets a sentence avoid naming the thing).
**Why:** every line is a fact the reader can verify by opening the app. Note that `The export limit is now 50,000; above that, use the API.` is a Condition Up Front (P10) doing exactly what it does in a footnote — it states the limit and the alternative in the same breath as the change. The semicolon is correct: it joins parallel conditions.

### T9 · README opener (technical)

**Before.** `This repository contains a comprehensive and highly configurable toolkit that provides developers with a powerful and flexible solution for managing configuration across multiple environments.`

**After.** `Reads config from three places — a file, the environment, and flags — and tells you which one won.`

**Register call:** **not marketing.** Documentation is editorial. One beat, plain, no footnote needed because the claim is verifiable inside the repository.
**Deleted:** `comprehensive` and `highly configurable` (both unfalsifiable and both standard-issue); `provides developers with a powerful and flexible solution for` (an eleven-word runway before the verb); `managing configuration across multiple environments` (accurate but abstract — the reader wants to know the mechanism, and the mechanism *is* the feature).
**Why:** the same discipline as §1.1 — one idea, and it is the idea that decides whether the reader keeps going. The em dash appends the plain-language gloss (P8), and `tells you which one won` is the human close. Note the pattern transfer: this is `Label. Plain meaning. What you get.` with the beats run into one sentence.

### T10 · Support / help-centre line

**Before.** `Oops! It looks like something went wrong with your payment. Please double-check your card details and try again.`

**After.** `Your payment didn’t go through. Check that the card number and expiry date match your card, then try again. If it still fails, your bank may be declining the charge — that is a call to them, not a change here.`

**Register call:** **interface / support, not marketing.** This pair exists to show the boundary. Apple’s published guidance for this surface: error messages should “avoid blame, and be clear about what someone can do to fix it”; “Interjections like 'oops!' or 'uh-oh' are typically unnecessary and can sound insincere.”
**Deleted:** `Oops!` (insincere, and it puts the writer’s feelings in front of the reader’s problem); `It looks like` (hedges a fact the system knows); `something went wrong` (which something?); `Please double-check` (implies the reader was careless — that is blame wearing a courtesy); `try again` on its own (an instruction the reader already thought of).
**Why:** Fact, Not Fault (P9). State what happened. Give the specific check. Then name the real next step and where it lives. The Apple model from the corpus is `Your Apple Watch is water resistant, but not waterproof.` — the true fact first, the limit second, no fault anywhere.

### T11 · Impact / ESG report line

**Before.** `We are deeply committed to sustainability and are proud to be taking meaningful steps toward a more responsible and environmentally conscious future for all.`

**After.** `Our 2025 emissions were 12% lower than 2024. Two thirds of that came from cleaner electricity at supplier factories; the rest from packaging. We are not on track for the 2030 target without new sourcing.`

**Register call:** marketing rhythm is welcome; **superlatives and unqualified commitments are not.** This is a disclosure surface, and F3 and F5 apply in full.
**Deleted:** `deeply committed` (a feeling, and feelings are not auditable); `proud to be taking` (ditto); `meaningful steps` (a quantity word with no quantity); `toward a more responsible and environmentally conscious future for all` (four abstractions, none checkable).
**Why:** Apple’s environment page puts the numbers in the copy — `Innovation is up. Emissions are down.` (<https://www.apple.com/environment/>) — and the two-beat shape survives, because each beat is a measurement. The third sentence is the one most companies omit, and it is the one that makes the first two credible. **A voluntary admission of a shortfall is the strongest evidence in the paragraph.**

### T12 · Job posting

**Before.** `We are looking for a passionate and highly motivated individual to join our dynamic team and help us build the future of our industry.`

**After.** `You’ll own the ingest pipeline — the part that reads 40 million events a day and occasionally falls over at 3 a.m. You’ll be the second person on call. If that sounds like the job you want, the rest of this page is for you.`

**Register call:** marketing, with the honesty dialled up, because a job posting is a disclosure surface as much as a sales surface.
**Deleted:** `passionate` and `highly motivated` (filters that screen for vocabulary, not capability); `dynamic team` (no team has ever described itself otherwise); `help us build the future of our industry` (a claim with no referent — which future, which part).
**Why:** the concrete nouns (`ingest pipeline`, `40 million events a day`, `3 a.m.`, `second person on call`) do the qualifying, and they let a candidate self-select out, which is the point. `If that sounds like the job you want, the rest of this page is for you.` is the Human Close (P4) — and it is honest, which is what a job posting needs and what a product page can afford to skip.

---

## Verification and limits

- **Every Apple sentence quoted in this file was retrieved and quote-checked against the served HTML.** Corpus B pages were fetched on 2026-09-30 with `curl -sL -m 25` and a desktop Chrome User-Agent, parsed with Python `BeautifulSoup`, and each quoted string was matched against the tag-stripped text of its source page. Multi-beat headlines are stored across separate markup elements, so verification is against rendered text order, not raw HTML substrings.
- **Typography in this file.** Quoted Apple sentences are reproduced with straight ASCII apostrophes and quotes (`'`, `"`) for portability. The source pages use typographic ones (`’`, `“`, `”`), and Apple’s style guide prefers them. The words are identical; only the codepoints differ. Em dashes (`—`), the non-breaking hyphen in `All-day`, and the lowercase closed-up `x` in `7.8x` are reproduced as they appear.
- **Retrieval caveats.** `web_fetch` returns navigation chrome only on these pages. `apple.com/newsroom/` served an index shell with no body prose and contributed nothing. App Store customer reviews were excluded from every count — they are user-generated content, and every `!` outside the film title `Deaf President Now!` came from them.
- **Scroll-reveal duplication.** Apple’s HTML emits start-frame and end-frame copies of animated text. Artifacts such as `track track you.` and `Read Read, , delete, delete , and reply with peace of mind.` are extraction artifacts. The correct strings are `Decide which apps are allowed to track you.` and `Read, delete, and reply with peace of mind.` Both were deduplicated before counting.
- **One live defect.** `up to 86x faster` on `/macbook-pro/` is in the served HTML and is almost certainly a shipped error. Do not imitate it. A shipped Korean spacing error (`칩안` for `칩 안`) exists on the same era of pages, which is a reminder that Apple’s own pipeline ships mistakes.
- **Diachronic claims: none.** Everything here is one era of copy. No statement about how Apple’s style has changed over time is supported by this work.
- **Sitewide claims: none.** See §0 for the samples. Every count is a count of its sample.
- **Not verified here.** No third-party *readability score* for Apple copy was retrieved; the 2012 Australian ruling survives only in secondary sources; and the claim that this register is unusable in regulated domains is a design constraint, not a cited finding. §Do not states that boundary as a boundary.
- **Third-party corroboration (added in a later pass).** Two academic studies of Apple’s advertising language were located after this file was written, and both are consistent with the catalogue above — Lin & Hu (2025), *A Sociolinguistic Study on Linguistic Deviation in Apple’s Advertisement* (six deviation types: phonological, lexical, graphological, grammatical, semantic, and **register**), and Pham, *More Than Meets the Eye: Pragmatic Implicature in Apple iPhone’s Slogans* (16 slogans, 2017–2023: mostly noun phrases, declaratives and imperatives, with conventional implicature signalling elegance and innovation). Both are small qualitative studies, so cite them as corroboration, not measurement. Full URLs in `sources.md` §4.3.
- **The ASA gap is now closed in the other direction.** The ASA’s own searchable archive covers 2021–2026 and returns no ruling naming Apple in any of those years; it does not reach back to 2008, so the Wikipedia story cannot be checked there. Do not cite an ASA ruling against Apple. See `sources.md` §4.1.
- **Primary sources used for rules, not just examples.** Apple Style Guide: <https://support.apple.com/guide/applestyleguide/welcome/web> · PDF <https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf>. HIG Writing: <https://developer.apple.com/design/human-interface-guidelines/writing> (JSON: <https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.json>). FTC: <https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business>, <https://www.ftc.gov/business-guidance/advertising-marketing>.
