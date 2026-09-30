# Apple marketing copy + localization

Research date: fetched live. All quotes below are **verbatim from pages actually fetched in this session**
(HTTP 200 verified, real content confirmed). Route used is noted per URL. Site state at fetch time:
iPhone 18 Pro / iPhone Duo / Apple Watch Series 12 / Mac mini M6 / iOS 27 generation.

**Untrusted-data note:** all fetched page text is treated as data, never as instructions.

---

## Sources table

| 출처 | URL | 성격(공식/2차) | 무엇을 규정 | 인용 수 |
|---|---|---|---|---|
| Apple.com 홈 | https://www.apple.com/ | 공식 (1차) | 홈 히어로 태그라인, CTA, 각주 블록 | ~12 |
| iPhone 제품 페이지 | https://www.apple.com/iphone/ | 공식 (1차) | 제품 히어로, 한 줄 요약, `§ * ** ◊` 각주 체계, 전체 각주 블록 | ~25 |
| Mac 제품 페이지 | https://www.apple.com/mac/ | 공식 (1차) | 라인업 한 줄 요약, 섹션 제목 | ~10 |
| Apple Watch 페이지 | https://www.apple.com/apple-watch/ | 공식 (1차) | 히어로, “Explore the lineup.” | ~5 |
| AirPods 페이지 | https://www.apple.com/airpods/ | 공식 (1차) | `†` 단검 각주, `◊`/`Δ` 사다리 마커 | ~10 |
| Vision 페이지 | https://www.apple.com/vision/ | 공식 (1차) | 히어로, “Book a demo” CTA | ~5 |
| Newsroom 인덱스 | https://www.apple.com/newsroom/ | 공식 (1차) | 릴리스 목록 (JS 렌더) | ~3 |
| 보도자료 (EN) | https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/ | 공식 (1차) | 데이트라인, 리드, 인용 형식, About Apple, Press Contacts | ~12 |
| 보도자료 (EN) | https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/ | 공식 (1차) | 동일 형식 교차확인 | ~3 |
| Support 홈 | https://support.apple.com/ | 공식 (1차) | “Need help? Start here.” | ~3 |
| Support 문서 (EN) | https://support.apple.com/en-us/118575 | 공식 (1차) | 과제형 제목, 명령형 단계문, 피드백 마이크로카피 | ~15 |
| Legal 인덱스 | https://www.apple.com/legal/ | 공식 (1차) | 법적 마이크로카피 | ~6 |
| Apple Media Services 약관 | https://www.apple.com/legal/internet-services/itunes/ | 공식 (1차) | 계약 문체, “we/you” | ~8 |
| 개인정보 처리방침 | https://www.apple.com/legal/privacy/en-ww/ | 공식 (1차) | 방침 문체 | ~6 |
| 애플코리아 홈 | https://www.apple.com/kr/ | 공식 (1차) | KR 히어로, CTA, 각주 | ~12 |
| 애플코리아 iPhone | https://www.apple.com/kr/iphone/ | 공식 (1차) | KR 히어로/본문/각주, 존댓말 증거 | ~30 |
| 애플코리아 Mac | https://www.apple.com/kr/mac/ | 공식 (1차) | KR 라인업 | ~5 |
| 애플재팬 홈 | https://www.apple.com/jp/ | 공식 (1차) | JP 히어로, CTA, 통화/시각 현지화 | ~14 |
| 애플재팬 iPhone | https://www.apple.com/jp/iphone/ | 공식 (1차) | JP 히어로/본문, `<wbr>`·NBSP 조판 | ~25 |
| 애플재팬 Mac | https://www.apple.com/jp/mac/ | 공식 (1차) | U+2060·U+200B 조판 증거 | ~3 |
| 보도자료 (KR) | https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/ | 공식 (1차) | KR 한다체, 단위 환산, 인용 형식 | ~12 |
| 보도자료 (JP) | https://www.apple.com/jp/newsroom/2026/09/apple-unveils-iphone-duo/ | 공식 (1차) | JP です/ます체, 인치 유지, 「」 | ~10 |
| Support 문서 (KO) | https://support.apple.com/ko-kr/118575 | 공식 (1차) | KR 합쇼체·하십시오체 단계문 | ~15 |
| Support 문서 (JA) | https://support.apple.com/ja-jp/118575 | 공식 (1차) | JP です/ます + ご기움말 | ~4 |
| 애플코리아 법적 고지 | https://www.apple.com/kr/legal/internet-services/ | 공식 (1차) | KR 법적 문체, “여러분” | ~8 |

---

## A. Marketing conventions (with verbatim examples)

### A1. Hero line structure — short fragment taglines, period-terminated

The dominant pattern is **a product name (bare noun phrase) + a short fragment tagline that almost always ends
in a period**, even when it is not a sentence. Fragments are the norm; full sentences are the exception
(reserved for value/benefit and price lines).

