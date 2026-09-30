# Source Verification: Published Critiques & Failure Modes of Apple Inc.'s Prose Style

**Categories covered:** (2) Footnote / small-print criticism; (3) Plain-language / accessibility failures.

**Method note.** `web_search` is non-functional in this environment (all providers fail). Sources below were
located with Bing News RSS, Google News RSS, Hacker News (Algolia) search, site-specific search endpoints
(MacRumors, 9to5Mac, Consumer Reports, EPIC, ToS;DR), the Wayback Machine CDX/Machine, and direct URL
retrieval with `curl`. **Every URL below was actually fetched and returned real content.** Every quote was
copied character-for-character from the retrieved page (curly quotes and en-dashes preserved as published).
Where a page is only retrievable through the Wayback Machine, both the live URL and the archival route are given.

Research date: 30 September 2026.

---

## 2. FOOTNOTE / SMALL-PRINT CRITICISM

### 1. Apple Inc. — iPhone 18 Pro / iPhone 18 Pro Max — Tech Specs (battery footnotes)

- **Title (verbatim):** “iPhone 18 Pro and iPhone 18 Pro Max - Technical Specifications” (page; footnote text as quoted below)
- **Author / publication:** Apple Inc. (primary source)
- **Full URL:** https://www.apple.com/iphone-18-pro/specs/
- **Date:** Page current as of retrieval; footnotes reference testing “in July 2026” and “in August 2026”. Retrieved 30 September 2026.
- **The specific claim:** Apple's headline battery figures are bare “up to” numbers (e.g. “Up to 45 hours” video playback, “Up to 36 hours” video streaming) whose qualifying conditions exist only in a dense footnote block, and the actual test parameters plus a variance disclaimer are buried there rather than surfaced with the claim.
- **Short verbatim quote** (from the battery footnote block on that page):
  > “Testing conducted by Apple in July 2026 using preproduction iPhone 18 Pro and iPhone 18 Pro Max units and software, subscribed to LTE and 5G carrier networks. Video playback consisted of a repeated 2-hour 23-minute HDR movie purchased from the iTunes Store. … Battery life varies by use, configuration, cellular network, signal strength and other factors; actual results may vary based on usage.”

  Bare headline strings on the same page, for contrast: `Up to 45 hours` / `Up to 36 hours` / `Up to 33 hours` / `Up to 24 hours`
- **Classification:** DOCUMENTED (primary source — this is the exact artifact the criticism is about)

---

### 2. “Apple's Fine Print: Daily Usage Limits for Siri AI, 'Expanded Access' Coming for a Fee”

- **Title (verbatim):** “Apple's Fine Print: Daily Usage Limits for Siri AI, 'Expanded Access' Coming for a Fee”
- **Author / publication:** Juli Clover / MacRumors
- **Full URL:** https://www.macrumors.com/2026/09/09/apple-siri-ai-usage-limits/
- **Date:** Wednesday, September 9, 2026, 12:51 pm PDT (HTTP 200, verified)
- **The specific claim:** Apple disclosed material limitations on its headline Apple Intelligence / Siri AI announcement only in the small print — a daily usage cap plus the prospect of paying for more — while the marketing framing presented the features as simply available. The article's own headline labels this “Apple's Fine Print,” making the editorial criticism explicit.
- **Short verbatim quote:**
  > “In the future, Apple will implement usage limits on these and other Apple Intelligence and Siri AI features to ensure a high-quality, reliable experience for everyone. If you reach a limit in a particular feature, that feature will become available again after a time out period. Limits may vary by feature, request complexity, system demand, system policies, and other factors. Increased access to such features will be available for a fee.”
