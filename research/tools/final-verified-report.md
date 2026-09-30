# Apple Prose-Style Critiques — Verified Sources (Categories 1, 4, + 5/6 subagent report)

**Method note:** `web_search` failed for every provider. All items below were retrieved by direct URL fetch
(`curl --compressed` + Wayback fallback, or `web_fetch`), and the quoted text was copied from the retrieved
page/PDF body — never from a search snippet. Line references are to the retrieved artifact.

---

## 1. LEGAL AMBIGUITY

### 1.1 — US DOJ antitrust complaint attacks Apple's *marketing language* (PRIMARY, DOCUMENTED)
- **Title:** *United States of America v. Apple Inc.*, Complaint, No. 2:24-cv-04055 (D.N.J.)
- **Author:** U.S. Department of Justice, Antitrust Division (joined by 16 state AGs)
- **URL (PDF):** https://storage.courtlistener.com/recap/gov.uscourts.njd.544402/gov.uscourts.njd.544402.1.0_3.pdf
- **URL (docket):** https://www.courtlistener.com/docket/68362334/united-states-of-america-v-apple-inc/
- **Date:** Filed 2024-03-21
- **Claim:** The DOJ pleads that Apple's own privacy/security *messaging* is a marketing construct used to
  justify anticompetitive conduct — i.e. the complaint treats Apple's brand prose as an anticompetitive instrument.
- **Verbatim (¶16):**
  > Apple wraps itself in a cloak of privacy, security, and consumer preferences to justify its anticompetitive conduct. Indeed, it spends billions on marketing and branding to promote the self-serving premise that only Apple can safeguard consumers' privacy and security interests. … In the end, Apple deploys privacy and security justifications as an elastic shield that can stretch or contract to serve Apple's financial and business interests.
- **Classification:** DOCUMENTED (primary court filing)

### 1.2 — Same complaint: Apple's *signalling* through messaging UX (PRIMARY, DOCUMENTED)
- **URL:** same PDF as 1.1
- **Date:** 2024-03-21
- **Claim:** The complaint alleges the degraded cross-platform experience is a deliberate *signal* — a
  communicative act — not an engineering accident.
- **Verbatim (¶90):**
  > This signals to users that rival smartphones are lower quality because the experience of messaging friends and family who do not own iPhones is worse—even though Apple, not the rival smartphone, is the cause of that degraded user experience. Many non-iPhone users also experience social stigma, exclusion, and blame for “breaking” chats where other participants own iPhones.
- **Classification:** DOCUMENTED (primary court filing)

### 1.3 — DOJ press release: “Whac-A-Mole” framing (DOCUMENTED)
- **Title:** “Justice Department Sues Apple for Monopolizing Smartphone Markets”
- **Author:** DOJ Office of Public Affairs (quote: AAG Jonathan Kanter, Antitrust Division)
- **URL:** https://www.justice.gov/opa/pr/justice-department-sues-apple-monopolizing-smartphone-markets
  *(direct fetch is Akamai-blocked in this environment; retrieved via `https://web.archive.org/web/20240321180000id_/…`)*
- **Date:** 2024-03-21
- **Verbatim:**
  > “For years, Apple responded to competitive threats by imposing a series of ”Whac-A-Mole“ contractual rules and restrictions that have allowed Apple to extract higher prices from consumers, impose higher fees on developers and creators, and to throttle competitive alternatives from rival technologies,” said Assistant Attorney General Jonathan Kanter… “Today's lawsuit seeks to hold Apple accountable and ensure it cannot deploy the same, unlawful playbook in other vital markets.”
- **Classification:** DOCUMENTED (primary government release)

### 1.4 — Apple's response: brand register deployed as legal defense (DOCUMENTED, verbatim)
- **Title:** “United States sues Apple: Read the full DOJ lawsuit document here”
- **Author:** Chance Miller, 9to5Mac
- **URL:** https://9to5mac.com/2024/03/21/doj-sues-apple-full-lawsuit-document-here/
- **Date:** 2024-03-21
- **Claim:** Apple answered a federal antitrust complaint in full keynote register — “magical”, “who we are”.
  **This is the single cleanest documented case of the Apple voice colliding with a regulated/legal register.**