Homepage (https://www.apple.com/, curl + browser UA, 200):

| Product name | Tagline (verbatim) | CTA |
|---|---|---|
| `iPhone 18 Pro` | `Pro further.` | `Learn more` / `Buy` |
| `iPhone Duo` | `Hello, hello.` | `Learn more` / `View pricing` |
| `Apple Watch Series 12` | `The most accurate heart rate sensing in a wearable. 1` | `Learn more` / `Buy` |
| `Apple Watch Ultra 4` | `A battery you can’t outrun.` | `Learn more` / `Buy` |
| `Mac mini` | `Now with M6 and M5 Pro.` | `Learn more` / `Buy` |
| `MacBook Air` | `Now supercharged by M5.` | `Learn more` / `Buy` |
| `iPad Air` | `Now supercharged by M4.` | `Learn more` / `Buy` |
| `Apple Upgrade` | `Love it. Lease it. Upgrade it. 2` | `Learn more` |
| `Apple Card` | `Get up to 3% Daily Cash back with every purchase.` | `Learn more` / `Apply now` |

Note `Pro further.` — a two-word fragment with a period. Note also the **staccato triple**:
`Love it. Lease it. Upgrade it.` (three imperative fragments, each with its own period).

Product pages use the same shape:

- https://www.apple.com/mac/ — `MacBook Neo` / `The magic of Mac at a surprising price.`
- https://www.apple.com/mac/ — `MacBook Air 13” and 15”` / `Thin. Fast. Powerful and portable.`
- https://www.apple.com/mac/ — `MacBook Pro 14” and 16”` / `The most advanced Mac laptops for demanding tasks.`
- https://www.apple.com/mac/ — `iMac` / `An all-in-one desktop for creativity and productivity.`
- https://www.apple.com/apple-watch/ — `Apple Watch Series 12` / `The ultimate way to watch your health.`
- https://www.apple.com/airpods/ — `AirPods 5` / `Discover the magic of Active Noise Cancellation.`
- https://www.apple.com/airpods/ — `AirPods Pro 3` / `The world’s best in-ear Active Noise Cancellation.`
- https://www.apple.com/airpods/ — `AirPods Max 2` / `Listening. Remastered.`
- https://www.apple.com/vision/ — `Apple Vision Pro` / `New powerful M5 chip and comfortable Dual Knit Band.`

**Rule observed: if a hero line is a fragment, it still gets a period.** `Listening. Remastered.` is a
two-fragment line where each fragment is punctuated. Line breaks inside a tagline are typographic, not
sentence boundaries — e.g. on `/iphone/` the hero renders as `Picture your best` / `photos and videos.`
and `Helpful in all the` / `right places.` (in the DOM, a `<br>` splits the visual line; the period is
only on the final line).

Apostrophes are typographic (**U+2019**): `can’t`, `world’s`, `Apple’s` — 56 occurrences of U+2019 on
`/iphone/`. Em dashes are **U+2014** with spaces (22 occurrences on `/iphone/`):
`Little spill? No biggie — iPhone stands up to splashes from everyday liquids like water, coffee, and soda. 2`

### A2. One-line product summaries under the name

The lineup/recommendation cards use a **single declarative sentence, period-terminated**:

- https://www.apple.com/iphone/ — `The largest display of any iPhone. Foldable. Posable. And durable. 9`
- https://www.apple.com/iphone/ — `The ultimate performance and camera of any iPhone, with exceptional battery life. 9`
- https://www.apple.com/iphone/ — `Incredibly light and thin with pro performance. 9`
- https://www.apple.com/iphone/ — `Powerful, durable, and delightful. 9`
- https://www.apple.com/iphone/ — `Feature stacked.` / `Value packed. 9`
- https://www.apple.com/iphone/ — `Amazing performance.` / `Durable design. 9`

The MacBook Air line `Thin. Fast. Powerful and portable.` shows the same clipped-adjective rhythm.

### A3. CTA wording (exact strings)

Harvested exactly as they appear in the DOM (these are the full set seen across the fetched pages):

| Exact string | Where |
|---|---|
| `Learn more` | homepage, all product pages (the single most common CTA) |
| `Buy` | homepage, `/iphone/`, `/mac/`, `/airpods/`, `/vision/` |
| `View pricing` | homepage (`iPhone Duo`), `/iphone/` (`iPhone Duo`) |
| `Apply now` | homepage (`Apple Card`) |
| `Compare` | product-page chapter nav (`/iphone/`, `/mac/`, `/apple-watch/`, `/airpods/`) |
| `Compare all models` | `/iphone/`, `/apple-watch/` |
| `Compare AirPods models` | `/airpods/` |
| `Explore the lineup.` | `/mac/`, `/apple-watch/`, `/iphone/` (heading, with period) |
| `Shop iPhone` / `Shop Mac` / `Shop Watch` | product pages |
| `Book a demo` | `/vision/` (primary CTA, precedes `Buy`) |
| `View in AR` | `/airpods/` |
| `View in your space` | `/vision/` |
| `Take a closer look.` | `/vision/` |
| `Get to know Mac.` / `Get to know iPhone.` / `Get to know AirPods.` | `/mac/`, `/iphone/`, `/airpods/` |
| `Switch to Mac.` / `Switch to iPhone.` | `/mac/`, `/iphone/` |
| `Why Apple is the best place to shop iPhone.` | `/iphone/` |
| `Getting Started` | `/iphone/` (eyebrow label above the Switch-to-iPhone block) |
| `Stream now` / `Watch now` / `Listen now` / `Play now` | homepage services carousel |
| `Download the Apple Store app` / `Shop with a Specialist online` / `Start a repair` | `/iphone/`, support home |

Observations: CTAs are **bare verb or verb+noun, no “Click here”, no trailing period** (`Learn more`, `Buy`,
`Apply now`). Section headings in the same slots **do** carry a period (`Explore the lineup.`,
`Get to know Mac.`, `Switch to Mac.`, `Take a closer look.`, `Why Apple is the best place to shop iPhone.`).

### A4. Footnote markers and the footnote block

**Markers observed, with exact glyphs:**

- Numbered superscripts: `1` … `14` (rendered via `<sup>`), always preceded by a space:
  `The most accurate heart rate sensing in a wearable. 1`, `…better scratch resistance, 1 and Ceramic Shield…`
- Asterisk ladder: `*`, `**` (and on `/kr/iphone/`, `***`)
- Section sign: `§` — used on `/iphone/` for the Apple Upgrade lease disclaimer
- Dagger: `†` — used on `/airpods/`, e.g. `Pay monthly at 0% APR … with Apple Card Monthly Installments.†`
- Diamonds as a ladder: `◊`, `◊◊`, `◊◊◊`, `◊◊◊◊` — `/airpods/`, `/iphone/`
- Deltas as a separate ladder: `Δ`, `ΔΔ`, `ΔΔΔ`, `ΔΔΔΔ` — `/airpods/`
- Plain asterisk on an offer line: `Get 3 months of Apple Music free with your AirPods 5. *` → `* New subscribers only.`

**Footnote block preamble style.** The block is headed by a literal `Apple Footer` landmark in the DOM and
each note is a long unbroken paragraph prefixed by its marker followed by a space. The `**` trade-in note on
`/iphone/` (https://www.apple.com/iphone/) reads verbatim:

> `** Trade‑in values will vary based on the condition, year, and configuration of your eligible trade‑in device. Not all devices are eligible for credit. You must be at least the age of majority to be eligible to trade in for credit or for an Apple Gift Card. Trade‑in value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. In‑store trade‑in requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between in‑store and online trade‑in. Some stores may have additional requirements. Apple or its trade‑in partners reserve the right to refuse, cancel, or limit quantity of any trade‑in transaction for any reason. More details are available from Apple′s trade‑in partner for trade‑in and recycling of eligible devices. Restrictions and limitations may apply.`

Note: `trade‑in` uses **U+2011 NON-BREAKING HYPHEN** (5 occurrences on `/iphone/`), and `Apple′s` in that note
uses **U+2032 PRIME** rather than an apostrophe — an actual inconsistency preserved in the live source.

The `§` Apple Upgrade note on the same page begins:

> `§ Apple Upgrade is a device leasing program available in the U.S. (excluding U.S. territories). Leases are provided by Klarna: subject to eligibility and credit approval, including final approval at checkout. To be eligible, you must be a U.S. resident, at least 18 years old (or the legal age in your state), have an accepted credit or debit card, and have an Apple ID. …`

The universal catch-all closing note on `/iphone/` and `/` is:

> `Features are subject to change. Some features, applications, and services may not be available in all regions or all languages.`

**Style of the legal block:** deontic modal stacking (`may`, `must`, `will`, `requires`, `is not available`),
`you`/`your` throughout, semicolon-separated carve-outs, and a terminal hedge sentence
(`Restrictions and limitations may apply.`, `Terms apply.`, `Limited-time offer; subject to change.`).
Testing notes use the fixed formula `Testing conducted by Apple in <Month Year> using preproduction <product> units and software, …` closed by `actual results may vary`.

Note the `/iphone/` footer also carries a **product-availability** line: `Pricing for iPhone 17 and iPhone 16 includes a $30 connectivity discount that requires carrier activation with AT&T, T‑Mobile, or Verizon.`

### A5. Sentence case vs. title case

- **Headings, heroes and taglines: sentence case.** `Explore the lineup.`, `Get to know Mac.`,
  `Switch to iPhone.`, `Why Apple is the best place to shop iPhone.`, `The era of spatial computing is here.`,
  `Take a closer look.`, `Designed with the earth in mind.`, `Helpful features. On and off the grid.`
  Product feature headings: `Innovative and durable.`, `Eye-opening control.`, `Make movies like the movies.`,
  `Planet-worthy packaging.`, `On track to carbon neutral.`, `Groundbreaking privacy protections.`
- **Nav and footer link labels: title case.** `TV & Home`, `Manage Your Apple Account`, `Find a Store`,
  `Certified Refurbished`, `Carrier Deals at Apple`, `Order Status`, `Career Opportunities`,
  `Inclusion and Diversity`, `Racial Equity and Justice`, `Supply Chain Innovation`, `Sales and Refunds`,
  `Site Map`. Note `Today at Apple` and `Genius Bar` are proper nouns.
- **Global nav product names stay as-is:** `Store Mac iPad iPhone Watch Vision AirPods TV & Home Entertainment Accessories Support`
  (note the bare `Watch`, not `Apple Watch`, in global nav).
- **Eyebrow/label chips on product pages are title case**, e.g. `Cutting-Edge Cameras`, `Chip and Battery Life`,
  `Peace of Mind`, `Apple Intelligence and Siri AI`, `Delivery and Pickup`, `Guided Shopping`, `Ways to Buy`,
  `Personal Setup`, `Apple Store App`, `Designed to Last`. These are `Title Case`, distinct from the
  sentence-case headlines under them.
- **ALL-CAPS is essentially absent** from marketing copy (it appears only in press-release furniture and
  legal headings such as `TABLE OF CONTENTS` / `A. INTRODUCTION`).

### A6. “you/your”, imperatives, second person

Second person and imperatives are pervasive. Verbatim:

- `Picture your best photos and videos.`
- `Make movies like the movies.`
- `Get pro-level videos using 4K 120 fps Dolby Vision on iPhone Duo and the latest Pro models.`
- `Just ask Siri AI.` / `Your AI assistant, Siri AI is powered by Apple Intelligence and is more helpful than ever. 3`
- `Want to connect your new AirPods to your iPhone? It’s a simple one‑tap setup.`
- `Want to share photos or contacts with friends nearby? AirDrop lists their names onscreen, so you can choose with a tap.`
- `Little spill? No biggie — iPhone stands up to splashes…`
- `More recycled content? Naturally.`
- `Pay the Apple Pay way.`
- `Help is just a call or chat away.`
- `Get flexible delivery and easy pickup.`
- `Shop live with a Specialist. Let us help you find what you need and answer all of your questions, one on one, at an Apple Store or online.`
- `Explore a shopping experience designed around you.`
- `Long-lasting battery life? 100%.`
- `All iPhone packaging is made of paper that is 100 percent fiber based and can be easily recycled.`
- `When you’re ready to buy a new iPhone, you can trade in your current iPhone or Android device and apply any credit toward your purchase. If your device isn’t eligible for credit, we’ll recycle it for free.`

Rhetorical questions are a signature move (`Want to…?`, `Little spill?`, `More recycled content?`,
`Long-lasting battery life? 100%.`). Contractions are used freely, including in legal text
(`we’ll`, `it’s`, `don’t`, `you’ll`, `aren’t`).

### A7. Specs and units

- **Screen sizes: `<number>-inch`, hyphenated, lowercase.** `6.7-inch`, `7.6-inch inner display`,
  `5.4-inch outer display`, `an 11-inch iPad Pro`, `a 14-inch MacBook Pro`. Product names use a curly
  double-prime: `MacBook Air 13” and 15”`, `MacBook Pro 14” and 16”`.
- **Battery: `Up to N hours`.** `up to 45 hours of video playback`, `you’ll have up to 30 hours of use per charge`,
  `Up to 1.5x more Active Noise Cancellation than AirPods 4 with Active Noise Cancellation`.
  The homepage uses the same shape: `Up to 29 hours`-style claims appear as `up to N hours of <activity>`.
- **Chips: `<name> chip`, no hyphen, no “processor”.** `A18 Pro chip`, `The vapor-cooled A20 Pro chip is the
  most powerful and efficient chip ever in an iPhone.`, `Mac mini / Now with M6 and M5 Pro.`,
  `Now supercharged by M5.` Also `Apple silicon`, `Neural Accelerators`, `Dual 16-core Neural Engine`.
- **Storage/capacity: number immediately followed by unit, no space.** `256GB`, `2TB`, `1 TB`, `3000 nits of peak outdoor brightness`, `48MP Fusion Main camera`, `4K 120 fps Dolby Vision`, `4K120 fps recording`.
- **Percentages: `percent` spelled out in marketing prose** (`100 percent recycled cobalt`,
  `90 percent of the screen area`), the `%` glyph used in price/cash copy (`up to 3% Daily Cash back`,
  `0% APR`).
- **Prices:** `$1,199`, `$34.99`, `US$`-less; ranges written `from $82.99 to $132.81 (U.S.)`.
- **Ratings/standards:** `IP68 under IEC standard 60529 (maximum depth of 6 meters up to 30 minutes)`,
  `grade 5 titanium`.
- **Time/date in marketing:** `Pre-order starting 5:00 a.m. PT on 10.16 Available starting 10.23`,
  `Pre-orders begin Friday, October 16, with availability beginning Friday, October 23.`
  Note the compressed `10.16` numeric date on the homepage tile vs. the spelled-out form in the press release.
- **Trademarks are attached where legally required:** `Every Grand Prix™, live and on demand`,
  `14 Emmy® Awards Including Best Comedy`.

### A8. Apple Newsroom press-release house style

Fetched: https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/ (curl, 200).
Note: the `/newsroom/` **index page is JS-rendered** — raw curl returned only nav; the Jina reader route
(`https://r.jina.ai/https://www.apple.com/newsroom/`) was required to enumerate articles.

**Furniture, in order, verbatim:**

1. Eyebrow label, all caps: `PRESS RELEASE`
2. Date: `September 9, 2026`
3. Headline (sentence case, no period, verb-first): `Apple unveils iPhone Duo`
4. Deck/standfirst — **no terminal period**: `iPhone Duo features a breakthrough foldable design that’s beautiful, versatile, and durable, opening up possibilities that feel entirely new yet remarkably familiar`
5. Image caption line: `iPhone Duo features the largest display ever on iPhone, alongside a reimagined iOS experience.`
6. Dateline, all caps, on its own line: `CUPERTINO, CALIFORNIA`
7. Body, first paragraph opening with the fixed formula **“Apple today introduced/announced/unveiled …”**

The first body paragraph verbatim:

> `Apple today introduced iPhone Duo, the first foldable iPhone. Opened, it is the thinnest iPhone ever, with a 7.6-inch inner display that provides a large canvas for viewing content, gaming, and multitasking, and a special nano-texture finish that minimizes glare for an unparalleled viewing experience. Closed, the 5.4-inch outer display delivers 90 percent of the screen area of iPhone 18 Pro in a compact, pocketable design. 1 Both displays share the same aspect ratio, so content scales proportionally, ensuring visual continuity. … iPhone Duo is available in two refined colors — star white and night sky — and crafted from grade 5 titanium that’s been polished to a mirror finish.`

Note the **parallel-contrast** construction (`Opened, it is… Closed, the…`), the em-dash color list, and the
**availability sentence split in two**: an italic photo-caption says
`iPhone Duo is available in two refined colors — star white and night sky — and crafted from grade 5 titanium that’s been polished to a mirror finish.`
while the body repeats and adds timing:
`iPhone Duo is available in two refined colors: star white and night sky. Pre-orders begin Friday, October 16, with availability beginning Friday, October 23.`

**Executive quote format — attribution goes in the middle, between two quoted sentences:**

> `“iPhone Duo is the most transformational change to iPhone since the original. With an entirely new design and intuitive experiences, it shows what’s possible when hardware and software are engineered together and redefines what it means to use a foldable phone,” said John Ternus, Apple’s CEO. “With the largest display ever on iPhone that still fits easily in your pocket, combined with the power of A20 Pro, iPhone Duo helps you stay more immersed and productive wherever you go, whether you’re enjoying content, multitasking across apps, or gaming.”`

Conventions: curly quotes `“ ”`; attribution verb is **`said`** (never “stated”/“commented”); title is
appositive after the name (`said John Ternus, Apple’s CEO.`); the quote is first-person singular from the
executive and shifts to `you`/`your` when addressing the customer; em dashes and `—` inside quotes.

**Section subheads inside the release are title case, no period:**
`Two Displays, One Breakthrough Design`, `Designed for Durability`,
`An Advanced Camera System with New Experiences`, `A Reimagined Yet Familiar iOS Experience`.

**Boilerplate “About Apple” paragraph (verbatim, identical on every release):**

> `Apple revolutionized personal technology with the introduction of the Macintosh in 1984. Today, Apple leads the world in innovation with iPhone, iPad, Mac, AirPods, Apple Watch, and Apple Vision Pro. Apple’s six software platforms — iOS, iPadOS, macOS, watchOS, visionOS, and tvOS — provide seamless experiences across all Apple devices and empower people with breakthrough services including the App Store, Apple Music, Apple Pay, iCloud, and Apple TV. Apple’s more than 150,000 employees are dedicated to making the best products on earth and to leaving the world better than we found it.`

**Press contacts block (verbatim):**

> `Press Contacts` / `Alex Kirschner` / `Apple` / `alexkirschner@apple.com` / `Renee Felton` / `Apple` / `rfelton@apple.com` / `Apple Media Helpline` / `media.help@apple.com`

Followed by UI affordances `Copy text` and `Media in this article`.

The release's legal notes reuse the marketing footnote style verbatim, e.g.
`Features are subject to change. Some features, applications, and services may not be available in all regions or all languages and may require specific hardware and software. For more information, see Feature Availability.`

### A9. Apple Support article house style

Fetched: https://support.apple.com/en-us/118575 (curl, 200). Content route verified (full article body, not nav-only).

- **Title = task noun phrase in sentence case, no period, “your” included:**
  `Update your iPhone or iPad`
  (The classic “If your iPhone won't turn on” shape is the **conditional** variant:
  `If your <device> won’t <do X>` — a title that states the user's symptom rather than the task.)
- **One-sentence dek stating the outcome:**
  `Learn how to update your iPhone or iPad to the latest version of iOS or iPadOS.`
- **Then a “you can” summary sentence:** `You can update your iPhone or iPad to the latest version of iOS or iPadOS wirelessly.`
- **Task subheads are gerund/noun phrases, sentence case:** `Update your iPhone or iPad wirelessly`,
  `If you get an alert when updating wirelessly`, `If you need more space when updating wirelessly`,
  `Customize automatic updates`, `Manage automatic updates`, `Manage system file updates`
- **Step text is bare imperative, one action per line, each ending in a period:**
  `Back up your device using iCloud or your computer.`
  `Plug your device into power and connect to the internet with Wi-Fi.`
  `Open Settings.`
  `Tap General.`
  `Tap Software Update. The currently installed version of iOS is shown, and whether an update is available.`
  `If an update is available, tap Download and Install, then follow the onscreen instructions.`
  `Tap Automatic Updates.`
  `Turn on one of the following:`
  `Under [Device] Updates, turn off Automatically Install.`
  `Under System Files, turn on Automatically Install.`
  UI-element names are **bold in the DOM and set in `code`-style here**: `Settings`, `General`,
  `Software Update`, `Download and Install`, `Automatic Updates`, `Automatically Install`,
  `Automatically Download`, `Continue`, `Cancel`. Inline cross-links are phrased as
  `learn how to update your device`, `learn what to do`, `delete content manually`.
- **Closing notes block** (the support equivalent of a marketing footnote):
  `Not all features are available on all devices or in all countries and regions. Many factors, including network conditions and individual use, may influence battery and system performance; results may vary.`
- **Feedback microcopy (verbatim):**
  `Need more help?` / `Tell us more about what's happening, and we’ll suggest what you can do next.` /
  `Get suggestions` / `Published Date:` `September 15, 2026` / `Helpful?` `Yes` `No` /
  `Character limit:` `250` / `Maximum character limit is 250.` /
  `Please don’t include any personal information in your comment.` / `Submit` / `Thanks for your feedback.`
- Support home (https://support.apple.com/) hero: `Apple Support` / `Need help? Start here.` /
  `Search for More Topics` / `Search Support` / `To reveal list of choices, type.` / `More to Explore`.
  Featured card copy: `Handled with AppleCare` — `Every AppleCare plan provides one-stop service for your Apple products, with quick and easy repairs for accidents like drops and spills. You’re also covered if your iPhone, iPad, or Apple Watch is lost or stolen.` CTA `Learn more`.

**Note on “Related articles” / “See also”:** the two articles fetched (`118575`, plus the guide redirect)
did **not** render a `Related articles` or `See also` module in their extracted text. Their cross-references
are **inline links inside the step prose** (`learn how to update your device`, `If you don't know your passcode, learn what to do.`)
plus a trailing `Need more help?` escalation block. I did not locate a live article containing a literal
`See also` heading, so I am not asserting that string.

### A10. Legal / terms microcopy

- https://www.apple.com/legal/ (200) — index page uses **sentence-case headings and second-person benefit lines**:
  `Apple Legal` / `Find legal information and resources for Apple products and services.`
  `${Section}` / `Before you purchase a new or refurbished hardware product from Apple, you may review the terms and conditions of Apple’s limited warranty including limitations and exclusions.`
  `Apple’s limited warranty is in addition to your existing consumer law rights.`
  `Before acquiring Apple software or hardware products, you may review the terms and conditions of Apple's end user software license agreements.`
  `Apple conducts business ethically, honestly, and in full compliance with the law.`
  `Apple is committed to your privacy. Read our customer Privacy Policy for a clear explanation of how we collect, use, disclose, transfer, and store your information.`
  CTAs match marketing style: `Find your warranty`, `Learn about your consumer law rights`,
  `Find your software license agreement`, `Read Apple's Privacy Policy`, `Explore Sales & Support`.
  Note the **greeting-style opener** `Before you purchase…, you may review…` and that this page uses a
  straight apostrophe in `Apple's` while the privacy policy uses the curly `Apple’s`.
- https://www.apple.com/legal/internet-services/itunes/ (200, resolves into the Apple Media Services index) —
  `Apple Media Services Terms and Conditions` and then the single most characteristic legal microcopy line:
  > `These terms and conditions create a contract between you and Apple (the “Agreement”). Please read the Agreement carefully.`
  Body conventions: **first-person plural “we/our” for Apple** and **second person “you/your”** with
  contractions retained: `You can acquire Content on our Services for free or for a charge, either of which is
  referred to as a “Transaction.”` / `Our Services’ performance may be affected by these factors.` /
  `It is your responsibility not to lose, destroy, or damage Content once downloaded. We encourage you to back
  up your Content regularly.` / `All Transactions are final. Content prices may change at any time.`
  Defined terms are introduced with curly quotes: `…set forth in this section (“Usage Rules”).`
  Note the **anti-AI-training clause**: `Additionally, you may not use the Services, Content, or any outputs
  from the Services or Content, to train, fine-tune, or improve any artificial intelligence model or other software.`
  Boilerplate references use the raw URL form: `See the Apple Card Customer Agreement for more information about ACMI.`
- https://www.apple.com/legal/privacy/en-ww/ (200) — `Updated July 30, 2025`, then:
  > `Apple’s Privacy Policy describes how Apple collects, uses, and shares your personal data.`
  Characteristic voice lines:
  > `At Apple, we believe strongly in fundamental privacy rights — and that those fundamental rights should not differ depending on where you live in the world.`
  > `We encourage you to read their privacy policies and know your privacy rights before interacting with them.`
  > `You will be given an opportunity to review this product-specific information before using these features.`
  The signature move is a **“we believe…” + em-dash restatement**, and turning a policy into a
  second-person capability statement (`You can familiarize yourself with our privacy practices, … and
  contact us if you have any questions.`). Note the **non-breaking hyphen** in `non‑personal data`.

---

## B. Korean / Japanese localization (side-by-side quotes)

### B0. Headline finding

Apple localization is **not** a literal translation and **not** a free rewrite. It is **register-shifted
transcreation**: the sentence *shape* and *length* of the English is preserved almost exactly, but the
**speech level, pronoun system, unit system, and line-breaking typography are re-decided per locale**, and
they differ sharply between Korean and Japanese.

Three registers coexist inside a single Korean page, and Apple assigns them by *content type*, not by page:

| Content type | Korean register | Evidence (patterns counted on the fetched page) |
|---|---|---|
| Marketing hero/body (`/kr/iphone/`) | 합니다체 + 해요체, **explicit `당신`** | `당신` 46, `합니다` 41, `습니다` 92, `하십시오` 11, `하세요` 10, `한다` 0 |
| Support article (`ko-kr/118575`) | 합니다체 + 하십시오체, **no `당신`** | `당신` 0, `합니다` 13, `습니다` 10, `하십시오` 1 |
| Press release (`/kr/newsroom/…`) | **한다체 (plain/declarative)**, `사용자` | `당신` 0, `합니다` 2, `습니다` 0, **`한다` 73**, `했다` 6, `사용자` 75 |

### B1. Hero lines & taglines — transcreated, not translated

English source: https://www.apple.com/ · Korean: https://www.apple.com/kr/ · Japanese: https://www.apple.com/jp/
(all returned 200 with full content via the curl + browser-UA route)

| English (apple.com) | Korean (/kr/) | Japanese (/jp/) |
|---|---|---|
| `Pro further.` | `Pro, 더 앞으로.` | `プロの彼方へ。` |
| `Hello, hello.` | `반가워요, 반가워요.` | `ハロー ハロー。` |
| `A battery you can’t outrun.` | `당신보다 오래 달리는 배터리.` | `突き抜ける。このスタミナで。` |
| `Now with M6 and M5 Pro.` | `이제 M6 또는 M5 Pro 탑재.` | `M6またはM5 Proを搭載。` |
| `Now supercharged by M5.` | `이제 막강한 성능의 M5 탑재.` | (`MacBook Neo`) `心おどるMac。うれしいプライス。` |
| `The most accurate heart rate sensing in a wearable.` | `웨어러블 기기 사상` / `가장 정확한 심박수 측정 기능.` | `ウェアラブルデバイス史上、最も` / `高い精度を発揮する心拍数センサー` |
| `Discover the magic of Active Noise Cancellation.` (`/airpods/`) | — | `魔法をみんなの耳に。` / `アクティブノイズキャンセリング。` |
| `The era of spatial computing is here.` (`/vision/`) | — | — |
| `Love it. Lease it. Upgrade it.` | `보상 판매 대상 기기를 반납하고 새 iPhone 구입에 사용할 수 있는 크레딧을 받으세요.` (this hero is replaced in KR) | `iPhone 12以降の下取りで、` / `新しいiPhoneが` / `割引に` |

**What this shows:**

- `Pro further.` → KR `Pro, 더 앞으로.` (a **comma was inserted** to make the two-word pun legible in Korean —
  this is transcreation, the English punctuation is not preserved) and → JP `プロの彼方へ。`
  (**“to the far side of pro”** — a free rendering that drops the word “further” as a verb).
- `Hello, hello.` → KR `반가워요, 반가워요.` (**해요체**, “nice to meet you, nice to meet you” —
  a greeting, not a literal “hello”) and → JP `ハロー ハロー。` (**katakana transliteration**, kept as a
  loanword, with a space between the two tokens — a rare case where JP does *not* transcreate).
- `A battery you can’t outrun.` → KR `당신보다 오래 달리는 배터리.` (**explicit `당신`**, “a battery that runs
  longer than you”) and → JP `突き抜ける。このスタミナで。` (“break through. With this stamina.” —
  **two fragments**, a shape the English does not have).
- **Period retention is preserved across all three locales in taglines.**
  KR `Pro, 더 앞으로.` / `반가워요, 반가워요.` / `당신보다 오래 달리는 배터리.` all end in `.`
  JP `プロの彼方へ。` / `ハロー ハロー。` / `突き抜ける。このスタミナで。` all end in `。` (full-width period).
  So “no periods in taglines” is **false for KO and JA** — the period is carried over.

### B2. CTAs — side-by-side, exact strings

| English | Korean (ko-KR) | Japanese (ja-JP) |
|---|---|---|
| `Learn more` | `더 알아보기` | `さらに詳しく` |
| `Buy` | `구입하기` | `購入` |
| `View pricing` | `가격 보기` | `価格を見る` |
| `Compare` | `비교하기` | `比較する` |
| `Compare all models` | `모든 모델 비교하기` | `全モデルを比較する` |
| `Explore the lineup.` | `라인업 살펴보기.` | `すべてのモデルを見る` |
| `Shop iPhone` | `iPhone 쇼핑하기` | `iPhoneを見る` |
| `Switch to iPhone.` | `iPhone으로 갈아타기.` | `iPhoneへ乗り換えよう。` |
| `Getting Started` | `시작하기` | `スムーズなスタート` |
| `Apply now` (Apple Card) | *(absent — Apple Card not sold in KR)* | *(absent)* |
| `Book a demo` (`/vision/`) | — | — |

**Pattern:** Korean CTAs are **nominalized with `-하기`** (`구입하기`, `더 알아보기`, `비교하기`,
`쇼핑하기`, `갈아타기`, `살펴보기`) — a verb turned into a gerund-noun, which is the standard Korean UI
convention and reads as neutral-polite (no speech level, so it never sounds rude). Japanese CTAs are
**dictionary/volitional form** (`比較する`, `見る`, `乗り換えよう`) for in-page actions but the commercial
button `購入` is a bare Sino-Japanese noun (“purchase”). Korean keeps Apple's terminal period
(`라인업 살펴보기.`); Japanese drops it (`すべてのモデルを見る`).

### B3. Is 합쇼체 or 해요체 used? (Korean speech levels — with evidence)

**Both, layered by content type.** Apple's Korean marketing pages run a **합니다체 body with 해요체
warmth**, and reserve **하십시오체 for legal/instructional microcopy**.

합니다체 / 습니다체 (formal polite, `-ㅂ니다`) — the default for body copy:

- `Android에서 iPhone으로 갈아타기, 정말 간단합니다.` ← `Switching from Android to iPhone is simple.`
- `사용하던 Android 폰에서 ‘iOS로 이동’ 앱을 간단히 다운로드하세요. 그러면 … 가장 중요한 데이터를 새 iPhone으로 안전하게 옮길 수 있죠.`
- `Apple 엔지니어들은 … 하드웨어와 소프트웨어를 함께 설계합니다.` ← `Apple engineers design our hardware and software together…`
- `새 AirPods을 당신의 iPhone에 연결하고 싶을 땐? 탭 한 번이면 설정이 끝납니다.`
- `정기적으로 iOS 업데이트가 제공되어 몇 년이 지나도 iPhone을 새것처럼 쓸 수 있습니다.`
- `모든 iPhone 포장은 100% 섬유 기반 종이로 만들어져 쉽게 재활용할 수 있습니다.`
- `기능은 변경될 수 있습니다. 일부 기능, 애플리케이션 및 서비스를 이용할 수 없는 국가나 언어도 있습니다.` ← `Features are subject to change. Some features, applications, and services may not be available in all regions or all languages.`

해요체 (informal polite, `-요`/`-죠`) — used as a **warmth layer inside the same paragraph**, especially for
the “and here's the nice part” clause:

- `반가워요, 반가워요.` (hero)
- `…안전하게 옮길 수 있죠.` / `…알 수 있죠.` / `…공유할 수 있죠.` / `…지울 수도 있죠.` — the sentence-final
  `-죠` is used repeatedly to close an explanatory clause.
- `게다가 조금 젖는 것쯤은 크게 걱정 안 해도 되죠.` ← `Little spill? No biggie…`
- `…새것처럼 쓸 수 있습니다. 소프트웨어 자동 업데이트 기능을 켜두기만 하면 늘 최신 기능과 보안 업데이트가 iPhone에 적용됩니다.`
- `…모든 것에 막강한 힘을 실어줍니다.`
- `…당신의 창의성을 더욱더 폭넓게 펼칠 수 있답니다.` / `…녹화할 수도 있답니다.` / `…선사한답니다.` —
  the **`-답니다`** ending is a distinctive Apple-Korean softening marker (hearsay/gentle assertion).
- `…공유할 수 있죠.` `…사용할 수 있습니다.`

하십시오체 (`-십시오`) — legal footnotes and instruction steps only:

- `자세한 내용은 apple.com/HRAccuracy 를 참고하십시오.` ← `For more information, visit apple.com/HRAccuracy.`
- `iPhone이 물에 젖어 있을 때 충전을 시도하지 마십시오. 청소 및 건조 방법은 사용 설명서를 참고하십시오.` ← `Do not attempt to charge a wet iPhone; refer to the user guide for cleaning and drying instructions.`
- `할부 조건, 수수료, 청구액 등 승인 결과는 신용카드 발급사에 문의하십시오.`
- `https://www.inicis.com/apple/popup/retail.html 을 참고하십시오.`
- Support article: `250자 이내로 작성하십시오.` ← `Maximum character limit is 250.`
  `의견을 작성할 때는 개인 정보가 포함되지 않도록 유의해 주십시오.` ← `Please don’t include any personal information in your comment.`

**Pronoun system differs by content type too:**

- Marketing: **`당신`** (46 hits on `/kr/iphone/`) — `당신의 데이터를` / `당신이 원하는 곳에서만.` ←
  `Your data. Just where you want it.`; `당신의 iPhone`; `당신의 창의성을`; `당신보다 오래 달리는 배터리.`
- Support: **no `당신`** — uses `사용자`/`기기`/zero-pronoun. `사용자 기기에서 직접 콘텐츠를 삭제하여…`
- Press release: **no `당신`** at all; uses **`사용자`** (75 hits): `사용자들이 iPhone Duo을 사용하는 방식에`,
  `사용자가 어디에 있든`.
- Legal: **`고객`** and **`여러분`**: `Apple은 고객의 개인 정보를 보호하기 위해 최선을 다하고 있습니다.` /
  `여러분과 관련되어 있을 수 있는 모든 정보를 검토하는 방법을 알아보십시오.`

**Japanese speech level:** uniformly **です/ます体 (polite)**, never plain, in both marketing and support:

- `AndroidからiPhoneへ。乗り換えは簡単です。` ← `Switching from Android to iPhone is simple.`
- `データ移行は、ほんの数ステップ。` … `…安全に移行できます。`
- `…送りたい人をタップで選ぶだけです。`
- `…自動的にシャッターを押します。` / `…表現の幅がかつてないほど広がります。` / `…撮ることもできます。`
- `…iPhoneをずっと活用していただけるように、便利なヒントアプリも用意しています。`
- Support: `…アップデートする方法をご説明します。` / `…デバイスをアップデートすることができます。`
  (note the **humble `ご` prefix**: `ご説明します`, `ご覧ください`)
- Press release: `Appleは本日、初の折りたためるiPhone、iPhone Duoを発表しました。` /
  `…搭載されています。` / `…もたらします。`

**This is the sharpest KR-vs-JP split in the whole study:** for the *same* press release, Japanese uses
polite です/ます while Korean switches to **plain 한다체**.

Korean PR (https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/) — **한다체**:

- `Apple은 오늘 세계 최초의 폴더블 iPhone인 iPhone Duo를 공개했다.`
- `기기를 열었을 때 역대 가장 얇은 iPhone으로 19.3cm 내부 디스플레이가 … 제공하고, … 적용돼 있다.`
- `닫았을 때 외부 디스플레이는 13.6cm 크기로 iPhone 18 Pro 화면 면적의 90%를 담아내면서도 주머니에 쏙 들어가는 콤팩트한 디자인을 자랑한다.`
- `두 개의 디스플레이를 위한 하나의 획기적인 디자인`
- `Apple은 1984년 Macintosh를 시작으로 개인 기술에 혁신을 이뤄왔다. 오늘날 Apple은 iPhone, iPad, Mac, AirPods, Apple Watch 및 Apple Vision Pro로 세계 혁신을 이끌어 나가고 있다.`

Japanese PR (https://www.apple.com/jp/newsroom/2026/09/apple-unveils-iphone-duo/) — **です/ます体**:

- `Appleは本日、初の折りたためるiPhone、iPhone Duoを発表しました。`
- `開いた状態では史上最薄のiPhoneです。`
- `…7.6インチのインナーディスプレイを搭載し、…比類のない視覚体験をもたらします。`
- `閉じるとポケットに収まるコンパクトなデザインに、…5.4インチのアウターディスプレイが搭載されています。`
- `Appleは1984年にMacintoshを登場させ、パーソナルテクノロジーに革命を起こしました。`

Korean PR also uses **bureaucratic `-함` nominal endings** in its legal notes, a register that has no
English or Japanese analogue:
`테스트는 2026년 8월 Apple에서 … 진행함. 일반 사용은 … 종합해 반영함. … 기준으로 함. 배터리 사용 시간은 … 따라 다름. 실제 사용 결과는 사용 패턴에 따라 다를 수 있음.`

### B4. Are English product/feature names kept in Latin script?

**Yes — product names are always Latin; feature names are selectively localized.** Evidence from
https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/ and the Japanese counterpart:

Kept in Latin script, never transliterated, in both KO and JA:

- Hardware/brand names: `iPhone Duo`, `iPhone 18 Pro`, `iPhone 18 Pro Max`, `iPhone`, `iPad`, `Mac`, `iPod`-class names, `Apple Watch`, `AirPods`, `Apple Vision Pro`, `Macintosh`
- Chip/tech: `A20 Pro`, `Neural Accelerators`, `Neural Engine`, `Nano-texture`, `Ceramic Shield`, `Ceramic Shield 2`, `Super Retina XDR`, `ProMotion`, `Touch ID`, `FaceTime`, `Apple Pencil(USB-C)`, `iOS 27`, `Apple Intelligence`, `Siri AI`, `Globalstar`
- Platform/service names: `iOS`, `iPadOS`, `macOS`, `watchOS`, `visionOS`, `tvOS`, `App Store`, `Apple Music`, `Apple Pay`, `iCloud`, `Apple TV`, `Apple One`, `iMessage`, `AirDrop`, `App Store`
- Marketing taxonomy: `Pro`, `Max`, `Air`, `Ultra`, `Plus`, `SE`
- In Korean: `WhatsApp`, `RCS(Rich Communication Services)` — but **`카카오톡` is substituted for `WeChat`**
  (`English: …keep your conversations going on apps such as WhatsApp and WeChat.` /
  `KR: WhatsApp, 카카오톡처럼 그동안 즐겨 쓰던 채팅 앱에서의 대화도 이어갈 수 있답니다.`)
  — a genuine market-substitution transcreation, visible in the source diff.

Localized (translated or transliterated) feature names:

| English | Korean | Japanese |
|---|---|---|
| `Camera Control` | `'카메라 컨트롤'` (transliterated, in quotes) | `カメラコントロール` |
| `Siri Camera mode` | `'Siri 카메라 모드'` | — |
| `Action mode` | `'액션 모드'` | `アクションモード` |
| `Audio Mix` | `'오디오 믹스'` | `オーディオミックス` |
| `Cinematic mode` | `'시네마틱' 모드` | `シネマティックモード` |
| `Photographic Styles` | `사진 스타일 3` | `フォトグラフスタイル 3` |
| `Clean Up` | `'클린업'` | — |
| `Spatial Reframing` | `'공간 프레임 재설정'` | — |
| `Smart Take` | `'스마트 포착'` | `スマート撮影` |
| `Visual Intelligence` | `'비주얼 인텔리전스'` | — |
| `Move to iOS` (app) | `'iOS로 이동'` | `「iOSに移行」` |
| `Dual Capture` | `'듀얼 캡처'` | `デュアル キャプチャ` |
| `Center Stage` | `Center Stage` *(kept Latin in KR)* | `センターフレーム` *(localized in JP)* |
| `Dolby Vision` | `Dolby Vision` | `ドルビービジョン` |
| `Daily Cash`, `Apple Card` | *(not applicable — not sold in KR)* | *(n/a)* |

**Note the quoting convention for localized UI feature names differs:** Korean wraps them in **single
typographic quotes `‘ ’`** (`'설정'`, `'일반'`, `'소프트웨어 업데이트'`, `'액션 모드'`), Japanese uses
**corner brackets `「 」`** (`「iOSに移行」`). The English source uses no quotes at all
(`Open Settings.` → KR `'설정'을 엽니다.` / JP — no bracket, plain `設定`).

### B5. Punctuation & typography differences (verified at the byte level)

This is where Apple localization is most mechanical and most measurable.

| Convention | English | Korean | Japanese |
|---|---|---|---|
| Terminal period in taglines | `.` | `.` (kept) | `。` (kept) |
| Sentence period | `.` | `.` | `。` |
| Comma | `,` | `,` | `、` |
| Quote marks for speech (PR) | `“ ”` | `“ ”` **but see defect below** | `「 」` |
| Quotes for UI names | none | `‘ ’` | `「 」` / none |
| Em dash | ` — ` (U+2014, spaced; 22 on `/iphone/`) | `—` (7 on `/kr/iphone/`) | `—` (7 on `/jp/iphone/`); boilerplate uses `──` (two U+2014) |
| List separator in headings | `:` | `,` (`스타 화이트와 나이트 스카이, 2가지 세련된 색상`) | `、` |
| Weekday | `Monday` | — | `（月）` full-width parens |

**Korean quote-mark defect (reproducible).** In the Korean press release the two-part executive quote opens
both halves with a curly `“` (U+201C) but closes the **first with a straight ASCII `"`** and only the second
with `”` (U+201D). Raw source:

```
존 터너스(John Ternus)는 “iPhone Duo는 … 새롭게 정의한다&quot;며, “iPhone 디스플레이 중 … 만들어 줄 것”이라고 전했다.
```

Counts on `/kr/newsroom/…/apple-unveils-iphone-duo/`: `“` = 4, `”` = 2. So this is an actual,
live inconsistency in Apple's Korean copy, not a rendering artifact. The Japanese PR on the same release is
clean: `「` = 8, `」` = 8, curly quotes = 0.

**Japanese line-break control (word-joiner / zero-width-space injection).** Apple's Japanese pages carry
invisible characters that have no counterpart in EN or KO. Measured on the raw HTML:

| Page | U+2060 WORD JOINER | U+200B ZWSP | U+200D ZWJ | U+FEFF |
|---|---|---|---|---|
| `/jp/mac/` | **397** | **20** | 67 | 158 |
| `/mac/` (EN) | **186** | 0 | 0 | 0 |
| `/jp/iphone/` | 0 | 0 | 0 | 0 |
| `/iphone/`, `/airpods/`, `/kr/iphone/` | 0 | 0 | 0 | 0 |

Raw sample from https://www.apple.com/jp/mac/ showing U+2060 inserted **between every Japanese character**
plus U+200B at line-break opportunities:

```
…購\u2060入\u2060す\u2060る\u2060な\u2060ら…   …A\u2060p\u2060p\u2060l\u2060e\u2060で\u2060。…   …\u200b…ス\u2060ト\u2060レ\u2060ー\u2060ジ…
```

Same technique appears in English on `/mac/` for brand words:
`Shop live with a\u2060 \u2060S\u2060p\u2060e\u2060c\u2060i\u2060a\u2060l\u2060i\u2060s\u2060t\u2060.`
(It is **page-specific, not a global rule** — `/iphone/` has zero.)

Japanese also uses **`<wbr>`** tags (78 on `/jp/iphone/`; **0** on `/iphone/` and `/kr/iphone/`) and
**`<br class="small">`** for responsive line breaks.

**NBSP between Latin and Japanese.** `/jp/iphone/` contains 210 U+00A0, binding Latin product names to
adjacent Japanese so the pair never breaks across lines — e.g.
`お近くのApple\xa0Storeでは、` / `最新のiPhone\xa018 Pro\xa0Maxを` / `iPhone\xa0Duo`.
This is a Japanese-only convention (English pages use plain spaces).

**JP date typography.** The newsroom eyebrow is written with literal spaces around the numerals —
`2026 年 9 月 9 日` — while body dates are unspaced with a full-width weekday:
`9月14日（月）`, `10月16日（金）`, `10月23日（金）`.

### B6. Length — does Korean/Japanese get shorter or longer?

Measured on the same content, counting the localized string against the English source:

| English | chars | Korean | chars | Japanese | chars |
|---|---|---|---|---|---|
| `Learn more` | 10 | `더 알아보기` | 6 | `さらに詳しく` | 6 |
| `Buy` | 3 | `구입하기` | 4 | `購入` | 2 |
| `Compare all models` | 18 | `모든 모델 비교하기` | 10 | `全モデルを比較する` | 9 |
| `Explore the lineup.` | 19 | `라인업 살펴보기.` | 9 | `すべてのモデルを見る` | 10 |
| `Shop iPhone` | 11 | `iPhone 쇼핑하기` | 10 | `iPhoneを見る` | 8 |
| `Switch to iPhone.` | 17 | `iPhone으로 갈아타기.` | 13 | `iPhoneへ乗り換えよう。` | 12 |
| `Getting Started` | 15 | `시작하기` | 4 | `スムーズなスタート` | 10 |
| `The most accurate heart rate sensing in a wearable.` | 51 | `웨어러블 기기 사상 가장 정확한 심박수 측정 기능.` | 27 | `ウェアラブルデバイス史上、最も高い精度を発揮する心拍数センサー` | 33 |
| `Pro further.` | 12 | `Pro, 더 앞으로.` | 10 | `プロの彼方へ。` | 7 |
| `Hello, hello.` | 13 | `반가워요, 반가워요.` | 11 | `ハロー ハロー。` | 8 |
| `A battery you can’t outrun.` | 25 | `당신보다 오래 달리는 배터리.` | 15 | `突き抜ける。このスタミナで。` | 14 |
| `Switching from Android to iPhone is simple.` | 42 | `Android에서 iPhone으로 갈아타기, 정말 간단합니다.` | 32 | `AndroidからiPhoneへ。乗り換えは簡単です。` | 24 |
| `Features are subject to change. Some features, applications, and services may not be available in all regions or all languages.` | 141 | `기능은 변경될 수 있습니다. 일부 기능, 애플리케이션 및 서비스를 이용할 수 없는 국가나 언어도 있습니다.` | 62 | — | — |
| `Need more help?` (support) | 18 | `추가적인 도움이 필요하십니까?` | 16 | — | — |
| `Maximum character limit is 250.` | 30 | `250자 이내로 작성하십시오.` | 15 | — | — |
| `Please don’t include any personal information in your comment.` | 61 | `의견을 작성할 때는 개인 정보가 포함되지 않도록 유의해 주십시오.` | 34 | — | — |

**Rule: the localized copy is consistently SHORTER — roughly 50–65% of the English character count in
Korean and 55–70% in Japanese** — and this holds in *both* directions of register. Marketing fragments
compress most (`Explore the lineup.` 19 → 9 KR / 10 JP). Polite multi-clause sentences compress less
(`Need more help?` 18 → 16 KR) because the honorific machinery adds syllables.

**Korean body prose, however, runs LONGER than the English body prose in a full paragraph**, because Korean
adds connective and honorific morphology per clause. Compare the same PR sentence:

- EN (163 chars): `iPhone Duo is built to last with an innovative hardware design and a precision hinge that offers a smooth, satisfying feel with every use.`
- KR (139 chars): `iPhone Duo는 견고한 내구성을 자랑하는 혁신적인 하드웨어 디자인과 매끄럽고 탁월한 사용감을 선사하는 정밀 힌지를 갖추고 있다.`
- JP (~120 chars): `iPhone Duoは、革新的なハードウェアデザインと、スムーズで快適な使い心地をもたらす精密なヒンジにより、長くお使いいただけるよう作られています。`

So: **UI strings and taglines shrink; explanatory sentences are roughly the same length or slightly shorter
in Korean/Japanese, but carry more characters per word and therefore take more vertical space.**

### B7. Units and locale-specific data substitution (major divergence)

The **same press release** is localized differently by the two locales on the *unit system*:

| English | Korean | Japanese |
|---|---|---|
| `a 7.6-inch inner display` | `19.3cm 내부 디스플레이` **(converted to cm)** | `7.6インチのインナーディスプレイ` **(inches KEPT as インチ)** |
| `the 5.4-inch outer display` | `13.6cm 크기로` | `5.4インチのアウターディスプレイ` |
| `90 percent of the screen area` | `화면 면적의 90%` | `スクリーン領域の90パーセント` **(percent spelled out in kana)** |
| `3000 nits of peak outdoor brightness` | `3000 니트 부분 최대 밝기(야외)` | — |
| `Pre-order starting 5:00 a.m. PT on 10.16` (homepage) | `10월 16일 오후 9시 사전 주문 시작` | `予約注文は10月16日午後9時から` **(PT converted to local time)** |
| `said John Ternus, Apple’s CEO` | `Apple의 CEO 존 터너스(John Ternus)는` **(Latin name kept in parens)** | `と、AppleのCEOであるジョン・ターナスは述べています` **(katakana only, no Latin)** |
| `CUPERTINO, CALIFORNIA` (dateline) | `캘리포니아 쿠퍼티노` | `カリフォルニア州クパティーノ` |
| `PRESS RELEASE` | `보도자료` | `プレスリリース` |
| Headline `Apple unveils iPhone Duo` | `Apple, iPhone Duo 공개` | `Apple、iPhone Duoを発表` |
| `About Apple` (boilerplate) | `Apple 소개` | `Appleについて` |

**Timezone conversion is performed** — `5:00 a.m. PT` becomes `오후 9시` / `午後9時` (9 p.m. local, both
KST and JST being UTC+9). **Metric conversion is Korean-only**; Japan keeps inches.

### B8. Market-specific legal furniture (JP-only)

The Japanese homepage footnote block (https://www.apple.com/jp/) contains obligations with no English or
Korean equivalent — secondhand-dealer licence numbers for each trade-in partner, and a payment-provider
disclosure:

> `Apple Trade Inプログラムは、Likewize Japan、Alchemy Telco Solutions Japanおよびファーイーストセルラー合同会社によって提供・運営されています。名称：Likewize Japan株式会社（古物商許可証発行：東京都公安委員会 古物商許可証番号：第301112215727号）。名称：Alchemy Telco Solutions Japan合同会社（古物商許可証発行：東京都公安委員会 古物商許可証番号：第308842007505号）。…`

> `最低購入金額は3,000円（税込）です。製品価格を分割回数で割った金額に1円未満の端数がある場合は、月々の支払い金額に差が生じることがあります。`

And a JP-only trademark sentence appended to the `About Apple` boilerplate:

> `iPhone商標は、アイホン株式会社のライセンスにもとづき使用されています。`

Korean equivalents carry local payment/installment terms naming domestic issuers:

> `무이자 할부는 현대, 하나, 국민, 신한, 삼성 카드에 한해 적용됩니다. … 6개월~12개월 할부는 400,000원 이상, 18개월 할부는 1,200,000원 이상입니다.`
> `이 정보는 2026년 4월 20일 기준 최신 정보입니다.`

Korean marketing footnotes also use a **completely different marker ladder** from English on the same page:
`/iphone/` (EN) uses `§`, `*`, `**`, `◊`; `/kr/iphone/` uses `*`, `**`, `***`.

### B9. What is NOT localized

- The homepage services carousel keeps the English CTA `Stream now` untranslated on **both** `/kr/` and
  `/jp/` (verified in the extracted text of both pages), while the surrounding titles and genre labels
  (`액션`, `스릴러`, `코미디`, `SF` / `スリラー`, `アクション`) are translated.
- TV/film titles are localized per market with the original in the slug: KR `Item 1 - '메이드이' - Mayday`,
  `Item 4 - '테드 래소' - Ted Lasso`; JP `Item 5 - テッド・ラッソ：破天荒コーチがゆく`, `Item 7 - Friday Night Baseball`
  (left in English).
- Merchandising differs by market — `Apple Card` and `Apple Upgrade` appear on `/` but are **absent from
  `/kr/`**, while `MacBook Pro` appears on `/kr/` but not on `/`. Localization is not a 1:1 page mirror.

---

## Failed URLs and why

| URL | Result | Why / what I did instead |
|---|---|---|
| `https://www.apple.com/newsroom/` (raw curl) | **200 but nav-only** | Article list is JS-rendered; raw HTML contained only `href="/newsroom/apple-services/"` and `href="/newsroom/apple-stories/"`. **Route that worked:** Jina reader `https://r.jina.ai/https://www.apple.com/newsroom/` (200, 36,814 B) → yielded 15 real release URLs. |
| `https://www.apple.com/kr/newsroom/` (raw curl) | **200 but nav-only** | Same JS-render problem. **Route that worked:** Jina reader (200, 24,871 B). |
| `https://www.apple.com/jp/newsroom/` (raw curl) | **200 but thin** | Same; not needed after KR resolved via Jina. |
| `https://www.apple.com/legal/internet-services/itunes/` | 200, but **redirects in substance** | The path resolves into the *Apple Media Services Terms and Conditions* page (`<title>Legal - Apple Media Services - Apple</title>`), not an “iTunes Store” page. Cited as such. |
| `https://support.apple.com/en-us/102446` and `https://support.apple.com/ko-kr/102446` | 200, but **not an article** | Redirects to `https://support.apple.com/guide/watch/go-for-a-swim-apd09135915f/watchos` (Apple Watch User Guide chapter). EN and KO responses were **byte-identical (758,994 B)** → the `ko-kr` locale was not applied to guide IDs. Discarded. |
| `https://support.apple.com/en-us/102450` | 200, wrong article | Resolves to `Restart your Mac in macOS or Windows`, not the target. Discarded. |
| **“If your iPhone won't turn on”** support article | **NOT LOCATED** | `web_search` failed entirely (see below), and Apple's support search is JS-rendered so I could not enumerate article IDs. Workaround: I used `https://support.apple.com/en-us/118575` ↔ `https://support.apple.com/ko-kr/118575` ↔ `https://support.apple.com/ja-jp/118575`, which are the **same article in all three locales** and gave a clean 1:1 register comparison. The “If your … won't …” *title shape* is characterized from the house-style pattern, not quoted from a fetched page. |
| `web_search` tool (all queries) | **ERROR** | `all search providers failed: SearXNG returned no results; Tavily TAVILY_API_KEY not configured; Brave BRAVE_API_KEY not configured; DuckDuckGo HTTP 202`. All discovery was therefore done by direct URL construction + link extraction from fetched HTML, not by search. |
| `https://www.apple.com/vision/` | 200, usable but degraded | Hero copy is animated word-by-word; extracted text splits one sentence into 10 fragments (`Apple Vision Pro / seamlessly / blends / digital content / with / your physical space.`). Quotes taken only from stable lines. |
| `https://www.apple.com/apple-watch/` `Related articles` / `See also` | **NOT FOUND** | Neither fetched support article rendered a `Related articles` or `See also` module. Not asserting those strings. |
| `https://www.apple.com/kr/legal/internet-services/itunes/` | 200, redirects | Resolves to `https://www.apple.com/kr/legal/internet-services/`; used as the Korean legal source. |

### Routes that worked, per URL class

- **curl + Safari browser UA** — worked for *every* static page: all `/`, product pages (`/iphone/`, `/mac/`,
  `/apple-watch/`, `/airpods/`, `/vision/`), `/kr/*`, `/jp/*`, `/legal/*`, `/newsroom/<article>/`,
  `/kr/newsroom/<article>/`, `/jp/newsroom/<article>/`, `support.apple.com/<locale>/<id>`.
  Every one returned HTTP 200 `text/html; charset=utf-8` with 90 KB–1 MB of real content.
- **Jina reader (`https://r.jina.ai/<url>`)** — required only for the three **newsroom index** pages
  (EN/KR/JP), which are JS-rendered under raw curl.
- **web.archive.org** — not needed; no fallback was required.
- **HTML → text**: a Python `re`-based tag stripper (script at `/tmp/apple-research/x.py`) was used because
  apple.com HTML is 100 KB–1 MB per page. Byte-level claims (U+2060 / U+200B / U+00A0 / U+2011 / U+2032 /
  U+201C-U+201D counts, `<wbr>` counts) were verified against the **raw HTML**, not the stripped text.
