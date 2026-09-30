# Marcom, internal philosophy, leaked/internal documents

Scope: Apple's internal tone-of-voice / marketing-philosophy material and the famous leaked/internal
documents, each classified PRIMARY / SECONDHAND / MYTH-DISPUTED.

**Method note (important for trust):** every quote below was read by me from the page/file I actually
fetched on this run. No quote is reconstructed from memory. Where a source is a third-party upload or a
transcription rather than an Apple publication or a scan, that is called out explicitly.

**Environment constraint on this run:** the web-search tool was down for the entire session
(`pi-web-access: all search providers failed` — SearXNG returned no results, Tavily/Brave had no API key,
DuckDuckGo returned HTTP 202). DuckDuckGo HTML/lite returned HTTP 202 (bot challenge), Mojeek 403,
`s.jina.ai` 401 (auth required), `timetravel.mementoweb.org` DNS failure. URL discovery was therefore done
via the Internet Archive **advancedsearch/metadata JSON APIs** and Wikipedia's article bodies — both of
which worked. The Internet Archive **CDX API** was “Temporarily Offline” all session, but
`web.archive.org/web/<timestamp>/<url>` retrieval worked fine.

## Sources table

| 출처 | URL | 성격(공식 1차/2차/루머) | 무엇을 규정 | 인용 수 |
|---|---|---|---|---|
| The Apple Marketing Philosophy (scan) | https://archive.org/details/102789075-05-01-acc | **1차 (facsimile)** — 단, 제3자 업로드; 저자 미기재 | Empathy / Focus / Impute 3원칙, 마케팅 철학 원문 | 7 |
| Markkula 저자 귀속 | (해당 문서에 없음) | **2차 / 미검증** | 저자 귀속 자체는 1차 artifact로 확인 불가 | 0 |
| Apple Style Guide (PDF, 244pp) | https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf | **공식 1차** | Apple 사내 문서 스타일 규범, Marcom 존재 언급 | 3 |
| Apple Style Guide (web) | https://support.apple.com/guide/applestyleguide/about-the-guide-apsg0a1a8f0e/web | **공식 1차** | 위와 동일 (HTML판) | (동일) |
| Thoughts on Flash (2010) | https://web.archive.org/web/20101231041029/http://www.apple.com/hotnews/thoughts-on-flash/ | **공식 1차** (Apple 발행, archive 경유) | Jobs 공개서한 — 논증 구조와 보이스 | 6 |
| Apple's commitment to privacy (2014) | https://web.archive.org/web/20151231214053/http://www.apple.com/privacy/ | **공식 1차** (Apple 발행, archive 경유) | Tim Cook 2014 프라이버시 서한 | 6 |
| apple.com/privacy/ (현행) | https://www.apple.com/privacy/ | **공식 1차** | 현행 하우스 보이스 | 3 |
| apple.com/environment/ (현행) | https://www.apple.com/environment/ | **공식 1차** | 현행 하우스 보이스 | 3 |
| apple.com/values/ | https://www.apple.com/values/ | **존재하지 않음 (404)** | — | 0 |
| Business Conduct Policy (PDF) | https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf | **공식 1차** | 임직원 발언·기고·기록 정확성 규정 | 4 |
| Krause “Media Guidelines” (1985) | https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html | **1차** (Stanford 아카이브 원본 메모) | 사내 미디어 응대 지침 | 4 |
| Krause “Inquiries from the Press” (1985) | https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause1.html | **1차** (Stanford 아카이브 원본 메모) | 사내 미디어 응대 지침 | 3 |
| McKenna, Relationship Marketing (1991) | https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/relationmkt.html | **2차** (출판된 책 발췌) | Macintosh 마케팅 메시지 전략 | 2 |
| Siltanen, Forbes “Real Story…” (2011) | https://web.archive.org/web/2018/https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/ | **2차** (Forbes 게재, 필자=카피라이터 본인) | “Crazy Ones” 원고 및 캠페인 기원 | 6 |
| Creative Review, Think Different history | https://www.creativereview.co.uk/apple-think-different-slogan/ | **2차** (업계 전문지) | 슬로건·보이스오버 기원, Isaacson 반박 | 4 |
| Think Different Booklet (1997) | https://archive.org/details/think-different-booklet-1997 | **2차 (필사본)** — 스캔 아님, 출처 미검증 | “Crazy Ones” 전문 | 4 |
| Think Different Really Different Brochure (1997) | https://archive.org/details/19971110-really-different-brochure_202201 | **1차 (facsimile)** — 제3자 업로드 | 1997년 Apple 인쇄 프로모 보이스 | 4 |
| Apple Internal – Introducing the Think Different Campaign (1997) | https://archive.org/details/introducing-campaign-to-apple-internal | **유출 내부자료** (Apple 발행 아님) | 내부 캠페인 브리핑 (Jobs + Lee Clow) | 0 (영상) |
| Apple Internal – Apple Retail Store Philosophy (2011) | https://archive.org/details/11243 | **유출 내부자료** (Apple 발행 아님) | 리테일 철학, Ron Johnson 트랜스크립트 | 4 |
| Apple Internal – Greg Joswiak On Confidentiality (2017) | https://archive.org/details/apple-internal-greg-jozwiak-on-confidentiality | **유출 내부자료** | 기밀 유지 문화 | 0 (영상) |

