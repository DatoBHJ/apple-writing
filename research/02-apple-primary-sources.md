# Apple 1차 문장/보이스 소스 조사

> 조사 목적: Apple의 **글쓰기 스타일 / 산문 보이스**를 AI 에이전트 스킬로 인코딩하기 위한 1차 출처 확보.
> 원칙: 이 문서의 모든 인용문은 **실제로 fetch에 성공한 페이지**에서 나온 것이다. 2차 출처는 명시적으로 표기했다. 지어낸 규칙 없음.
> 조사일 기준 최신 확인 버전: **Apple Style Guide, June 2026** / **HIG Writing, 변경 기록 2025-12-16 기준** / **App Store Review Guidelines, Last Updated: June 8, 2026**
> 페치 방법 표기: `curl` = 브라우저 UA로 직접 HTML 수신, `jina` = `https://r.jina.ai/<url>` 리더 프록시(JS 렌더링 페이지용), `pdf` = 공식 PDF 다운로드 후 pypdf 텍스트 추출.
> **증거 등급**: 이 문서는 §7에서 **PRIMARY**(Apple 발행물 또는 원본 스캔) / **SECONDHAND**(2차 자료가 인용) / **MYTH·DISPUTED**(검증 가능한 1차 실물 없음)를 명시적으로 구분한다. §1–§6은 등급이 모두 공식 1차이며, §5만 “공식 1차 페이지를 관찰한 컨벤션”임을 밝힌다.
> **주의**: §2·§4·§6의 여러 페이지는 JS 렌더링 SPA라 `curl`로는 본문이 나오지 않는다. §(d)의 “도구·라우트 요약” 표를 먼저 볼 것.

---

## (a) 출처 총괄표

| 출처 | URL | 성격 | 무엇을 규정하는가 | 인용 가능한 규칙 수 |
| --- | --- | --- | --- | --- |
| **Apple Style Guide (PDF, June 2026, 244p)** | https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf | 공식 1차 (Apple 발행, 최신판) | 대문자 표기, 숫자, 하이픈, 약어, 단위, 제품명, 트레이드마크, 포용적 언어, 국제 스타일, 기술 표기 | 약 30+ (전체 244p, A–Z 사전식) |
| **Apple Style Guide (웹판)** | https://support.apple.com/guide/applestyleguide/welcome/web | 공식 1차 (PDF와 동일 내용의 웹 버전) | 위와 동일. 개별 항목 딥링크 가능 | 위와 동일 |
| ASG 웹 – About the guide | https://support.apple.com/guide/applestyleguide/about-the-guide-apsg0a1a8f0e/web | 공식 1차 | 적용 범위, Merriam-Webster/Chicago 의존, Marcom 서브 가이드 존재 | 4 |
| ASG 웹 – Capitalization | https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web | 공식 1차 | sentence-style vs title-style 대문자 규칙 전문 | 12+ |
| ASG 웹 – Writing inclusively | https://support.apple.com/guide/applestyleguide/writing-inclusively-apdcb2a65d68/web | 공식 1차 | 포용적 언어, 성별 중립, 장애 표현 | 10+ |
| **HIG — Writing** | https://developer.apple.com/design/human-interface-guidelines/writing | 공식 1차 (권고) | 앱 UI 카피 전반: voice/tone, 능동태, 버튼 레이블, 대문자, 오류 메시지, 빈 상태, 설정 레이블 | 14 |
| **HIG — Inclusion** | https://developer.apple.com/design/human-interface-guidelines/inclusion | 공식 1차 | 환영하는 언어(welcoming language), you/your vs the user, 전문용어·구어체·유머 | 5 |
| HIG — Buttons (Content) | https://developer.apple.com/design/human-interface-guidelines/buttons | 공식 1차 | 버튼 레이블: title-style 대문자, 동사로 시작 | 2 |
| HIG — Alerts (Content) | https://developer.apple.com/design/human-interface-guidelines/alerts | 공식 1차 | 경고 제목/본문/버튼 카피, OK 사용 제한, 문장 vs 구절 대문자 | 5 |
| HIG — Onboarding | https://developer.apple.com/design/human-interface-guidelines/onboarding | 공식 1차 | 온보딩 카피 분량·톤·스킵 | 4 |
| HIG — Feedback | https://developer.apple.com/design/human-interface-guidelines/feedback | 공식 1차 | 피드백 강도와 메시지 톤 매칭 | 3 |
| HIG — Settings | https://developer.apple.com/design/human-interface-guidelines/settings | 공식 1차 | 설정 레이블 최소화 | 3 |
| HIG — Notifications (Content) | https://developer.apple.com/design/human-interface-guidelines/notifications | 공식 1차 | 알림 제목/본문 대문자·문장부호, 미리보기 텍스트 | 4 |
| HIG — Labels / Text fields | https://developer.apple.com/design/human-interface-guidelines/labels · https://developer.apple.com/design/human-interface-guidelines/text-fields | 공식 1차 | 레이블·플레이스홀더·필드 오류 카피 | 3 |
| HIG — Branding | https://developer.apple.com/design/human-interface-guidelines/branding | 공식 1차 | 브랜드 보이스/톤, Apple 상표를 앱 이름에 쓰지 말 것 | 2 |
| HIG — 한국어판 Writing | https://developer.apple.com/kr/design/human-interface-guidelines/writing | 공식 1차 (Apple 한국어 현지화) | 한국어 카피의 실제 문체(합쇼체), 용어 선택 | 6+ |
| HIG — 日本語版 Writing | https://developer.apple.com/jp/design/human-interface-guidelines/writing | 공식 1차 (Apple 일본어 현지화) | 일본어 카피의 실제 문체(です・ます調) | 5+ |
| **App Store Review Guidelines** | https://developer.apple.com/app-store/review/guidelines/ | 공식 1차 (구속력) | 메타데이터 정확성, 앱 이름 30자, 키워드 스터핑 금지, What’s New | 8 |
| **Creating Your Product Page** | https://developer.apple.com/app-store/product-page/ | 공식 1차 (권고) | 앱 이름·부제·설명·프로모션 텍스트·키워드·What’s New 작성법 + 30/30/170/100자 | 8 |
| ASC Help — App information | https://developer.apple.com/help/app-store-connect/reference/app-information/app-information | 공식 1차 (필드 정의) | App Name 2–30자, Subtitle 30자 | 2 |
| ASC Help — Platform version information | https://developer.apple.com/help/app-store-connect/reference/platform-version-information | 공식 1차 (필드 정의) | Promotional Text 170자, Description 4000자, Keywords 100 bytes | 4 |
| ASC Help — View and edit app information | https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information | 공식 1차 | 검색 인덱싱 대상 4개 필드 | 2 |
| ASC Help — Localize app information | https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information | 공식 1차 | 메타데이터 스토어프론트별 현지화 | 1 |
| Discovery on the App Store | https://developer.apple.com/app-store/discoverability/ | 공식 1차 (권고) | 검색 랭킹 텍스트 요인 | 3 |
| Apple Ads — Create Ad Variations | https://ads.apple.com/app-store/help/ads/0077-create-ad-variations | 공식 1차 | 광고 크리에이티브 = 커스텀 제품 페이지 | 3 |
| **apple.com / apple.com/kr / apple.com/jp** | https://www.apple.com/ · https://www.apple.com/kr/ · https://www.apple.com/jp/ · https://www.apple.com/iphone/ · https://www.apple.com/kr/iphone/ · https://www.apple.com/jp/iphone/ | 공식 1차 (관찰 대상) | 히어로 태그라인, CTA, 각주 체계, 현지화 문체 | 40+ |
| Apple Newsroom 보도자료 (EN/KR/JP) | https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/ · https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/ · https://www.apple.com/jp/newsroom/2026/09/apple-unveils-iphone-duo/ | 공식 1차 | 데이트라인, 리드, 임원 인용, 보일러플레이트, 한다체 vs です/ます体 | 25+ |
| Apple Support 문서 (EN/KO/JA) | https://support.apple.com/en-us/118575 · https://support.apple.com/ko-kr/118575 · https://support.apple.com/ja-jp/118575 | 공식 1차 | 과제형 제목, 명령형 단계문, 피드백 마이크로카피 | 20+ |
| Apple Legal / Privacy | https://www.apple.com/legal/internet-services/itunes/ · https://www.apple.com/legal/privacy/en-ww/ | 공식 1차 | 계약 문체, we/you, 정의 용어 도입 | 8 |
| **Swift API Design Guidelines** | https://www.swift.org/documentation/api-design-guidelines/ | 공식 (Apple 저작, Swift.org 호스팅) | 명명·명료성·용어 — “Clarity at the point of use” | 8 |
| DocC — Writing symbol documentation | https://www.swift.org/documentation/docc/writing-symbol-documentation-in-your-source-files (Apple 미러: `.../xcode/writing-symbol-documentation-in-your-source-files.md`) | 공식 (Apple 저작) | 심볼 문서 요약문 길이·형식 | 6 |
| DocC — Adding structure to docs pages | https://www.swift.org/documentation/docc/adding-structure-to-your-documentation-pages | 공식 (Apple 저작) | 랜딩 페이지/개요 분량 | 5 |
| **WWDC22 10037 — Writing for interfaces** | https://developer.apple.com/videos/play/wwdc2022/10037/ | 공식 1차 (세션 전문) | UI 카피 4원칙 PACE, 보이스/톤, 감탄사·`please` 절제 | 8 |
| **WWDC25 404 — Make a big impact with small writing changes** | https://developer.apple.com/videos/play/wwdc2025/404/ | 공식 1차 (세션 전문) | 필러 제거, 반복 제거, why 선행, 워드리스트 | 9 |
| WWDC24 10140 — Add personality through UX writing | https://developer.apple.com/videos/play/wwdc2024/10140/ | 공식 1차 | voice vs tone, Apple의 4품질 | 6 |
| WWDC21 10221 — Streamline your localized strings | https://developer.apple.com/videos/play/wwdc2021/10221/ | 공식 1차 | 번역자용 코멘트 3요소 | 6 |
| WWDC22 10110 — Build global apps: Localization by example | https://developer.apple.com/videos/play/wwdc2022/10110/ | 공식 1차 | 문자열 분리, 코멘트, 문자열 결합 위험 | 5 |
| WWDC19 254 — Writing Great Accessibility Labels | https://developer.apple.com/videos/play/wwdc2019/254/ | 공식 1차 | 접근성 레이블 간결성 | 6 |
| WWDC22 10034 — Design for Arabic | https://developer.apple.com/videos/play/wwdc2022/10034/ | 공식 1차 | RTL 조판·문화적 적합성 | 4 |
| ASG 웹 – Intro to international style | https://support.apple.com/guide/applestyleguide/intro-to-international-style-apsg1ff68ab5/web | 공식 1차 | 번역 친화 문체 4원칙 | 5 |
| ASG 웹 – Gender identity | https://support.apple.com/guide/applestyleguide/gender-identity-apd2a7af8d36/web | 공식 1차 | 성별 중립 표현 | 4 |
| ASG 웹 – Writing about disability | https://support.apple.com/guide/applestyleguide/writing-about-disability-apd49cbb2b06/web | 공식 1차 | identity-first/person-first | 6 |
| ASG 웹 – Inclusive representation | https://support.apple.com/guide/applestyleguide/inclusive-representation-apd7a037f274/web | 공식 1차 | 예시 이름·고정관념 | 4 |
| ASG 웹 – General guidelines | https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web | 공식 1차 | 포용적 언어 일반 | 5 |
| **HIG 한국어판 Writing** | https://developer.apple.com/kr/design/human-interface-guidelines/writing | 공식 1차 (Apple 자체 현지화) | 한국어 합쇼체 지침문의 실물 증거 | 6 |
| **HIG 日本語版 Writing** | https://developer.apple.com/jp/design/human-interface-guidelines/writing | 공식 1차 (Apple 자체 현지화) | 일본어 です/ます体 지침문의 실물 증거 | 5 |
| Apple Newsroom 인덱스 | https://www.apple.com/newsroom/ | 공식 1차 | 릴리스 목록 (JS 렌더 → jina 필요) | 3 |
| **“The Apple Marketing Philosophy” (Dec. 1979)** 스캔 | https://archive.org/details/102789075-05-01-acc | **PRIMARY 팩시밀리** (커뮤니티 업로드, 진본 인증 없음) | Empathy / Focus / Impute — 마케팅 철학 | 8 |
| “Thoughts on Flash” (Jobs, 2010) | https://web.archive.org/web/20101231041029/http://www.apple.com/hotnews/thoughts-on-flash/ | 공식 1차 (Apple 게시, Wayback) | 경영진 공개 서한의 산문 규칙, `we` 레지스터 | 6 |
| “Apple’s commitment to privacy” (Cook, 2014) | https://web.archive.org/web/20151231214053/http://www.apple.com/privacy/ | 공식 1차 (Apple 게시, Wayback) | 프라이버시 서한 보이스 | 6 |
| Stanford Krause 미디어 메모 (1985) | https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html · .../krause1.html | **PRIMARY 아카이브** (`M1007, Apple Computer Inc. Papers`) | 사내 미디어 대응·단일 메시지 원칙 | 6 |
| Apple Business Conduct Policy (Feb 2026) | https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf | 공식 1차 (Apple 공개 게시) | 직원 발언·기고 승인 규정 | 4 |
| Think Different Really Different Brochure (1997) | https://archive.org/details/19971110-really-different-brochure_202201 | **PRIMARY 팩시밀리** (실제 스캔 검증) | 1997년 제품 마케팅 목소리 | 7 |
| “Crazy Ones” 대본 | https://web.archive.org/web/2018/https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/ | **SECONDHAND** (원작자 Siltanen/Forbes) | 캠페인 카피 — Apple 하우스 스타일 아님 | 4 |
| “Think Different Booklet (1997)” | https://archive.org/details/think-different-booklet-1997 | **SECONDHAND 전사본** (팩시밀리 **아님**) | 캠페인 카피 교차 확인용 | 4 |
| apple.com/privacy/ · /environment/ · /accessibility/ | https://www.apple.com/privacy/ · https://www.apple.com/environment/ · https://www.apple.com/accessibility/ | 공식 1차 (현재 라이브) | 가치 서술 보이스 문법 | 8 |
| **Apple Marcom 톤오브보이스 가이드** | — | **존재하지 않음 (clean negative)** | — | 0 |
| **`apple.com/values/`** | — | **404 (존재하지 않음)** | — | 0 |

---

## (b) 출처별 상세 + 실제 인용문

### 1. Apple Style Guide — Apple의 공식 편집 스타일 가이드

**URL (PDF):** https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf
**URL (웹):** https://support.apple.com/guide/applestyleguide/welcome/web
**페치:** PDF `curl` 200, 4,158,788 bytes → pypdf로 244페이지 / 488,708자 추출 성공. 웹판 `curl` 200, 588,475 bytes.
**성격:** 공식 1차. Apple이 직접 “Editorial guidelines for Apple”로 발행. 표지 기준 **June 2026**.

#### 목차 (PDF 페이지 2–3 그대로)

```
About this guide 4 / About the guide 4 / Changes to the guide 6
Style and usage A–Z 11 / Numbers 11 / A 11 / B 36 / C 44 / D 61 / E 77 / F 83 /
G 92 / H 97 / I 104 / J 118 / K 119 / L 122 / M 131 / N 146 / O 150 / P 153 /
Q 172 / R 173 / S 179 / T 199 / U 209 / V 213 / W 216 / X 221 / Y 221 / Z 222
Writing inclusively 223 / Intro to inclusive writing 223 / General guidelines 223 /
Inclusive representation 225 / Gender identity 226 / Writing about disability 227
Units of measure 230 / Intro to units of measure 230 / Prefixes for units of measure 231 /
Names and unit symbols for units of measure 232
Technical notation 237 / Intro to technical notation 237 / Code 237 /
Syntax descriptions 237 / Code font in text 238 / Placeholder names in text 238
International style 239 / Intro to international style 239 / Countries 239 /
Currency 240 / Dates and times 241 / Decimals 241 / Languages 242 /
Telephone numbers 243 / Units of measure 243
Copyright and trademarks 244
```