- **Classification:** DOCUMENTED (bylined reporting quoting Apple's own announcement text)

---

### 3. “Apple's charts set the M1 Ultra up for an RTX 3090 fight it could never win”

- **Title (verbatim):** “Apple's charts set the M1 Ultra up for an RTX 3090 fight it could never win”
  (deck: “The M1 Ultra is not more powerful than an RTX 3090, and that's OK”)
- **Author / publication:** Chaim Gartenberg / The Verge
- **Full URL:** https://www.theverge.com/2022/3/17/22982915/apple-m1-ultra-rtx-3090-comparison-specs-charts-cpu-gpu-performance
- **Date:** March 17, 2022 (HTTP 200, verified)
- **The specific claim:** Apple's performance charts use an undefined “relative performance” Y-axis with no disclosed methodology, and the chart is truncated at the point where the competitor becomes faster — i.e. the chart is technically true but materially misleading. This is the canonical “marketing-selected benchmark, no methodology disclosure” critique.
- **Short verbatim quotes:**
  > “The charts, in Apple's recent fashion, were maddeningly labeled with ”relative performance“ on the Y-axis, and Apple doesn't tell us what specific tests it runs to arrive at whatever numbers it uses to then calculate ”relative performance.“”

  > “But that's because Apple's chart is, for lack of a better term, cropped.”
- **Classification:** DOCUMENTED (bylined reporting with the chart reproduced and benchmark evidence cited; contains explicit critical judgement)

---

### 4. “Apple's M1 Ultra GPU comparison with Nvidia was misleading – Macworld”

- **Title (verbatim):** “Apple's M1 Ultra GPU comparison with Nvidia was misleading – Macworld”
- **Author / publication:** Ben Lovejoy / 9to5Mac (reporting on Macworld's analysis; Macworld's own article is at https://www.macworld.com/article/627222/nvidia-geforce-rtx-3090-m1-ultra-benchmarks.html)
- **Full URL:** https://9to5mac.com/2022/03/31/m1-ultra-gpu-comparison-with-nvidia/
- **Date:** March 31, 2022, 5:28 am PT (HTTP 200, verified)
- **The specific claim:** Apple's “very carefully-worded” claim that the M1 Ultra delivers “faster performance than even the highest-end PC GPU available” was technically true only because Apple truncated the graph at ~320 W while the RTX 3090's TDP is 350 W. The critique targets both the chart and the hedged headline sentence.
- **Short verbatim quotes** (Apple's claim as quoted by 9to5Mac):
  > “For the most graphics-intensive needs, like 3D rendering and complex image processing, M1 Ultra has a 64-core GPU — 8x the size of M1 — delivering faster performance than even the highest-end PC GPU available while using 200 fewer watts of power.”

  (9to5Mac's own words:)
  > “Apple achieved this misleading comparison by cutting off the graph before the Nvidia GPU got anywhere close to its maximum performance.”
- **Classification:** DOCUMENTED (bylined reporting; the disputed Apple sentence and the chart mechanics are both quoted)

---

### 5. “Apple significantly overstates iPhone battery life compared to Which? tests”

- **Title (verbatim):** “Apple significantly overstates iPhone battery life compared to Which? tests”
- **Author / publication:** Which? (UK consumer organisation) — press office release; named spokesperson Natalie Hitchins, Which? Head of Home Products and Services
- **Full URL:** https://press.which.co.uk/whichpressreleases/apple-significantly-overstates-iphone-battery-life-compared-to-which-tests/
  (Live page is JS-rendered on direct fetch; full text verified via https://web.archive.org/web/2020id_/https://press.which.co.uk/whichpressreleases/apple-significantly-overstates-iphone-battery-life-compared-to-which-tests/)
- **Date:** 4 May 2019 (HTTP 200 via Wayback, verified; text retrieved in full)
- **The specific claim:** Independent testing of nine iPhone models found **all nine** fell short of Apple's published “up to N hours” talk-time claims, by 18%–51%; the iPhone XR was worst, at 51% short of Apple's 25-hour claim. This is the leading consumer-group critique of Apple's “up to” battery-life prose.
- **Short verbatim quotes:**
  > “Which? tested nine iPhone models and found that all of them fell short of Apple's battery time claims. In fact, Apple stated that its batteries lasted between 18 per cent and 51 per cent longer than the Which? results.”

  > “In Which? tests, the battery lasted for 16 hours and 32 minutes, whereas Apple claimed that it would last 25 hours – 51 per cent more.”

  > “we should be able to count on our handsets living up to the manufacturer's claims” (Natalie Hitchins)
- **Classification:** DOCUMENTED (primary consumer-organisation source with named methodology and named spokesperson)

---

### 6. “Apple's iPhone battery life claims are exaggerated, claims UK watchdog”

- **Title (verbatim):** “Apple's iPhone battery life claims are exaggerated, claims UK watchdog”
- **Author / publication:** Stephen Lambrechts / TechRadar
- **Full URL:** https://www.techradar.com/news/apples-iphone-battery-life-claims-are-exaggerated-claims-uk-watchdog
- **Date:** 6 May 2019 (HTTP 200, verified)
- **The specific claim:** Reports the Which? findings and Apple's rebuttal verbatim, and — importantly for a writing doc — attacks the *methodology disclosure* on both sides: neither Apple's “up to” footnotes nor Which?'s own test description state the conditions (screen brightness, background processes, notifications) needed to interpret the numbers.
- **Short verbatim quotes:**
  > “It's worth noting that the consumer watchdog's testing methods are slightly vague, only stating that it used fully-charged phones and timed continuous phone calls until the devices eventually gave out – no mention was made regarding screen brightness, background processes or notifications.”

  (Apple's response, as quoted:) > “”We rigorously test our products and stand behind our battery life claims,“ said Apple in a statement provided to Business Insider … ”Our testing methodology reflects that intelligence.“”
- **Classification:** DOCUMENTED (bylined reporting; Apple's rebuttal given verbatim)

---

### 7. “CFPB Orders Apple and Goldman Sachs to Pay Over $89 Million for Apple Card Failures”

- **Title (verbatim):** “CFPB Orders Apple and Goldman Sachs to Pay Over $89 Million for Apple Card Failures”
  (subhead: “Companies illegally mishandled transaction disputes and misled iPhone purchasers about interest-free payment options”)
- **Author / publication:** Consumer Financial Protection Bureau (US federal regulator) — press release; quotes CFPB Director Rohit Chopra
- **Full URL:** https://www.consumerfinance.gov/about-us/newsroom/cfpb-orders-apple-and-goldman-sachs-to-pay-over-89-million-for-apple-card-failures/
  (Live page: browser-accessible but returns **HTTP 403 to automated fetches** via Akamai, and now carries a Sept 22, 2025 notice that the order was terminated. The October 2024 text quoted below was verified at https://web.archive.org/web/20241101id_/https://www.consumerfinance.gov/about-us/newsroom/cfpb-orders-apple-and-goldman-sachs-to-pay-over-89-million-for-apple-card-failures/ — HTTP 200)
- **Date:** October 23, 2024 (original text verified via Wayback; archival snapshot HTTP 200)
- **The specific claim:** Apple's Apple Card marketing prose led customers to believe interest-free financing was automatic when it was not; the terms that governed this were not surfaced. A regulator found the disclosure failure unlawful — directly relevant to “headline claim vs. qualifying fine print.”
- **Short verbatim quote:**
  > “The CFPB also found that Apple and Goldman Sachs misled consumers about interest-free payment plans for Apple devices. Many customers thought they would automatically get interest-free monthly payments when buying Apple devices with their Apple Card. Instead, they were charged interest.”
- **Classification:** DOCUMENTED (primary regulatory source with formal findings)

---

### 8. “Apple Responds After Being Fined Alongside Goldman Sachs for 'Apple Card Failures'”

- **Title (verbatim):** “Apple Responds After Being Fined Alongside Goldman Sachs for 'Apple Card Failures'”
- **Author / publication:** Joe Rossignol / MacRumors
- **Full URL:** https://www.macrumors.com/2024/10/23/apple-responds-to-apple-card-fine/
- **Date:** October 23, 2024 (HTTP 200, verified)
- **The specific claim:** Sets out the CFPB's findings on how Apple's payment-plan wording and checkout presentation misled buyers, and carries Apple's verbatim disagreement — useful as a paired “claim / response” example.
- **Short verbatim quotes:**
  > “”The marketing of the Apple Card Monthly Installments plan led consumers to believe they would automatically receive interest-free financing when purchasing iPhones and other Apple devices with their Apple Card,“ the CPFB said, resulting in some consumers being ”unknowingly charged interest because they were not automatically enrolled as expected.“”

  (Apple's statement, as quoted:) > “”Apple is committed to providing consumers with fair and transparent financial products,“ an Apple spokesperson said. … ”While we strongly disagree with the CFPB's characterization of Apple's conduct, we have aligned with them on an agreement.“”
- **Classification:** DOCUMENTED (bylined reporting with regulator findings and Apple's on-record response)

---

## 3. PLAIN-LANGUAGE / ACCESSIBILITY FAILURES

### 9. “I read all the small print on the internet and it made me want to die”

- **Title (verbatim):** “I read all the small print on the internet and it made me want to die”
- **Author / publication:** Alex Hern / The Guardian
- **Full URL:** https://www.theguardian.com/technology/2015/jun/15/i-read-all-the-small-print-on-the-internet
- **Date:** 15 June 2015 (`"datePublished":"2015-06-15T10:56:41.000Z"` in page metadata; HTTP 200, verified)
- **The specific claim:** A week spent reading terms of service, starting with Apple's. Hern finds Apple's legal prose structurally unreadable — all-caps “conspicuous” boilerplate, obsolete clauses left in (a still-live Google Maps clause), and word counts that make reading impractical (21,586 words for the iPhone terms; ~20,000 for the OS + iTunes agreements). This is the strongest located readability critique of Apple's actual legal prose.
- **Short verbatim quotes:**
  > “Apple may be famous for products that ruthlessly strip out obsolete parts in pursuit of ease-of-use and simplicity, but that philosophy hasn't reached its legal department.”

  > “My iPhone is also my alarm, which means that at 6am on a Monday, I was greeted by 21,586 words to read before breakfast.”

  > “It seems that no one at all reads Apple's terms and conditions – even people who work for Apple.”

  > “The terms typically start with an introduction where every word is capitalised, because not a single lawyer cares about anyone being able to read their actual documents.”
- **Classification:** OPINION (bylined first-person critique — but with concrete, checkable word counts and a specific reproduced clause)

---

### 10. ToS;DR — “Apple Services” service rating (Grade C)

- **Title (verbatim):** “Apple Services - ToS;DR”
- **Author / publication:** ToS;DR (“Terms of Service; Didn't Read”), a non-profit FOSS project that grades terms of service
- **Full URL:** https://tosdr.org/en/service/158
- **Date:** Undated service page, continuously maintained; retrieved 30 September 2026 (HTTP 200, verified)
- **The specific claim:** ToS;DR's structured, clause-by-clause analysis of Apple's agreements assigns the service an overall **Grade C**, and flags clauses that make the terms hard for a user to rely on — in particular unilateral, un-notified amendment and inferred consent by continued use.
- **Short verbatim quotes** (page text):
  > “Apple Services — Grade C”

  > “Terms may be changed any time at their discretion, without notice to you — The Agreements can be updated at any time, including in a way that negatively affects user rights, without notifying before or after the changes.”

  > “Instead of asking directly, this Service will assume your consent to changes of terms merely from your usage.”
- **Classification:** DOCUMENTED (primary structured analysis of the actual terms, with clause-level citations)

---

### 11. “noyb files complaints against Apple's tracking code 'IDFA'”

- **Title (verbatim):** “noyb files complaints against Apple's tracking code ”IDFA“”
- **Author / publication:** noyb – European Center for Digital Rights (Max Schrems' organisation) — quotes Stefano Rossetti, privacy lawyer at noyb.eu; complaints filed with the Berlin and Spanish data protection authorities
- **Full URL:** https://noyb.eu/en/noyb-files-complaints-against-apples-tracking-code-idfa
- **Date:** 16 November 2020 (HTTP 200, verified)
- **The specific claim:** Apple creates and stores a tracking identifier (IDFA) on every iPhone **without the user's knowledge or consent**, and its own later “improvement” (an ATT-style app prompt) still leaves Apple's own first-party storage and use of the IDFA unconsented. The criticism targets the gap between Apple's privacy *rhetoric* and what its own device-level defaults and disclosure actually do.
- **Short verbatim quotes:**
  > “Apple places these tracking codes without the knowledge or agreement of the users.”

  > “Smartphones are the most intimate device for most people and they must be tracker-free by default.” (Stefano Rossetti, privacy lawyer at noyb.eu)

  > “the initial storage of the IDFA and Apple's use of it will still be done without the users' consent and therefore in breach of EU law”
- **Classification:** DOCUMENTED (primary source — the complainant's own published complaint summary and quotes)

---

### 12. “Privacy labels fail: Many 'tracking-free' apps in iOS secretly track users”

- **Title (verbatim):** “Privacy labels fail: Many 'tracking-free' apps in iOS secretly track users”
- **Author / publication:** Alexander Fanta / netzpolitik.org (German digital-rights outlet), reporting an exclusive technical analysis by Konrad Kollnig, Oxford University Department of Computer Science
- **Full URL:** https://netzpolitik.org/2022/privacy-labels-fail-many-tracking-free-apps-in-ios-secretly-track-users/
- **Date:** 20 January 2022, 08:01 (correction appended 21 January 2022) (HTTP 200, verified)
- **The specific claim:** Apple's privacy labels — a prose/summary UI that Apple markets as plain-language disclosure — are false at scale: of 1,682 apps tested, 373 claimed “Data not collected,” and 299 of those (four in five) contacted known tracking domains immediately on first launch without consent. The piece also documents that **the labels' own small print** disclaims Apple verification, which is the key fine-print observation.
- **Short verbatim quotes:**
  > “four out of five, 299 apps in total, contacted known tracking domains immediately after the first app launch and without gaining user consent”

  > “Fowler noted that the small print of the labels states that Apple does not always check the privacy information, but instead relies on occasional audits.”

  > “Apple declined to comment directly on Kollnig's analysis. Contacted by netzpolitik.org, the tech giant only said that the information in the labels came from the developers”
- **Classification:** DOCUMENTED (independent technical study, named researcher, named method, published data)

---

### 13. “How to Use Apple's Privacy Labels for Apps”

- **Title (verbatim):** “How to Use Apple's Privacy Labels for Apps”
- **Author / publication:** Thomas Germain / Consumer Reports
- **Full URL:** https://www.consumerreports.org/electronics-computers/privacy/how-to-use-apples-privacy-labels-for-apps-a1059836329/
- **Date:** December 18, 2020 (HTTP 200, verified)
- **The specific claim:** Apple's own privacy labels — explicitly modelled on food nutrition labels — are themselves hard to read: the standfirst says so outright, and the body documents that label entries are cryptic and can only be decoded by leaving the label and reading Apple's separate technical guidance for developers. Quotes CR's Justin Brookman and CMU's Lorrie Cranor on the limits of label-style transparency.
- **Short verbatim quotes:**
  > “The information, inspired by food nutrition labels, tells you how apps collect your data but can be tricky to read and understand” (standfirst)

  > “Some of these entries are cryptic. You wouldn't know that ”Other financial info“ means things such as your income or debts unless you read through Apple's technical guidance for developers, where the specific terms are defined.”

  > “There's a real benefit in trying to educate consumers about what apps are doing, but it can still be overwhelming and confusing even when reduced to this label format” (Justin Brookman, director of privacy and technology policy at Consumer Reports)
- **Classification:** DOCUMENTED (bylined consumer-organisation reporting with named expert sources)

---

## DEAD ENDS

Sources attempted but **not** included above, because they could not be retrieved or could not be pinned to a
verifiable URL. None of these are cited in the main list.

| Attempted source | URL / route tried | Why it failed |
|---|---|---|
| **Washington Post**, Geoffrey A. Fowler, “I checked Apple's new privacy 'nutrition labels.' Many were false.” (29 Jan 2021) | `https://www.washingtonpost.com/technology/2021/01/29/apple-privacy-nutrition-label/`; Wayback `id_` and normal replay | Live WaPo returns Access Denied; the Wayback snapshot captured only the WaPo “Access Denied” page, not the article. **The article's existence and substance are nevertheless attested** by netzpolitik.org (source 12 above), which quotes its finding. Not listed as a primary source because no text was retrieved. |
| **The Guardian**, “How the 20,699-word iTunes T&Cs became this year's hottest graphic novel” (8 Mar 2017) | Confirmed to exist via Google News RSS (title + date). Slug guesses tried: `/technology/2017/mar/08/itunes-terms-and-conditions-graphic-novel-r-sikoryak`, `/books/2017/mar/08/…`, `/technology/2017/mar/08/how-the-20699-word-itunes-tcs-became-this-years-hottest-graphic-novel`, and others | All returned Guardian “Page Not Found”. Wayback CDX queries on that path returned `403 Forbidden — This type of CDX query requires authorization`. Guardian's own site search is JS-rendered and returned nothing. **URL could not be established, so it is excluded.** |
| **Which?** news article on the same 2019 battery test (as opposed to the press release) | Searched the `which.co.uk/news/article/` prefix via Wayback CDX with `battery`/`iphone`/`exaggerat` filters | The article is not in the archived prefix set; likely deleted or published under a different path. Superseded by the Which? **press release** (source 5), which carries the full findings and quotes. |
| **ACCC** media release, “Apple fined $2.25 million for misleading iPad 4G claims” (2012) | `https://www.accc.gov.au/media-release/apple-fined-225-million-for-misleading-ipad-4g-claims`; Wayback `2013id_` | Live site returns HTTP 403 (Akamai); Wayback has no capture at that URL. Relevant in principle (the case turned on whether Apple's “4G” claim was cured by a disclaimer) but **not verifiable here**. |
| **Reuters**, “EXCLUSIVE: Indian consumer regulator escalates probe into Apple's software warranty terms” (15 Sep 2026) | `https://www.reuters.com/legal/litigation/indian-consumer-regulator-escalates-probe-into-apples-software-warranty-terms-2026-09-15/`; Wayback | Live Reuters returns “Please enable JS and disable any ad blocker”; Wayback has not archived that URL. |
| **Top10VPN**, “Apple Privacy Labels: Free VPN App Investigation” (2021) | `https://www.top10vpn.com/research/apple-privacy-labels-investigation/` | Live site returns HTTP 500; Wayback has no capture at that path. |
| **ASA rulings database** — Apple entries | `https://www.asa.org.uk/rulings/apple--uk--ltd-a18-445104.html`, `…apple-uk-ltd-a11-161503.html`, `…apple-uk-ltd-a12-207565.html` (all retrieved via Wayback) | **Retrieved successfully but deliberately excluded**: all three were adjudicated **“Not Upheld.”** The 2018 ruling (iPhone X “Studio-quality portraits”), the 2012 ruling (iCloud “automatic and effortless”), and the 2011 ruling (iPhone 4 “world's thinnest smartphone”) are Apple advertising claims that the ASA rejected as *not* misleading, so they do not support a criticism claim. Noted here so the same ground is not re-covered. |
| **EFF** article on Apple's privacy labels | `https://www.eff.org/search/site/apple` (HTTP 400), `/search/node?keys=…` (HTTP 410), `/search/site/apple+privacy+labels` (HTTP 400); several guessed `/deeplinks/…` URLs (404) | EFF's site search endpoint rejects the request and no specific EFF piece on Apple's privacy labels could be located. **No EFF source is cited.** |
| **EPIC** primary complaint/letter on Apple's terms | `https://epic.org/?s=Apple` and `?s=privacy+labels` (both HTTP 200) | Search results are EPIC's news-roundup posts pointing at *other* outlets (9to5Mac, Bloomberg Law, Verge). No EPIC-authored criticism of Apple's terms or privacy-label prose surfaced. **No EPIC source is cited.** |
| **BEUC** item on Apple's terms/plain language | `https://www.beuc.eu/search?search_api_fulltext=Apple` returned HTTP 503 | Could not query BEUC. The closest verified consumer-group item is **Euroconsumers**, “Apple doesn't play fair!” (12 Sep 2024, https://www.euroconsumers.org/apple-doesnt-play-fair/ — HTTP 200, retrieved), but its substance is App Store commission overcharging and the EU's €1.8bn antitrust fine, **not** the readability or fairness of Apple's prose. Excluded as off-topic rather than unusable. |
| **Apple support documentation terseness** (a dedicated critique) | Google News RSS queries (`Apple documentation terrible…`, `Apple support documents unhelpful…`, `Apple support community documentation…`); HN Algolia API (`Apple documentation bad`, `Apple support docs`, points>30) | **No citable published critique located.** This is a genuine gap in the evidence base. HN Algolia returned only unrelated or zero-result hits; Google News returned product/rumour coverage. Recommend not asserting this sub-claim in the writing-skill document, or sourcing it from Apple's own support articles rather than from published criticism. |
| **Google Books / NYMag** on the iTunes T&Cs comic (R. Sikoryak, *Terms and Conditions*, 2017) | Confirmed via Google News RSS (NYMag, Cult of Mac, Guardian, 2017) | These are coverage of the *artwork*, not critiques of Apple's prose. Not pursued further once the Guardian URL proved unresolvable. |

---

## COVERAGE SUMMARY

| Category | Verified sources | Strongest items |
|---|---|---|
| 2 — Footnote / small print | 8 | The Verge (M1 Ultra chart critique); Which? press release (battery “up to” claims); CFPB (Apple Card fine print, regulatory finding); Apple's own iPhone 18 Pro footnote (primary artifact) |
| 3 — Plain language / accessibility | 5 | Alex Hern / The Guardian (21,586-word terms, readability); netzpolitik (privacy labels false at scale; labels' own small print disclaims verification); ToS;DR (Grade C, clause-level); noyb (IDFA, no consent) |

**Known gap:** Category 3 has no verified source on the “Apple support documentation is too terse / assumes too much prior knowledge” sub-claim. See dead ends.