---

## Per-source detail

### 1. The Apple Marketing Philosophy — scan of the original typed memo (Empathy / Focus / Impute)

URL: https://archive.org/details/102789075-05-01-acc
Direct file: https://archive.org/download/102789075-05-01-acc/102789075-05-01-acc.pdf
Evidence class: **PRIMARY (scan/facsimile of the original document)** — *with two explicit caveats below.*
Route that worked: IA advancedsearch JSON API → IA metadata API → `archive.org/download/...pdf` via curl →
`pypdf` embedded-image extraction → visual inspection with `read_image`. (IA `advancedsearch.php` returned
`numFound: 1` for the phrase “Apple Marketing Philosophy”.)

**What the artifact actually is (verified visually, not assumed):** a **10-leaf, 600-dpi scan** (`scandata.xml`
reports `dpi 600`, `leafCount 10`). It contains:
- leaf 1 — a black-and-white **portrait photograph** of a man (no caption, no name);
- leaves 2, 4, 6, 8 — **envelopes** addressed to `ROBERT A. ISAACS / 1646 MARY AVENUE / SUNNYVALE, CALIFORNIA`;
- **leaves 9 and 10 — two copies of the memo itself**, typed on Apple letterhead-style layout, headed
  `THE APPLE / MARKETING PHILOSOPHY` with the line `EMPATHY   FOCUS   IMPUTE`.
The bottom of leaf 10 carries a stamp reading **`ACH Dec. 79`**. The IA item metadata gives `date: 1979`,
`creator: Apple Inc.`, `description: Internal Apple Document`.