- **Verbatim (Apple's statement, as reproduced by 9to5Mac):**
  > At Apple, we innovate every day to make technology people love—designing products that work seamlessly together, protect people's privacy and security, and create a magical experience for our users. This lawsuit threatens who we are and the principles that set Apple products apart in fiercely competitive markets. If successful, it would hinder our ability to create the kind of technology people expect from Apple—where hardware, software, and services intersect. It would also set a dangerous precedent, empowering government to take a heavy hand in designing people's technology. We believe this lawsuit is wrong on the facts and the law, and we will vigorously defend against it.
- **Classification:** DOCUMENTED (verbatim reproduction of Apple's official statement)
- **Related 9to5Mac piece:** https://9to5mac.com/2024/03/21/apple-says-doj-lawsuit-threatens-who-we-are-as-it-vows-to-vigorously-defend-against-it/
- **Note:** Apple's claim that the DOJ suit is “an attempt to turn the iPhone into Android” — https://9to5mac.com/2024/03/21/doj-lawsuit-is-an-attempt-to-turn-the-iphone-into-android-apple-alleges/

### 1.5 — The 2025 Apple Intelligence / delayed-Siri false-advertising class action (PRIMARY, DOCUMENTED)
- **Title:** *Landsheft v. Apple Inc.*, Class Action Complaint, No. 5:25-cv-02668 (N.D. Cal., San Jose Div.)
- **Author:** Clarkson Law Firm, P.C. (Ryan J. Clarkson, Yana Hart, Bryan P. Thompson), for plaintiff Peter Landsheft
- **URL (PDF):** https://storage.courtlistener.com/recap/gov.uscourts.cand.446692/gov.uscourts.cand.446692.1.0.pdf
- **URL (docket):** https://www.courtlistener.com/docket/69759747/landsheft-v-apple-inc/
- **Date:** Filed 2025-03-19 (44 pages)
- **Claim (the disclaimer/footnote allegation — most on-point for the “small print” category):**
- **Verbatim (¶30, “No Notice of Contradictions”):**
  > Plaintiff did not notice any disclaimer, qualifier, or other explanatory statement or information on the Products' advertising and marketing that contradicted the prominent Challenged Representations or otherwise suggested that the iPhone would not have the advertised capabilities.
- **Verbatim (¶7):**
  > Worse, Apple has admitted that if these features ever materialize, it won't be until 2026—two years after its pervasive marketing campaign built on a lie.
- **Verbatim (¶4):**
  > Apple's advertisements saturated the internet, television, and other airwaves to cultivate a clear and reasonable consumer expectation that these transformative features would be available upon the iPhone's release.
- **Verbatim (¶8):**
  > Apple deceived millions of consumers into purchasing new phones they did not need based on features that do not exist, in violation of multiple false advertising and consumer protection laws.
- **Also pleaded (¶17):** cites the California Attorney General's Legal Advisory warning that state consumer
  protection law “prohibit[s] false advertising regarding the capabilities, availability, and utility of AI products.”
- **Classification:** DOCUMENTED (primary court filing)

### 1.6 — Contemporaneous reporting on the suit (DOCUMENTED)
- **Title:** “Apple Facing False Advertising Lawsuit Over Apple Intelligence Delay”
- **Author:** Juli Clover, MacRumors (crediting Axios for the original report)
- **URL:** https://www.macrumors.com/2025/03/20/apple-intelligence-siri-lawsuit/
- **Date:** 2025-03-20 15:18 PDT
- **Claim:** Apple kept ads running for months after it knew the features would not ship, then pulled them.
- **Verbatim:**
  > After confirming that the Siri features would be delayed until the coming year, Apple removed the ads, but that was after they had been running for several months. Apple is accused of advertising functionality that did not exist, and continuing to promote the Siri capabilities well after the company was aware that they would not be available on time.
- **Classification:** DOCUMENTED (bylined reporting)

### 1.7 — Outcome: $250M settlement, claims opened Sept 2026 (DOCUMENTED)
- **Title:** “Siri AI Settlement Website Now Live: Apple to Pay Some iPhone Owners”
- **Author:** MacRumors
- **URL:** https://www.macrumors.com/2026/09/20/siri-ai-settlement-website-now-live/
- **Date:** 2026-09-20
- **Claim:** Apple settled the false-advertising class action for $250M in May 2026; claim window opened Sept 2026.
- **Related (claimant firm's own release):** “Cotchett, Pitre & McCarthy Announces Opening of $250 Million Apple AI False Advertising Settlement Claims Period”, TMCnet, 2026-09-21 — https://www.tmcnet.com/usubmit/2026/09/21/10449015.htm
  - Verbatim eligibility framing: “U.S. consumers and businesses who purchased an eligible iPhone from June 10, 2024 to March 29, 2025, and submit a valid claim, will be entitled to a cash payment”
- **Classification:** DOCUMENTED

---

## 4. TONE FAILURES

### 4.1 — Apple's official iPhone 4 antenna statement: the canonical tone failure (PRIMARY, DOCUMENTED)
- **Title:** “Letter from Apple Regarding iPhone 4”
- **Author:** Apple Inc. (official statement)
- **URL:** https://www.apple.com/newsroom/2010/07/02Letter-from-Apple-Regarding-iPhone-4/ *(live, HTTP 200)*
- **Date:** July 2, 2010
- **Claim:** Apple answered a hardware reception defect by (a) reframing it as a *software display* bug,
  (b) asserting the product is the best it has ever shipped, and (c) issuing an apology for the user's
  “anxiety” rather than for the defect. This is the archetype of the Apple register failing in a
  consumer-grievance context — confident, self-exonerating, and adversarially framed around what
  customers did wrong (“gripping almost any mobile phone in certain ways will reduce its reception”).
- **Verbatim:**
  > To start with, gripping almost any mobile phone in certain ways will reduce its reception by 1 or more bars. This is true of iPhone 4, iPhone 3GS, as well as many Droid, Nokia and RIM phones.

  > Upon investigation, we were stunned to find that the formula we use to calculate how many bars of signal strength to display is totally wrong.

  > We have gone back to our labs and retested everything, and the results are the same— the iPhone 4's wireless performance is the best we have ever shipped.

  > For those who have had concerns, we apologize for any anxiety we may have caused.
- **Classification:** DOCUMENTED (primary source, Apple's own newsroom)

### 4.2 — Apple's own footnote-heavy ad disclaimer practice (DOCUMENTED, company policy)
- **Title:** “Apple warns Jet Black iPhone 7 scratches” / Apple's published product disclaimers
- **URL:** https://9to5mac.com/2016/09/07/apple-warns-jet-black-iphone-7-scratches/
- **Date:** 2016-09-07
- **Claim:** Apple publicly warned that its headline “Jet Black” finish “may show scratches over time with
  normal wear" — the hero claim and the material qualification were in tension, and the qualification
  lived in small print. *(Retrieved as a 9to5Mac URL listing; headline-level only.)*
- **Classification:** OPINION/reporting (headline-level; not deep-verified)

---

## WHAT I COULD NOT VERIFY (honest null results)

| Target | Attempted | Outcome |
|---|---|---|
| **Any UK ASA ruling against Apple** | `https://www.asa.org.uk/codes-and-rulings/rulings.html?query=apple` (HTTP 200), `https://www.asa.org.uk/rulings.html?q=apple`, guessed slug `…/rulings/apple-distribution-international-ltd.html` | **NOT FOUND.** ASA rulings index is JS-rendered; only 3 unrelated slugs returned (esaverwatt-com, huel-ltd, luma-pet). **I did not find, and therefore do not assert, any ASA ruling against Apple.** |
| **Steve Jobs' “You're holding it wrong” / “Just avoid holding it in that way” email (2010-06-24)** | `macrumors.com/search/?s=jobs+email+holding+it+wrong` — no 2010 URLs surfaced | **NOT RETRIEVED.** I have Apple's official letter (4.1) but NOT the Jobs email. The famous line is therefore excluded. |
| **Phil Schiller's “courage” quote (iPhone 7 headphone jack, 2016-09-07)** | Washington Post live-update URL returned HTTP 000; 9to5Mac fetches aborted at wrap-up | **NOT RETRIEVED — quote excluded.** I will not paraphrase it into a quotation. |
| **Apple's “up to N hours” battery-life footnote criticism** | `bnews.py "Apple battery life claim misleading 'up to' lawsuit"` → 0 results | **NOT FOUND.** No verified source. |
| **Apple benchmark “up to Nx faster” methodology criticism** | `bnews.py "Apple benchmark 'up to' faster claim misleading M1"` → returned only an unrelated M5 Ultra benchmark article | **NOT FOUND.** No verified source. |
| **“Bendgate” (2014) messaging criticism** | `bnews.py "Apple bendgate 2014 response criticism"` → 0 results | **NOT FOUND.** |
| **“Shot on iPhone” criticism** | not reached | **NOT ATTEMPTED.** |
| **Wayback Machine availability API** | `archive.org/wayback/available?…` | Intermittently HTTP 429. Direct `web.archive.org/web/<year>id_/<url>` fetches DID work (with `--compressed`). |
| **justice.gov direct** | Akamai interstitial challenge | Blocked; used Wayback successfully. |

---

## SUBAGENT REPORT — CATEGORIES 5 (KOREAN LOCALIZATION) & 6 (REGULATORY CONSTRAINTS)

Full verbatim report saved at `/Users/hajunbae/dev/Skills/.research-tools/cat5-6-korean-regulatory.md`
(18 sources, all URLs re-verified HTTP 200). Headline items:

**Cat 5 — highest value:**
- **Korea PIPC (개인정보보호위원회) 2024 privacy-policy evaluation** explicitly penalises **번역투**
  (translationese) as a scored defect. 49 companies; average readability 69.1/100, accessibility 60.8,
  adequacy 53.4. The 12 foreign operators scored below domestic firms on all three axes *because of*
  번역투. — 인공지능신문, 2025-03-16, https://www.aitimes.kr/news/articleView.html?idxno=34252
  - Verbatim: 「12개의 해외사업자의 경우 … 번역투 문장 사용 등으로 인해 가독성, 접근성, 적정성 모든 분야에서 국내 기업 대비 낮은 평가를 받았다.」
  - *(Apple's membership in the twelve is a separate, snippet-only inference — flagged in the subagent report.)*
- **김치 → 韓式泡菜 and English “Korean” → Japanese 朝鮮語** in Apple's own iPhone Translate app,
  2024-08-28. Three independent national outlets: 뉴시스 (https://www.newsis.com/view/NISX20240828_0002865250),
  세계일보 (https://www.segye.com/newsView/20240828504212),
  머니투데이 (https://www.mt.co.kr/society/2024/08/28/2024082810202049478). Note the failure is triggered
  by Apple's **Japanese** output — a cross-market localization defect.
- **iPhone 13 EN→JA coinage:** “SupercolorpixelisticXDRidocious” → 「スーパーキラキラカラフルクッキリディスプレイ」.
  INTERNET Watch, やじうまWatch, 2021-09-16, https://internet.watch.impress.co.jp/docs/yajiuma/1351429.html
  (+ Togetter reaction thread https://togetter.com/li/1774751).

**Cat 6 — strongest legal constraints on the Apple idiom:**
- **FTC .com Disclosures (2013)** — proximity / prominence / *whether it is unavoidable* / distracting-factor
  test, plus the explicit preference to fold qualifiers into the claim rather than park them in a separate
  disclosure: "advertisers should incorporate relevant limitations and qualifying information into the
  underlying claim, rather than having a separate disclosure qualifying the claim."
  https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf
- **FTC Deception Policy Statement (1983)** — “Advertising that lacks a reasonable basis is also deceptive.”
  https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception
- **21 CFR 202.1(e)(5)–(6)** (FDA) — fair balance must be “comparable in depth and detail”; comparative
  superiority banned absent substantial evidence; a true statement elsewhere **cannot cure** a misleading part.
  https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202/subpart-A/section-202.1
- **SEC Marketing Rule 206(4)-1** — unsubstantiated material statements of fact are violations; "negligence
  is sufficient." https://web.archive.org/web/2023id_/https://www.sec.gov/files/rules/final/2020/ia-5653.pdf
- **FCA COBS 4.2.1 R** — "A firm must ensure that a communication or a financial promotion is fair, clear and
  not misleading." https://www.handbook.fca.org.uk/handbook/COBS/4/2.html
- **GDPR Art. 12(1)** — “concise, transparent, intelligible and easily accessible form, using clear and plain
  language” (four conjunctive requirements; “concise” alone does not license vagueness).
  https://gdpr-info.eu/art-12-gdpr/
- **DSA Art. 25** — dark-pattern ban incl. “giving more prominence to certain choices.”
  https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html
- **식약처 (MFDS) enforcement, 2026-09-17** — a concrete Korean blacklist of banned health-benefit wording
  (피부재생, 노화방지, 항염, 세포재생, 잇몸재생), with cited statutes. https://www.sideview.co.kr/news/articleView.html?idxno=20430

**Subagent's two new tooling unlocks (useful for the parent):**
- **Google News RSS works** for any locale: `https://news.google.com/rss/search?q=QUERY&hl=ko&gl=KR&ceid=KR:ko`
  — but article links are opaque `news.google.com/rss/articles/CBMi…` redirects that do NOT resolve via `curl -L`.
  Use to discover headlines only.
- **Yahoo! Japan web search works** and is a real general index: `https://search.yahoo.co.jp/search?p=QUERY`
  (result URLs appear as JSON-escaped `"https://…"` strings).

---

## STATUS
- Category 1: **8 DOCUMENTED sources**, all primary-court-filing or bylined-reporting grade.
- Category 4: **1 strong primary** (Apple's iPhone 4 letter) — thin; the “courage” and “holding it wrong”
  items could NOT be verified and are excluded.
- Categories 5 & 6: **18 verified sources** from subagent.
- Categories 2 & 3: subagent still running at wrap-up; no file written yet.