웹판 목차(https://support.apple.com/guide/applestyleguide/welcome/web)도 동일하며, “Apple Style Guide **June 2026**”으로 표기된다.

#### 적용 범위 (About the guide, p.4)

> “The Apple Style Guide provides editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and user interfaces. The intent of these guidelines is to help maintain a consistent voice in Apple materials.”

> “Writers, editors, and developers can use this document as a guide to writing style, usage, and Apple product terminology.”

> “Apple developers and third-party developers should follow these guidelines for user-facing text.”

#### 상위 권위 문서 (Other editorial resources used at Apple, p.5)

> “In general, follow the style and usage rules in: Merriam-Webster’s Collegiate Dictionary / The Chicago Manual of Style”

> “In cases where resources conflict with each other, follow The Chicago Manual of Style for style and usage questions, and Merriam-Webster’s Collegiate Dictionary for spelling guidance.”

> “Guidance on style, usage, and spelling in the Apple Style Guide is based on U.S. English conventions. For localized content, consult resources specific to the language or region.”

> “Some departments at Apple (Marcom, for example) have supplemental style guides.”

> “For information about the user interface, see Apple’s Human Interface Guidelines.”

#### 하이픈 규칙 (Conventions used in this guide, p.5)

> “Modifiers consisting of two or more words are often hyphenated when they precede a noun, but not when they follow the verb as a compound predicate adjective.”

> “An entry followed by **adj.** in parentheses gives the form to be used when the adjective immediately precedes the noun it modifies.”

> “If a hyphenated compound has no **pred. adj.** entry, hyphenate the compound wherever it appears in a sentence.”

#### 대문자 표기 (capitalization, p.45–47) — 스킬에 가장 이식성 높은 규칙

> "Two styles of capitalization are commonly used at Apple:
> • Sentence-style capitalization: This line provides an example of sentence-style capitalization.
> • Title-style capitalization: This Line Provides an Example of Title-Style Capitalization."

> “Except for user interface text, guidelines for when to use sentence-style capitalization and when to use title-style capitalization are a matter of department style.”

> “In general, capitalize the names of onscreen elements exactly as they appear onscreen.”

> “If an onscreen element uses all capital letters or all lowercase letters, use title-style capitalization when writing the element name in documentation.”

Title-style에서 **대문자로 쓰는 것**:
> “The first and last word, regardless of the part of speech”
> “Nouns, pronouns, verbs, adjectives, and adverbs—no matter their length (for example, It, This, You, Your, My, Is, Are, and Be)”
> “Prepositions of five letters or more (for example, About, Between, Through)”
> “Prepositions of any length when they’re part of a phrasal verb (such as Start Up, Turn On, or Log In)”
> “The second word in a hyphenated compound (except for Built-in and Plug-in)”

Title-style에서 **대문자로 쓰지 않는 것**:
> “Articles (a, an, the), unless an article is the first word or follows a colon”
> “Coordinating conjunctions (and, but, or, nor, for, yet, and so)”
> “The word to in infinitives (How to Start Your Computer)”
> “The word as, regardless of the part of speech (Export a Document as a PDF)”
> “Words that always begin with a lowercase letter, such as iPad and macOS”
> “Prepositions of four letters or fewer (at, by, for, from, in, into, of, off, on, onto, out, over, to, up, and with)”

**sentence-style capitalization** (별도 항목):
> “Capitalize only the first letter of the first word, proper nouns, and proper adjectives.”

**title-style capitalization** (별도 항목):
> “Capitalize each word—except for articles, prepositions of four or fewer letters, and so on.”

#### 태(voice) — 능동태/수동태 (passive voice, p.154)

> “Avoid when possible and use active voice. Passive voice is sometimes appropriate and necessary—for example, when using the active voice would require either a highly convoluted sentence structure or excessive anthropomorphism—but rewrite to avoid passive voice if you can.”

> "In tutorials, a passive construction might be appropriate to avoid miscuing the reader—that is, when you describe an action that the user isn’t supposed to try yet.
> Explanation screen: An icon is selected by clicking it.
> User-try screen: You try it. Click the icon."

#### 1인칭 금지 (first person, p.87)

> “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.”

#### 독자를 주어로 — allow (p.42)

> "Avoid using allow when you can restructure a sentence to make the reader the subject.
> Avoid: FileMaker Pro allows you to create a database.
> Preferable: You can create a database with FileMaker Pro."

#### 능력 표현 — capability (p.45)

> "If possible, avoid capability when you discuss features of software or hardware. Reword in terms of what the user can do with the feature.
> Correct: With Photos, you can create slideshows.
> Incorrect: Photos has the capability to create slideshows."

#### 숫자 (numbers, p.148–149)

> “Spell out the following numbers: • Cardinal numbers from one through nine. (However, use a numeral, no matter how small, to express numbers as numbers and as units of measure.) • Ordinal numbers from zero through nine. • Numbers that appear at the beginning of a sentence. (Try to rephrase to avoid starting a sentence with a number.) • A number that appears next to another number, if it helps readability.”

> “Use numerals: • To refer to numbers as numbers. • To refer to a specific address, bit, byte, chapter, field, key, pin, sector, slot, or track, or when expressing amounts of memory.”

#### 하이픈 (hyphenation, p.104)

> “In general, hyphenate two words that precede and modify a noun as a unit.”

> “Adverbs: Don’t hyphenate compounds with very or with adverbs that end in -ly.” (예: `very high speed`, `recently completed project`)

> “Units of measure: When you use a spelled-out unit of measure in a compound adjective, hyphenate the compound (27-inch screen). When you use an abbreviation or a metric unit of measure, including KB, MB, mm, and so on, don’t hyphenate (500 GB hard disk).”

> “Keyboard shortcuts using combination keystrokes: Use hyphens to signify that the first key or keys should be held down while the last key is pressed.”

#### 단위 (Units of measure, p.243)

> “Use only units of the International System of Units (SI) to express the values of quantities.”

> “Quantities are always expressed with a unit symbol. Use a nonbreaking space (Option-Space bar) between the quantity and its symbol. Unit symbols are unaltered in the plural and are never hyphenated, even when they’re used as an adjective.”

> “Symbols for SI units of measure aren’t followed by a period unless they appear at the end of a sentence.”

> “Don’t imply more precision than is reasonable in choosing a unit symbol.”

> “Equivalent values in non-SI units may be given in parentheses following SI values.” (예: `iPad mini (A17 Pro) Wi-Fi models weigh 293 g (0.65 lb.).`)

#### 약어·두문자어 (abbreviations and acronyms, p.11–12)

> “When to spell out: If you think your audience might not be familiar with an abbreviation or acronym, spell out its first occurrence on a page or in a section. In user materials, spell out the term when you introduce it.”

> “How to spell out: When you spell out a term, generally put the spelled-out version first, with the abbreviation or acronym in parentheses.” (예: `internet service provider (ISP)`)

> “Punctuation: Don’t use periods except in abbreviations for nonmetric units of measure and in the abbreviations a.m., p.m., and U.S.”

> “Plural: Don’t add an apostrophe before the s when you form the plural of an abbreviation.” (예: `CDs, ICs, ISPs`)

> “Latin: Avoid using Latin abbreviations.” — “Correct: for example, and others, and so on, and that is, or equivalent phrases. Incorrect: e.g., et al., etc., i.e.”

> “Product names: Don’t abbreviate any Apple product or service names, whether or not the product or service is trademarked or has a service mark.”

#### 제품명 (product names, p.168) · 트레이드마크 (trademarks (usage), p.207)

> “Follow the capitalization style of the official product name. Don’t shorten or abbreviate product names.”

> “Names as verbs: Don’t use product names or trademarks as verbs: make a FaceTime call to a friend, not FaceTime a friend.”

> “Plurals and possessives: Rewrite to avoid using plural or possessive forms of product names that are trademarks: Mac computers, not Macs; check the storage on your iPad, not check your iPad’s storage.”

> “Names with lowercase letters: If a product name starts with a lowercase letter, use that capitalization style even at the beginning of sentences and in title-style headings: iPhone Safety Features, not IPhone Safety Features; Set Up Your Mac mini, not Set Up Your Mac Mini. In all-caps text, capitalize all the letters: THE NEW IPAD, not THE NEW iPAD.”

> “Trademark symbols: In user and developer materials (print and electronic), don’t use trademark symbols for Apple trademarks in headings or text. Note that other types of documents, such as press releases, do use trademark symbols in text.”

#### 문장부호·관용 (commas / ellipsis / humor)

> “commas — Use a serial comma before and or or in a list of three or more items.” (Correct: “…send reminders, and more.” / Incorrect: “…send reminders and more.”)

> “ellipsis — If the name of a menu item or button ends with an ellipsis, don’t include the ellipsis in running text. Correct: Choose File > New and click a template. Incorrect: Choose File > New… and click a template.”

> “humor — Humor can enhance documentation by adding to a reader’s enjoyment and by helping to lighten the tone. Humor usually works best in examples… Be careful that your humor is in good taste—one reader’s joke can be another reader’s insult—and keep in mind that humor may not translate well in localized text.”

#### 동작 동사 구분 (choose / select / enter / press / tap)

> “choose — Use choose, not select, for menu items. In general, the user selects something (such as a file or disk icon, an email message, or a section of text) and then chooses a command to act on the selection.”

> “select (v.) — Use select, not choose, to refer to the action users perform when they select among multiple objects… or when they highlight text for editing.”

> “enter — Use enter, not type, to describe inputting text-based information by typing, copying and pasting, dragging, or some other method. Use type to describe pressing or tapping keys to produce characters on the screen. Use press, not type, to refer to pressing keys on the keyboard.”

> “press — Use to describe the act of pressing and quickly releasing keys on the keyboard and mechanical buttons and switches. Don’t use click, hit, push, tap, or type.”

> “tap (n., v.) — On devices with touchscreens or trackpads, tap refers to the act of quickly touching and releasing the touchscreen or trackpad. **Don’t use tap on.**” (Correct: “Tap Return to move from one field to another.” / Incorrect: “Tap on the video you want to play.”)

> “tap and hold — Don’t use. Tap means to touch and release quickly, so use touch and hold instead.”

#### 버튼/온스크린 요소 인용 (button, p.43)

> “If the button’s name uses sentence-style capitalization, enclose the name in quotation marks.” (예: `Click the "Position on screen" button.`)

> “If the button’s name uses title-style capitalization, don’t enclose the name in quotation marks, even if one of the words is lowercase.” (예: `Tap Add to Favorites.`)

> “If an element in the user interface acts like a button (initiates an action when clicked or tapped), call it a button, even if it displays an icon or an image.”

#### 포용적 언어 (Writing inclusively, p.223–229)

> “Avoid terms that are violent, oppressive, or ableist. Don’t describe technology using terms that are inherently violent—like kill or hang. Don’t use the terms master and slave, which describe an oppressive human relationship. In addition, don’t use terms like sanity check, which associates mental health with being functional.”

> “Avoid idioms and colloquial expressions. Common sayings—like fall through the cracks, on the same page, or backseat driver—can add flavor to writing, but they can also be difficult to understand for people who are learning the language.”

> “Don’t use color to convey positive or negative qualities. Avoid assigning good and bad values to colors (for example, blacklist, white hat hacker, or red team hacker).”

> "Use gender-neutral pronouns. Don’t use gender-specific pronouns (such as he, she, he or she, and so on) to refer to people of unspecified gender. Instead, it’s OK to use they, their, or them as a singular, gender-neutral pronoun.
> Correct: A subscriber can post their recipes to your shared folder.
> Incorrect: A subscriber can post his or her recipes to your shared folder."

> “Avoid language that refers to using specific senses. When writing instructions… avoid using phrases that refer to the use of specific senses, like you see a message, you see a flashing light, or you hear an alert sound. Instead, simply describe what happens: A message appears, a light flashes, an alert sound plays.”

> “Avoid ableist language. Don’t use language that presents people without disabilities as the norm. For example, don’t describe nondisabled people as normal, healthy, regular, or able-bodied.”

> “Don’t treat disability as something to overcome, and don’t describe people with disabilities as brave, courageous, or inspiring, which can come across as condescending.”

> “Err on the side of caution. If you’re not sure about a term, but you believe it might be questionable based on your research or feedback from others, then choose a different term.”

---

### 2. Apple Human Interface Guidelines — Writing 계열

**URL:** https://developer.apple.com/design/human-interface-guidelines/writing
**페치:** `curl` 200이지만 **17572 bytes의 JS 셸만 반환(본문 없음)**. `jina` 프록시(`https://r.jina.ai/https://developer.apple.com/design/human-interface-guidelines/writing`) 200 → **본문 전체 markdown 확보.** web.archive.org 2024 캡처는 5,506 bytes 셸만 반환해 실패.
**성격:** 공식 1차(권고). 변경 기록상 최신 개정 **December 16, 2025** (“Clarified guidance on language patterns, and added guidance for possessive pronouns”). 페이지 최초 생성 February 27, 2023.

#### 도입부

> “Whether you’re building an onboarding experience, writing an alert, or describing an image for accessibility, designing through the lens of language will help people get the most from your app or game.”

메타 설명(HTML `<meta name="description">`에서 직접 확인):
> “The words you choose within your app are an essential part of its user experience.”

#### Getting started

> “**Determine your app’s voice.** Think about who you’re talking to, so you can figure out the type of vocabulary you’ll use. … Create a list of common terms, and reference that list to keep your language consistent.”

> “**Match your tone to the context.** Once you’ve established your app’s voice, vary your tone based on the situation. … Situational factors affect both what you say and how you display the text on the screen.”

> “**Be clear.** Choose words that are easily understood and convey the right thing. Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.”

> “**Write for everyone.** … Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology.”

#### Best practices (스킬 핵심)

> “**Consider each screen’s purpose.** Pay attention to the order of elements on a screen, and put the most important information first.”

> “**Be action oriented.** Active voice and clear labels help people navigate… When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying ”Send“ often works better than ”Let’s do it!“ For links, avoid using ”Click here“ in favor of more descriptive words or phrases, such as ”Learn more about UX Writing.“”

> “**Build language patterns.** Consistency builds familiarity, helping your app feel cohesive, intuitive, and thoughtfully designed.”

> “**Adopt capitalization rules that align with your app’s style, then apply them consistently.** While certain components, like button labels, have specific guidelines, how you format text reflects your app’s voice. **Title case is generally considered formal, while sentence case is more casual.** Choose a style for each UI element type and use it consistently throughout your app — for example, title case for all alerts or sentence case for all headlines.”

> “**Give clear guidance and use consistent language throughout processes with multiple steps.** … Begin with language like ”Get Started“ to indicate you’re starting a flow. You can use the button label to hint at the next step, or use terms like ”Continue“ or ”Next,“ but be consistent with what you choose. Make it clear when a flow is complete by using language like ”Done.“”

> “**Use possessive pronouns sparingly.** Possessive pronouns like *my* and *your* are often unnecessary to establish context. For example, ”Favorites“ conveys the same message as ”Your Favorites,“ and is more succinct. … **Avoid using *we* altogether because it may be unclear who the ”we“ in question refers to.** This is particularly problematic in error messages like ”We’re having trouble loading this content.“ Something like ”Unable to load content“ is much clearer.”

> “**Write for how people use each device.** … Make sure you describe gestures correctly on each device — for example, not saying ”click“ for a touch device like iPhone or iPad where you mean ”tap.“”

> “**Provide clear next steps on any blank screens.** An empty state… can provide a good opportunity to make people feel welcome and educate them about your app. … Remember that empty states are usually temporary, so don’t show crucial information that could then disappear.”

> “**Write clear error messages.** It’s always best to help people avoid errors. When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, ”That password is too short“ isn’t as helpful as ”Choose a password with at least 8 characters.“ Remember that errors can be frustrating. **Interjections like ”oops!“ or ”uh-oh“ are typically unnecessary and can sound insincere.** If you find that language alone can’t address an error that’s likely to affect many people, use that as an opportunity to rethink the interaction.”

> “**Keep settings labels clear and simple.** … If the setting label isn’t enough, add an explanation. **Describe what it does when turned on, and people can infer the opposite.** … If you need to direct someone to a setting, provide a direct link or button, rather than trying to describe its location.”

> “**Show hints in text fields.** … Show errors right next to the field, and instruct people how to enter the information correctly, rather than scolding them for not following the rules. ”Use only letters for your name“ is better than ”Don’t use numbers or symbols.“ **Avoid robotic error messages with no helpful information, like ”Invalid name.“**”

#### HIG — Inclusion (Welcoming language)

**URL:** https://developer.apple.com/design/human-interface-guidelines/inclusion (페이로드: `jina` 200, 18,086 bytes)

> “Using plain, inclusive language welcomes everyone and helps them understand your app or game. Carefully review the writing in your experience to make sure that your tone and words don’t exclude people.”

> “**Pay attention to how you refer to people.** It typically works well to use *you* and *your* to address people directly. **Referring to people indirectly as *the user* or *the player* can make your experience feel distant and unwelcoming.** Also, consider reserving words like *we* and *our* to represent your software or company; otherwise, these terms can suggest a personal relationship with people that might be interpreted as insulting or condescending.”

> “**Avoid using specialized or technical terms without defining them.** … If you must use such terms, be sure to define them first… Even when people know the definition of a specialized or technical term in a sentence, the sentence is easier to read — and translate — when it uses plain language instead.”

> “**Replace colloquial expressions with plain language.** Colloquial expressions are often culture-specific and can be difficult to translate. Worse, some colloquial phrases have exclusionary meanings you might not know. For example, the phrases *peanut gallery* and *grandfathered in* both arose from oppressive contexts and continue to exclude people.”

> “**Consider carefully before including humor.** Humor is highly subjective and — similar to colloquial expressions — difficult to translate from one culture to another. Including humor in your experience risks confusing people who don’t understand it…”

> (Gender identity) “…a recipe-sharing app that uses copy like ”You can let a subscriber post his or her recipes to your shared folder“ could avoid unnecessary gender references by using an alternative like ”Subscribers can post recipes to your shared folder.“”

#### HIG — Buttons / Alerts / Notifications / Onboarding / Feedback / Settings

**Buttons** (https://developer.apple.com/design/human-interface-guidelines/buttons):
> “**Consider using text when a short label communicates more clearly than an icon.** To use text, write a few words that succinctly describe what the button does. Using title-style capitalization, consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label ”Add to Cart.“”

**Alerts** (https://developer.apple.com/design/human-interface-guidelines/alerts):
> “**In all alert copy, be direct, and use a neutral, approachable tone.** Alerts often describe problems and serious situations, so avoid being oblique or accusatory, or masking the severity of the issue.”

> “**Write a title that clearly and succinctly describes the situation.** … Avoid writing a title that doesn’t convey useful information — like ”Error“ or ”Error 329347 occurred“ — but also avoid overly long titles that wrap to more than two lines. **If the title is a complete sentence, use sentence-style capitalization and appropriate ending punctuation. If the title is a sentence fragment, use title-style capitalization, and don’t add ending punctuation.**”

> “**Include informative text only if it adds value.** If you need to add an informative message, keep it as short as possible, using complete sentences, sentence-style capitalization, and appropriate punctuation.”

> “**Create succinct, logical button titles.** Aim for a one- or two-word title that describes the result of selecting the button. Prefer verbs and verb phrases that relate directly to the alert text — for example, ”View All,“ ”Reply,“ or ”Ignore.“ **In informational alerts only, you can use ”OK“ for acceptance, avoiding ”Yes“ and ”No.“ Always use ”Cancel“ to title a button that cancels the alert’s action.** As with all button titles, use title-style capitalization and no ending punctuation.”

> “**Avoid using OK as the default button title unless the alert is purely informational.** … A specific button title like ”Erase,“ ”Convert,“ ”Clear,“ or ”Delete“ helps people understand the action they’re taking.”

> “**Avoid explaining alert buttons.** If your alert text and button titles are clear, you don’t need to explain what the buttons do. In rare cases where you need to provide guidance on choosing a button, use a term like *choose* to account for people’s current device and interaction method, and **refer to a button using its exact title without quotes.**”

**Notifications** (https://developer.apple.com/design/human-interface-guidelines/notifications):
> “**Provide concise, informative notifications.** People turn on notifications to get quick updates, so you want to provide valuable information succinctly.”

> “**Use an alert — not a notification — to display an error message.**”

> “**Create a short title if it provides context for the notification content.** … Use title-style capitalization and no ending punctuation.”

> “**Write succinct, easy-to-read notification content.** Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.”

> “**Avoid including your app name or icon.**”

> (액션 버튼) “For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name or any extraneous information in the button label, keep the text brief to avoid truncation, and take localization into account as you write it.”

**Onboarding** (https://developer.apple.com/design/human-interface-guidelines/onboarding):
> “Ideally, people can understand your app or game simply by experiencing it, but if onboarding is necessary, design a flow that’s fast, fun, and optional.”

> “**If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn’t require people to memorize a lot of information.** When onboarding is quick and entertaining, people are more likely to complete it. In contrast, if you try to teach too much, people can feel overwhelmed…”

> “**Keep onboarding content focused on the experience you provide.** People enter your onboarding flow to learn about your app or game; they don’t need to learn how to use the system or the device.”

> “**Briefly display a splash screen if necessary.** If you need to include a splash screen, design a beautiful graphic that communicates succinctly. … without feeling that it’s delaying their experience.”

**Feedback** (https://developer.apple.com/design/human-interface-guidelines/feedback):
> “The most effective feedback tends to match the significance of the information to the way it’s delivered. For example, it often works well to display status information in a passive way so that people can view it when they need it. In contrast, a warning about possible data loss needs to interrupt people so they have a chance to avoid the problem.”

**Settings** (https://developer.apple.com/design/human-interface-guidelines/settings):
> “**Minimize the number of settings you offer.** Although people appreciate having control over an app or game, too many settings can make the experience feel less approachable, while also making it hard to find a particular setting.”

**Branding** (https://developer.apple.com/design/human-interface-guidelines/branding):
> “**Use your brand’s unique voice and tone in all the written communication you display.** For example, your brand might convey feelings of encouragement and optimism by using plain words, occasional exclamation marks and emoji, and simple sentence structures.”

> “**Follow Apple’s trademark guidelines.** Apple trademarks must not appear in your app name or images.”

**참고 (없는 페이지):** HIG에는 독립된 “**Terminology**” 페이지가 존재하지 않는다. 용어 규정은 (i) HIG 각 컴포넌트 페이지, (ii) **Apple Style Guide A–Z**, (iii) HIG Writing 페이지가 링크하는 “Writing inclusively”로 분산되어 있다. HIG “Materials”는 **시각적 재료(블러/반투명)** 페이지만 있고 카피 규정은 없다(요청 항목이지만 카피 규칙 없음 — 명시).

---

### 3. App Store — 카피를 규정하는 공식 문서

> 아래 §3은 하위 조사에서 수집·검증된 내용을 그대로 통합한 것이다. 모든 인용은 실제 fetch 성공 페이지에서 나왔다.

#### App Store Review Guidelines
**URL:** https://developer.apple.com/app-store/review/guidelines/ · **페치:** `curl` 200, 237,909 bytes. 페이지 푸터 “Last Updated: June 8, 2026”.
**성격:** 공식 1차, **구속력 있음**(위반 시 리젝이 아니라 앱 제거 사유가 될 수 있음).

- “2.3 Accurate Metadata — Customers should know what they’re getting when they download or buy your app, so make sure all your app metadata, including privacy information, your app description, screenshots, and previews accurately reflect the app’s core experience and remember to keep them up-to-date with new versions.”
- “2.3.7 … **App names must be limited to 30 characters.** Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type. App subtitles are a great way to provide additional context for your app; they must follow our standard metadata rules and should not include inappropriate content, reference other apps, or make unverifiable product claims.”
- “2.3.3 Screenshots should show the app in use, and not merely the title art, login page, or splash screen.”
- “2.3.8 Metadata should be appropriate for all audiences… Use of terms like ”For Kids“ and ”For Children“ in app metadata is reserved in the App Store for the Kids Category.”
- “2.3.10 Make sure your app metadata is focused on the app itself and its experience. Don’t include irrelevant information.”
- “2.3.12 Apps must clearly describe new features and product changes in their ”What’s New“ text. Simple bug fixes, security updates, and performance improvements may rely on a generic description, but more significant changes must be listed in the notes.”
- “2.3.1 (a) … marketing your app in a misleading way, such as by promoting content or services that it does not actually offer … or promoting a false price, whether within or outside of the App Store, is grounds for removal of your app from the App Store…”
- “4.2 Minimum Functionality — Your app should include features, content, and UI that elevate it beyond a repackaged website.”
- “5.2.1 Generally: … don’t include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name.”

→ **이식 가능한 규칙:** App Store 카피는 *마케팅 장식*이 아니라 **제품에 대한 사실 진술**이다. 모든 단어가 검증 가능해야 하고, 해당 필드에 특화되어야 하며, 비교·과장 표현은 금지된다.

#### Creating Your Product Page
**URL:** https://developer.apple.com/app-store/product-page/ · **페치:** `curl` 200, 134,611 bytes. (`&nbsp;` 엔티티 디코딩 필요 — “30 characters” 부분)
**성격:** 공식 1차, 권고.

- “Choose a simple, memorable name that is easy to spell and hints at what your app does. Be distinctive. Avoid names that use generic terms or are too similar to existing app names. **An app name can be up to 30 characters long.**”
- “Your app’s subtitle is intended to summarize your app in a concise phrase. Consider using this, rather than your app’s name, to explain the value of your app in greater detail. **Avoid generic descriptions such as ”world’s best app.“** Instead, highlight features or typical uses of your app that resonate with your audience. … A subtitle can be up to 30 characters long and appears below your app’s name throughout the App Store.”
- “Provide an engaging description that highlights the features and functionality of your app. **The ideal description is a concise, informative paragraph followed by a short list of main features.** … Communicate in the tone of your brand, and use terminology your target audience will appreciate and understand. **The first sentence of your description is the most important** — this is what users can read without having to tap to read more. Every word counts, so focus on your app’s unique features.”
- “If you choose to mention an accolade, we recommend putting it at the end of your description or as part of your promotional text. Don’t add unnecessary keywords to your description in an attempt to improve search results. Also avoid including specific prices in your app description.”
- “Your app’s promotional text appears at the top of the description and is **up to 170 characters long**. You can update promotional text at any time without having to submit a new version of your app.”
- “**Keywords are limited to 100 characters total, with terms separated by commas and no spaces.** … Maximize the number of words that fit in this character limit by avoiding the following: Plurals of words that you’ve already included in singular form / Names of categories or the word ”app“ / Duplicate words / Special characters — such as # or @ — unless they’re part of your brand identity.”
- “**Improper use of keywords is a common reason for App Store rejections.** Do not use the following in your keywords: Unauthorized use of trademarked terms, celebrity names, and other protected words and phrases / Terms that are not relevant to the app / Competing app names / Irrelevant, inappropriate, offensive, or objectionable terms”
- “When you update your app, you can use What’s New to communicate changes to users. … List new features, content, or functionality in order of importance, and add call-to-action messaging that gets users excited about the update.”
- “In-app purchase names are limited to 35 characters and descriptions are limited to 55 characters, so be descriptive, accurate, and concise when highlighting their benefits.”

→ **이식 가능한 규칙:** 하우스 보이스는 **구체성 > 최상급**. “world’s best app” 류 최상급, 키워드 패딩, 가격, 앞머리 수상 언급이 명시적 실패 모드다.

#### App Store Connect Help — 필드별 정확한 글자 수
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-information (`curl` 200, 378,351 bytes)
  - “Name | The localized name of your app as it appears on App Store product pages and when users install your app. **The name must be at least two characters and no more than 30 characters.**”
  - “Subtitle | A summary of your app that appears under your app’s name on your App Store product page. **This can’t be longer than 30 characters.**”
- https://developer.apple.com/help/app-store-connect/reference/platform-version-information (`curl` 200, 376,074 bytes)
  - “Promotional Text | … This property **can’t be longer than 170 characters**.”
  - “Description | A description of the app, detailing the features and functionality. **Limited to 4000 characters.** The description should be in plain text, with line breaks as needed. **HTML format isn’t supported.**”
  - “Keywords | One or more keywords (each greater than two characters) describing your app. You can provide **up to 100 bytes of content**. Your app is searchable by app name and company name, so you shouldn’t duplicate these values in the keyword list. Names of other apps or companies aren’t allowed.”
  - “What’s New in this Version | … **Limited to 4000 characters.** … This property isn’t available for the first version of the app but required for all subsequent versions.”
  - “Support URL | … **This URL must lead to actual contact information** (legal address, email address, telephone number), as may be required by local law…”
- https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information (`jina` 200)
  - “Your app is searchable on the App Store by **app name, app subtitle, keywords, and your company name.**”
  - “After updating your app information, it may take up to 24 hours for the changes to appear on the App Store or when users install your app.”
- https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information (`curl` 200, 373,812 bytes)
  - “Enter localized metadata—such as descriptions and keywords—for the platform, then click Save.”
- https://developer.apple.com/app-store/discoverability/ (`curl` 200, 117,168 bytes)
  - “When customers search for an app, the App Store returns a list of apps that are ranked based on a number of factors, including **text relevance (matches for the app’s title, keywords, and primary category)** and customer behavior…”
- https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization (`jina` 200)
  - “Optimize your iOS or iPadOS app’s product page on the App Store by testing **up to three different app icons, screenshots, and previews** to see which resonate best with customers.”
- https://ads.apple.com/app-store/help/ads/0077-create-ad-variations (`jina` 200)
  - “You can build **up to 70 custom product pages** with different app preview videos, screenshots, promotional text, and deep links.”

→ **필드 예산 요약:** Name 30 / Subtitle 30 / Keywords 100 **bytes** / Promotional Text 170 / Description 4000 / What’s New 4000 / IAP 이름 35 / IAP 설명 55.

**부정 발견(negative finding):** App Store Connect OpenAPI 스펙(`https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip`, `curl` 200, 263,653 bytes, `openapi.oas.json` 7.2 MB)에서 `AppStoreVersionLocalization.description/keywords/promotionalText/whatsNew` 및 `AppInfoLocalization.name/subtitle`은 **`maxLength` 제약이 없는 plain `string`** 이다. → **글자 수 제한은 API 스펙이 아니라 ASC Help에서만 인용해야 한다.**

---

### 4. Apple Developer 문서 스타일 / WWDC 글쓰기 세션

#### 핵심 결론(공식 확인): 공개된 “Apple Developer Documentation Style Guide”는 **존재하지 않는다**

`curl`로 직접 프로브한 부정 결과:

| 프로브한 URL | 결과 |
| --- | --- |
| `https://developer.apple.com/documentation/style-guide` | **404** |
| `https://developer.apple.com/documentation/documentation-style-guide` | **404** |
| `https://developer.apple.com/documentation/xcode/style-guide` | **404** |
| `https://developer.apple.com/documentation/docc/style-guide` | 200이지만 `https://www.swift.org/documentation/docc/`로 리다이렉트(소프트 404) |
| GitHub `org:apple` 검색: `documentation style`, `style guide`, `style guide in:name` | 세 쿼리 모두 `total_count: 0` |

대신 실제로 존재하는 Apple 공식 문서 스타일 소스는 4가지다:
1. **Apple Style Guide** — “About the guide”가 **개발자에게 user-facing text에 이 가이드를 따르라고 명시**한다.
2. **DocC 저작 문서** — `developer.apple.com/documentation/xcode/...` 및 swift.org 미러.
3. **Swift API Design Guidelines** (swift.org, Apple 저작).
4. **WWDC 세션 transcript** — 실질적인 writing-craft 규칙은 대부분 여기에 있다.

> **재사용 가능한 라우트 발견:** Apple Developer 문서 페이지는 DocC JS 렌더링이지만 두 개의 깨끗한 엔드포인트가 plain `curl`로 동작한다:
> - `https://developer.apple.com/documentation/<path>.md` → `text/markdown`
> - `https://developer.apple.com/tutorials/data/documentation/<path>.json` → DocC 원본 JSON
>
> WWDC 세션 페이지(`https://developer.apple.com/videos/play/wwdcYYYY/NNNN/`)는 **정적 HTML에 전체 transcript가 들어 있다** — `curl`로 충분.

#### Swift API Design Guidelines (Apple 저작, swift.org 호스팅)
**URL:** https://www.swift.org/documentation/api-design-guidelines/ · **페치:** `curl --compressed` 200, ~28.6 KB
**성격:** 공식(Apple 저작, Swift 프로젝트 문서). *Apple Developer Documentation 페이지가 아님을 명확히 표기.*

> “**Clarity at the point of use** is your most important goal. Entities such as methods and properties are declared only once but used repeatedly.”

> “**Clarity is more important than brevity.** Although Swift code can be compact, it is a non-goal to enable the smallest possible code with the fewest characters.”

> “Write a documentation comment for every declaration. Insights gained by writing documentation can have a profound impact on your design, so don’t put it off.”

> “If you are having trouble describing your API’s functionality in simple terms, you may have designed the wrong API.”

> “**Focus on the summary; it’s the most important part.** Many excellent documentation comments consist of nothing more than a great summary.”

> “Use a single sentence fragment if possible, ending with a period. Do not use a complete sentence.”

> “**Omit needless words.** Every word in a name should convey salient information at the use site.”

> “**Avoid obscure terms if a more common word conveys meaning just as well.** Don’t say 'epidermis' if 'skin' will serve your purpose.”

> “**Avoid abbreviations.** Abbreviations, especially non-standard ones, are effectively terms-of-art…”

#### DocC — Writing symbol documentation in your source files
**URL:** https://www.swift.org/documentation/docc/writing-symbol-documentation-in-your-source-files (Apple 미러: https://developer.apple.com/documentation/xcode/writing-symbol-documentation-in-your-source-files.md) · **페치:** swift.org는 `jina`, developer.apple.com은 `.md` 엔드포인트 `curl` 200.
**성격:** 공식(Apple 저작).
*(주의: `.../writing-symbol-documentation` 슬러그는 소프트 404 — 전체 슬러그를 써야 한다.)*

> “A common characteristic of a well-crafted API is that it’s easy to read and practically self-documenting.”

> “The first step toward writing great documentation is to add single-sentence abstracts or summaries”

> “A summary describes a symbol and augments its name with additional details. **Try to keep summaries short and precise; use a single sentence or sentence fragment that’s ideally 150 characters or fewer.** Use plain text, and avoid including links, technical terms, or other symbol names.”

> “For a property, explain how it affects the behavior of its parent. Describe typical usage and any permitted or default values.”

> “Describe each parameter in isolation. Discuss its purpose and, where necessary, the range of acceptable values.”

#### DocC — Adding structure to your documentation pages
**URL:** https://www.swift.org/documentation/docc/adding-structure-to-your-documentation-pages (Apple 미러: https://developer.apple.com/documentation/xcode/adding-structure-to-your-documentation-pages.md) · **페치:** `jina` / `curl` 200

> “A landing page provides an overview of your framework, introduces important terms, and organizes the resources within your documentation catalog”

> “The landing page is an opportunity for you to ease the reader’s learning path, discuss key features of your technology, and offer motivation for the reader to return to when they need it.”

> “**Try to keep the Overview brief — typically less than a screen’s worth of content. Avoid detailing every feature in your framework.** Instead, provide content that helps the reader understand what problems the framework solves.”

> “Use group names that are unique, mutually exclusive, and clear.”

#### WWDC22 10037 — “Writing for interfaces” (UI 카피 최고의 1차 소스)
**URL:** https://developer.apple.com/videos/play/wwdc2022/10037/ · **페치:** `curl` 200, 157 KB — **transcript가 정적 HTML에 포함**. JS/Jina 불필요.
**성격:** 공식 1차(Apple이 공개한 세션 전문). 발표자: Kaely Coon, Jennifer Bush (Apple Human Interface design teams의 writer).

> “it’s our job to **design through the lens of language**.”

> “the earlier you make writing a part of the process of designing your app, the better the experience will be for the people who use it.”

> “These are: **Purpose, Anticipation, Context, and Empathy.**” / “You’ll notice we’ve given you an acronym of **'PACE'**”

> “**Know what to leave out.** Rather than give too many details, aim for simplicity. You can tell people the purpose of a screen; it’s not a secret!”

> “**Develop your app’s voice first, and then you can vary its tone.** Start by asking yourself: what would it say and not say?”

> “The tone is quite celebratory, so it has an exclamation point. **Be careful how often you use those, though. They can look silly when they’re frequent.**”

> “When writing for alerts, it’s always best to be specific about the action the buttons are going to take. On this alert, **if you only read the button labels, you would still understand what you were choosing.**”

> “**interjections like 'oops!' or 'uh-oh' can sound patronizing, and 'please' and 'sorry' can sound insincere. Use them sparingly.**”

> “It’s best to use simple, plain language, as idioms and humor can be misunderstood or not translate, and some phrases have meanings that exclude people.”

> “**read your writing out loud.** It can really help make sure your writing sounds conversational, like how you’d talk to a friend. Reading out loud can also help you find unnecessary or repetitive words, grammatical mistakes, or typos.”

#### WWDC25 404 — “Make a big impact with small writing changes” (가장 최신·구체적)
**URL:** https://developer.apple.com/videos/play/wwdc2025/404/ · **페치:** `curl` 200 (정적 HTML transcript). 발표자: Liv Huntley, Jennifer Bush (Apple UX Writers). 4가지: remove fillers / avoid repetition / lead with the why / make a word list.

> “when we’re asked about how to improve the writing in apps, the advice we give most often is to **simplify**.”

> “A common misconception in UX writing is that we need to fill all the empty space.” / “**Fortunately, your app doesn’t have a minimum word count. In fact, usually the opposite is true and it’s best to remove words.**”

> (on “Simply enter your license plate number to quickly pay for parking.”) “If I remove the words 'simply' and 'quickly' from this message… I haven’t lost any clarity, and I don’t make assumptions about the context of the person using it.”

> “While it might seem like these words make your app feel more personal, it’s best to remove them when they don’t add any meaning to the message.”

> “Words like ”uh oh,“ ”oops“ or ”oh no!“ in error messages can make it sound like you’re not taking the problem seriously.”

> “Try to avoid unnecessary punctuation disguised as a kind of filler.”

> “**UX writing is all about economy of language. Resist the urge to fill all available space with repeated information.**”

> “Messaging is most effective when you tell the people using your app **why** taking that next step will be fun, or interesting, or beneficial to them.” / “if you’re leaving the benefit for the end of the sentence, try moving it to the front.”

> “Using the same button name for the same action, in this case, moving to the next screen, helps build trust through consistency. **Button labels are a great thing to add to your word list.**”

> “If you’re not sure what to use for some of the terms in your app, **the Apple Style Guide, available to anyone, is a good place to start.**”

> “Read your writing out loud. It makes it easier to hear those filler and repetitive words and know where to tighten up your writing.”

#### WWDC24 10140 — “Add personality to your app through UX writing” (voice vs tone 정의)
**URL:** https://developer.apple.com/videos/play/wwdc2024/10140/ · **페치:** `curl` 200

> “You can think of **voice** as the expression of your brand and values through words. It’s the things about your writing that tend not to change.”

> “**Clarity, simplicity, friendliness, and helpfulness.**” — Apple writer가 염두에 두는 4가지 (“I see these pretty consistently throughout Apple’s writing”)

> “You can think of **tone** as the way your voice adapts to the situation.”

> “Voice represents the consistent elements that are always there. The tone represents things that can and should change depending on the moment.”

> “even though we tend to use exclamation marks pretty sparingly around here, this screen gets one, because of the situation.”

> “Notice how there’s a little bit of tension here. **Simplicity and friendliness are just slightly at odds with each other.** If you’re adding an extra word here or there to create some friendliness, you’re taking away from the simplicity and vice versa. **They balance each other out. That can help modulate tone.**”

#### WWDC21 10221 — “Streamline your localized strings” (번역자용 코멘트 규칙)
**URL:** https://developer.apple.com/videos/play/wwdc2021/10221/ · **페치:** `curl` 200

> “Think about all the strings in your app as movie subtitles. In the movie you watch, you want all subtitles to be in the right language, at the right time, with the right context, and consistent throughout the movie.”

> “Translators don’t have the full app UI in front of them while they translate string by string… So you need to help them, just like you help your coworkers understand your code by adding code comments.”

> “**I insist, no matter the string, you should always define a comment.**”

> “First, comments should explain **where the string is visible**. For instance, is this a button? A label? Some VoiceOver text? Knowing if this is an action -- to order -- or a statement -- an order -- is critical.”

> “Second, they should explain **the context**… Lastly, comments should explain **variables**.”

> “be careful not to overuse variables. **Gluing strings together is handy but could lead to translation problems.**”

#### WWDC22 10110 — “Build global apps: Localization by example”
**URL:** https://developer.apple.com/videos/play/wwdc2022/10110/ · **페치:** `curl` 200

> “Internationalization means preparing your app to run on devices all across the world. **When localization is done well, everybody gets to enjoy the same great experience and utility– regardless of the language they speak.**”

> “**Even though the English words are the same, when they appear in different contexts, other languages might use different words. You should use two strings in code in this case.**”

> “A great comment explains which interface element the string is shown in, like a label or a button. It also explains the context of the UI element and where it is shown on screen.” / “If the string contains variables, make sure to explain their value at runtime.”

> “Remember that translators might not see the app at runtime when translating your content.”

> “Joining strings might have surprising consequences in other languages: they might need to inflect the grammar or could have troubles with capitalization”

#### WWDC19 254 — “Writing Great Accessibility Labels”
**URL:** https://developer.apple.com/videos/play/wwdc2019/254/ · **페치:** `curl` 200

> “It’s a localized string that **succinctly identifies** the accessibility element.”

> “VoiceOver knows what the element in your apps is based on the element type. So, **it’s redundant to add text to your string like button or tab.**”

> “When there’s multiple buttons with the same action like adding an item to the cart, **remember to provide the context.**”

> “**Avoid redundant labels.**” / “Remember, we want these labels to be as succinct as possible.”

#### WWDC21 10275 / WWDC25 316 / WWDC22 10034 — 포용적 디자인 · RTL
**URL:** https://developer.apple.com/videos/play/wwdc2021/10275/ · https://developer.apple.com/videos/play/wwdc2025/316/ · https://developer.apple.com/videos/play/wwdc2022/10034/ · **페치:** `curl` 200

> (10034, Design for Arabic) “Titles, buttons, and the Navigation bar should change order and position. Paragraphs should be always aligned to the right. Carousals and swipeable elements should also flow from right to left.”

> (10034) “it is always important to make sure that your app is **culturally relevant**.”

#### Apple Style Guide — Intro to international style (번역 친화 문체 규칙)
**URL:** https://support.apple.com/guide/applestyleguide/intro-to-international-style-apsg1ff68ab5/web · **페치:** `curl` 200 (정적 HTML)

> “Following international style helps readers with limited English proficiency read what you write. **By following international style, you also help translators—human or machine—localize your writing by minimizing the burdens of cultural and customary language usage.**”

> “These are the basic rules: **Write in simple structures.** / **Don’t use idiomatic or colloquial expressions.** / **Avoid shortcuts, symbols, and abbreviations that could easily be spelled out.** / **Express data using the standard international conventions outlined in this chapter.**”

---

### 5. Apple 마케팅 카피 — 관찰 가능한 하우스 컨벤션

**성격:** 공식 1차(Apple 자사 페이지를 관찰·인용). 페이지 자체가 “규칙”을 선언하지는 않으므로 **관찰된 컨벤션**으로 표기한다.
**페치:** apple.com 정적 페이지 전부 `curl` + Safari UA 200. `/newsroom/` **인덱스만** JS 렌더 → `jina` 필요.

#### 히어로 = 제품명(명사구) + 짧은 단편 태그라인, **문장이 아니어도 마침표로 끝난다**

https://www.apple.com/ 에서 그대로:

| 제품명 | 태그라인 (verbatim) | CTA |
| --- | --- | --- |
| `iPhone 18 Pro` | `Pro further.` | `Learn more` / `Buy` |
| `iPhone Duo` | `Hello, hello.` | `Learn more` / `View pricing` |
| `Apple Watch Series 12` | `The most accurate heart rate sensing in a wearable. 1` | `Learn more` / `Buy` |
| `Apple Watch Ultra 4` | `A battery you can’t outrun.` | `Learn more` / `Buy` |
| `Mac mini` | `Now with M6 and M5 Pro.` | `Learn more` / `Buy` |
| `Apple Upgrade` | `Love it. Lease it. Upgrade it. 2` | `Learn more` |

- 두 단어 단편에도 마침표: `Pro further.`
- **스타카토 3연타**: `Love it. Lease it. Upgrade it.` (각 단편이 각자의 마침표를 가짐)
- 추가 예: `/mac/` `Thin. Fast. Powerful and portable.` · `/airpods/` `Listening. Remastered.` · `/mac/` `The magic of Mac at a surprising price.`
- `iOS로 이동`/타이포그래피: 아포스트로피는 **U+2019**(`can’t`, `world’s`) — `/iphone/`에 56회. 엠대시는 **U+2014 + 양쪽 공백**(22회): `Little spill? No biggie — iPhone stands up to splashes…`

#### CTA 정확한 문자열

`Learn more`(압도적 다수) · `Buy` · `View pricing` · `Apply now` · `Compare` · `Compare all models` · `Compare AirPods models` · `Shop iPhone`/`Shop Mac`/`Shop Watch` · `Book a demo`(`/vision/`, `Buy`보다 앞) · `View in AR` · `View in your space` · `Stream now`/`Watch now`/`Listen now`/`Play now` · `Download the Apple Store app` · `Start a repair`

**규칙: CTA는 마침표 없음. 같은 자리의 섹션 제목은 마침표 있음.**
- CTA: `Learn more`, `Buy`, `Apply now` (period 없음)
- 제목: `Explore the lineup.` / `Get to know Mac.` / `Switch to Mac.` / `Take a closer look.` / `Why Apple is the best place to shop iPhone.`

#### 대소문자

- **히어로·태그라인·섹션 제목 = sentence case.** `Innovative and durable.` / `Eye-opening control.` / `Make movies like the movies.` / `Planet-worthy packaging.` / `On track to carbon neutral.`
- **네비게이션·푸터 링크 레이블 = title case.** `Manage Your Apple Account` / `Find a Store` / `Certified Refurbished` / `Carrier Deals at Apple` / `Order Status` / `Career Opportunities` / `Sales and Refunds` / `Site Map`
- **제품 페이지 아이브로우 칩 = title case.** `Cutting-Edge Cameras` / `Chip and Battery Life` / `Peace of Mind` / `Delivery and Pickup` / `Guided Shopping` / `Ways to Buy` / `Personal Setup` / `Designed to Last`
- **ALL-CAPS는 마케팅 카피에 사실상 없음** (PR 푸터의 `PRESS RELEASE`, 법적 문서의 `TABLE OF CONTENTS` 정도)

#### 각주 체계 (footnote system)

- 마커 글리프: 위첨자 숫자 `1`–`14`; 별표 사다리 `*` `**` `***`; `§` (Apple Upgrade 리스); `†` (AirPods); 다이아몬드 사다리 `◊` `◊◊` `◊◊◊` `◊◊◊◊`; **델타 사다리** `Δ` `ΔΔ` `ΔΔΔ` `ΔΔΔΔ` (`/airpods/`)
- 블록은 DOM 랜드마크 **`Apple Footer`**로 시작. 각 노트는 마커 + 공백 + **하나의 긴 문단**.
- `**` 트레이드인 노트 verbatim (https://www.apple.com/iphone/):
  > `** Trade‑in values will vary based on the condition, year, and configuration of your eligible trade‑in device. Not all devices are eligible for credit. You must be at least the age of majority to be eligible to trade in for credit or for an Apple Gift Card. … Apple or its trade‑in partners reserve the right to refuse, cancel, or limit quantity of any trade‑in transaction for any reason. … Restrictions and limitations may apply.`
  - 주의: `trade‑in`은 **U+2011 NON-BREAKING HYPHEN**, 같은 노트 안의 `Apple′s`는 **U+2032 PRIME** — 실제 소스에 남아 있는 오류.
- 마무리 상투구(모든 페이지 공통): `Features are subject to change. Some features, applications, and services may not be available in all regions or all languages.`
- 테스트 고지 공식: `Testing conducted by Apple in <Month Year> using preproduction <product> units and software, …` + `actual results may vary`
- 스타일: deontic modal 누적(`may`, `must`, `will`, `requires`), `you`/`your` 일관, 세미콜론으로 예외 나열, 마지막에 hedge 한 문장(`Restrictions and limitations may apply.` / `Terms apply.`)

#### 스펙·단위 표기

`7.6-inch inner display`(하이픈, 소문자) · `up to 45 hours of video playback` · `48MP Fusion Main camera` · `3000 nits` · `4K 120 fps` · `0% APR` · `3% Daily Cash back` · 산문에서는 percent를 풀어씀: `100 percent recycled cobalt`

#### Apple Newsroom 보도자료 하우스 스타일
**URL:** https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/ (`curl` 200)

순서 그대로: `PRESS RELEASE`(all caps 아이브로우) → `September 9, 2026` → 헤드라인 `Apple unveils iPhone Duo`(sentence case, 마침표 없음) → **deck(마침표 없음)** → `CUPERTINO, CALIFORNIA`(all caps 데이트라인) → 본문.

> (deck) “iPhone Duo features a breakthrough foldable design that’s beautiful, versatile, and durable, opening up possibilities that feel entirely new yet remarkably familiar”

> (리드) “**Apple today introduced** iPhone Duo, the first foldable iPhone. Opened, it is the thinnest iPhone ever, with a 7.6-inch inner display… Closed, the 5.4-inch outer display delivers 90 percent of the screen area of iPhone 18 Pro in a compact, pocketable design.”

- **평행 대조 구문**(`Opened, it is… Closed, the…`)과 엠대시 색상 목록이 특징적.
- **임원 인용 형식 — 귀속 동사는 항상 `said`, 두 인용문 *사이*에 온다:**
  > `"iPhone Duo is the most transformational change to iPhone since the original. …," said John Ternus, Apple’s CEO. "With the largest display ever on iPhone that still fits easily in your pocket, …"`
- 섹션 소제목은 **title case, 마침표 없음**: `Two Displays, One Breakthrough Design` / `Designed for Durability` / `An Advanced Camera System with New Experiences`
- **`About Apple` 보일러플레이트**(모든 릴리스 동일):
  > `Apple revolutionized personal technology with the introduction of the Macintosh in 1984. Today, Apple leads the world in innovation with iPhone, iPad, Mac, AirPods, Apple Watch, and Apple Vision Pro. Apple’s six software platforms — iOS, iPadOS, macOS, watchOS, visionOS, and tvOS — provide seamless experiences across all Apple devices and empower people with breakthrough services including the App Store, Apple Music, Apple Pay, iCloud, and Apple TV. Apple’s more than 150,000 employees are dedicated to making the best products on earth and to leaving the world better than we found it.`
- `Press Contacts` 블록 + 이름/이메일 나열로 끝남.

#### Apple Support 문서 하우스 스타일
**URL:** https://support.apple.com/en-us/118575 (`curl` 200, 본문 확인)

- **제목 = sentence case 과제 명사구, 마침표 없음, `your` 포함**: `Update your iPhone or iPad`
  - 고전적 변형은 조건문 형태: `If your <device> won’t <do X>` — 과제가 아니라 **사용자의 증상**을 제목으로 삼는다.
- **한 문장 dek**: `Learn how to update your iPhone or iPad to the latest version of iOS or iPadOS.`
- 이어서 `You can …` 요약문: `You can update your iPhone or iPad to the latest version of iOS or iPadOS wirelessly.`
- **단계문 = 날것의 명령형, 한 줄에 한 동작, 각각 마침표로 끝남**: `Back up your device using iCloud or your computer.` / `Plug your device into power and connect to the internet with Wi-Fi.` / `Open Settings.` / `Tap General.` / `Tap Software Update. The currently installed version of iOS is shown, and whether an update is available.`
- UI 요소 이름은 DOM에서 bold.
- **피드백 마이크로카피**: `Need more help?` / `Tell us more about what’s happening, and we’ll suggest what you can do next.` / `Get suggestions` / `Helpful?` `Yes` `No` / `Character limit: 250` / `Maximum character limit is 250.` / `Please don’t include any personal information in your comment.` / `Submit` / `Thanks for your feedback.`
- Support 홈 히어로: `Need help? Start here.`
- ⚠️ **`Related articles` / `See also` 문자열은 실제로 확인하지 못했다** — 교차 참조는 단계 산문 안의 인라인 링크(`learn how to update your device`) + 마지막 `Need more help?` 블록으로 처리된다. 이 문자열을 인용하지 말 것.

#### Legal / 약관 마이크로카피
**URL:** https://www.apple.com/legal/internet-services/itunes/ · https://www.apple.com/legal/privacy/en-ww/ (둘 다 `curl` 200)

> `These terms and conditions create a contract between you and Apple (the "Agreement"). Please read the Agreement carefully.`

- **Apple은 1인칭 복수 `we/our`, 독자는 `you/your`**, 축약형 유지: `We encourage you to back up your Content regularly.` / `All Transactions are final. Content prices may change at any time.`
- 정의된 용어는 curly quote로 도입: `…set forth in this section ("Usage Rules").`
- 프라이버시 정책의 시그니처 문장:
  > `At Apple, we believe strongly in fundamental privacy rights — and that those fundamental rights should not differ depending on where you live in the world.`
  → **“we believe…” + 엠대시 재진술** 구조가 Apple 목소리의 핵심 패턴.

---

### 6. Apple 현지화 — 한국어(ko-KR) / 일본어(ja-JP)

**성격:** 공식 1차(Apple이 직접 현지화한 페이지를 관찰·대조). **모든 인용은 실제 fetch 성공 페이지에서 나온 문자열.**

#### 핵심 결론: **번역이 아니라 “레지스터 전환형 트랜스크리에이션(transcreation)”**

문장의 **모양과 길이**는 영어 원문을 거의 그대로 보존하되, **경어 레벨·대명사 체계·단위 체계·줄바꿈 조판은 로케일별로 다시 결정**된다. 그리고 한국어와 일본어가 서로 **정반대로** 갈린다.

#### 6-1. 히어로/태그라인 — 트랜스크리에이션 증거

| English (apple.com) | Korean (/kr/) | Japanese (/jp/) |
| --- | --- | --- |
| `Pro further.` | `Pro, 더 앞으로.` | `プロの彼方へ。` |
| `Hello, hello.` | `반가워요, 반가워요.` | `ハロー ハロー。` |
| `A battery you can’t outrun.` | `당신보다 오래 달리는 배터리.` | `突き抜ける。このスタミナで。` |
| `Now with M6 and M5 Pro.` | `이제 M6 또는 M5 Pro 탑재.` | `M6またはM5 Proを搭載。` |
| `The most accurate heart rate sensing in a wearable.` | `웨어러블 기기 사상 가장 정확한 심박수 측정 기능.` | `ウェアラブルデバイス史上、最も高い精度を発揮する心拍数センサー` |
| `Switching from Android to iPhone is simple.` | `Android에서 iPhone으로 갈아타기, 정말 간단합니다.` | `AndroidからiPhoneへ。乗り換えは簡単です。` |
| `Your data. Just where you want it.` | `당신의 데이터를 당신이 원하는 곳에서만.` | — |
| `Little spill? No biggie — …` | `게다가 조금 젖는 것쯤은 크게 걱정 안 해도 되죠.` | — |

- `Pro further.` → 한국어는 **쉼표를 삽입**해(`Pro, 더 앞으로.`) 말장난을 살렸고, 일본어는 “프로의 저편으로”로 **재창작**했다.
- `Hello, hello.` → 한국어 `반가워요, 반가워요.`(**해요체 인사**), 일본어 `ハロー ハロー。`(**가타카나 음차** — 일본어가 트랜스크리에이션하지 *않은* 드문 예).
- **태그라인의 마침표는 세 로케일 모두 유지된다**: KR `.`, JP `。`. → **“Apple 태그라인에는 마침표를 쓰지 않는다”는 통념은 거짓이다.**

#### 6-2. CTA 대조

| English | Korean | Japanese |
| --- | --- | --- |
| `Learn more` | `더 알아보기` | `さらに詳しく` |
| `Buy` | `구입하기` | `購入` |
| `View pricing` | `가격 보기` | `価格を見る` |
| `Compare all models` | `모든 모델 비교하기` | `全モデルを比較する` |
| `Explore the lineup.` | `라인업 살펴보기.` | `すべてのモデルを見る` |
| `Switch to iPhone.` | `iPhone으로 갈아타기.` | `iPhoneへ乗り換えよう。` |
| `Getting Started` | `시작하기` | `スムーズなスタート` |

**패턴:** 한국어 CTA는 **`-하기` 명사화**(`구입하기`, `더 알아보기`, `비교하기`, `쇼핑하기`, `갈아타기`, `살펴보기`) — 어느 경어 레벨도 아니어서 결코 무례해지지 않는다. 일본어 CTA는 **사전형/의지형**(`比較する`, `見る`, `乗り換えよう`)이나 상업 버튼은 한자 명사 `購入`. **한국어는 마침표를 유지**(`라인업 살펴보기.`), **일본어는 탈락**(`すべてのモデルを見る`).

#### 6-3. 경어 레벨 — 한국어는 **콘텐츠 유형별로 레지스터가 갈린다** (카운트 근거)

| 콘텐츠 유형 | 한국어 레지스터 | 증거(해당 페이지에서 패턴 카운트) |
| --- | --- | --- |
| 마케팅 (`/kr/iphone/`) | 합니다체 + 해요체, **`당신` 명시** | `당신` 46, `합니다` 41, `습니다` 92, `하십시오` 11, `하세요` 10, `한다` 0 |
| 지원 문서 (`ko-kr/118575`) | 합니다체 + 하십시오체, **`당신` 없음** | `당신` 0, `합니다` 13, `습니다` 10, `하십시오` 1 |
| 보도자료 (`/kr/newsroom/…`) | **한다체(평서/plain)**, `사용자` | `당신` 0, `합니다` 2, `습니다` 0, **`한다` 73**, `했다` 6, `사용자` 75 |

- **합니다체 본문**: `Apple 엔지니어들은 … 하드웨어와 소프트웨어를 함께 설계합니다.` / `기능은 변경될 수 있습니다. 일부 기능, 애플리케이션 및 서비스를 이용할 수 없는 국가나 언어도 있습니다.`
- **해요체 온기 레이어**(같은 문단 안에서 설명 절을 닫을 때): `…안전하게 옮길 수 있죠.` / `…공유할 수 있죠.` / `…지울 수도 있죠.`
- **`-답니다` 어미** — Apple 한국어 특유의 부드러운 단정 표지: `…당신의 창의성을 더욱더 폭넓게 펼칠 수 있답니다.` / `…선사한답니다.`
- **하십시오체는 법적 각주·지시문 전용**: `자세한 내용은 apple.com/HRAccuracy 를 참고하십시오.` / `할부 조건, 수수료, 청구액 등 승인 결과는 신용카드 발급사에 문의하십시오.` / 지원 문서 `250자 이내로 작성하십시오.`
- **대명사도 유형별로 다르다**: 마케팅 `당신` / 지원 `사용자`·생략 / 보도자료 `사용자`(75회) / 법무 `고객`·`여러분`(`여러분과 관련되어 있을 수 있는 모든 정보를…`)

**일본어는 마케팅·지원·보도자료 전부 です/ます体로 균일하다**:
`AndroidからiPhoneへ。乗り換えは簡単です。` / `…安全に移行できます。` / `…アップデートする方法をご説明します.`(겸양 `ご`) / `Appleは本日、初の折りたたみ式iPhone、iPhone Duoを発表しました。`

> **이 조사에서 가장 날카로운 KR↔JP 대비:** *동일한* 보도자료에서 일본어는 です/ます体를 쓰는데 한국어는 **한다체**로 떨어진다.
> - KR: `Apple은 오늘 세계 최초의 폴더블 iPhone인 iPhone Duo를 공개했다.` / `Apple은 1984년 Macintosh를 시작으로 개인 기술에 혁신을 이뤄왔다.`
> - JP: `Appleは本日、初の折りためるiPhone、iPhone Duoを発表しました。` / `Appleは1984年にMacintoshを登場させ、パーソナルテクノロジーに革命を起こしました。`
> - 한국어 PR은 법적 노트에서 **`-함` 명사형 종결**까지 쓴다(영어·일본어에 없는 레지스터): `테스트는 2026년 8월 Apple에서 … 진행함. … 기준으로 함. … 따라 다름.`

#### 6-4. 라틴 문자 유지 vs 현지화

- **제품·칩·플랫폼 이름은 전부 라틴 문자 유지**: `iPhone Duo`, `A20 Pro`, `Ceramic Shield`, `ProMotion`, `Touch ID`, `Super Retina XDR`, `visionOS`, `iOS`, `App Store`, `AirDrop`, `Pro`/`Max`/`Air`/`Ultra`
- **기능 이름은 선별적으로 현지화**: `Camera Control` → KR `'카메라 컨트롤'` / JP `カメラコントロール`; `Move to iOS` → KR `'iOS로 이동'` / JP `「iOSに移行」`; `Center Stage`는 KR에서 라틴 유지, JP에서는 `センターフレーム`
- **시장 대체(market substitution)**: `…apps such as WhatsApp and WeChat.` → KR `WhatsApp, 카카오톡처럼 그동안 즐겨 쓰던 채팅 앱…` — **WeChat 자리에 카카오톡**.
- **UI 이름 인용 부호가 로케일마다 다르다**: 한국어 `' '`, 일본어 `「 」`, 영어는 부호 없음(`Open Settings.` → KR `'설정’을 엽니다.`)

#### 6-5. 조판 (바이트 단위 검증)

- 한국어 PR의 **따옴표 결함(재현 가능)**: 두 부분 임원 인용에서 두 쪽 모두 U+201C로 열지만 **첫 번째는 ASCII 직선 `"`로 닫는다**. 카운트 `“`=4, `”`=2. 같은 릴리스의 일본어는 `「`=8, `」`=8로 깨끗하다.
- 일본어 페이지의 **보이지 않는 개행 제어**: `/jp/mac/`에 U+2060 WORD JOINER **397개**(거의 모든 일본어 문자 사이), U+200B 20, U+200D 67, U+FEFF 158 — 영어 `/mac/`은 U+2060 186, 나머지 0, `/iphone/`·`/kr/iphone/`·`/jp/iphone/`은 0. `/jp/iphone/`은 대신 `<wbr>` 78개 + NBSP 210개(`お近くのApple\xa0Storeでは、`, `最新のiPhone\xa018 Pro\xa0Maxを`)로 라틴↔일본어 경계를 묶는다. **페이지별 처방이지 전역 규칙이 아니다.**
- 일본어 날짜: 아이브로우는 띄어 쓴 `2026 年 9 月 9 日`, 본문은 `9月14日（月）`(전각 요일).

#### 6-6. 길이 — 현지화 카피는 **더 짧아진다**

| English | chars | Korean | chars | Japanese | chars |
| --- | --- | --- | --- | --- | --- |
| `Learn more` | 10 | `더 알아보기` | 6 | `さらに詳しく` | 6 |
| `Compare all models` | 18 | `모든 모델 비교하기` | 10 | `全モデルを比較する` | 9 |
| `Explore the lineup.` | 19 | `라인업 살펴보기.` | 9 | `すべてのモデルを見る` | 10 |
| `Getting Started` | 15 | `시작하기` | 4 | `スムーズなスタート` | 10 |
| `The most accurate heart rate sensing in a wearable.` | 51 | `웨어러블 기기 사상 가장 정확한 심박수 측정 기능.` | 27 | `ウェアラブルデバイス史上、…センサー` | 33 |
| `A battery you can’t outrun.` | 25 | `당신보다 오래 달리는 배터리.` | 15 | `突き抜ける。このスタミナで。` | 14 |
| `Features are subject to change. Some features, applications, and services may not be available in all regions or all languages.` | 141 | `기능은 변경될 수 있습니다. 일부 기능, 애플리케이션 및 서비스를 이용할 수 없는 국가나 언어도 있습니다.` | 62 | — | — |

→ **규칙: 한국어 약 50–65%, 일본어 약 55–70% 수준으로 줄어든다.** 정중한 문장은 덜 압축되지만 세로 공간은 더 차지한다.

#### 6-7. 단위·로케일 데이터 — **같은 보도자료에서 KR과 JP가 정반대로 간다**

| English | Korean | Japanese |
| --- | --- | --- |
| `7.6-inch inner display` | `19.3cm 내부 디스플레이` (**미터법 환산**) | `7.6インチのインナーディスプレイ` (**인치 유지**) |
| `5.4-inch outer display` | `13.6cm` (**환산**) | `5.4インチ` (**유지**) |
| `5:00 a.m. PT` | `오후 9시` (시간대 변환) | `午後9時` (시간대 변환) |
| executive name | `존 터너스(John Ternus)` (라틴 병기) | `ジョン・ターナス` (가타카나만) |
| percent | — | `90パーセント` (가나로 풀어씀) |

#### 6-8. 현지화되지 *않는* 것 / 시장별 차이
- `Stream now`는 `/kr/`와 `/jp/` 캐러셀 모두에서 영어 그대로 남는다.
- 상품 구성은 1:1 미러가 아니다: Apple Card·Apple Upgrade는 `/kr/`에 없고, MacBook Pro는 `/kr/`에는 있지만 `/`에는 없다.
- 일본어 법적 푸터에만 있는 항목: 중고상 면허번호(`古物商許可証番号：…`), Paidy 할부 조건, 별도 보일러플레이트(`iPhone商標は、アイホン株式会社のライセンスにもとづき使用されています。`).
- 한국어 `/iphone/`은 영어(`§ * ** ◊`)와 **다른 각주 마커 사다리**(`* ** ***`)를 쓴다.

#### 6-9. Apple의 한국어 HIG (자기 자신을 현지화한 메타 증거)
**URL:** https://developer.apple.com/kr/design/human-interface-guidelines/writing · **페치:** `jina` 200, 14,881 bytes

- 영어 `Determine your app’s voice.` → 한국어 `앱의 보이스를 결정하십시오.` — **HIG 지침문 자체가 합쇼체**.
- 영어 `Be clear.` → `명확하게 표현하십시오.`
- 영어 `"Send" often works better than "Let’s do it!"` → `'보내기' 대신에 '진행하세요!'를 사용하는 것이 더 효과적일 때가 많습니다.`
- 영어 `Learn more about UX Writing` → `UX 글쓰기에 대해 자세히 알아보기`
- **`보이스`·`톤`을 음차로 유지**하고, UI 문자열은 단일 인용부호 `' '`로 감싼다.
- 일본어판(https://developer.apple.com/jp/design/human-interface-guidelines/writing, `jina` 200, 16,152 bytes): 전부 **です/ます体** — `アプリに適したボイスを決める。` / `明確にする。` / `「やりましょう!」とするより、単に「送信」とした方が効果的です。`

→ **이것이 “Apple이 자기 지침을 현지화할 때 어떤 문체를 쓰는가”에 대한 가장 직접적인 1차 증거다: 한국어는 합쇼체, 일본어는 です/ます体, 두 언어 모두 문장 구조와 길이는 원문을 따른다.**

---

### 7. Marcom · 내부 톤오브보이스 · 유출/내부 문서 (증거 등급 분류)

이 절의 원칙: **모든 항목에 증거 등급을 명시한다.** 등급 정의:
- **PRIMARY**: Apple이 발행한 문서, 또는 원본 문서의 스캔/팩시밀리.
- **SECONDHAND**: 2차 자료(언론·책·위키)가 문서를 인용한 것 — 인용은 그 2차 자료에서 온 것임을 명시.
- **MYTH / DISPUTED**: 검증 가능한 1차 실물이 없거나, 널리 반복되지만 출처가 확인되지 않는 것.

#### 7-1. “Apple Style Guide” 자체가 Marcom의 존재를 인정한다 — PRIMARY, 검증됨

> “Some departments at Apple (**Marcom**, for example) have supplemental style guides.”
> — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (About the guide, p.5)

**→ 이것이 Marcom 서브 가이드에 대해 공개적으로 확인 가능한 유일한 Apple의 진술이다.**
**Marcom의 톤오브보이스 가이드 자체는 공개되어 있지 않다.** `Apple Marcom tone of voice`, `"Apple Marcom" style guide` 등의 검색으로는 공개 문서를 찾지 못했다. **“Marcom 톤오브보이스 가이드”를 1차 출처로 인용하지 말 것 — 존재가 확인되지 않는다.** 존재가 확인되는 것은 (i) 위 문장, (ii) Apple 공개 마케팅 카피 자체(§5)뿐이다.

#### 7-2. “The Apple Marketing Philosophy” (Dec. 1979) — **원본 스캔 확인 / 저자 귀속은 MYTH-DISPUTED**

**URL (아이템 페이지):** https://archive.org/details/102789075-05-01-acc
**URL (PDF 스캔):** https://archive.org/download/102789075-05-01-acc/102789075-05-01-acc.pdf
**URL (OCR 텍스트):** https://archive.org/download/102789075-05-01-acc/102789075-05-01-acc_djvu.txt
**페치:** `curl` 200 — item page 211,074 bytes, PDF 526,045 bytes(`application/pdf`, **10페이지**), OCR 텍스트 6,920 bytes.

**증거 등급 — 두 부분으로 나눠서 표기해야 한다:**

| 대상 | 등급 |
| --- | --- |
| **문서 자체** (1979년 Apple 내부 메모의 스캔) | **PRIMARY 팩시밀리** (단, 아래 Caveat 1) |
| **“Mike Markkula가 썼다”는 귀속** | **MYTH / DISPUTED — 1차 근거 없음** |
| **“1980년 1월 3일자”라는 날짜** | **오류 — 스캔 도장은 `ACH Dec. 79`** |
| **“3개 원칙 불릿 리스트”라는 통념** | **오류 — 실제로는 산문 한 페이지 전체** |

**Caveat 1 — 소장·출처:** `applemedia`는 **사용자 생성 컬렉션**(“A collection images, media and commercials related to Apple Computer and Apple Inc.”)이며 Apple이나 대학 아카이브가 운영하는 것이 아니다. `creator: Apple Inc.`는 **업로더가 입력한 메타데이터**이지 기관의 진본 인증이 아니다.

**Caveat 2 — 문서에 저자 이름이 없다.** 메모는 회사를 3인칭으로 서술하고(“Apple believes…”), **Markkula의 이름도 서명도 없다.** 따라서 Markkula 귀속은 이 팩시밀리로 입증되지 않는다.

**Stanford 아카이브 확인 실패:** Stanford “Making the Macintosh” 1차 문서 인덱스(`https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/index.html`)를 전수 열거한 결과 **Markkula 메모는 없다.** `primary/docs/marketing.html`, `philosophy.html`, `markkula.html`, `mktphil.html`, `applemkt.html`은 모두 404. Wikipedia의 Mike Markkula 문서에도 이 메모 언급이 **없다.**

**문서 실물 구성 (시각 검증):** 10-leaf 600 dpi 스캔(`scandata.xml`: `dpi 600`, `leafCount 10`).
- leaf 1 — 이름 없는 남성 흑백 **인물 사진**
- leaf 2·4·6·8 — `ROBERT A. ISAACS / 1646 MARY AVENUE / SUNNYVALE, CALIFORNIA` **봉투**
- **leaf 9·10 — 메모 자체가 2부** 실려 있음. 제목 `THE APPLE / MARKETING PHILOSOPHY`, 그 아래 `EMPATHY   FOCUS   IMPUTE`
- leaf 10 하단 도장: **`ACH Dec. 79`**

**핵심 문장 (스캔 페이지에서 옮긴 것 / OCR 정규화):**
> “We normally think of marketing in terms of forecasting, strategic and product planning, selling, advertising, merchandising and the like.”

> “The essence of Apple’s marketing philosophy is contained in just three words... **empathy, focus, and impute**.”

> **Empathy** — “Understanding so intimate that the feelings, thoughts, and motives of one are readily comprehended by another. **If we have empathy for our customers and dealers, we will truly understand their needs better than any other company.**”

> “Just 'being sensitive' is not enough to do an Apple marketing job.... it takes **intimate understanding of our customers, fellow employees, competitors, and our dealers**... empathy.”

> **Focus** — “A thorough and complete understanding of the marketplace always provides more opportunities than can or should be attacked. In order to do a good job of those things that we decide to do, **we must eliminate all of the unimportant opportunities, select from the remainder only those that we have the resources to do well, and concentrate our efforts on them.**”

> “This process requires that **we set priorities carefully, and that we discipline ourselves to religiously stick to our plans.**”

> **Impute** — “the process by which an impression of a product, company or person is formed by mentally transferring the characteristics of the communicating media to the product, company or person.”

> “**people DO judge a book by its cover, a company by its representatives, a product’s quality by the quality of its collateral materials** etc.”

> “The general impression of Apple Computer Inc. (our image) is the combined result of **everything the customer sees, hears or feels from Apple, not necessarily what Apple actually is!** … **if we present them in a slipshod manner, they will be perceived as slipshod; if we present them in a creative, professional manner, we will impute the desired qualities.**”

**→ 이 스킬에 주는 의미:** “Impute” 원칙은 **카피 자체가 제품 품질의 증거로 읽힌다**는 Apple 특유의 전제를 1979년에 이미 명문화한 것이다. 문장 품질은 장식이 아니라 제품 주장의 일부다.
**→ 인용 시 문장:** “1979년 12월자 Apple 내부 문서 스캔(archive.org 커뮤니티 업로드). 저자 귀속은 확인되지 않음.”

#### 7-3. “Think Different” (1997) — 스크립트는 SECONDHAND, 브로셔 스캔은 PRIMARY

**(a) “Crazy Ones” TV 스크립트 — SECONDHAND, Apple 발행본 없음**
Apple은 이 스크립트를 Apple 저작 텍스트로 **한 번도 공개하지 않았다.** 캠페인은 **외부 에이전시 TBWA\Chiat\Day**가 만들었으므로, 이는 **Apple이 채택한 에이전시 카피**이지 Apple 내부 하우스 스타일의 예가 아니다.

가장 좋은 확보 가능 출처 — 스크립트를 쓴 TBWA\Chiat\Day 크리에이티브 디렉터 **Rob Siltanen**의 글:
**URL:** https://web.archive.org/web/2018/https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/ (`forbes.com` 직접은 **403**, Wayback 200 / 510,681 bytes)

> “I also found the original 'To the crazy ones' television script I presented to Jobs, as well as a plethora of rough drafts.”

> “…on Steve Jobs. In his book, **Isaacson incorrectly suggests Jobs created and wrote much of the 'To the crazy ones' launch commercial. To me, this is a case of revisionist history.**”

> “'To the crazy ones. Here’s to the misfits. The rebels. The troublemakers. The people who see the world differently.'”

> “'The people who are crazy enough to believe they can change the world are the ones who actually do.'”

**⚠️ “Steve Jobs가 Crazy Ones를 썼다”는 통념은 MYTH / DISPUTED다.** 스크립트 원작자로 인정받는 사람이 반박했고, Apple은 스크립트를 자사 저작물로 공개한 적이 없다.

**(b) “Think Different Booklet (1997)” — 이건 스캔이 아니다 (분류 정정)**
**URL:** https://archive.org/details/think-different-booklet-1997
**등급: SECONDHAND(전사본), 팩시밀리 아님.** 메타데이터는 `creator: Apple Inc.`, `date: 1997`이라 주장하지만, PDF 페이지를 렌더링해 보면 **깨끗한 현대 디지털 조판**(Garamond계 세리프, 순백 배경, 700×889 px)이며 **종이 질감·하프톤·스캔 노이즈·정렬 아티팩트가 전혀 없다** — 누군가 다시 타이핑한 것이다. 4페이지, 353,603 bytes.
**→ 이 아이템을 “1997년 Apple 부클릿의 팩시밀리”로 인용하지 말 것.** 텍스트 자체는 잘 알려진 캠페인 카피와 일치하므로 **전사본**으로만 사용 가능:
> “The round pegs in the square holes.” / “You can praise them, disagree with them, quote them, disbelieve them, glorify or vilify them.” / “About the only thing you can’t do is ignore them.” / “Because the people who are crazy enough to think they can change the world, are the ones who do.”

**(c) “Think Different Really Different Brochure” (1997) — 진짜 스캔, PRIMARY 팩시밀리 ✅**
**URL:** https://archive.org/details/19971110-really-different-brochure_202201 (PDF 1,983,371 bytes; `pypdf` 이미지 추출 + 시각 검증: 8페이지, 1200×1600 px, **인쇄 하프톤과 페이지 가장자리 그림자가 보이는 실제 스캔**)

이것이 **Think Different / Power Macintosh G3 시대 Apple 제품 마케팅 목소리의 가장 잘 검증된 실물**이다:
> “**Computer science meets rocket science**” (헤드라인)

> “**A very different chip.**” (킥커)

> “**Did someone say ”faster“?** The new Power Macintosh G3 computers, built upon the relentlessly fast, third-generation PowerPC G3 chip, offer nothing less than the biggest performance leap in Power Mac history.”

> “Only a few people in the world can explain ”backside cache.“ **But everyone will savor the speed boost it provides.**”

> “**Oh, and did we mention that the Mac G3’s are fast?**”

> “**Who are you and what do you want from us?**”

> “**(But no anchovies.)** You can configure your computer literally hundreds of different ways…”

**→ 1997년 마케팅 목소리의 관찰된 특징:** 수사적 질문으로 시작, 기술 용어를 농담으로 해체(“backside cache” → “everyone will savor the speed”), 괄호로 말풍선을 넣음, 그리고 **“fast”라는 한 단어 주장을 반복**한다. §5의 현재 컨벤션(짧은 선언 + 마침표)과 같은 계보다. 단, **현재 Apple 마케팅은 이보다 훨씬 절제되어 있다** — “Oh, and did we mention…” 같은 구어체는 현재 apple.com에서 찾을 수 없다.

#### 7-4. Steve Jobs / Tim Cook의 Apple 발행 공개 서한 — **PRIMARY**

**(a) “Thoughts on Flash” (2010년 4월)** — Apple이 `apple.com/hotnews/`에 직접 게시. 원 URL은 죽었고 아카이브로 확인.
**URL:** https://web.archive.org/web/20101231041029/http://www.apple.com/hotnews/thoughts-on-flash/ (`curl` 200, 18,694 bytes; 본문 10,370자; 서명 `Steve Jobs` / `April, 2010`)

> “Apple has a long relationship with Adobe. In fact, we met Adobe’s founders when they were in their proverbial garage.”

> “I wanted to jot down some of our thoughts on Adobe’s Flash products so that customers and critics may better understand why we do not allow Flash on iPhones, iPods and iPads. Adobe has characterized our decision as being primarily business driven – they say we want to protect our App Store – but **in reality it is based on technology issues.**”

> “First, there’s 'Open'.” / “**By almost any definition, Flash is a closed system.**”

> “Though the operating system for the iPhone, iPod and iPad is proprietary, **we strongly believe that all standards pertaining to the web should be open.**”

> “We know from painful experience that letting a third party layer of software come between the platform and the developer ultimately results in sub-standard apps and hinders the enhancement and progress of the platform.”

> “Our motivation is simple – we want to provide the most advanced and innovative platform to our developers, and we want them to stand directly on the shoulders of this platform and create the best apps the world has ever seen.”

> “Perhaps Adobe should focus more on creating great HTML5 tools for the future, and less on criticizing Apple for leaving the past behind.”

**(b) “Apple’s commitment to privacy” — Tim Cook 서한 (2014년 9월)** — Apple이 `apple.com/privacy/`에 게시.
**URL:** https://web.archive.org/web/20151231214053/http://www.apple.com/privacy/ (`curl` 200, 36,382 bytes)

> “**At Apple, your trust means everything to us.**”

> “A few years ago, users of Internet services began to realize that when an online service is free, **you’re not the customer. You’re the product.**”

> “**Our business model is very straightforward: We sell great products.**”

> “**We don’t ”monetize“ the information you store on your iPhone or in iCloud.**” … “**Plain and simple.**”

> “Finally, I want to be absolutely clear that we have never worked with any government agency from any country to create a backdoor in any of our products or services.”

**→ Apple 공개 서한의 산문 규칙 (두 문서에서 공통으로 관찰):**
1. **1인칭 복수 `we`/`our`를 Apple로 쓴다** — ASG의 “first person 금지”(§c 규칙 59)와 **정면 충돌**한다. 즉 그 금지는 *지침·UI·사용자 문서*에 적용되고, **경영진 서명 서한·보도자료·프라이버시 정책은 별도 레지스터**다.
2. **상대 주장 먼저 요약 → 반박.** `Adobe has characterized… / they say… / but in reality…`
3. **서수 표지(`First, there’s "Open".`)** 로 긴 글에 뼈대를 준다.
4. **한 줄 클로저.** (“Plain and simple.” / “Perhaps Adobe should focus more on…”)
5. **문단당 하나의 주장.** 짧은 선언 + 즉시 근거.

#### 7-4b. Stanford “Making the Macintosh” — Krause 미디어 메모 (1985) — **PRIMARY 아카이브**

**URL (Media Guidelines, 1985-04-09):** https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html
**URL (Inquiries from the Press, 1985-03-04):** https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause1.html
**페치:** `curl` 200 (두 URL 모두). 각 페이지에 provenance 표기: `Location: M1007, Apple Computer Inc. Papers, Series 9, Box 1, Folder 2.`
**→ 재사용 교훈:** `web.stanford.edu/dept/SUL/**library/mac/**`는 403이지만, **`web.stanford.edu/dept/SUL/**sites/mac/primary/docs/**`는 200으로 열린다.**

> “Apple is probably more accessible to the news media than any other personal computer company. Because of this, many of you may find yourselves being asked to participate in an interview.”

> “**1. There is no such thing as ”off the record.“** Reporters can easily disarm you by allowing you to think the ”interview“ is over and that you are now just holding a conversation. Be careful. Anything you say can and may be used.”

> “**2. If the subject you are discussing is sensitive or confusing, repeat your message in a slightly different way** to make sure the reporter understands. This will lessen your chances of having the information misconstrued.”

> “**3. Stick to the subject of the interview and don’t volunteer additional information** unless it seems important to the story the reporter is working on at that time.”

> (Inquiries from the Press) “we do operate under guidelines to ensure that **the company’s position on issues is accurately and consistently stated.**”

**→ 이 스킬에 주는 의미:** Apple의 “일관된 목소리” 요구는 1985년 사내 미디어 지침까지 거슬러 올라간다 — 즉 **개인의 표현이 아니라 회사의 단일한 메시지**라는 원칙이 40년 된 것이다.

#### 7-4c. Apple Business Conduct Policy (2026년 2월판) — **PRIMARY, Apple이 공개 게시**

**URL:** https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf (`curl` 200, `application/pdf`, 808,333 bytes, **20페이지**, “February 2026”)

> (Public Speaking and Press Inquiries) “All public or outside speaking engagements that relate to Apple’s products or services or reasonably anticipated products or services or public or outside speaking engagements where you could be construed as speaking on behalf of the company, **must be pre-approved by your manager and Corporate Communications.**”

> (Publishing Articles) “If you want to contribute an article or other type of submission to a publication or blog on a topic that relates to Apple’s current or reasonably anticipated products or services, or that could be seen as a conflict of interest, **you must first request approval from Corporate Communications.**”

> “**Accurate and honest business records are critical to meeting our legal, financial, and management obligations.**”

> “You should never endorse a product or service of another business or individual in your role as Apple employee, unless the endorsement has been approved by your Director and Corporate Communications.”

**→ 이 스킬에 주는 의미:** 이것이 **Apple이 실제로 공개한, 직원의 글쓰기·발언을 규율하는 유일한 1차 문서**다. 단 내용은 *문체*가 아니라 *승인 절차*에 관한 것이다. “Apple 직원용 writing 가이드”를 이 문서로 대체하지 말 것.

#### 7-5. Apple “Our Values” 성격의 현재 페이지 — **PRIMARY** (검증됨)
`https://www.apple.com/values/`는 **404**이며, `/our-values/`, `/apple-values/`도 **404**다 (Wayback에도 404 캡처 1건뿐). 대신 다음이 살아 있다(모두 `curl` 200):

**https://www.apple.com/privacy/** (257,411 bytes):
> “**Privacy. That’s Apple.**”
> “Privacy is a fundamental human right. It’s also one of our core values. Which is why we design our products and services to protect it. **That’s the kind of innovation we believe in.**”
> “Safari. A browser that’s actually private.”
> “Apple Intelligence. Great powers come with great privacy.”

**https://www.apple.com/environment/** (438,565 bytes):
> “**Our planet deserves our best thinking.**”
> “**Innovation is up. Emissions are down.**”
> “We’re closer than ever to Apple 2030: Our ambitious, science-based goal to become carbon neutral across our global footprint.”
> “**A comprehensive approach. From design to disassembly.**” — 이어서 `Design and source.` / `Make.` / `Package and ship.` / `Use.` / `Recover.` / `Carbon removal.` 로 **한 단어 + 마침표** 리듬을 만든다.

**https://www.apple.com/accessibility/** (287,332 bytes):
> “**Innovation that’s accessible by design.**”
> “The best technology is designed with everyone in mind. **That’s why our products and services have built-in features to help you create, connect, and do what you love, your way.**”

**https://www.apple.com/legal/privacy/en-ww/**:
> “**At Apple, we believe strongly in fundamental privacy rights — and that those fundamental rights should not differ depending on where you live in the world.**”

**→ 관찰된 “Apple 가치 페이지” 보이스 문법(§5와 일치):**
1. **짧은 선언 + 마침표**, 문장이 아니어도 마침표: `Privacy. That’s Apple.` / `Innovation is up. Emissions are down.`
2. **`we believe` 구문** — Apple이 가치를 말할 때의 유일한 1인칭 허용 레지스터. (지침문에서는 금지, 가치 선언에서는 필수.)
3. **`That’s why…` 로 가치 → 제품 연결**: “That’s why we design our products…”, “That’s why our products and services have built-in features…”
4. **`your way` / `you love` 로 끝맺어 독자에게 반납** — 추상적 가치를 2인칭 이득으로 착지시킨다.

#### 7-6. 공개되지 **않은** 것 (명시적 부정 결과)

| 항목 | 상태 |
| --- | --- |
| Apple **Marcom 톤오브보이스 / 스타일 가이드** | **공개본을 찾지 못함 — clean negative.** ASG가 “Marcom has supplemental style guides”라고 존재만 인정한다. archive.org `"Apple" AND "marcom"` 검색 4건 모두 무관. **1차 출처로 인용 불가. 온라인에 도는 “Apple Marcom 스타일 가이드” 텍스트는 팩시밀리가 제시되지 않는 한 위조/미검증으로 취급할 것** |
| Apple **직원용 writing 가이드** | 공개본 없음. 가장 가까운 실물은 **Business Conduct Policy**(§7-4c)이나, 내용은 문체가 아니라 **승인 절차**다 |
| **“Crazy Ones” 대본의 Apple 발행 1차 URL** | **없음 — clean negative.** 캠페인은 외부 에이전시(TBWA\Chiat\Day) 제작이므로 Apple 내부 하우스 스타일의 예가 아니다 |
| **“Steve Jobs가 Crazy Ones를 썼다”** | **MYTH / DISPUTED.** 원작자 Rob Siltanen이 Isaacson 전기를 “revisionist history”라 반박 |
| **“Markkula가 이 메모를 썼다”** | **MYTH / DISPUTED.** 스캔본에 서명·저자명이 없고 회사를 3인칭으로 서술. Stanford 아카이브에도 없음 |
| **“메모는 1980년 1월 3일자”** | **오류.** 도장은 `ACH Dec. 79` |
| **“메모는 3개 불릿 원칙 목록”** | **오류.** 실제로는 산문 한 페이지 전체. 유통되는 불릿 요약은 편집자의 압축 |
| **archive.org “Think Different Booklet (1997)”** | **팩시밀리 아님 — 전사본.** 렌더링 결과 현대 디지털 조판(스캔 노이즈·하프톤 없음). 팩시밀리로 인용 금지 |
| `apple.com/values/` · `/our-values/` · `/apple-values/` | **모두 404.** Wayback에도 404 캡처 1건뿐 |
| **Steve Jobs의 내부 메시징 메모(1997)** | 검증 가능한 1차 실물 확인 실패 |
| **“Thoughts on Music” (2007)** | 회수 가능한 Wayback 캡처 없음 → 미검증 |
| Apple USPTO 상표 specimen (serial 77882684) | JS 전용이라 판독 불가 → 미검증 |
| `web.stanford.edu/dept/SUL/library/mac/` | **403 봇 차단.** 단 `web.stanford.edu/dept/SUL/**sites**/mac/primary/docs/*.html`은 **200으로 열린다**(§7-4b에서 활용) |
| `apple.com/pr/library/1997/09/19970923think.html` | **404** (아카이브 캡처도 404) |
| WWDC Q&A 세션(예: 111484, 110540, 10334) | 세션 페이지는 200이지만 **transcript가 게시되지 않음** |

#### 7-7. 발견 경로(재사용용): archive.org `applemedia` 컬렉션

Markkula 메모를 찾은 경로는 archive.org 전체 텍스트 검색 API다. 같은 방식으로 **Apple 내부 문서 1,720건**이 `applemedia` 컬렉션에 커뮤니티 업로드로 존재한다.

**검색 API (동작 확인됨):**
```
https://archive.org/advancedsearch.php?q=collection%3Aapplemedia&fl[]=identifier&fl[]=title&fl[]=date&rows=100&output=json
https://archive.org/advancedsearch.php?q=%22Apple+Marketing+Philosophy%22&fl[]=identifier&fl[]=title&rows=10&output=json
```

**이 컬렉션에서 확인한 내부 문서(등급·상태 명시):**

| 아이템 | URL | 상태 |
| --- | --- | --- |
| Apple internal - **Apple Marketing Philosophy** (Dec. 1979) | https://archive.org/details/102789075-05-01-acc | **스캔 10 leaf, 600 dpi, OCR 있음** — §7-2에서 인용. 저자 귀속은 MYTH-DISPUTED |
| **Think Different Really Different Brochure** (1997) | https://archive.org/details/19971110-really-different-brochure_202201 | **진짜 스캔(8p, 1200×1600, 하프톤·페이지 그림자 확인) → PRIMARY 팩시밀리.** §7-3(c)에서 인용. **이 시대 Apple 제품 마케팅 목소리의 최선의 검증 실물** |
| ⚠️ **Think Different Booklet** (1997) | https://archive.org/details/think-different-booklet-1997 | **팩시밀리 아님 — 재타이핑 전사본**(렌더링 검증: 현대 디지털 조판, 스캔 흔적 없음). 메타데이터의 `creator: Apple Inc.`를 믿지 말 것 |
| Apple Internal - **Apple Retail Store Philosophy** (2011) | https://archive.org/details/11243 | **유출 내부 자료**(Apple 발행 아님). 2011 리테일 내부 영상, **metadata에 전체 transcript 포함**(4,612자), `Apple Retail-eng.asr.srt` 자막도 있음. 내용은 **매장 설계·경험**이며 **산문 스타일 규정이 아니다** — 카피 규칙 출처로 인용하지 말 것 |
| Apple Internal - **Leadership Palette** (concept paper) | https://archive.org/details/leadership-palette-concept-paper | 4페이지 **이미지 전용 PDF(텍스트 레이어 없음)**, 날짜 없음, `description = "a"`. **텍스트 추출 불가 → 내용 검증 불가.** 이 스킬의 출처로 쓰지 말 것 |

> ⚠️ **모든 `applemedia` 아이템은 커뮤니티 업로드**(uploader `archiveapple1976@gmail.com`)이며 기관 인증이 없다. 메타데이터에 `creator = Apple Inc.`로 적혀 있어도 **진본 인증이 아니다.** 인용 시 “archive.org 커뮤니티 업로드 스캔”이라고 명시할 것. **스캔이라고 주장하는 아이템은 반드시 PDF를 렌더링해 하프톤·종이 질감을 눈으로 확인한 뒤에만 팩시밀리로 분류할 것** — 위 Booklet 사례가 그 이유다.

#### 7-8. §7 증거 등급 최종 요약표

| # | 항목 | 등급 | URL |
| --- | --- | --- | --- |
| 1 | Apple Style Guide의 Marcom 언급 한 줄 | **PRIMARY** | https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (p.5) |
| 2 | “The Apple Marketing Philosophy” 문서 실물 (Dec. 1979) | **PRIMARY 팩시밀리** (커뮤니티 업로드, 진본 인증 없음) | https://archive.org/details/102789075-05-01-acc |
| 3 | 그 문서의 **Markkula 저자 귀속** | **MYTH / DISPUTED** | 1차 근거 없음 |
| 4 | “Crazy Ones” 대본 텍스트 | **SECONDHAND** (Siltanen/Forbes, Wayback) | https://web.archive.org/web/2018/https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/ |
| 5 | “Steve Jobs가 대본을 썼다” | **MYTH / DISPUTED** | 위 Siltanen이 반박 |
| 6 | Think Different Booklet (1997) | **SECONDHAND 전사본** (팩시밀리 아님) | https://archive.org/details/think-different-booklet-1997 |
| 7 | Think Different Really Different Brochure (1997) | **PRIMARY 팩시밀리** (실제 스캔) | https://archive.org/details/19971110-really-different-brochure_202201 |
| 8 | “Thoughts on Flash” (Jobs, 2010) | **PRIMARY** (Apple 게시, Wayback) | https://web.archive.org/web/20101231041029/http://www.apple.com/hotnews/thoughts-on-flash/ |
| 9 | “Apple’s commitment to privacy” (Cook, 2014) | **PRIMARY** (Apple 게시, Wayback) | https://web.archive.org/web/20151231214053/http://www.apple.com/privacy/ |
| 10 | Krause 미디어 메모 (1985) | **PRIMARY 아카이브** (Stanford M1007 Papers) | https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html |
| 11 | Apple Business Conduct Policy (Feb 2026) | **PRIMARY** (Apple 공개 게시) | https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf |
| 12 | apple.com/privacy/ · /environment/ · /accessibility/ | **PRIMARY** (현재 라이브) | https://www.apple.com/privacy/ |
| 13 | **Apple Marcom 톤오브보이스 가이드** | **존재하지 않음(공개)** | — |
| 14 | **apple.com/values/** | **404 — 존재하지 않음** | — |

---

## (c) 에이전트가 이 스킬에서 신뢰할 수 있는 1차 규칙 목록

각 항목은 **실제로 fetch에 성공한 Apple 공식 페이지**에서 나온 것이다. 모든 규칙에 출처 URL을 붙였다.

### A. 태도·보이스 (최상위 원칙)

1. **독자를 `you`로 직접 부른다. `the user`/`the player`라고 부르지 않는다.**
   “It typically works well to use *you* and *your* to address people directly. Referring to people indirectly as *the user* or *the player* can make your experience feel distant and unwelcoming.”
   — https://developer.apple.com/design/human-interface-guidelines/inclusion

2. **1인칭(`we`, `us`, `I`)을 쓰지 않는다.** 독자 또는 제품을 주어로 재작성한다.
   “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.”
   — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (first person, p.87)
   HIG도 동일: “Avoid using *we* altogether because it may be unclear who the 'we' in question refers to.”
   — https://developer.apple.com/design/human-interface-guidelines/writing

3. **능동태를 쓴다. 수동태는 피한다.**
   “Avoid when possible and use active voice. … rewrite to avoid passive voice if you can.”
   — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (passive voice, p.154)

4. **보이스를 먼저 정하고, 톤은 상황에 맞춰 바꾼다.**
   “Develop your app’s voice first, and then you can vary its tone.”
   — https://developer.apple.com/videos/play/wwdc2022/10037/
   “Voice represents the consistent elements that are always there. The tone represents things that can and should change depending on the moment.” — https://developer.apple.com/videos/play/wwdc2024/10140/

5. **Apple이 일관되게 지키는 4가지 품질: Clarity, simplicity, friendliness, helpfulness.**
   “Clarity, simplicity, friendliness, and helpfulness.” (+ “I see these pretty consistently throughout Apple’s writing”)
   — https://developer.apple.com/videos/play/wwdc2024/10140/

### B. 간결성·문장

6. **더 적은 단어로 쓸 수 있으면 그렇게 한다. 소리 내어 읽어본다.**
   “Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.”
   — https://developer.apple.com/design/human-interface-guidelines/writing
   “UX writing is all about economy of language. Resist the urge to fill all available space with repeated information.” — https://developer.apple.com/videos/play/wwdc2025/404/

7. **`simply`, `quickly`, `just`, `please`, `sorry` 같은 필러를 제거한다.**
   “If I remove the words 'simply' and 'quickly' from this message… I haven’t lost any clarity, and I don’t make assumptions about the context of the person using it.”
   — https://developer.apple.com/videos/play/wwdc2025/404/
   “interjections like 'oops!' or 'uh-oh' can sound patronizing, and 'please' and 'sorry' can sound insincere. Use them sparingly.” — https://developer.apple.com/videos/play/wwdc2022/10037/

8. **이득(benefit)을 문장 앞으로 옮긴다 — “lead with the why”.**
   “if you’re leaving the benefit for the end of the sentence, try moving it to the front.”
   — https://developer.apple.com/videos/play/wwdc2025/404/

9. **명료함이 간결함보다 우선한다.**
   “Clarity is more important than brevity.”
   — https://www.swift.org/documentation/api-design-guidelines/
   “Clarity at the point of use is your most important goal.” — 같은 URL

10. **쓸데없는 단어를 뺀다. 흔한 단어로 충분하면 어려운 말을 쓰지 않는다.**
    “Omit needless words. Every word in a name should convey salient information at the use site.”
    “Avoid obscure terms if a more common word conveys meaning just as well. Don’t say 'epidermis' if 'skin' will serve your purpose.”
    — https://www.swift.org/documentation/api-design-guidelines/

### C. 대문자·문장부호·타이포그래피

11. **두 가지 대문자 스타일을 구분하고, UI 요소 유형별로 하나를 골라 일관되게 적용한다.**
    “Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently throughout your app — for example, title case for all alerts or sentence case for all headlines.”
    — https://developer.apple.com/design/human-interface-guidelines/writing

12. **경고(alert) 제목: 완전한 문장이면 sentence-style + 끝 문장부호, 구절이면 title-style + 문장부호 없음.**
    “If the title is a complete sentence, use sentence-style capitalization and appropriate ending punctuation. If the title is a sentence fragment, use title-style capitalization, and don’t add ending punctuation.”
    — https://developer.apple.com/design/human-interface-guidelines/alerts

13. **버튼 레이블은 title-style, 동사로 시작, 끝 문장부호 없음, 1–2 단어.**
    “Using title-style capitalization, consider starting the label with a verb…” — https://developer.apple.com/design/human-interface-guidelines/buttons
    “Aim for a one- or two-word title that describes the result of selecting the button.” — https://developer.apple.com/design/human-interface-guidelines/alerts

14. **sentence-style = 첫 단어 첫 글자 + 고유명사만 대문자. title-style = 관사·4자 이하 전치사·등을 제외한 각 단어 대문자.**
    “sentence-style capitalization — Capitalize only the first letter of the first word, proper nouns, and proper adjectives.”
    “title-style capitalization — Capitalize each word—except for articles, prepositions of four or fewer letters, and so on.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (p.182, p.205)

15. **시리얼 콤마를 쓴다.**
    “Use a serial comma before and or or in a list of three or more items.” (Correct: “…send reminders, and more.”)
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (commas, p.56)

16. **메뉴 항목/버튼 이름이 말줄임표로 끝나도 본문에서는 말줄임표를 쓰지 않는다.**
    “If the name of a menu item or button ends with an ellipsis, don’t include the ellipsis in running text.” (Correct: “Choose File > New…” ❌ → “Choose File > New” ✅)
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (ellipsis, p.79)

17. **태그라인/히어로는 문장이 아니어도 마침표로 끝난다. CTA에는 마침표를 쓰지 않는다.** (관찰된 컨벤션)
    `Pro further.` / `Listening. Remastered.` / `Love it. Lease it. Upgrade it.` ↔ CTA `Learn more`, `Buy`, `View pricing`
    — https://www.apple.com/ · https://www.apple.com/airpods/

### D. 숫자·단위·약어

18. **1–9는 풀어 쓰고, 숫자 자체·단위·주소/비트/슬롯 등은 숫자로 쓴다. 문장 첫머리 숫자는 풀어 쓴다.**
    “Spell out… Cardinal numbers from one through nine. (However, use a numeral, no matter how small, to express numbers as numbers and as units of measure.) … Numbers that appear at the beginning of a sentence.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (numbers, p.148)

19. **SI 단위만 쓴다. 수량과 기호 사이는 nonbreaking space. 단위 기호는 복수형이 없고 형용사로 쓰여도 하이픈을 넣지 않는다.**
    “Use only units of the International System of Units (SI)… Quantities are always expressed with a unit symbol. Use a nonbreaking space (Option-Space bar) between the quantity and its symbol. Unit symbols are unaltered in the plural and are never hyphenated, even when they’re used as an adjective.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (Units of measure, p.243)

20. **라틴 약어(`e.g.`, `i.e.`, `etc.`, `et al.`)를 쓰지 않는다.**
    “Avoid using Latin abbreviations.” (Correct: for example / and others / and so on / that is)
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (abbreviations and acronyms, p.11–12)

21. **약어 복수형에 아포스트로피를 넣지 않는다. 약어에는 마침표를 쓰지 않는다(비메트릭 단위·a.m./p.m./U.S. 예외).**
    “Don’t add an apostrophe before the s when you form the plural of an abbreviation.” (CDs, ICs, ISPs)
    — 같은 URL

### E. 제품명·상표

22. **제품명은 공식 표기를 그대로 따른다. 줄이거나 약어로 만들지 않는다.**
    “Follow the capitalization style of the official product name. Don’t shorten or abbreviate product names.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (product names, p.168)

23. **제품명을 동사로 쓰지 않는다. 트레이드마크의 복수형·소유격도 쓰지 않는다.**
    “Don’t use product names or trademarks as verbs: make a FaceTime call to a friend, not FaceTime a friend.”
    “Rewrite to avoid using plural or possessive forms of product names that are trademarks: Mac computers, not Macs.”
    — 같은 URL / (trademarks (usage), p.207)

24. **소문자로 시작하는 제품명은 문장 첫머리와 title-style 제목에서도 소문자를 유지한다.**
    “iPhone Safety Features, not IPhone Safety Features; Set Up Your Mac mini, not Set Up Your Mac Mini. In all-caps text, capitalize all the letters: THE NEW IPAD, not THE NEW iPAD.”
    — 같은 URL

25. **Apple 상표를 앱 이름이나 이미지에 쓰지 않는다.**
    “Apple trademarks must not appear in your app name or images.”
    — https://developer.apple.com/design/human-interface-guidelines/branding

### F. 하이픈

26. **명사를 앞에서 수식하는 두 단어는 하이픈으로 연결한다. `very`와 `-ly` 부사는 연결하지 않는다.**
    “In general, hyphenate two words that precede and modify a noun as a unit.”
    “Adverbs: Don’t hyphenate compounds with very or with adverbs that end in -ly.” (`very high speed`, `recently completed project`)
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (hyphenation, p.104)

27. **단위가 풀어쓴 말이면 하이픈(`27-inch screen`), 약어·메트릭이면 하이픈 없음(`500 GB hard disk`).**
    — 같은 URL

### G. 포용적 언어·현지화

28. **폭력적·차별적·능력주의 용어를 피한다.** `kill`, `hang`, `master`/`slave`, `sanity check` 금지.
    “Don’t describe technology using terms that are inherently violent—like kill or hang. Don’t use the terms master and slave… don’t use terms like sanity check.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (Writing inclusively, p.224)

29. **성별이 특정되지 않은 사람에게는 단수 `they`를 쓴다.**
    “Don’t use gender-specific pronouns (such as he, she, he or she, and so on) to refer to people of unspecified gender. Instead, it’s OK to use they, their, or them as a singular, gender-neutral pronoun.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (Gender identity, p.226)

30. **감각에 의존하는 지시문을 쓰지 않는다. 무슨 일이 일어나는지 서술한다.**
    “avoid using phrases that refer to the use of specific senses, like you see a message… Instead, simply describe what happens: A message appears, a light flashes, an alert sound plays.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (Writing about disability, p.227)

31. **관용구·구어체를 쓰지 않는다(번역과 이해 모두를 위해).**
    “Don’t use idiomatic or colloquial expressions.” / “Write in simple structures.”
    — https://support.apple.com/guide/applestyleguide/intro-to-international-style-apsg1ff68ab5/web

32. **색으로 긍정/부정을 함축하지 않는다(`blacklist`, `white hat`).**
    “Don’t use color to convey positive or negative qualities.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (p.224)

33. **유머는 예제에만, 그리고 번역되지 않을 수 있음을 기억한다.**
    “Humor usually works best in examples… keep in mind that humor may not translate well in localized text.”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (humor, p.103)

### H. UI 카피 실무

34. **오류 메시지: 문제 가까이에, 비난 없이, 해결책을 구체적으로. 감탄사 금지.**
    “display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, 'That password is too short' isn’t as helpful as 'Choose a password with at least 8 characters.'… Interjections like 'oops!' or 'uh-oh' are typically unnecessary and can sound insincere.”
    — https://developer.apple.com/design/human-interface-guidelines/writing

35. **“Invalid name” 같은 로봇적 오류 메시지를 쓰지 않는다. 올바른 방법을 알려준다.**
    “'Use only letters for your name' is better than 'Don’t use numbers or symbols.' Avoid robotic error messages with no helpful information, like 'Invalid name.'”
    — 같은 URL

36. **`Error` 또는 `Error 329347 occurred` 같은 제목을 쓰지 않는다. 제목은 두 줄을 넘기지 않는다.**
    “Avoid writing a title that doesn’t convey useful information — like 'Error' or 'Error 329347 occurred' — but also avoid overly long titles that wrap to more than two lines.”
    — https://developer.apple.com/design/human-interface-guidelines/alerts

37. **`OK`는 정보성 경고에서만. `Yes`/`No`는 쓰지 않는다. 취소 버튼은 항상 `Cancel`.**
    “In informational alerts only, you can use 'OK' for acceptance, avoiding 'Yes' and 'No.' Always use 'Cancel' to title a button that cancels the alert’s action.”
    — 같은 URL

38. **소유격 대명사를 아낀다. `Your Favorites` → `Favorites`.**
    “Possessive pronouns like my and your are often unnecessary to establish context. For example, 'Favorites' conveys the same message as 'Your Favorites,' and is more succinct.”
    — https://developer.apple.com/design/human-interface-guidelines/writing

39. **버튼·링크 레이블은 동사로. `Click here` 금지, `Let’s do it!` 같은 재치 금지.**
    “When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying 'Send' often works better than 'Let’s do it!' For links, avoid using 'Click here' in favor of more descriptive words or phrases.”
    — 같은 URL

40. **설정 설명은 켜졌을 때 무엇을 하는지만 쓴다. 꺼졌을 때는 독자가 유추한다.**
    “Describe what it does when turned on, and people can infer the opposite.”
    — 같은 URL

41. **다단계 흐름에서는 `Get Started` → `Continue`/`Next` → `Done`을 일관되게 쓴다.**
    “Begin with language like 'Get Started'… you can use terms like 'Continue' or 'Next,' but be consistent with what you choose. Make it clear when a flow is complete by using language like 'Done.'”
    — 같은 URL

42. **빈 화면(empty state)은 다음 행동을 안내하고, 사라질 핵심 정보는 넣지 않는다.**
    “guide people on actions they can take, and give them a button or link to do so if possible. Remember that empty states are usually temporary, so don’t show crucial information that could then disappear.”
    — 같은 URL

43. **기기별로 제스처를 정확히 쓴다. 터치 기기에서 “click”이 아니라 “tap”.**
    “not saying 'click' for a touch device like iPhone or iPad where you mean 'tap.'”
    — 같은 URL
    ASG 보강: “tap (n., v.) … **Don’t use tap on.**” / “press — Don’t use click, hit, push, tap, or type.” / “enter — Use enter, not type…”
    — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf

44. **알림 본문은 완전한 문장 + sentence case + 정상 문장부호. 잘라 쓰지 않는다(시스템이 알아서 자른다).**
    “Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.”
    — https://developer.apple.com/design/human-interface-guidelines/notifications

45. **접근성 레이블에 요소 유형(`button`, `tab`)을 넣지 않는다. 간결하게.**
    “VoiceOver knows what the element in your apps is based on the element type. So, it’s redundant to add text to your string like button or tab.” / “Avoid redundant labels.”
    — https://developer.apple.com/videos/play/wwdc2019/254/

46. **UI 문자열마다 번역자용 코멘트를 반드시 단다 — (1) 어디에 보이는지 (2) 맥락 (3) 변수 값.**
    “I insist, no matter the string, you should always define a comment.” / “comments should explain where the string is visible… they should explain the context… comments should explain variables.”
    — https://developer.apple.com/videos/play/wwdc2021/10221/

### I. App Store 카피 (수치·구속력)

47. **필드 예산: 이름 30자(최소 2자) / 부제 30자 / 키워드 100 bytes / 프로모션 텍스트 170자 / 설명 4000자 / What’s New 4000자 / IAP 이름 35자·설명 55자.**
    — https://developer.apple.com/help/app-store-connect/reference/app-information/app-information · https://developer.apple.com/help/app-store-connect/reference/platform-version-information · https://developer.apple.com/app-store/product-page/

48. **메타데이터에 상표 용어·인기 앱 이름·가격 정보·무관한 문구를 채워 넣지 않는다.**
    “don’t try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system.”
    — https://developer.apple.com/app-store/review/guidelines/ (2.3.7)

49. **부제에 `world’s best app` 같은 일반적 최상급을 쓰지 않는다.**
    “Avoid generic descriptions such as 'world’s best app.' Instead, highlight features or typical uses of your app that resonate with your audience.”
    — https://developer.apple.com/app-store/product-page/

50. **설명의 첫 문장이 가장 중요하다. “간결한 정보 문단 + 주요 기능 짧은 목록”이 이상적 형태다.**
    “The ideal description is a concise, informative paragraph followed by a short list of main features. … The first sentence of your description is the most important.”
    — 같은 URL

### J. 현지화 (한국어 스킬에 직접 적용)

51. **한국어 마케팅 카피는 합니다체 본문 + 해요체 온기 레이어, 지시/법적 마이크로카피는 하십시오체.**
    합니다체: `Apple 엔지니어들은 … 함께 설계합니다.` / 해요체: `…안전하게 옮길 수 있죠.` / 하십시오체: `자세한 내용은 apple.com/HRAccuracy 를 참고하십시오.`
    — https://www.apple.com/kr/iphone/ · https://www.apple.com/kr/

52. **한국어 보도자료는 한다체(평서형)로 쓴다.** `Apple은 오늘 세계 최초의 폴더블 iPhone인 iPhone Duo를 공개했다.`
    — https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/
    (대조: 같은 릴리스의 일본어는 です/ます体 — https://www.apple.com/jp/newsroom/2026/09/apple-unveils-iphone-duo/)

53. **한국어 CTA는 `-하기` 명사형.** `더 알아보기` / `구입하기` / `비교하기` / `쇼핑하기` / `갈아타기`
    — https://www.apple.com/kr/ · https://www.apple.com/kr/iphone/

54. **태그라인의 마침표는 한국어(`.`)와 일본어(`。`) 모두에서 유지된다.** `Pro, 더 앞으로.` / `プロの彼方へ。`
    — https://www.apple.com/kr/ · https://www.apple.com/jp/

55. **현지화 카피는 영어보다 짧아진다 — 한국어 약 50–65%, 일본어 약 55–70%.**
    (예: `Explore the lineup.` 19자 → `라인업 살펴보기.` 9자 → `すべてのモデルを見る` 10자)
    — https://www.apple.com/kr/iphone/ · https://www.apple.com/jp/iphone/

56. **제품·칩·플랫폼 이름은 라틴 문자 유지, 기능 이름은 선별적으로 현지화. 시장에 맞는 서비스로 대체한다.**
    `iPhone Duo`/`A20 Pro`/`Ceramic Shield` 유지; `Move to iOS` → `'iOS로 이동'`; `…apps such as WhatsApp and WeChat.` → `WhatsApp, 카카오톡처럼…`
    — https://www.apple.com/kr/iphone/ · https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/

57. **한국어는 미터법으로 환산하고, 일본어는 인치를 유지한다.** `7.6-inch` → KR `19.3cm` / JP `7.6インチ`
    — https://www.apple.com/kr/newsroom/2026/09/apple-unveils-iphone-duo/ · https://www.apple.com/jp/newsroom/2026/09/apple-unveils-iphone-duo/

58. **Apple 자신의 한국어 HIG 지침문은 합쇼체로 쓰인다.** `앱의 보이스를 결정하십시오.` / `명확하게 표현하십시오.`
    — https://developer.apple.com/kr/design/human-interface-guidelines/writing

### K. 레지스터 전환 — “1인칭 금지”의 정확한 적용 범위 (중요)

59. **`we`/`our`는 *지침·UI·사용자 문서*에서 금지되지만, *가치 선언·경영진 서한·법무·프라이버시*에서는 필수다.** 이 둘을 섞지 말 것.
    - 금지 레지스터: “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.” — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf (first person, p.87) · “Avoid using *we* altogether because it may be unclear who the 'we' in question refers to.” — https://developer.apple.com/design/human-interface-guidelines/writing
    - 허용/필수 레지스터: “**At Apple, we believe strongly in fundamental privacy rights** — and that those fundamental rights should not differ depending on where you live in the world.” — https://www.apple.com/legal/privacy/en-ww/ · “**That’s the kind of innovation we believe in.**” — https://www.apple.com/privacy/ · “Though the operating system for the iPhone, iPod and iPad is proprietary, **we strongly believe that all standards pertaining to the web should be open.**” — https://web.archive.org/web/2010/http://www.apple.com/hotnews/thoughts-on-flash/

60. **카피 품질 자체가 제품 품질의 증거로 취급된다 (“Impute”).**
    “The general impression of Apple Computer Inc. (our image) is the combined result of everything the customer sees, hears or feels from Apple, not necessarily what Apple actually is! … **if we present them in a slirshod [slipshod] manner, they will be perceived as slipshod; if we present them in a creative, professional manner, we will impute the desired qualities.**”
    — https://archive.org/download/102789075-05-01-acc/102789075-05-01-acc_djvu.txt (「THE APPLE MARKETING PHILOSOPHY」 Dec. 1979 스캔, OCR 정규화. **커뮤니티 업로드 스캔이며 저자 귀속(Markkula)은 미검증**)

60b. **“일관된 단일 목소리”는 1985년 사내 미디어 지침까지 거슬러 올라가는 Apple의 원칙이다.**
    “we do operate under guidelines to ensure that **the company’s position on issues is accurately and consistently stated.**”
    “**There is no such thing as 'off the record.'**”
    — https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause1.html · https://web.stanford.edu/dept/SUL/sites/mac/primary/docs/krause2.html (Stanford, `M1007, Apple Computer Inc. Papers, Series 9, Box 1, Folder 2`)

60c. **Apple에서 글을 공개하는 것은 승인 절차의 대상이다 (사내 규정).**
    “If you want to contribute an article or other type of submission to a publication or blog on a topic that relates to Apple’s current or reasonably anticipated products or services… **you must first request approval from Corporate Communications.**”
    — https://www.apple.com/compliance/pdfs/Business-Conduct-Policy.pdf (February 2026, “Publishing Articles”)

61. **가치 서술은 “짧은 선언 + `That’s why` + 2인칭 이득” 구조로 착지시킨다.**
    `Privacy. That’s Apple.` → “That’s why we design our products and services to protect it.” → “…do what you love, **your way**.”
    — https://www.apple.com/privacy/ · https://www.apple.com/accessibility/

### L. 존재하지 않거나 검증되지 않은 것 (에이전트가 인용하면 안 되는 것)

62. **Marcom 톤오브보이스 가이드는 공개되어 있지 않다 (clean negative).** Apple Style Guide가 존재만 인정한다(“Some departments at Apple (Marcom, for example) have supplemental style guides.” — https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf, p.5). archive.org `"Apple" AND "marcom"` 검색 4건 모두 무관. **1차 출처로 인용 불가. 팩시밀리 없이 돌아다니는 “Apple Marcom 스타일 가이드” 텍스트는 위조/미검증으로 취급할 것.**
63. **“Apple Developer Documentation Style Guide”는 존재하지 않는다.** (4개 경로 404 + GitHub org:apple `total_count: 0`)
64. **“Crazy Ones” 대본의 Apple 발행 1차 URL은 없다.** 캠페인은 외부 에이전시(TBWA\Chiat\Day) 제작 → **Apple 내부 하우스 스타일의 예가 아니다.** 텍스트는 Siltanen/Forbes(Wayback)라는 **2차** 출처로만 인용 가능. **“Steve Jobs가 썼다”는 MYTH/DISPUTED** (Siltanen이 “revisionist history”라 반박).
65. **archive.org “Think Different Booklet (1997)”을 팩시밀리로 인용하지 말 것.** 렌더링 검증 결과 **재타이핑된 디지털 조판**이다. 진짜 스캔은 `19971110-really-different-brochure_202201`.
66. **“Markkula가 1979년 메모를 썼다”는 MYTH/DISPUTED.** 스캔본에 서명·저자명이 없고 회사를 3인칭으로 서술한다. Stanford 아카이브에도 없다. **“1980년 1월 3일자”도 오류 — 도장은 `ACH Dec. 79`.**
67. **Apple Support의 `Related articles` / `See also` 문자열은 확인되지 않았다.** 교차 참조는 인라인 링크 + `Need more help?` 블록이다.
68. **App Store 글자 수 제한을 App Store Connect API 스펙에서 인용하지 말 것** — 스펙에는 `maxLength`가 없다. ASC Help만 인용 가능.
69. **`apple.com/values/`는 404다.** (그리고 `/our-values/`, `/apple-values/`도 404.) 가치 관련 콘텐츠는 `/privacy/`, `/environment/`, `/accessibility/`, `/supplier-responsibility/`, `/inclusion/`에 있다.
70. **“스캔”이라고 주장하는 아카이브 아이템은 반드시 PDF를 렌더링해 하프톤·종이 질감·스캔 노이즈를 눈으로 확인한 뒤에만 팩시밀리로 분류할 것.** Think Different Booklet이 그 반례다. 메타데이터의 `creator: Apple Inc.`는 **업로더 입력값**이지 진본 인증이 아니다.

---

## (d) 접근 실패한 URL과 그 이유

| URL | 결과 | 이유 / 우회 |
| --- | --- | --- |
| https://developer.apple.com/design/human-interface-guidelines/writing (직접 `curl`) | 200이지만 **17,572 bytes JS 셸, 본문 없음** | HIG는 React SPA. → **`https://r.jina.ai/<url>` 리더 프록시로 우회 성공** |
| https://web.archive.org/web/2024/https://developer.apple.com/design/human-interface-guidelines/writing | 200이지만 **5,506 bytes 셸** | 아카이브 캡처도 SPA 셸만 저장. 사용 불가 |
| https://developer.apple.com/tutorials/data/documentation/design/human-interface-guidelines/writing.json | **404** | HIG는 DocC JSON 시스템 밖에 있다. `human-interface-guidelines/writing.json`, `design/human-interface-guidelines.json`도 모두 404 |
| https://developer.apple.com/help/app-store-connect/reference/app-information/subtitle | 200이지만 **소프트 404** (82,040 bytes page-not-found 셸) | 실제 경로가 아님. ASC Help의 200 + 약 82 KB는 소프트 404의 tell. 실제 필드 정의는 `.../reference/app-information/app-information`에 있다 |
| https://developer.apple.com/help/app-store-connect/reference/app-information/app-name | 동일 소프트 404 | 위와 같음 |
| https://developer.apple.com/help/app-store-connect/manage-app-information/add-a-subtitle | 동일 소프트 404 | 위와 같음 |
| https://developer.apple.com/help/app-store-connect/manage-app-information/ | 동일 소프트 404 | 위와 같음 |
| https://developer.apple.com/help/app-store-connect/sitemap.xml | **404** | 사이트맵 없음 |
| https://developer.apple.com/help/app-store-connect/.../*.json | **404** | ASC Help에는 공개 데이터 API가 없다 |
| https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.json | **300 (multiple choices)** | `.zip` 형태만 제공된다 |
| https://developer.apple.com/documentation/style-guide | **404** | 그런 문서는 존재하지 않는다 (부정 결과) |
| https://developer.apple.com/documentation/documentation-style-guide | **404** | 위와 같음 |
| https://developer.apple.com/documentation/xcode/style-guide | **404** | 위와 같음 |
| https://developer.apple.com/documentation/docc/style-guide | 200이지만 **`swift.org/documentation/docc/`로 리다이렉트(소프트 404)** | 위와 같음 |
| https://www.swift.org/documentation/docc/writing-symbol-documentation (짧은 슬러그) | **소프트 404**(푸터만 렌더) | 전체 슬러그 `...-in-your-source-files`를 써야 한다 |
| https://support.apple.com/guide/applestyleguide/welcome/web (`web_fetch` 도구) | **`unsupported content type "unknown"`** | 도구 문제. → **`curl` + 브라우저 UA로 우회 성공 (200, 588,475 bytes)** |
| https://help.apple.com/applestyleguide/ | 200이지만 **248 bytes JS 리다이렉터 스텁** | 실제 문서가 아니다. `support.apple.com/guide/applestyleguide/<slug>/web`로 직접 가야 한다 |
| https://www.apple.com/newsroom/ (인덱스) | `curl`은 nav만 반환(JS 렌더) | → **`jina` 프록시 필요**. 개별 보도자료 기사 자체는 `curl`로 200 |
| https://web.stanford.edu/dept/SUL/library/mac/ | **403** | Stanford “Making the Macintosh” 아카이브가 봇을 차단. web.archive.org 2015 캡처에도 Markkula 메모 원문 없음 |
| https://www.apple.com/values/ | **404** (111,090 bytes) | 이 경로는 더 이상 존재하지 않는다 |
| https://developer.apple.com/videos/play/wwdc2023/111484/ 등 Q&A 세션 | 세션 페이지는 200이지만 **transcript가 게시되지 않음** | Apple이 Q&A 세션 전문을 공개하지 않는다 |
| `support.apple.com/102446` vs `support.apple.com/ko-kr/102446` | 둘 다 200, **byte-identical (758,994 B)** | 일부 guide ID에는 ko-kr 로케일이 적용되지 않는다 |
| “If your iPhone won’t turn on” 지원 문서 | **찾지 못함** | `web_search` 도구 전면 다운 + Apple 지원 검색이 JS 렌더라 ID 열거 불가. → 대체로 `https://support.apple.com/en-us/118575`(EN/KO/JA 3개 로케일 1:1 비교 가능)를 사용. **`If your … won’t …` 제목 형태는 하우스 패턴에서 유추한 것이며 fetch한 페이지에서 인용한 것이 아니다** |
| `Related articles` / `See also` 모듈 | **찾지 못함** | 실제 기사에는 이 제목의 모듈이 렌더되지 않는다. 교차 참조는 단계 산문 안의 인라인 링크 + `Need more help?` 블록. **이 문자열들을 인용하지 말 것** |

### 도구·라우트 요약 (재사용용)

| 페이지 종류 | 성공한 라우트 |
| --- | --- |
| `support.apple.com/guide/applestyleguide/<slug>/web` | plain `curl` + 브라우저 UA (정적 HTML) |
| Apple Style Guide PDF | `curl` → 4,158,788 bytes → `pypdf`로 244p 텍스트 추출 |
| `developer.apple.com/design/human-interface-guidelines/*` | **`https://r.jina.ai/<url>`** (curl은 SPA 셸만) |
| `developer.apple.com/documentation/<path>` | **`<url>.md` → `text/markdown`**, 또는 `/tutorials/data/documentation/<path>.json` |
| `developer.apple.com/videos/play/wwdcYYYY/NNNN/` | plain `curl` — **transcript가 정적 HTML에 들어 있다** |
| `developer.apple.com/app-store/*`, `/app-store/review/guidelines/` | plain `curl` (`&nbsp;` 엔티티 디코딩 주의) |
| `developer.apple.com/help/app-store-connect/**` | plain `curl` — **200 + 약 376 KB = 정상, 200 + 약 82 KB = 소프트 404** |
| `www.apple.com/**`, `/kr/**`, `/jp/**`, `/legal/**`, `support.apple.com/<locale>/<id>` | plain `curl` + Safari UA |
| `www.apple.com/newsroom/` (인덱스만) | `jina` 프록시 |
| `ads.apple.com/**` | `jina` 프록시 |
| `www.swift.org/documentation/docc/**` | `jina` 프록시 |
| `www.swift.org/documentation/api-design-guidelines/` | `curl --compressed` (gzip 필수) |
| 죽은 Apple 페이지 (예: Thoughts on Flash) | `https://web.archive.org/web/2010/<url>` |