**Caveat 1 — hosting/provenance.** This is a **third-party upload** to archive.org in the user-created
collection `applemedia` ("A collection images, media and commercials related to Apple Computer and Apple
Inc." — *not* an Apple-operated or university archive). The `creator: Apple Inc.` field is uploader-supplied
metadata, not an Apple or archival assertion. It is not a Stanford-hosted copy.

**Caveat 2 — authorship is NOT on the document.** The memo is written in the third person about the
company (“Apple believes…”, “He created the impression…”). **It does not name Mike Markkula, and it carries
no signature.** The universal attribution to Markkula is therefore *not* established by this facsimile.

Quotes (verbatim, transcribed by me from the scanned page images):
- “We normally think of marketing in terms of forecasting, strategic and product planning, selling, advertising, merchandising and the like.”
- “The essence of Apple's marketing Philosophy is contained in just three words...empathy, focus, and impute.”
- “Empathy - Understanding so intimate that the feelings, thoughts, and motives of one are readily comprehended by another.”
- “Focus - A thorough and complete understanding of the marketplace always provides more opportunities than can or should be attacked.”
- “Impute - the process by which an impression of a product, company or person is formed by mentally transferring the characteristics of the communicating media to the product, company or person.”
- “people DO judge a book by its cover, a company by its representatives, a product's quality by the quality of its collateral materials etc.”
- “if we present them in a slipshod manner, they will be perceived as slipshod, if we present them in a creative, professional manner, we will impute the desired qualities.”

Two scope notes that contradict common retellings:
- The document is dated **Dec. 79**, not “January 3, 1980”.
- The memo is a **full page of body prose**, not a terse three-bullet list. The bullet-style
  “three principles” summary circulating online is an editorial condensation.

### 2. Mike Markkula attribution for the memo

URL: none — **no primary artifact found that names him.**
Evidence class: **MYTH / DISPUTED (as to authorship)** — the *memo* is real and primary (see above); the
*attribution to Markkula* is a widely repeated claim I could not verify against any primary artifact.
Route that worked: negative result. I enumerated **every link** on the Stanford “Making the Macintosh”
primary-documents index (`https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/index.html`) — the
Markkula memo is **not there**. I probed `primary/docs/marketing.html`, `philosophy.html`, `markkula.html`,
`mktphil.html`, `applemkt.html` — all 404. Wikipedia's English article on Mike Markkula does **not**
mention the memo at all.

Quotes: none — nothing to quote from a negative result.

### 3. Apple Style Guide — the Marcom line (PRIMARY)

URL (PDF): https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf
URL (web): https://support.apple.com/guide/applestyleguide/about-the-guide-apsg0a1a8f0e/web
Evidence class: **PRIMARY** — Apple-authored, published by Apple.
Route that worked: `curl` with browser UA (HTTP 200, `application/pdf`, 4,158,788 bytes, 244 pages) →
`pypdf` text extraction.

Quotes (verbatim, from the section “Other editorial resources used at Apple”, p. 5):
- “Some departments at Apple (Marcom, for example) have supplemental style guides.”
- “In general, follow the style and usage rules in: • Merriam-Webster's Collegiate Dictionary • The Chicago Manual of Style”
- “For information about the user interface, see Apple's Human Interface Guidelines.”

**This is the single most important finding for the Marcom question: Apple's own public style guide
confirms that a Marcom supplemental style guide exists, and simultaneously makes clear it is NOT the
document you are reading.** The public guide covers product/UI/docs terminology, not marketing voice.

### 4. Apple Marcom tone-of-voice material — **PLAINLY: NO PUBLIC GUIDE EXISTS**

URL: none.
Evidence class: **NOT VERIFIABLE / DOES NOT EXIST PUBLICLY.**
Route that worked: negative result across multiple independent attempts.

I could not find **any** public, leaked, or archived Apple Marcom tone-of-voice / brand-voice style guide:
- No Marcom guide is published on apple.com, help.apple.com, or support.apple.com.
- The Apple Style Guide only *acknowledges* its existence (line above) without reproducing it.
- IA full-collection search for `"Apple" AND "marcom"` returned **4 hits, none of them an Apple style
  guide** (two unrelated “Beachwalks” podcast episodes, an iPod touch web ad, and a 1999 TEMIC
  Semiconductors CD-ROM).
- IA search for `"Apple Style Guide"` returned 9 hits; the only relevant one is a third-party mirror
  (`manualzilla-id-7251602`), i.e. the *public* guide, not Marcom.

**Conclusion to record in the skill:** Apple's Marcom voice guide is internal and has not surfaced
publicly. Any “Apple Marcom style guide” text you see quoted online should be treated as fabricated or
unverifiable unless it produces a facsimile. What *is* verifiable about Apple marketing voice must be
inferred from published Apple marketing copy itself (items 2 and 5 below).

### 5. “Thoughts on Flash” — Steve Jobs open letter, April 2010 (PRIMARY)

URL: https://web.archive.org/web/20101231041029/http://www.apple.com/hotnews/thoughts-on-flash/
Evidence class: **PRIMARY** — Apple-authored, published by Apple on apple.com/hotnews/; the live URL is dead,
retrieved via Wayback.
Route that worked: `web.archive.org/web/2010/<url>` via curl → tag-strip with python3 → `flash.txt`.

Quotes (verbatim):
- “Apple has a long relationship with Adobe. In fact, we met Adobe's founders when they were in their proverbial garage.”
- “I wanted to jot down some of our thoughts on Adobe's Flash products so that customers and critics may better understand why we do not allow Flash on iPhones, iPods and iPads.”
- “First, there's ”Open“.”
- “By almost any definition, Flash is a closed system.”
- “Our motivation is simple – we want to provide the most advanced and innovative platform to our developers, and we want them to stand directly on the shoulders of this platform and create the best apps the world has ever seen.”
- “Perhaps Adobe should focus more on creating great HTML5 tools for the future, and less on criticizing Apple for leaving the past behind.”

Signed on the page: “Steve Jobs” / “April, 2010”. Voice notes visible in the artifact: ordinal signposting
(“First…”, “Second…”, “Third…”, “Fourth…”, “Fifth…”, “Sixth, the most important reason.”), short
declaratives, and a one-line closer.

### 6. “Apple's commitment to privacy” — Tim Cook letter, September 2014 (PRIMARY)

URL: https://web.archive.org/web/20151231214053/http://www.apple.com/privacy/
Evidence class: **PRIMARY** — Apple-authored, published by Apple on apple.com/privacy/; captured here in the
2015-12-31 Wayback snapshot of that page.
Route that worked: `web.archive.org/web/2015/https://www.apple.com/privacy/` via curl (HTTP 200, 36,382 bytes).

Quotes (verbatim):
- “At Apple, your trust means everything to us.”
- “A few years ago, users of Internet services began to realize that when an online service is free, you're not the customer. You're the product.”
- “Our business model is very straightforward: We sell great products.”
- “We don't ”monetize“ the information you store on your iPhone or in iCloud.”
- “Plain and simple.”
- “Finally, I want to be absolutely clear that we have never worked with any government agency from any country to create a backdoor in any of our products or services.”

### 7. apple.com/privacy/ — current live page (PRIMARY)

URL: https://www.apple.com/privacy/
Evidence class: **PRIMARY** — Apple-authored, published by Apple.
Route that worked: `curl` with browser UA (HTTP 200, `text/html`, 257,411 bytes).

Quotes (verbatim):
- “Privacy. That's Apple.”
- “Privacy is a fundamental human right. It's also one of our core values. Which is why we design our products and services to protect it. That's the kind of innovation we believe in.”
- “Designed to protect your privacy at every step”

Voice notes: the signature move is the **two-word-fragment headline** (“Privacy. That's Apple.”) followed by
a plain-language paragraph opening on a definition.

### 8. apple.com/environment/ — current live page (PRIMARY)

URL: https://www.apple.com/environment/
Evidence class: **PRIMARY** — Apple-authored, published by Apple.
Route that worked: `curl` with browser UA (HTTP 200, `text/html`, 438,565 bytes).

Quotes (verbatim):
- “Our planet deserves our best thinking.”
- “Innovation is up. Emissions are down.”
- “We're closer than ever to Apple 2030: Our ambitious, science-based goal to become carbon neutral across our global footprint.”

Voice notes: headline as a moral claim (“deserves our best thinking”), then **two three-word
declaratives** (“Innovation is up. / Emissions are down.”), then the number.

### 9. apple.com/values/ — **DOES NOT EXIST (404)** — important negative finding

URL tested: https://www.apple.com/values/ → **HTTP 404** (`Page Not Found - Apple`, 111,090 bytes)
Evidence class: **not available.**
Route that worked: negative result, verified three ways.
- Live `curl`: `/values/` → 404; also probed `/our-values/` → 404 and `/apple-values/` → 404.
- `r.jina.ai/https://www.apple.com/values/` → returns the Apple 404 page (“Warning: Target URL returned error 404: Not Found”).
- Wayback: every timestamp I requested (2010, 2013, 2016, 2019, 2022) resolves to the **same single
  404 capture** at `https://web.archive.org/web/20160225064529/http://www.apple.com/values`.

**Conclusion to record in the skill: there is no live `apple.com/values/` URL, and the Wayback Machine
holds only a 404 capture for it.** Apple's values content is instead distributed across topic hubs, all of
which I verified return HTTP 200:
`/accessibility/`, `/inclusion/`, `/diversity/`, `/education/`, `/supplier-responsibility/`,
`/racial-equity-justice-initiative/`, plus `/privacy/` and `/environment/`.

### 10. Stanford “Making the Macintosh” — Krause media memos (PRIMARY archival)

URL (Media Guidelines, 9 Apr 1985): https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html
URL (Inquiries from the Press, 4 Mar 1985): https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause1.html
Evidence class: **PRIMARY** — the Stanford archive of the original internal Apple memos. Each page carries a
provenance line: `Location: M1007, Apple Computer Inc. Papers, Series 9, Box 1, Folder 2.`
Route that worked: `curl` with browser UA directly against `web.stanford.edu` (both HTTP 200).

Quotes from “Media Guidelines” (verbatim):
- “Apple is probably more accessible to the news media than any other personal computer company. Because of this, many of you may find yourselves being asked to participate in an interview.”
- “1. There is no such thing as ”off the record.“ Reporters can easily disarm you by allowing you to think the ”interview“ is over and that you are now just holding a conversation. Be careful. Anything you say can and may be used.”
- “2. If the subject you are discussing is sensitive or confusing, repeat your message in a slightly different way to make sure the reporter understands. This will lessen your chances of having the information misconstrued.”
- “3. Stick to the subject of the interview and don't volunteer additional information unless it seems important to the story the reporter is working on at that time.”

Quotes from “Inquiries from the Press” (verbatim):
- “we do operate under guidelines to ensure that the company's position on issues is accurately and consistently stated.”
- “we either answer their questions ourselves, arrange for an interview with the appropriate Apple person, or involve our public relations agency, Regis McKenna Inc.”
- “It might also be a good opportunity to remind your staff that Apple's unannounced products are confidential and should not be discussed with anyone outside the company.”

### 11. Think Different / “Crazy Ones” (1997) — the script

Primary-copy source available: **none verified as an Apple publication.**
Evidence class of the *script text*: **SECONDHAND.**

Best source I could actually fetch — Rob Siltanen (the TBWA/Chiat/Day creative director who wrote it),
“Forbes: The Real Story Behind Apple's 'Think Different' Campaign”, 14 Dec 2011:
URL: https://web.archive.org/web/2018/https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/
Route that worked: direct `forbes.com` curl returned **403**; the Wayback copy worked (HTTP 200, 510,681 bytes).

Quotes from Siltanen's Forbes piece (verbatim; these are Siltanen's words, not Apple's):
- “I also found the original ”To the crazy ones“ television script I presented to Jobs, as well as a plethora of rough drafts.”
- “on Steve Jobs. In his book, Isaacson incorrectly suggests Jobs created and wrote much of the ”To the crazy ones“ launch commercial. To me, this is a case of revisionist history.”
- “”To the crazy ones. Here's to the misfits. The rebels. The troublemakers. The people who see the world differently.“”
- “”The people who are crazy enough to believe they can change the world are the ones who actually do.“”
- “I told Steve I would write something in a similar tone of voice, and we'd come back in a week.”
- “To the crazy ones. / Here's to the misfits. The rebels. The troublemakers.”

Second fetched source — Creative Review, “The history of the Apple Think Different slogan”:
URL: https://www.creativereview.co.uk/apple-think-different-slogan/
Route that worked: `curl` with browser UA (HTTP 200, 134,994 bytes).
Quotes (verbatim, Creative Review's words):
- “Jobs wanted an ad campaign that would remind Apple's still loyal fanbase of the qualities that had made it great in the first place.”
- “”While several people played prominent parts in making it happen, the famous 'Think Different' line and the brilliant concept of putting the line together with black-and-white photographs of time-honoured visionaries … was invented by … Craig Tanimoto, a TBWAChiatDay art director at the time,“ he maintains.”
- “The original plan was for a print only campaign but ChiatDay also decided to make a 'mood video' to set the tone, originally cut to the Seal song Crazy.”
- “”It will be really powerful to have it in your voice. It will be a way to reclaim the brand,“ Isaacson has Clow arguing.”

**Contested-authorship note (this is the MYTH/DISPUTED element of item 2):** the popular story that
**Steve Jobs wrote the “Crazy Ones” script is disputed** by the credited copywriter, and Creative Review
records that Isaacson's biography “plays up Jobs' role”. Apple itself has never published the script as an
Apple-authored text. The campaign was created by an outside agency (TBWA/Chiat/Day), so it is **agency copy
that Apple adopted**, not an example of Apple's internal house style.

### 12. “Think Different Booklet (1997)” — a TRANSCRIPTION, not a scan (classification correction)

URL: https://archive.org/details/think-different-booklet-1997
Evidence class: **SECONDHAND (transcription with unverified provenance)** — **NOT** the PRIMARY facsimile
its metadata implies.
Route that worked: IA metadata API → `..._djvu.txt` download → **and** PDF download with `pypdf` image
extraction for visual verification.

**Why it is not primary:** the IA metadata says `creator: Apple Inc.`, `date: 1997`, but the PDF is **not a
scan**. Rendering its pages and looking at them shows clean, modern digital typesetting (a Garamond-style
serif on a pure-white ground at 700×889 px) with **no paper texture, no halftone, no scan noise, and no
alignment artefacts** — i.e. someone re-typed the text. The file is 4 pages, 353,603 bytes.
**Record this correction:** do not cite this item as a facsimile of Apple's 1997 booklet.

Its text nevertheless matches the well-known campaign copy and is useful as a corroborating transcription
(quoted here as *this transcription's* text, not as an Apple-published artifact):
- “The round pegs in the square holes.”
- “You can praise them, disagree with them, quote them, disbelieve them, glorify or vilify them.”
- “About the only thing you can't do is ignore them.”
- “Because the people who are crazy enough to think they can change the world, are the ones who do.”

### 13. “Think Different Really Different Brochure” (1997) — genuine scan (PRIMARY facsimile)

URL: https://archive.org/details/19971110-really-different-brochure_202201
Evidence class: **PRIMARY (scan/facsimile of Apple print collateral)** — third-party upload; the brochure is
Apple marketing material from the Think Different / Power Macintosh G3 era.
Route that worked: IA metadata API → `archive.org/download/...pdf` via curl (1,983,371 bytes) → `pypdf`
image extraction → visual inspection (8 pages, 1200×1600 px page images with visible print/halftone
character and page-edge shadow — i.e. real scans).

**This is the best verified artifact of Apple's actual *product-marketing* voice from the Think Different
era.** Quotes (verbatim, read from the scanned brochure pages):
- “Computer science meets rocket science” (headline)
- “A very different chip.” (kicker)
- “Did someone say ”faster“? The new Power Macintosh G3 computers, built upon the relentlessly fast, third-generation PowerPC G3 chip, offer nothing less than the biggest performance leap in Power Mac history.”
- “Only a few people in the world can explain ”backside cache.“ But everyone will savor the speed boost it provides.”
- “Oh, and did we mention that the Mac G3's are fast?”
- “Who are you and what do you want from us?”
- “(But no anchovies.) You can configure your computer literally hundreds of different ways…”

### 14. Apple Business Conduct Policy (PRIMARY) — employee speech/publishing rules

URL: https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf
Evidence class: **PRIMARY** — Apple-authored, published by Apple. Edition “February 2026”, 20 pages.
Route that worked: `curl` with browser UA (HTTP 200, `application/pdf`, 808,333 bytes) → `pypdf` extraction.

Quotes (verbatim):
- “Public Speaking and Press Inquiries” / “All public or outside speaking engagements that relate to Apple's products or services or reasonably anticipated products or services or public or outside speaking engagements where you could be construed as speaking on behalf of the company, must be pre-approved by your manager and Corporate Communications.”
- “Publishing Articles” / “If you want to contribute an article or other type of submission to a publication or blog on a topic that relates to Apple's current or reasonably anticipated products or services, or that could be seen as a conflict of interest, you must first request approval from Corporate Communications.”
- “Accurate and honest business records are critical to meeting our legal, financial, and management obligations.”
- “You should never endorse a product or service of another business or individual in your role as Apple employee, unless the endorsement has been approved by your Director and Corporate Communications.”

### 15. Apple Retail / internal training — LEAKED, not public

URL: https://archive.org/details/11243 (“Apple Internal – Apple Retail Store Philosophy”, 2011-07-07)
Evidence class: **LEAKED INTERNAL MATERIAL** — Apple-authored in origin but **not published by Apple**;
third-party upload. Treat as leaked, not official.
Route that worked: IA search (`collection:applemedia AND "retail" AND training`, `numFound: 2`) → metadata
API. The item's `description` field carries a **full transcript** and there is also an
`Apple Retail-eng.asr.srt` subtitle file (8,517 bytes).

Quotes (verbatim, from that transcript; speaker identified in it as Ron Johnson):
- “Ron Johnson: Every great journey begins with the first step.”
- “Then we discovered that if you can tailor a store uniquely to its setting, it can actually improve communities.”
- “Most retailers view their space as the square footage they rent. We view our space, the environment we inhabit.”
- “Every one of our stores, our primary objective is to create a place that people will love.”

Related leaked internal items located (metadata verified, not transcribed):
- “Apple Internal – Introducing the Think Different Campaign” (internal meeting dated **1997-09-23**;
  Steve Jobs on Apple's status, then Lee Clow on the campaign) —
  https://archive.org/details/introducing-campaign-to-apple-internal
- “Apple Internal – Greg Joswiak On Confidentiality” (2017) —
  https://archive.org/details/apple-internal-greg-jozwiak-on-confidentiality
- “Apple Internal – Retail Store Training Song” — https://archive.org/details/apple-internal-retail-store-training-song

**No public Apple Retail *writing* or tone-of-voice guide exists.** What is public is policy
(compliance) and what exists otherwise is leaked video, not a style guide.

### 16. Regis McKenna, *Relationship Marketing* (1991) — SECONDHAND book excerpt

URL: https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/relationmkt.html
Evidence class: **SECONDHAND** — a book excerpt (Addison-Wesley, 1991), hosted by Stanford. The quote is
McKenna's, not Apple's.
Route that worked: `curl` with browser UA (HTTP 200, 17,541 bytes).

Quotes (verbatim):
- “In 1982, though, the Macintosh group began adding some marketing people and holding strategy sessions.”
- “they helped develop the notion of the ”knowledge worker“ as the Mac's potential market, and also identified several key points about the Mac (”Macmessages,“ as they're called here) that were repeated endlessly”

---

## Failed URLs and why

| URL | Result | Why |
|---|---|---|
| https://www.apple.com/values/ | **404** | Page does not exist. Also `/our-values/`, `/apple-values/` → 404. Wayback holds only a 404 capture (20160225064529). |
| https://www.apple.com/hotnews/thoughts-on-flash/ | dead | Live URL retired; Wayback 2010 snapshot worked. |
| https://web.archive.org/web/2007/http://www.apple.com/hotnews/thoughts-on-music/ | **404** | Wayback has only a 404 capture for Thoughts on Music (20120120221635) at every timestamp I tried, incl. `20070206000000`. **Not verified.** |
| https://www.forbes.com/sites/onmarketing/2011/12/14/… | **403** | Direct curl blocked; retrieved via Wayback instead. |
| https://tsdr.uspto.gov/documentviewer?caseId=sn77882684&docId=SPE20091203073647 | empty | JS-only shell (15,709 bytes, no content). Apple's trademark specimen for “Think different” is therefore **not verified** here. |
| https://s.jina.ai/?q=… | **401** | Jina search endpoint requires an API key. |
| https://html.duckduckgo.com/html/?q=… | **202** | Bot challenge; 0 results parsed. |
| https://lite.duckduckgo.com/lite/?q=… | **202** | Bot challenge. |
| https://www.mojeek.com/search?q=… | **403** | Blocked. |
| https://r.jina.ai/https://www.bing.com/search?q=… | no results | Returned navigation chrome only. |
| https://r.jina.ai/https://search.brave.com/search?q=… | no results | 1,004 bytes, empty. |
| http://web.archive.org/cdx/search/cdx?… | **offline** | “Internet Archive: Temporarily Offline” all session (retrieval endpoint still worked). |
| http://timetravel.mementoweb.org/api/json/… | **DNS failure** | Host does not resolve. |
| https://makingthemac.stanford.edu/ | **DNS failure** | Host does not resolve. |
| http://www-sul.stanford.edu/mac/ | **403** | Redirects to web.stanford.edu /library/prod/mac/ and is forbidden. |
| https://computerhistory.org/search/?q=… | **404** | CHM search URL pattern invalid; catalog page is JS-rendered (no parseable results). |
| https://oac.cdlib.org/findaid/ark:/13030/kt9p3011rf/ | **406** | Not Acceptable; finding aid not retrieved. |
| Stanford `primary/docs/{marketing,philosophy,markkula,mktphil,applemkt}.html` | **404** | No Markkula memo at any of these paths. |
| tool `web_search` | **error** | `pi-web-access: all search providers failed` for the whole session. |

## Explicitly NOT verifiable

1. **That Mike Markkula wrote the Apple Marketing Philosophy memo.** The scanned memo carries no
   signature, no author name, and refers to Apple in the third person. No primary artifact naming him was
   found. The attribution is **widespread but unverified**.
2. **That the memo is held by Stanford University Libraries.** The `M1007, Apple Computer Inc. Papers`
   provenance line belongs to the *Krause* memos, not to the marketing-philosophy memo. The Stanford
   “Making the Macintosh” primary-document index does **not** list the Markkula memo.
3. **The “January 3, 1980” date.** The scanned copy is stamped `ACH Dec. 79`; IA metadata says 1979.
4. **Any Apple Marcom tone-of-voice or brand-voice style guide.** No public, leaked, or archived copy
   found. Apple's own Style Guide confirms the document class exists internally but is not public.
5. **That Steve Jobs wrote the “Crazy Ones” script.** Actively disputed by the credited copywriter.
6. **Apple's USPTO trademark specimen for “Think different”** (serial 77882684) — the TSDR viewer is
   JavaScript-only and returned no readable content.
7. **“Thoughts on Music” (2007).** No retrievable Wayback capture; the letter is real but I could not
   verify its text on this run, so no quotes are offered.
8. **The provenance/authenticity of the `applemedia` archive.org uploads.** The collection is
   user-created and its `creator: Apple Inc.` metadata is uploader-supplied. The *scans* I inspected
   (memo, brochure) are internally consistent with genuine period material, but no Apple or archival
   institution vouches for them.
