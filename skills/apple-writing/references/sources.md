# Sources — what Apple actually published, and how to re-read it

Apple’s copy and guidance change. This file records **what exists**, **how to retrieve it**, and **what does not exist** — so you neither cite a hallucinated source nor trust this skill’s memory of a moving target.

Everything below was verified by direct fetch. Where a route failed, the failure is recorded too.

---

## 1. The three rulebooks

| Register | Rulebook | Public? | Where it lives |
|---|---|---|---|
| **Editorial** (docs, UI text, support) | *Apple Style Guide*, June 2026, 244 pp. | **Yes** — full PDF + web | `help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf` · `support.apple.com/guide/applestyleguide/<slug>/web` |
| **Interface** (app UI) | HIG — *Writing*, *Inclusion*, plus component pages | **Yes** | `developer.apple.com/design/human-interface-guidelines/<slug>` |
| **Marketing** | Marcom style guide | **No — internal** | Reverse-engineered from live `apple.com` copy only. The Style Guide merely acknowledges it: *“Some departments at Apple (Marcom, for example) have supplemental style guides.”* |

The Style Guide states its own scope: *“editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and user interfaces… Apple developers and third-party developers should follow these guidelines for user-facing text.”* It does **not** govern marketing.

---

## 2. Retrieval routes that work

### Apple Style Guide — PDF (the richest single source)
```bash
curl -sL -m 90 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15" \
  -o apple-style-guide.pdf \
  "https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf"
# verified: 200 · application/pdf · 4,158,788 bytes · 244 pages · June 2026
python3 -c "from pypdf import PdfReader; r=PdfReader('apple-style-guide.pdf'); \
print(''.join((p.extract_text() or '') for p in r.pages))" > apple-style-guide.txt
# verified: 489,928 characters extracted with pypdf 4.2.0
```

### Apple Style Guide — web (per-section, server-rendered)
```bash
curl -s -m 30 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15" -L \
  "https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web"
# verified: 200 · clean text after stripping boilerplate
```
Section slugs (52 of them, including the A–Z letter pages) are listed in `research/asg-sections.txt`.
**Trap:** the guide root `support.apple.com/guide/applestyleguide/` is a 588 KB JavaScript shell, and `help.apple.com/applestyleguide/` is a **248-byte redirect stub**. Fetch a *section* URL, never the root.

### HIG — JSON endpoint (no browser needed) ★
```bash
curl -s "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.json"
# verified twice: 200 · 37,074 bytes · contains the full Writing page text
```
Works for `writing`, `inclusion` (51 KB), `branding`, `onboarding`, `feedback`, `accessibility`, `layout`, `privacy`, `typography`…
Index pages for enumeration: `…/human-interface-guidelines.json` and `…/human-interface-guidelines/foundations.json`.
**Trap:** the HTML page is a React SPA and returns a ~17 KB empty shell; `web.archive.org` captures of it are shells too. A sibling agent concluded the JSON route 404s — it had used `/tutorials/data/documentation/…`, which does. **The correct path has no `documentation/` segment.** Fallback if a slug ever 404s: `curl -sS "https://r.jina.ai/https://developer.apple.com/design/human-interface-guidelines/<slug>"`.

### apple.com product copy (the marketing calibration target)
```bash
curl -sL -m 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36" \
  "https://www.apple.com/iphone-duo/" -o page.html
# verified: 200 · 723,842 bytes · 49,295 chars of visible text · 23 footnote items
```
Useful selectors: `.header-headline`, `.section-header-headline`, footnotes are `<li id="footnote-N">`.
**Trap:** `web_fetch` returns navigation only for these pages — use `curl`. **And** Apple’s HTML ships both the start-frame and end-frame copy of scroll-animated text, so naive extraction invents typos (`track track you.`). Deduplicate; never quote a doubled artifact as an Apple error.

### Apple developer documentation — markdown route
```bash
curl -s "https://developer.apple.com/documentation/swift/array.md"
# verified: 200 · 46,916 bytes of clean markdown
```

### WWDC transcripts — static HTML
```bash
curl -s "https://developer.apple.com/videos/play/wwdc2022/10037/"   # no JS needed
```
High-value sessions for writing: **10037** (2022, voice and tone), **404** (2025, UX writing), **10140** (2024).

### App Store Connect Help — the only citable source for character limits
Name 30 · Subtitle 30 · Keywords 100 bytes · Promotional text 170 · Description 4,000 · What’s New 4,000.
**Trap:** these limits are *not* in the App Store Connect OpenAPI spec, and ASC Help returns a **soft 404** as HTTP 200 with ~82 KB where a real page is ~376 KB. Check the byte size, not the status code.

---

## 3. What does **not** exist — do not cite it

- **No public “Apple Developer Documentation Style Guide.”** Four candidate paths 404; a GitHub `org:apple` search returns `total_count: 0`. The real public doctrine is the style guide + DocC + the Swift API Design Guidelines + WWDC transcripts.
- **No public Marcom tone-of-voice guide.** The Style Guide only acknowledges that one exists.
- **No Apple-published URL for the 1997 “Crazy Ones” script** (agency copy; Jobs' authorship is disputed).
- **`apple.com/values/` is a hard 404.**
- The archive.org “Think Different Booklet (1997)” is a **retyped transcription, not a scan**.
- **The Markkula attribution of the 1979 “Apple Marketing Philosophy” memo is disputed.** The real facsimile (`archive.org/details/102789075-05-01-acc`, stamped `ACH Dec. 79`) carries no signature and refers to Apple in the third person. The famous “Jan 3, 1980 / three bullets” retellings are embellished. The memo’s three words — **Empathy, Focus, Impute** — are genuine; the byline and the date are not.

---

## 4. Second verification pass — a real browser (2026-09-30)

Four things plain HTTP could not settle were checked with `ego-browser`, which renders JavaScript. All results below are from Apple’s or the regulator’s own site.

### 4.1 The ASA has no Apple rulings — and its archive is shallower than it looks

From the ASA’s own rulings search (`https://www.asa.org.uk/codes-and-rulings/rulings.html`):

| Query | Result |
|---|---|
| `Apple Inc` | **0 rulings** |
| `Apple Distribution International` | **0 rulings** |
| `Apple Distribution` (with a 2004–2026 date range) | **0 rulings** |
| `Apple` (no filter) | 30 keyword matches — **none titled Apple**; they are ads that merely mention it (games, drinks, funeral plans) |
| `Samsung` (method check) | 5 results including `Samsung Electronics (UK) Ltd` — so the search does index advertiser names |

- The three ruling URLs reported elsewhere as adjudicated *Not Upheld* (`apple-distribution-international-ltd-a18-445104`, `‑a12-207565`, `‑a11-161503`) return **HTTP 404** in the browser.
- **Coverage limit, measured with the date filter** (`dd/mm/yyyy` works; ISO and long-form are ignored): the archive returns rulings for **2021–2026 only** — 2021: 83, 2022: 278, 2023: 330, 2024: 280, 2025: 294, 2026: 244 — and **0 for every year tested from 2007 to 2020**. Ryanair, which certainly has older rulings, returns only two (2023, 2026).

**What this supports:** do not cite an ASA ruling against Apple. The Wikipedia-sourced 2008 story can be neither confirmed nor denied from the ASA itself, because the archive does not reach back that far. For the modern period the verified statement is stronger than the old one: *in the years its own search covers, the ASA has published no ruling naming Apple.* The verified UK pressure point remains the 2019 Which? battery study.

### 4.2 App Store character limits — verified field by field

From App Store Connect Help (`developer.apple.com/help/app-store-connect/reference/app-information/` and `…/platform-version-information/`):

| Field | Limit | Apple’s wording |
|---|---|---|
| Name | **30 characters** | “…than 30 characters” |
| Subtitle | **30 characters** | “This can’t be longer than 30 characters.” |
| Promotional text | **170 characters** | “This property can’t be longer than 170 characters.” |
| Description | **4,000 characters** | “Limited to 4000 characters.” |
| Keywords | **100 bytes** | “You can provide up to 100 bytes of content.” (each keyword longer than two characters) |
| What’s New | **4,000 characters** | “Limited to 4000 characters.” |

### 4.3 Third-party linguistic research does exist — the earlier gap is closed

A previous pass recorded “no corpus-linguistics or discourse-analysis study of Apple’s register was located.” Two were then found and retrieved:

- **Lin, Q. & Hu, X. (2025). “A Sociolinguistic Study on Linguistic Deviation in Apple’s Advertisement.”** *Journal of Social Science and Humanities* 7(1). PDF: `https://bryanhousepub.com/index.php/jssh/article/download/1367/1322`. Applies Leech’s deviation model and finds six deviation types in Apple’s ads: **phonological** (alliteration, repetition, consonance for rhythm), **lexical** (coined terms signalling novelty), **graphological** (altered word forms, including deliberate misspellings), **grammatical** (heavy ellipsis — “Think huge.”), **semantic**, and — notably — **deviation of register**.
- **Pham, T. T. H. “More Than Meets the Eye: Pragmatic Implicature in Apple iPhone’s Slogans.”** *VNU Journal of Foreign Studies*. `https://jfs.ulis.vnu.edu.vn/index.php/fs/article/view/86-103`. Analyses 16 English slogans (2017–2023) with Yule’s pragmatic framework: predominantly **noun phrases, declaratives and imperatives**, with **conventional implicature** used to suggest elegance and innovation.

Both are qualitative and small-sample; treat them as corroboration of the pattern catalogue, not as measurement. Notably, neither is a readability study, so **no Flesch-Kincaid or similar score for Apple copy has been located** — that gap stands.

### 4.4 Korean register, measured on Apple’s own support pages

Apple’s Korean **support and user-guide** pages use **하십시오체** with **zero occurrences of `당신`** — `따르십시오`, `설정하십시오`, `조절하십시오` (`support.apple.com/ko-kr/102639`, `support.apple.com/ko-kr/guide/iphone/welcome/ios`). This is a third distinct Korean register alongside marketing (합니다체 + 해요체, `당신` present) and press releases (한다체). This skill is English-only; the finding is recorded for whoever builds the Korean layer.

---

## 5. Local copies already collected (in this repository’s `research/`)

| File | What it is |
|---|---|
| `research/apple-style-guide.pdf` · `.txt` | The official guide, 244 pp. / 490 K chars |
| `research/asg/*.txt` · `asg-sections.txt` | The same guide as 52 web sections / 507 K chars |
| `research/02-apple-primary-sources.md` | Source table, 70 numbered primary rules with URLs, failure log, route table |
| `research/03-voice-systems-and-corpus.md` | 52-sentence corpus with URLs, 22 measured rules with counts, Failure modes F1–F8, comparison of voice systems, evaluation protocol |
| `research/01-prior-art-agent-skills.md` | What already exists, and the exact gap |
| `research/00-recon-findings.md` | Verified retrieval recipes and tool status |

---

## 6. How to re-verify a rule before you rely on it

1. Find the rule’s source in §1–2. If it is editorial, grep the PDF text: `grep -o ".\{0,80\}the rule phrase.\{0,120\}" apple-style-guide.txt`.
2. If it is interface, pull the HIG JSON and search its `text` fields.
3. If it is marketing, fetch a live page and check the pattern still holds — **count it**, do not eyeball it.
4. If the rule and the live copy disagree, **the live copy wins for marketing and the published guide wins for editorial/UI**, and you say which you followed.
5. Cite what you checked: `Apple Style Guide, p.154` or the URL. A rule with no citation is not a rule.
