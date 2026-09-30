
---

# Part A — Voice systems

**Scope of Part A.** Primary published voice-and-tone systems, read as *structural templates* for our Apple-prose skill. For each: how voice is defined, how tone branches, what executable rules exist (checklists / before-after / banned words / lint), and what we should copy. Companion to Part B (Apple evidence). Part B owns the Apple corpus; Part A owns the comparison set and the transferable structure.

**Access note (honest failure log).** `web_search` was degraded for this whole session (SearXNG returned zero results; the Bing-backed `search.sh` fallback returned query-mismatched, region-shifted junk). Everything below came from **direct URL fetches** plus **web.archive.org**. Specific failures, stated plainly:

| Target | Status |
|---|---|
| `https://www.gov.uk/guidance/content-design/writing-for-gov-uk` | **Fails** — cross-origin redirect to `guidance.publishing.service.gov.uk`, then 404 on that path. Retired/migrated. Used archive.org snapshot `web.archive.org/web/20190101033138/https://www.gov.uk/guidance/content-design/writing-for-gov-uk` (dated 2019-01-01) + the current beta guidance set. |
| Mailchimp “per-situation tone pages” | **Do not exist.** Mailchimp’s TOC has *no* per-situation tone section. Situation-branching at Mailchimp is done by **subject-area sections** (Legal, Educational, Email Newsletters, Social Media) + a one-paragraph user-emotional-state instruction on the Voice and Tone page. The premise of item 1 was partly wrong; corrected below. |
| `https://polaris.shopify.com/content` | **Fails** — 301 to `shopify.dev`, and Polaris has since been restructured. Polaris *was* the primary source. Used archive.org snapshots dated 2024-12-27 (`.../content/voice-and-tone`) and 2024-12-01 (`.../content/error-messages`). |
| `https://atlassian.design/content/` | 404. The live path is `https://atlassian.design/foundations/content/voice-tone` — page is JS-rendered, so fetched raw and text-extracted. |
| IBM Design Language “voice” pages | **Dead.** `ibm.com/design/language/experience/writing/voice/` → 404; archive.org CDX search over `ibm.com/design/language*` for voice/writing/tone returned **no archived HTML** (only a JS chunk). Substituted **IBM Style** (`ibm.com/docs/en/ibm-style`), which *does* publish a `Tone` topic and is more relevant anyway. IBM docs is JS-rendered; only its TOC was retrievable. |
| `https://carbondesignsystem.com/...` | DNS failure (`ENOTFOUND`) from this environment. |
| `https://www.ibm.com/docs/en/ibm-style?topic=style-tone` | 200 but JS-rendered — returned TOC only, not topic body. Marked **UNVERIFIED** below. |

No site blocked us with a paywall; the failures are migration, JS rendering, and DNS.

---

## A(a) 표 — 시스템 비교

| 시스템 | URL | 보이스 정의 방식 | 톤 분기 방식 | 실행 규칙 유무 | 배울 점 |
|---|---|---|---|---|---|
| **Mailchimp Content Style Guide** | https://styleguide.mailchimp.com/voice-and-tone/ | 4개 형용사 + 각 형용사의 **서술적 근거** (Human·Familiar·Friendly·Straightforward). 본문에서는 “We are plainspoken / genuine / translators / our humor is dry” 4개 1인칭 원칙으로 재진술 | “**독자의 감정 상태**(emotional state)” 기준. 명시적 매트릭스 없음. 상황 분기는 주제별 섹션(Legal·Educational·Email·Social)으로 처리 | **강함.** ✅금지어/선호어 (Word List 섹션), ✅전후 예시 (Yes/No 쌍 다수), ✅문법 규칙 (대문자·컴마·em dash·exclamation), ✅상황별 금지 (“Never use exclamation points in failure messages or alerts”), ✅체크리스트 (TL;DR 단일 페이지 요약) | **TL;DR 페이지** — 17개 섹션 전체를 1페이지 불릿으로 압축. 그리고 **“언제 유머를 쓰지 않는가”** 를 유머 원칙 안에 명시 |
| **GOV.UK / GDS** | https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/ (구: gov.uk/guidance/content-design/writing-for-gov-uk) | 보이스 자체를 형용사로 정의하지 않음. **“tone of voice”라는 이름의 형용사 목록**으로 대체: specific·informative·clear and concise·brisk but not terse·incisive but remain human·serious but not pompous·emotionless | **user need** 기준. “Do not publish everything you can online. Publish only what someone needs to know.” 톤은 사용자 필요에서 *도출*됨. 별도 상황 매트릭스 없음 | **최강.** ✅금지어 목록 (Words to avoid, 30+ 항목, 각각 대체어 지정), ✅전후 예시 (Bad/Good 쌍 다수), ✅수치 규칙 (25단어 문장, 5문장 문단, 65자 제목, 160자 요약, 9세 읽기연령), ✅A to Z 사전 (수백 항목), ✅“하지 말 것” (FAQs 금지, footnotes 금지, block capitals 금지, negative contractions 금지) | **금지어를 “대체어와 함께” 제시.** “leverage → use/influence”, “utilise → use”. 단순 금지가 아니라 치환 규칙. 그리고 **규칙마다 근거 연구를 링크** |
| **Shopify Polaris** | https://polaris.shopify.com/content/voice-and-tone (archive 2024-12-27) | “Be real / Be proactive / Be dynamic / Guide” — 각 항목이 **“X, but not Y”** 형태로 상한과 하한을 동시에 규정 (예: “Be real, **but not** too tough or overly familiar”) | **“상황(situation)” 기준이며, 감정 상태 추정을 명시적으로 거부**: “the reality is we never know a person’s emotional state… **don’t assume or tell them how to feel**.” 6개 상황: Everyday tasks / Learning / Simple errors / Acknowledging effort / Motivate action / Serious problems | **강함.** ✅Do/Don’t 쌍이 **모든 상황에** 존재, ✅전후 예시 (실제 UI 문자열: “Product saved” vs “You successfully added a product.”), ✅금지어 (simple errors에 “Bad request, forbidden, fatal, expectation failed, unresolved, invalid” 금지), ✅컴포넌트 매핑 (상황→토스트/배너/모달) | **감정 상태 대신 상황.** “사용자는 화났을 것이다”라고 단정하지 않고 “이 상황에서는 이렇게” 로 분기. **금지어를 에러 등급별로** 지정. 안티패턴(토스트/모달로 에러 금지)까지 명시 |
| **Atlassian Design System** | https://atlassian.design/foundations/content/voice-tone | 3개 특성: **Bold · Optimistic · Practical, with a wink** | **이중 구조.** ①각 특성마다 “When to be more / less X” — 감정 상태 목록(confident, interested, trust ↔ apprehension, confusion, annoyance, fear, anger)과 사용자 유형(power users ↔ new/trial users)으로 강도 조절. ②6개 **voice-and-tone principles**(Inform to build trust / Empower to inspire action / Encourage along the path / Motivate by showing possibilities / Satisfy by meeting expectations / Delight with unexpectedly pleasing) — 각 원칙에 “Places to use” 로 UI 컴포넌트를 명시 | **가장 정교.** 보이스 = 강도 조절 가능한 형용사, 톤 = 그 강도. “with a wink”에 **명시적 상한**: “isn’t always appropriate to use… Once may amuse, but a dozen times may annoy” | ✅Do/Don’t (Language and grammar 섹션 전반), ✅금지어 (e.g./i.e./etc./& 금지, “simply”류 금지), ✅문법 규칙 (sentence case, 관사 생략, gerund 금지, curly apostrophe), ✅컴포넌트 매핑 테이블 (메시지 타입 × 컴포넌트) | **특성별 “more/less” 다이얼.** 형용사를 on/off가 아니라 **강도 조절 대상**으로 만든다. 그리고 **“wink”에 사용량 제한** — 캐리커처화 방지 장치가 원문에 있음 |
| **Microsoft Writing Style Guide + brand voice** | https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human · https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice | 3원칙: **Warm and relaxed · Crisp and clear · Ready to lend a hand**. “voice = personality, substance, tone, style의 상호작용” | “voice is constant… we **adapt our tone—from serious to empathetic to lighthearted**—to fit the context and the customer’s state of mind.” **연속선(spectrum)** 으로 표현, 매트릭스 아님 | **강함.** ✅**“Replace this / With this” 쌍이 10개** (Top 10 tips 전체가 이 형식), ✅“Use this / Not this” 단어 테이블 (utilize→use, in order to→to), ✅금지 목록 (adverbs: quite/very/quickly/easily/effectively), ✅문법 (sentence case, serial comma, one space, no period in headings) | **Top 10 tips = 10개의 전후 예시.** 각 팁이 “원칙 1문장 + Replace/With 쌍” 구조. 스킬 파일의 이상적 밀도 |
| **Google developer documentation style guide** | https://developers.google.com/style/tone · https://developers.google.com/style/voice | 명시적 형용사 3개: “**conversational, friendly, and respectful** without using slang or being overly colloquial or frivolous” | 상황 분기 없음. 대신 **금지 목록**으로 경계를 그림. “Too informal ↔ Just about right ↔ Too formal” **3열 테이블** | **강함.** ✅**3열 예시 테이블** (같은 내용의 3가지 톤 — 이 문서 최고의 자산), ✅금지 목록 14항목 (buzzwords, cutesy, figurative language, “please note”, exclamation marks, “let’s”, “simply/easy/quickly”, internet slang), ✅문법 (active voice + 예외 3가지 명시) | **3열 톤 테이블.** “이렇게 쓰지 마라”보다 “이 셋 중 가운데” 가 훨씬 강력한 지시. 그리고 **예외를 명시** (passive voice가 허용되는 3가지 경우) |
| **IBM Style** | https://www.ibm.com/docs/en/ibm-style | TOC에 `Tone` 독립 토픽 + `AI assistants`·`LLMs`·`Conversational style`·`Marketing`·`Social media` 토픽 | 주제별 토픽 분기 (medium/audience 기준: Marketing vs Social media vs AI assistants vs Red Hat) | **강함 (구조상).** 별도 `Word usage` + `Topics A to Z` + `Terminology` + `Messages` 토픽. **UNVERIFIED:** 본문은 JS 렌더링으로 추출 실패, TOC만 확인 | **매체(medium)별 톤 분기**를 TOC 최상위로 올림. `AI assistants`와 `LLMs`가 **독립 토픽** — LLM 상호작용 문체를 엔터프라이즈 스타일가이드가 정식 주제로 편입한 선례 |
| **Salesforce Lightning Design System** | https://v1.lightningdesignsystem.com/guidelines/voice-and-tone/ (PDF 배포) + https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide | “At Salesforce, we have guidelines we follow when we create written content… We use the same guidelines for other types of information, such as online help, developer doc, Walkthroughs, and Trailhead modules” | 가이드가 **PDF로 배포**되며 SLDS 페이지는 배포 채널 역할. 본문 미검증 | ⚠️ **PDF 미확보.** 페이지는 “Download Voice and Tone Guidelines” 링크 + 별도 Style Guide 사이트를 가리킴. 상세 규칙 **UNVERIFIED** | **한 벌의 규칙을 UI·help·dev doc·교육 콘텐츠에 공통 적용**한다고 선언 — “any domain” 야심의 선례. 다만 문서가 분리 배포되어 검증 불가 |
| **NHS digital service manual** (추가 발굴) | https://service-manual.nhs.uk/content/voice-and-tone | 보이스 5개 형용사: **neutral and factual · authoritative · calm and reassuring · empowering rather than patronising · personal rather than formal** | **“감정 상태” 명시 분기**: “We consider the situation and what the emotional state might be for the user.” 진단/치료 맥락 → “direct, serious and reassuring”; 운동/식이 맥락 → “encouraging and conversational”. **각 분기에 실제 문장 예시를 붙임** | ✅금지 (should 금지 — “it can sound patronising”), ✅전후/맥락 예시, ✅GOV.UK 스타일가이드로 위임하는 명시적 상속 구조 | **톤 분기에 “실제 완성 문장”을 붙인다.** “reassuring”이라는 형용사 대신 세르트랄린 부작용 문장을 그대로 보여줌. 그리고 **“guide, not a rulebook”** 선언 |
| **`surendranb/writing-skills`** (커뮤니티 선례, 39★) | https://github.com/surendranb/writing-skills | 해당 없음 — **보이스를 SKILL.md 계약으로 인코딩** | 스킬을 두 부류로 분리: *Frameworks*(표준, 강제) vs *Voices*(캐릭터, “rate-limited against caricature”) | ✅**CI 검증기** `scripts/validate_skills.py`: frontmatter name==폴더명, description ≥80자 & “Use when” 포함, 필수 섹션 4개(`## The core rule`, `## Mechanics`, `## Verify`, `## Do not`), 전후 예시 ≥2개, 본문 ≤120줄 | **스킬 자체를 검증 가능한 계약으로.** 그리고 `template/SKILL.md`라는 **복사용 골격** 제공 |

---

## A(b) 시스템별 상세 + 실제 인용 / 전후 예시

### A1. Mailchimp Content Style Guide — 상황별 톤 *페이지*는 없다, 주제별 섹션이 있다

**확인된 사실(중요):** 요청받은 “per-situation tone pages”는 **존재하지 않는다.** Mailchimp 스타일가이드 TOC는 Writing Goals and Principles · Voice and Tone · Writing about Mailchimp · Writing About People · Grammar and Mechanics · Web Elements · How to Write Educational Content · Writing Legal Content · Writing Email Newsletters · Writing for Social Media · Writing for Accessibility · Writing for Translation · Creating Structured Content · Copyright and Trademarks · Word List · Further Reading · TL;DR 로 구성되며, 상황별 톤 페이지는 없다. 상황 분기는 **주제 영역별 섹션**(Legal / Educational / Email / Social)이 담당한다. (출처: https://styleguide.mailchimp.com/voice-and-tone/ 및 /tldr/, 2023 CC BY-NC 라이선스)

**보이스 정의** — 형용사 4개 + 1인칭 원칙 4개, 그리고 **“우리는 ~하지 않는다”** 절:

> **We are plainspoken.** We understand the world our customers are living in: one muddled by hyperbolic language, upsells, and over-promises. We strip all that away and value clarity above all. Because businesses come to Mailchimp to get to work, we avoid distractions like fluffy metaphors and cheap plays to emotion.
>
> **We are genuine.** …
>
> **We are translators.** Only experts can make what’s difficult look easy, and it’s our job to demystify B2B-speak and actually educate.
>
> **Our humor is dry.** Our sense of humor is straight-faced, subtle, and a touch eccentric. We’re weird but not inappropriate, smart but not snobbish. We prefer winking to shouting. We’re never condescending or exclusive—we always bring our customers in on the joke.

**톤 분기** — 감정 상태 기반, 매트릭스 없음:

> Mailchimp’s tone is usually informal, but it’s always more important to be clear than entertaining. When you’re writing, consider the reader’s state of mind. Are they relieved to be finished with a campaign? Are they confused and seeking our help on Twitter? Once you have an idea of their emotional state, you can adjust your tone accordingly.
>
> Mailchimp has a sense of humor, so feel free to be funny when it’s appropriate and when it comes naturally to you. But don’t go out of your way to make a joke—forced humor can be worse than none at all. If you’re unsure, keep a straight face.

**전후 예시 (실제 인용)** — Mailchimp의 전후 쌍은 대부분 `Yes:` / `No:` 형식이며, **설탕/도넛 예문**으로 유명하다:

| 규칙 | Yes | No |
|---|---|---|
| Active voice | `Marti logged into the account.` | `The account was logged into by Marti.` |
| Write positively | `To get a donut, stand in line.` | `You can’t get a donut if you don’t stand in line.` |
| Serial comma | `David admires his parents, Oprah, and Justin Timberlake.` | `David admires his parents, Oprah and Justin Timberlake.` |
| Fractions | `two-thirds` | `2/3` |
| Abbreviations | `First use: Coordinated Universal Time (UTC)` → `Second use: UTC` | — |

**상황별 금지 규칙(가장 실용적인 한 줄):**

> Never use exclamation points in failure messages or alerts. When in doubt, avoid!

**의도적으로 남긴 예외** — 규칙에 예외를 명시하는 방식:

> One exception is when you want to specifically emphasize the action over the subject. In some cases, this is fine.
> — `Your account was flagged by our Abuse team.`

**Legal 콘텐츠 분기** — 같은 보이스, 톤만 격식 상향, 그리고 **평문 요약 대신 본문 자체를 평문으로**:

> Legal content is serious business, so the tone is slightly more formal than most of our content. That said, we want all of our users to be able to understand our legal content.
>
> Instead of: “If an individual purports, and has the legal authority, to sign these Terms of Use electronically on behalf of an employer or client then that individual represents and warrants that they have full authority to bind the entity herein to the terms of this hereof agreement”
>
> We say: “If you sign up on behalf of a company or other entity, you represent and warrant that you have the authority to accept these Terms on their behalf.”

그리고 대명사 규칙으로 법률문서를 인간화하는 트릭:

> At the beginning of the document, say something like: “Mailchimp is owned and operated by The Rocket Science Group, LLC d/b/a Mailchimp, a Georgia limited liability corporation (”Mailchimp,“ ”we,“ or ”us“). As a user of the Service or a representative of an entity that’s a user of the Service, you’re a ”Member“ according to this agreement (or ”you“).” After that, you’re free to use “we,” “us,” “you,” and “your” throughout the rest of the agreement. That simple change makes the document much friendlier to read.

**스케일링/거버넌스:** 명시적 편집 거버넌스는 Legal에만 존재 — “all legal content either starts with or passes through the Legal team”, “The Legal team performs periodic reviews of all marketing and technical content”, 고객 문의는 “a support agent will send the proposed reply to the Legal team for review… More complex issues… will be drafted by a paralegal and then escalated to a lawyer for review.” 그 외 콘텐츠는 **Word List + Grammar and Mechanics를 lint 대상으로 삼을 수 있는 형태로 제공**(명시적 린터는 없음).

---

### A2. GOV.UK / GDS — 보이스를 형용사로 정의하지 않고, 톤 목록으로 대체한다

**보이스 vs 톤:** GOV.UK은 “voice”라는 단어를 거의 쓰지 않는다. **“tone of voice”라는 제목 아래 형용사 목록**을 둔다:

> The 'tone of voice' for GOV.UK content is:
> - specific
> - informative
> - clear and concise
> - brisk, but not terse
> - incisive (friendliness can lead to a lack of precision and unnecessary words) – but remain human (not a faceless machine)
> - serious but not pompous
> - emotionless – adjectives can be subjective and make the text sound more emotive and like spin
> — https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/right-tone/

**톤 분기의 실제 기준은 감정이 아니라 “user need”:**

> Do not publish everything you can online. Publish only what someone needs to know so they can complete their task. Nothing more. People do not usually read text unless they want information. When you write for the web, start with the same question every time: what does the user want to know?
> — archive.org, /web/20190101033138/https://www.gov.uk/guidance/content-design/writing-for-gov-uk

**“We are not precious about words” 정신** — 원문에서 이 취지를 가장 직접적으로 말하는 문장들:

> The list is not exhaustive. It’s an indicator to show you the sort of language that confuses users.
>
> With all of these words you can generally get rid of them by breaking the term into what you’re actually doing. Be open and specific.
>
> Words ending in '–ion' and '–ment' tend to make sentences longer and more complicated than they need to be.

그리고 규칙을 **연구에 근거**시킨다:

> Research shows that higher literacy people prefer plain English because it allows them to understand the information as quickly as possible.
>
> For example, research into use of specialist legal language in legal documents found:
> - 80% of people preferred sentences written in clear English - and the more complex the issue, the greater that preference (eg, 97% preferred 'among other things' over the Latin 'inter alia')
> - the more educated the person and the more specialist their knowledge, the greater their preference for plain English

**금지어 목록 = 치환 규칙 (Words to avoid, 발췌 — 전 항목이 “금지어, use 'X' instead” 형식):**

> - agenda (unless it’s for a meeting), use 'plan' instead
> - advance, use 'improve' or something more specific
> - collaborate, use 'work with'
> - combat (unless military), use 'solve', 'fix' or something more specific
> - deliver, use 'make', 'create', 'provide' or a more specific term (pizzas, post and services are delivered - not abstract concepts like improvements)
> - deploy (unless it’s military or software), use 'use' or if putting something somewhere use 'build', 'create' or 'put into place'
> - empower, use 'allow' or 'give permission'
> - impact (unless talking about a collision), use 'have an effect on' or 'influence'
> - key (unless it unlocks something), usually not needed but can use 'important' or 'significant'
> - leverage (unless in the financial sense), use 'influence' or 'use'
> - robust (unless talking about a sturdy object), depending on context, use 'well thought out' or 'comprehensive'
> - streamline, use 'simplify' or 'remove unnecessary administration'
> - utilise, use 'use'
> — https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/#words-to-avoid

**메타포 금지도 별도 블록:**

> Avoid using metaphors - they do not say what you actually mean and lead to slower comprehension of your content. For example:
> - drive, use 'create', 'cause' or 'encourage' instead (you can only drive vehicles, not schemes or people)
> - going/moving forward, use 'from now on' or 'in the future' (it’s unlikely we are giving travel directions)
> - in order to, usually not needed - do not use it
> - hub, portal or one-stop shop, use 'website' or 'service'

**전후 예시 — 가장 값진 자산. 길이 문제를 한 쌍으로 보여준다:**

> “The recently implemented categorical standardisation procedure on waste oil should not be applied before 1 January 2015.”
> — 이렇게 바꾼다 →
> “Do not use the new waste oil standards before 1 January 2015.”

**Bullet 구조의 전후 (front-loading):**

> **Good example**
> At the activity centre you can:
> - swim
> - play
> - run
>
> **Bad example**
> At the activity centre:
> - you can swim
> - you can play
> - you can run

**제목/요약 전후:**

> Bad title example: Hazardous waste - new process
> Good title example: How to dispose of hazardous waste in your area
>
> Bad summary example: Implementing the government’s strengthened approach to budget support: technical note
> Good summary example: How the government is making budget support more effective in countries supported by the UK
>
> Bad summary example: Please complete the attached form to apply to gain a licence to sail on the River Thames.
> Good summary example: Get a licence to sail your pleasure boat on the River Thames.

**수치 규칙(= lint 가능):** 문장 ≤25단어 / 문단 ≤5문장 / 제목 ≤65자 / 요약 ≤160자 / 9세 읽기연령 / block capitals 금지 / ampersand 금지 / `must` vs `need` vs `can` 구분.

**법률 vs 일반 콘텐츠 분기 — 강도 등급으로 처리:**

> If you’re talking about a legal requirement, use 'must'. … If a requirement is legal, but it’s administrative or part of a process that will not have criminal repercussions, then use 'need'. … If something is optional, you can use 'can'. Avoid more complicated terms like 'You may be able to'.

**거버넌스:** GDS가 스타일가이드 영향 연구를 발주했고(“GDS commissioned research on the impact of style guides”), 변경 사항을 **이메일 구독으로 공지**하며, 린터로 Hemingway 앱을 **공식 권장**한다: “You can use tools such as the Hemingway app to check if your writing needs to be more active.”

---

### A3. Shopify Polaris — 감정 상태 추정을 명시적으로 거부한 유일한 시스템

**보이스 vs 톤:**

> Shopify’s voice is a reflection of who we are. We should always sound like Shopify. At the same time, some aspects of our personality might be more or less apparent, depending on the audience and their context. That’s tone.

**보이스 4축 — 모두 “X, but not Y” 형태(상한+하한 동시 규정):**

> ### Be real, but not too tough or overly familiar
> - Use business casual language—be plain-spoken, not pretentious or overly playful
> ### Be proactive, but not needy or pushy
> ### Be dynamic, but not scattered or impulsive
> - Avoid words that generalize success like “every,” “all,” and “most”
> ### Guide, but don’t handhold or prescribe
> - Be specific when explaining benefits without making things sound better than they are
> — archive.org, /web/20241227041731/https://polaris.shopify.com/content/voice-and-tone

**핵심 발명 — 감정 상태 거부:**

> Often people frame tone guidance around adapting to the emotional state of the audience. The reality is we never know a person’s emotional state. Even when things seem the most positive, we can’t be sure. While it’s helpful to consider how your audience is likely to feel, **don’t assume or tell them how to feel.** Instead, focus on the specifics of the situation and less on the emotions.

**상황 6분기 + 각 상황의 실제 Do/Don’t 문자열 (전부 verbatim):**

| 상황 | Do (실제 문자열) | Don’t (실제 문자열) |
|---|---|---|
| Everyday tasks | “Be consistent for identical actions or destinations when possible.” → `Delete product` / `Delete collection` | “Add extra text just to fill space.” |
| Learning and education | “Help people understand why they should do something, not just how.” | “Oversell or overpromise.” → `Create a new campaign and you could double your sales this holiday season.` |
| Learning and education | “Break down complicated tasks into steps…” | “Be overly prescriptive…” → `You need to add at least 10 products before opening your store.` |
| Simple errors | “Clearly explain the situation and how it can be resolved.” → `Product weight needs to be positive. Change the product weight to be greater than or equal to 0 and try again.` | “Use overly dramatic or scary words for simple errors.” → **`Bad request, forbidden, fatal, expectation failed, unresolved, invalid`** |
| Acknowledging effort | “…consider ways to confirm completion without words or messaging.” → `Product saved` | “Refer to simple actions or completed steps as 'successes.'” → `You successfully added a product.` |
| Acknowledging effort | “If the task was something we initiated or required, thank them for their time.” → `Thanks for taking the time to share your feedback.` | “Assume people are excited or celebrating.” → `Congrats! You set up your single login for Shopify.` |
| Motivate action | “Help people understand what the next steps are and why they should take them.” → `Your email address is connected to 8 accounts. Set up a single login to switch between stores faster and log in less often.` | “Assume the next step or outcome is guaranteed.” → `You’re just a few steps away from receiving your first order.` |
| Serious problems | “Explain the impact on their business clearly, without using confusing or scary language.” → `Some of today’s sales data hasn’t been updated yet. This will be fixed shortly. Your data is safe, and your sales are not affected.` | (truncated) |

**에러 메시지 규칙(별도 페이지, archive 2024-12-01):**

> Error messages should:
> - Tell merchants what happened. If there’s a solution, explain it. If possible, offer a one-click fix with a button. If there’s no solution, give troubleshooting instructions.
> - Be placed close to the source of the problem.
> - Communicate severity using the appropriate color and tone of voice.
> - Use plain language.
> - Be specific. For example, use precise numbers and dates.
> - Be brief.

그리고 **금지어를 명시적으로 지정:**

> - Use two or three words to explain what’s wrong or what’s needed to fix the problem.
> - Avoid using the word “invalid” to define an error. When appropriate, use “not valid” instead.

**색 = 심각도 = 톤 매핑:**

> Red is the scariest error color. Only use red for critical messages that merchants need to deal with immediately to avoid harm to their business. … Yellow error messages still demand attention, but are more appropriate for messages that are part of a daily workflow.

**안티패턴까지 규칙화:** “Avoid using toast for error messages”, “Don’t use modals for errors”, “Avoid using home notifications for errors.”

---

### A4. Atlassian Design System — 형용사를 “강도 다이얼”로 만든 유일한 시스템

**보이스 vs 톤:**

> Our voice is essentially Atlassian’s personality and is made up of the following traits: **Bold · Optimistic · Practical, with a wink**
>
> Tone is how we express Atlassian’s voice, and it should change depending on the situation the user is in (for example, receiving an error versus successfully completing a project).

**적용 메커니즘 — 감정 상태 × 사용자 유형으로 강도 결정:**

> How each trait is applied should depend on the audience and situation. Use these questions to help you work out the right balance:
> - What is the emotional state of the user when they encounter your content or solution, and where are they on their journey?
> - How might our personality traits enhance a moment of celebration?
> - How might our personality traits diffuse a moment of frustration or pain?

각 특성마다 3블록: 정의 → 불릿 실천 → **When to be more / When to be less**. 예 (Bold):

> **When to be more bold** — Person is feeling: confident, interested, trust, anticipation. Examples: power users, admins, daily users.
> **When to be less bold** — Person is feeling: apprehension, confusion, annoyance, fear, anger. Examples: new users, trial users, when introducing a new concept, feature, or app.

**모든 시스템 중 가장 명시적인 캐리커처 방지 장치 (“with a wink”의 상한):**

> The 'with a wink' part of this trait needs more discernment when applying it to UI and app content (as opposed to marketing content) and remember that it isn’t always appropriate to use. … **When you can add the 'wink'** — Person is feeling: successful, joy, proud, relief. Examples: power users, during social interactions, success messages.

그리고 6원칙 중 마지막:

> **Delight with unexpectedly pleasing experiences** — You can deliver appropriate delight (a 'wink') by celebrating success or progress, but only once you’ve built trust. Don’t overdo it.
> - Delight means little flourishes, not humor or being cheeky.
> - Always ask yourself what someone might be feeling at that moment and if delight is appropriate. Also question whether it will be understood or appreciated by our global audience.
> - **Think about the timing and how frequently a user will see this. Once may amuse, but a dozen times may annoy.**

**원칙 → UI 컴포넌트 매핑 (매우 실용적):**

> **Inform to build trust** … Places to use 'Inform to build trust' — In-app: flags, error messages, and spotlights; New features or apps; In confusing, warning, or error states
> **Satisfy by meeting expectations** … Places to use — In-app: warning messages, information messages, and error messages; Across all UI and app content

**문법/기계 규칙 (Language and grammar 페이지, 실제 Do/Don’t):**

> **Articles (a, an, the)** — Avoid articles in buttons, labels, and action-based headings in the UI. → Do: `Create password` / Don’t: `Create a password`
> **Capitalization** — Use sentence case in all titles, headings, menu items, labels, and buttons. → Do: `Create work item` / Don’t: `Create Work Item`
> **Contractions** — Use contractions, where possible, as they convey a conversational, friendly tone.
> **Headings** — Avoid gerunds (the 'ing' form of verbs) in UI copy. → Do: `Add a page to your project` / Don’t: `Adding a page to your project`
> **Abbreviations** — Don’t use 'e.g.', 'i.e.', 'etc.', or '&' as they’re not localization friendly and can be confusing for users of assistive technologies.

**포용 언어(inclusive writing)에서 가장 날카로운 구별:**

> **Don’t make assumptions about abilities** … Do: `Set up your new project in a few steps.` / Don’t: `It’s easy to set up a new project.`
> **Avoid metaphors and idioms** … Do: `Automation helps teams create work items faster.` / Don’t: `Automation makes creating work items a piece of cake.`

---

### A5. Microsoft — “Top 10 tips”는 사실상 전후 예시 10쌍이다

**보이스 정의 (4요소 분해):**

> There’s *what* we say, our message. And there’s *how* we say it, our voice.
> The Microsoft voice is how we talk to people. It’s the interplay of **personality, substance, tone, and style**.
> Though our voice is constant regardless of who we’re talking to or what we’re saying, we adapt our tone—**from serious to empathetic to lighthearted**—to fit the context and the customer’s state of mind.
> — https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human

**3원칙 + 각 원칙의 “why”와 “how”:**

> - **Warm and relaxed**—We’re natural. Less formal, more grounded in real, everyday conversations. Occasionally, we’re fun. (We know when to celebrate.)
> - **Crisp and clear**—We’re to the point. We write for scanning first, reading second. We make it simple above all.
> - **Ready to lend a hand**—We show customers we’re on their side. We anticipate their real needs and offer great information at just the right time.

**스타일 팁 3개 (동사로 시작):** “Get to the point fast” / “Talk like a person” / “Simpler is better”

**Top 10 tips = 원칙 1문장 + Replace/With 쌍. 전부 verbatim:**

| # | 원칙 | Replace this | With this |
|---|---|---|---|
| 1 | Use bigger ideas, fewer words | `If you’re ready to purchase Office 365 for your organization, contact your Microsoft account representative.` | `Ready to buy? Contact us.` |
| 2 | Write like you speak | `Invalid ID` | `You need an ID that looks like this: someone@example.com` |
| 3 | Project friendliness | `…Cortana needs to know what you are interested in, what is on your calendar, and who you are doing things with.` | `…Cortana needs to know what you’re interested in, what’s on your calendar, and who you’re doing things with.` |
| 4 | Get to the point fast | `Templates provide a starting point for creating new documents. A template can include the styles, formats, and page layouts that you use frequently. Consider creating a template if you often use the same page layout and style for documents.` | `Save time by creating a document template that includes the styles, formats, and page layouts that you use most often. Then use the template whenever you create a new document.` |
| 5 | Be brief | `The **Recommended Charts** command on the **Insert** tab recommends charts that are likely to represent your data well. Use the command when you want to visually present data and you’re not sure how to do it.` | `Create a chart that’s just right for your data by using the **Recommended Charts** command on the **Insert** tab.` |
| 6 | When in doubt, don’t capitalize | `Find a Microsoft Partner / Office 365 Customer / Limited-Time Offer / Join Us Online` | `Find a Microsoft partner / Office 365 customer / Limited-time offer / Join us online` |
| 7 | Use end punctuation in the right places | `**Move a tile.**` | `**Move a tile**` |
| 8 | Remember the last comma | `Android, iOS and Windows` | `Android, iOS, and Windows` |
| 9 | Don’t be spacey | `Use pipelines — logical groups of activities — to consolidate activities that are part of a task.` | `Use pipelines—logical groups of activities—to consolidate activities that are part of a task.` |
| 10 | Revise weak writing | `You can access Office apps across your devices, and you get online file storage and sharing.` | `Store files online, access them from all your devices, and share them with coworkers.` |
— https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice

**단어 치환 테이블 (Use this / Not this):**

| Use this | Not this |
|---|---|
| use | utilize, make use of |
| remove | extract, take away, eliminate |
| tell | inform, let know |
| to | in order to, as a means to |
| also | in addition |
| connect | establish connectivity |
| `Because` you created the table, you can change it. | `Since` you created the table, you can change it. |

**금지 부사 목록(그대로 lint 가능):** `quite`, `very`, `quickly`, `easily`, `effectively` — “Omit unnecessary adverbs—words that describe how, when, or where. Unless they’re important to the meaning of a statement, leave them out.”
— https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences

**거버넌스:** 편집팀이 없으면 외부 전문가를 쓰라고 명시(“If writing isn’t a functional role your team has, consider bringing in expert help”), 피드백 수신 주소 공개(`msstyle@microsoft.com`).

---

### A6. Google developer documentation style guide — 3열 톤 테이블이 최고의 자산

**보이스 정의:**

> In your documents, aim for a voice and tone that’s **conversational, friendly, and respectful** without using slang or being overly colloquial or frivolous. Use a voice that’s casual, natural, and approachable, not pedantic or pushy. **Try to sound like a knowledgeable friend** who understands what the developer wants to do.
> — https://developers.google.com/style/tone

**“하지 말 것” 목록 14항목 (그대로 금지어 사전이 된다):**

> - Buzzwords or technical jargon.
> - Being too cutesy.
> - Avoid figurative language, which includes metaphors and ableist language.
> - Placeholder phrases like *please note* and *at this time.*
> - Choppy or long-winded sentences.
> - Starting all sentences with the same phrase (such as *You can* or *To do*).
> - Current pop-culture references.
> - Exclamation marks. In general, avoid exclamation points.
> - Wackiness, zaniness, and goofiness.
> - Phrasing that denigrates or insults any group of people.
> - Phrasing in terms of *let’s* do something.
> - Using phrases like *simply*, *It’s that simple*, *It’s easy*, or *quickly* in a procedure.
> - Internet slang, or other internet abbreviations such as *tl;dr* or *ymmv*.

**3열 톤 테이블 — 이 문서에서 가장 이식 가치가 높은 형식 (verbatim):**

| Too informal | Just about right | Too formal |
|---|---|---|
| `Dude! This API is totally awesome!` | `This API lets you collect data about what your users like.` | `The API documented by this page may enable the acquisition of information pertaining to user preferences.` |
| `Just like a certain pop star, this call gets your telephone number. The easy way to ask for someone’s digits!` | `To get the user’s phone number, call user.phoneNumber.get.` | `The telephone number can be retrieved by the developer via the simple expedient of using the get method on the user object’s phoneNumber property.` |
| `Then—BOOM—just garbage-collect, and you’re golden.` | `To clean up, call the collectGarbage method.` | `Please note that completion of the task requires the following prerequisite: executing an automated memory management function.` |

**“please” 규칙(전후 쌍):**

> Recommended: `To view the document, click View.`
> Not recommended: `To view the document, please click View.`

**예외를 명시하는 문법 규칙 (active voice):**

> In general, use active voice … although there are exceptions. …
> - To emphasize an object over an action. → Recommended: `The file is saved.`
> - To de-emphasize a subject or actor. → Recommended: `Over 50 conflicts were found in the file.` Not recommended: `You created over 50 conflicts in the file.`
> - If your readers don’t need to know who’s responsible for the action. → Recommended: `The database was purged in January.`
— https://developers.google.com/style/voice

**셀프 체크 기법(에이전트 지시로 그대로 쓸 수 있음):** “read parts of your document out loud, or at least mouthing the words”; “ask a colleague to take a look”; “If you’re having trouble expressing something, step back and ask yourself, 'What am I trying to say?'”

---

### A7. IBM Style / Salesforce SLDS — 구조는 확인, 본문은 미확보

**IBM Style (https://www.ibm.com/docs/en/ibm-style) — TOC에서 확인된 구조 (본문 UNVERIFIED, JS 렌더링):**

최상위 목차가 **매체/맥락 기준으로 분기**되어 있다. 이것이 IBM의 톤 분기 방식이다:

> Basics · **Audience and medium** · Accessibility · **AI assistants** · **Conversational style** · Global audiences · **LLMs** · **Marketing** · Mobile · Red Hat · **Social media** · Third-party tools · **Tone** · Videos
> … 그리고 별도로 Language and grammar(Abbreviations / Adverbs - only / Anthropomorphism / Articles / Capitalization / … / Pronouns / Verbs), Punctuation, Numbers and measurement, Structure and format(**Messages** / Notes / Paragraphs / Procedures), Word usage, **Topics A to Z**

**배울 점 (구조 차원에서 확실한 것):**
1. `Tone`이 독립 토픽이고, 그 **형제 토픽이 매체(Audience and medium)와 상황(Marketing / Social media / AI assistants / Conversational style)** 이다 → 톤은 매체별로 분기한다는 선언.
2. **`AI assistants`와 `LLMs`가 정식 스타일가이드 토픽** — LLM 상호작용 문체를 엔터프라이즈 스타일가이드가 1급 주제로 편입한 선례. 우리 스킬의 정당성을 뒷받침하는 인용으로 쓸 수 있다.
3. `Adverbs - only` 같은 **단일 품사 토픽**을 독립 항목으로 둔다 → 금지어 사전을 품사 단위로 인덱싱.

**Salesforce Lightning Design System (https://v1.lightningdesignsystem.com/guidelines/voice-and-tone/) — 페이지 전문:**

> Your custom applications shouldn’t just look and act like the Salesforce app – they should sound like it too.
>
> At Salesforce, we have guidelines we follow when we create written content. **We apply the guidelines to text that appears in the app, including on-screen instructions and error messages. We use the same guidelines for other types of information, such as online help, developer doc, Walkthroughs, and Trailhead modules.**
>
> Use the Voice & Tone Guidelines to get a quick introduction to our unique voice and tone… The doc provides some quick writing guidelines, and includes great examples of the voice and tone from the app and the doc.

⚠️ **본문 미확보.** “Download Voice and Tone Guidelines”가 PDF를 가리키지만 PDF URL을 특정하지 못했고, 별도 `Salesforce Style Guide for Documentation and User Interface Text`(developer.salesforce.com)는 JS 렌더링으로 본문 추출 실패. **SLDS의 실제 보이스 형용사·전후 예시는 UNVERIFIED로 남긴다.** 확실한 것은 **“한 벌의 규칙을 UI·help·dev doc·교육 콘텐츠에 공통 적용”** 한다는 선언이며, 이는 우리 스킬의 “any domain” 주장에 유용한 선례다.

---

### A8. 추가 발굴 ①: NHS digital service manual — 톤 분기에 완성 문장을 붙인다

**보이스 5축 (전부 형용사):**

> Our voice is **neutral and factual**. It’s **authoritative**, but also **calm and reassuring**. It’s **empowering, rather than patronising**, and **personal, rather than formal**.

**보이스 → 실천 규칙 (금지어 포함):**

> We:
> - address the user as “you”
> - reassure by saying things like “Sertraline can cause side effects, but many people have no side effects or only minor ones”
> - empower by saying things like “talk to your doctor about...” rather than “your doctor will tell you about...”
> - **avoid using “should” as it can sound patronising**

**톤 분기 — 감정 상태 + 맥락, 그리고 각 분기에 실제 문장:**

> Tone can change depending on the context. We consider the situation and what the emotional state might be for the user.
>
> For example, we may use a **direct, serious and reassuring** tone when writing about a diagnosis:
> *If you’ve had a stroke or heart attack or are at high risk of a heart attack, your doctor may recommend that you take a daily low dose aspirin. This is different to taking aspirin for pain relief. Only take low dose aspirin if your doctor recommends it.*
>
> We may use an **encouraging and conversational** tone when writing about exercise or diet:
> *It’s tempting to skip a session if the weather’s bad. But you’re less likely to use the weather as an excuse if you’ve arranged to exercise with a friend or if you’re following a training programme.*
> — https://service-manual.nhs.uk/content/voice-and-tone

**거버넌스/상속:** “It’s meant as a guide, not a rulebook. You’re welcome to adapt a style pattern if it does not meet your users' needs.” + “Check the GOV.UK A to Z style guide and GOV.UK content design guide for any points of style that you do not find here.” → **연방형 스타일가이드**: 자체 규칙 + 상위 규칙 위임 + Slack/GitHub 이슈로 피드백.

---

### A9. 추가 발굴 ②: 커뮤니티 “style-as-skill” 생태계 — 우리 스킬의 직접 경쟁/선례

이 절은 **Part A의 원래 8개 시스템 범위를 넘어서는 발견**이지만, 우리 스킬이 *실제로 배포될 형태(SKILL.md)* 를 이미 누군가 표준화했다는 점에서 구조 설계에 직접 영향을 준다. 아래는 모두 공개 GitHub 저장소이며, 별점·규모를 함께 적는다(검증 시점 기준, 정확한 수치는 변동).

| 저장소 | 규모 | 무엇을 하는가 | 우리에게 중요한 이유 |
|---|---|---|---|
| `surendranb/writing-skills` | 39★, MIT, npm+PyPI | “16 writing-style skills for AI agents: 9 measurable frameworks, 7 character voices. Plain SKILL.md files.” | **가장 직접적인 선례.** 아래 별도 분석 |
| `yzhao062/agent-style` | 700★, CC-BY-4.0+MIT | “The Elements of Agent Style” — Strunk & White·Orwell·Pinker·Gopen&Swan에서 12개 + LLM 출력 관찰에서 9개 = **21개 규칙**, 각 규칙이 출처 챕터를 인용 | **실제 with/without 벤치를 돌린 유일한 사례.** 규칙을 `RULE-01..12` + `RULE-A..I`로 ID화 |
| `gerizekali/apple-editorial-style` | 0★ | “Apple Style Guide skill for AI agents” | **직접 경쟁.** 30,236 bytes / 950줄 — 표준 권고(500줄) **위반** |
| `rootcastleco/Apple-style-guide-skill` | 0★ | SKILL.md + `agents/openai.yaml` + `references/` 4개 파일, ChatGPT Skills용 `skill.zip` 배포 | **references/ 분리 구조**의 선례. “PDF는 저장소에 포함하지 않음” 명시 |
| `chaos-xxl/apple-design-skill` | 21★ | Apple 스타일 **프론트엔드 UI 코드** (산문 아님) | 인접하지만 중복 아님 |
| `powerstacks-corp/microsoft-style-skill` | 19★ | “audits and rewrites technical documentation to align with the Microsoft Writing Style Guide” | **“벤더 스타일가이드 → audit+rewrite 스킬”** 패턴이 정착했음을 증명 |
| `jzOcb/writing-style-skill` | 271★ (해당 분야 최다) | “AI writes → you edit → rules auto-extracted → SKILL.md” | 자동 규칙 추출 패턴 |
| `shannhk/writing-style-extractor` | 22★ | “Extract writing style DNA… Produces structured **JSON profile** + markdown report” | **공개된 보이스 스키마에 가장 가까움** |
| `donrami/airspeak` | — | “Automatic writing-style **linting** for Markdown prose. English: ASD-STE100 Issue 9. VSCode extension + portable Agent Skill.” | **프롬프트가 아니라 린터로 보이스를 강제**하는 노선 |
| `pasunboneleve/oiticica-style` | 10★ | “A century-old style manual, converted into a taxonomy of agentic writing skills.” | **출판된 스타일 매뉴얼 → 스킬 분류체계** 전환의 선례 (= 우리의 Apple Style Guide 작업과 동형) |
| `petems/ai-prose-review-skill` | — | `yzhao062/agent-style`의 21개 규칙으로 마크다운 산문 감사 | 규칙셋 재사용 패턴 |

**`surendranb/writing-skills`의 `template/SKILL.md` 전문 (이식할 골격, verbatim):**

```
---
name: skill-folder-name
description: One sentence stating what this skill produces and per which standard or character. Use when the user [concrete trigger situations, the actual phrases they'd type, and the contexts where this beats default prose].
---

# Skill Title

One line: the essence of this style in a sentence fragment.

## The core rule

**The single bolded sentence that IS this skill.** One or two sentences of
sharpening — what this style is really doing and the failure it prevents.

Workflow: `first move` → `second move` → `third move` → `run the Verify checklist`.

## Mechanics

1. **Named rule.** Concrete and checkable — a cap, a ban list, a required shape.
2. **Named rule.** "X not Y" with a real example inline.
3. **Named rule.** Numbers where possible (sentence length, ratios, counts).
4. **Named rule.** For voices: include a rate-limit that prevents caricature.

## Verify

- Checkable statement (an agent can pass/fail this mechanically)
- Checkable statement
- Checkable statement

## Do not

- The tempting mistake this style invites
- The failure mode that looks like the style but isn't

## Example transformations

**Before:** "A realistic 'default prose' input."

**After:** "The same content, transformed by the mechanics above."
```

**그리고 이 저장소는 스킬 계약을 CI로 강제한다** (`scripts/validate_skills.py`가 실제로 검사하는 항목, verbatim):

> - each `skills/*/SKILL.md` has parseable frontmatter with name + description
> - frontmatter name matches its folder name
> - **description is trigger-rich: >= 80 chars and contains “Use when”**
> - **required sections present: The core rule, Mechanics, Verify, Do not, and at least two before/after transform examples**
> - **skill body stays context-tight (<= 120 lines)**
> - plugin.json, .claude-plugin/plugin.json, .claude-plugin/marketplace.json parse, agree on version, and the marketplace skill list matches `skills/`

**실제 스킬 예시 (`skills/gov-uk-style/SKILL.md`) — GOV.UK 가이드를 어떻게 압축했는가:**

> ## The core rule
> **Start with the user’s need. Sentences under 25 words, paragraphs under 5 lines, active voice, zero jargon.**
> ## Verify
> - First sentence directly addresses the user’s primary intent
> - Sentences average under 20 words
> - Bullet points used for lists of 3 or more items
> - Zero Latin abbreviations (e.g., i.e., et al.)
> - Active voice used throughout
> ## Do not
> - Use introductory throat-clearing (“It is important to note that...”)
> - Assume prior knowledge of government processes
> ## References
> For exact mechanical rules …, read `references/REFERENCE.md` when a draft includes any of these — **load on demand, not upfront.**

주목할 점: **`## Verify`가 형용사가 아니라 기계적 판정문**이고, **`## Do not`이 “이 스타일이 유혹하는 실수”** 를 지목하며, 세부 규칙은 `references/`로 밀어 **점진적 공개(progressive disclosure)** 를 구현한다. 그리고 “9 measurable frameworks”와 “7 character voices”를 **분리**하고 캐릭터 보이스에는 **“rate-limited against caricature”** 라는 상한을 붙인다 — 애플 스킬이 반드시 겪을 실패 모드(애플풍 과잉 적용 → 패러디)에 대한 정면 답변.

---

## A(c) 우리 스킬에 가져올 구조 패턴 Top 7

각 패턴은 **“왜 좋은가 → 애플 문체 스킬에 어떻게 이식할지”** 순서로 쓴다.

---

### 패턴 1. 보이스 = 상시 불변 / 톤 = 상황 분기, 그리고 **분기 축을 “상황”으로 잡는다 (감정 추정 금지)**

**어디서:** Mailchimp(“You have the same voice all the time, but your tone changes”), Microsoft(“our voice is constant… we adapt our tone”), Atlassian(“Tone is how we express Atlassian’s voice, and it should change depending on the situation”), NHS. **그리고 결정적으로 Shopify Polaris:**

> Often people frame tone guidance around adapting to the emotional state of the audience. **The reality is we never know a person’s emotional state.** Even when things seem the most positive, we can’t be sure. … **don’t assume or tell them how to feel.** Instead, focus on the specifics of the situation and less on the emotions.

**왜 좋은가:** 감정 상태는 관측 불가능하다. 에이전트가 “사용자가 화났을 것이다”를 추론하기 시작하면 **환각된 감정에 근거해 톤을 정한다.** 반면 “상황”은 프롬프트에서 관측 가능하다 — 이 글이 에러 메시지인지, 마이그레이션 가이드인지, 릴리스 노트인지는 텍스트 자체가 알려준다. 관측 가능한 입력에 분기를 걸면 규칙이 결정론적으로 작동한다.

**애플 스킬 이식:** 애플은 감정 기반 톤 가이드를 쓰지 않는다. Apple HIG “Writing”은 “Determine your app’s voice… **Create a list of common terms**, and reference that list to keep your language consistent”라고 말할 뿐, 감정 매트릭스가 없다. 따라서 우리 스킬은 **상황 축만** 쓴다:

```markdown
## Tone is situational, never emotional
Never infer the reader's mood. Classify the content type instead, then apply its row.
| Situation | Tone shift | Apple evidence |
|---|---|---|
| UI microcopy / button | imperative verb, no articles, no first person | "Send", "Favorites" (not "Your Favorites") |
| Error / failure | state the fact, name the fix, no blame, no interjection | "Choose a password with at least 8 characters" (not "That password is too short"); no "oops!" |
| Docs / README | second person, present tense, task-first | "Check each word to be sure it needs to be there" |
| Marketing | warm, concrete benefit, still no exclamation | "As part of Apple's informal voice, contractions are used and recommended" |
| Legal / compliance | same voice, formality up; never paraphrase the binding term | (no Apple evidence — mark as inherited rule) |
| Analytics report | finding first, then number, then caveat | derived from HIG "Be clear" + Part B |
```

**핵심:** 금지 축을 명시한다 — “Do not write a row for 'user is frustrated.' If you cannot tell the situation from the prompt, ask or default to the `Docs` row.”

---

### 패턴 2. 전후 변환 예시가 **규칙의 본체**다 (형용사는 라벨일 뿐)

**어디서:** Microsoft “Top 10 tips” = **10쌍의 Replace/With**. Google = **3열 테이블**. Mailchimp = Yes/No 쌍 5개+. GOV.UK = Bad/Good 쌍 6개+. Polaris = 상황마다 Do/Don’t 쌍. Atlassian = 문법 항목마다 Do/Don’t.

**왜 좋은가:** “Be clear”는 지시가 아니다. `Ready to buy? Contact us.` ← `If you’re ready to purchase Office 365 for your organization, contact your Microsoft account representative.` 는 지시다. 전후 쌍은 ①압축 비율, ②삭제된 단어, ③유지된 정보를 동시에 보여주므로 에이전트가 **변환 연산**으로 학습한다. 형용사만 있으면 에이전트는 형용사를 흉내 낸다. 그리고 Google의 3열 형식은 특히 강력하다 — “이렇게 쓰지 마라”보다 **“이 셋 중 가운데”** 가 훨씬 정밀한 목표 지정이다.

**애플 스킬 이식:** 스킬 본문에 **도메인별 전후 쌍 5~7개**를 넣는다(마이크로카피/에러/README/이메일/한국어). 각 쌍에 **삭제된 것**을 주석으로 단다:

```markdown
**Before:** "We're sorry, but we were unable to save your changes due to an unexpected error."
**After:** "Couldn't save changes. Try again."
# deleted: apology, "We", "unable to", "due to an unexpected error", 3 hedges
```
그리고 Google식 3열을 **한국어 행에 대해** 추가한다(과잉 번역체 ↔ 애플 한국어 ↔ 지나친 격식). 한국어는 Part B가 미검증으로 남긴 영역이므로, 스킬은 **가설임을 명시**하고 검증 대상으로 표시해야 한다.

---

### 패턴 3. `## Verify` — 형용사가 아니라 **기계적 판정문**으로 끝낸다

**어디서:** `surendranb/writing-skills` — *“Every skill ends with a `Verify` checklist the agent must pass before it delivers.”* 실제 예:

> ## Verify
> - First sentence directly addresses the user’s primary intent
> - Sentences average under 20 words
> - Bullet points used for lists of 3 or more items
> - Zero Latin abbreviations (e.g., i.e., et al.)
> - Active voice used throughout

그리고 이 저장소는 이 계약을 **CI로 강제한다**: `description` ≥80자 + “Use when” 포함, 필수 섹션 4개, 전후 예시 ≥2개, 본문 ≤120줄.

**왜 좋은가:** `Verify`는 스킬을 **자기 채점 가능**하게 만든다. 없으면 에이전트는 초안을 내놓고 끝낸다. 있으면 낸 뒤에 한 번 더 본다. 결정적으로, 체크 가능한 항목만 넣으면 **캐리커처를 잡는다** — “애플처럼 들리는가?”는 체크할 수 없지만 “`!`가 0개인가”, “`we`가 0개인가”, “버튼 라벨이 동사로 시작하는가”는 체크할 수 있고, 애플 과잉 적용은 대개 이 항목들에서 먼저 드러난다.

**애플 스킬 이식:** Part A의 조사에서 **실제로 애플이 문서화한 기계적 규칙**만 넣는다(출처: Apple HIG “Writing”, Apple Style Guide):

```markdown
## Verify (run before delivering; report failures honestly)
- [ ] Contractions present where natural (Apple: "used and recommended throughout most documentation, interface text, and marketing copy")
- [ ] Passive voice absent unless active would be convoluted or anthropomorphic (ASG's own stated exception)
- [ ] No first-person "we" in product copy (HIG: "Avoid using we altogether")
- [ ] No possessive pronouns where a bare noun works ("Favorites" not "Your Favorites")
- [ ] No interjections: no "oops", "uh-oh", "Whoops" (HIG: "typically unnecessary and can sound insincere")
- [ ] Action labels are verb-first: "Send" not "Let's do it!"
- [ ] No blame in errors: instruction, not accusation
- [ ] "tap" for touch, never "click"
- [ ] Sentence case for UI; title case reads as formal (HIG: "Title case is generally considered formal, while sentence case is more casual")
```

**중요:** 각 항목에 **출처를 붙인다.** 근거 없는 체크리스트는 에이전트가 즉흥적으로 채운다.

---

### 패턴 4. 금지어를 **치환 규칙**으로 준다 (금지 목록이 아니라)

**어디서:** GOV.UK “Words to avoid” — 30개 항목 전부 `단어, use 'X' instead` 형식. Microsoft — `Use this / Not this` 테이블. Atlassian — `e.g./i.e./etc./&` 금지 + 이유(“not localization friendly”). Google — 14항목 avoid 목록 + `please` 제거 예시.

**왜 좋은가:** 금지어는 에이전트를 마비시킨다(지우고 나면 빈칸이 남는다). 치환어를 주면 **지웠을 때 무엇을 넣을지** 안다. 또한 GOV.UK은 **예외를 단어마다 조건으로** 명시한다 — “leverage (unless in the financial sense)”, “key (unless it unlocks something)”, “combat (unless military)”. 이건 단순 블랙리스트로는 불가능한 정밀도이고, 에이전트가 문맥 판단을 하도록 강제한다.

**애플 스킬 이식:** 애플이 쓰는 **금지가 아니라 선호** 목록을 치환표로 만든다. 예: `in order to → to`, `utilize → use`, `navigate to → open`, `in the event that → if`, `please → (delete)`, `we’re sorry → (delete)`. 주의: **한국어 치환표는 근거가 없다.** 스킬에서 한국어 치환은 “Part B 미검증”으로 라벨링하고, 후보로만 제시한다(예: `~해 주시기 바랍니다 → ~하세요`, `~할 수 있습니다 → ~합니다`).

**그리고 반드시 붙일 것 — 캐리커처 상한.** Atlassian이 “wink”에 붙인 장치를 그대로 베낀다:

> Delight means little flourishes, not humor or being cheeky. … **Think about the timing and how frequently a user will see this. Once may amuse, but a dozen times may annoy.**

애플 스킬 버전: “Apple’s restraint is itself the device. If a draft contains more than one deliberately 'Apple-ish' flourish — a fragment stack, a dry aside, a mid-sentence reversal — cut it to one. Repetition of the signature move is the parody.”

---

### 패턴 5. 같은 규칙을 **세 해상도**로 중복 게시한다 (TL;DR → 규칙 → A to Z)

**어디서:** Mailchimp는 동일 내용을 ①`TL;DR` 한 페이지(불릿 ~40개), ②본문 섹션별 설명+예시, ③`Word List` + `Grammar and Mechanics` 사전 **세 층**으로 낸다. GOV.UK은 ①Writing guidelines 8개 페이지, ②A to Z style guide(수백 항목), ③Technical A to Z. `surendranb/writing-skills`는 이를 **점진적 공개**로 구현한다: `## The core rule`(1문장) → `## Mechanics`(번호 규칙 8개) → `references/REFERENCE.md`(**load on demand, not upfront**).

**왜 좋은가:** 세 독자가 있다 — 훑는 사람, 쓰는 사람, 특정 단어를 찾는 사람. 그리고 에이전트에게는 **컨텍스트 예산** 문제가 있다. Agent Skills 표준은 “Keep SKILL.md body under 500 lines”이고 “The context window is a public good”라고 못 박는다. A to Z 사전을 본문에 넣으면 예산이 터진다(직접 경쟁 스킬 `gerizekali/apple-editorial-style`이 **950줄로 이 예산을 위반**한다 — 우리의 구조적 우위).

**애플 스킬 이식 — 3층 구조:**

```
SKILL.md            (~120줄)  트리거 description + core rule + 상황표 + Verify + Do not + 전후 예시 5쌍
references/
  apple-rules.md    규칙 상세 + 각 규칙의 HIG/ASG 출처 인용
  transformations.md 전후 쌍 확장판 (도메인 × 언어)
  ko-notes.md       한국어 미검증 가설 + 후보 치환표 (명시적 UNVERIFIED 라벨)
```
그리고 **“load on demand”** 를 본문에 명시: 초안이 날짜/단위/UI 라벨을 포함할 때만 해당 reference를 읽는다.

---

### 패턴 6. 문서가 스스로 **상속·우선순위·예외**를 선언한다

**어디서:** 네 곳에서 독립적으로 같은 장치가 나온다.
- `gerizekali/apple-editorial-style`: **7단계 “Authority and precedence”** — 사용자 요구 > 실제 제품 UI > 공식 Apple 용어 > 이 스킬/ASG > 프로젝트 스타일시트 > Chicago > Merriam-Webster.
- NHS: “It’s meant as a guide, not a rulebook… Check the **GOV.UK A to Z style guide** … for any points of style that you do not find here.” → **상위 규칙으로 위임.**
- GOV.UK: “There are some circumstances when the passive voice can work. These include: when the outcome is more important than the agent of the action…” → **예외를 규칙 안에.**
- Google: passive voice 예외 3가지, Apple ASG: passive 허용 조건(“when using the active voice would require either a highly convoluted sentence structure or excessive anthropomorphism”).

**왜 좋은가:** 규칙에는 반드시 충돌이 생긴다. 충돌 해소를 문서가 미리 선언하지 않으면 에이전트는 **가장 최근에 읽은 규칙**을 따른다(비결정론). 우선순위를 선언하면 충돌이 결정론적으로 해소된다. 그리고 “예외를 명시”하는 것은 규칙을 약화시키는 게 아니라 **강화**한다 — 예외가 적힌 규칙만이 나머지 경우에 대해 단호해질 수 있다.

**애플 스킬 이식:**

```markdown
## Precedence (resolve conflicts in this order)
1. The user's explicit instruction for this task.
2. Existing product/UI terminology — never silently rename a shipped label, string, or API name.
3. The Apple Style Guide term, if this text is English Apple-adjacent copy.
4. This skill's rules.
5. The host project's own style guide.
If two rules conflict and this list does not resolve it, state the conflict instead of guessing.

## Protected text — never alter silently
Code, identifiers, filenames, UI labels quoted from a real product, legal/contractual wording,
numbers and units, and any quoted source. If a fix requires changing protected text, flag it.
```
이 “protected text” 조항은 직접 경쟁 스킬 두 곳(`gerizekali`, `rootcastleco`)과 Apple Style Guide가 모두 요구하는 사항이며, **평가에서 non-modification 픽스처로 검증 가능**하다(→ A(d)).

---

### 패턴 7. 규칙마다 **“왜”와 “실패 모드”를 함께 적는다** (`## Do not` = 유혹 목록)

**어디서:** `surendranb/writing-skills`의 `## Do not` 섹션 정의가 정확히 이것이다 — *“The tempting mistake this style invites”* / *“The failure mode that looks like the style but isn’t”*. GOV.UK은 규칙마다 연구 근거를 링크한다(80%가 평문 선호, 97%가 'among other things' 선호). Anthropic 프롬프팅 가이드도 같은 원리다: `NEVER use ellipses`보다 **“Your response will be read aloud by a text-to-speech engine, so never use ellipses…”** 가 강하다(“Claude is smart enough to generalize from the explanation”).

**왜 좋은가:** 이유 없는 금지는 새 문맥에서 무너진다. 이유가 있으면 **일반화**된다. 그리고 문체 스킬의 최대 실패 모드는 규칙 위반이 아니라 **과잉 준수**다 — 애플 문체를 흉내 내려다 파편 문장만 남은 글, 모든 문장이 반전으로 끝나는 글. 이 실패는 “하지 마라”가 아니라 **“이렇게 보이면 그것은 이 스타일이 아니다”** 로만 잡힌다.

**애플 스킬 이식:**

```markdown
## Do not
- **Do not confuse brevity with omission.** Cutting a necessary condition is not Apple-brief; it is
  a bug. Apple's "Check each word to be sure it needs to be there" removes words, not information.
- **Do not stack fragments.** One deliberate fragment per paragraph is a device. Three is a tic.
- **Do not manufacture warmth.** Contractions are recommended; exclamation marks and "Oops!" are not.
  Enthusiasm that the product has not earned reads as insincere.
- **Do not apply UI brevity to prose.** "Send" is right for a button and wrong for a paragraph.
  The situation table governs which rules are in force.
- **Do not rewrite protected text** to make it sound better.
- **Do not use this skill's Korean rules as established fact.** Part B did not verify Korean
  Apple prose. Treat Korean guidance as a labelled hypothesis.
```

---

## A(d) 보이스 매칭을 어떻게 검증할 것인가

핵심 전제: **“애플처럼 들리는가?”는 직접 채점할 수 없다.** IFEval(Zhou et al., arXiv 2311.07911)은 채점 가능한 지시 25개만 다루며 톤을 의도적으로 제외한다 — *“when judging if LLM’s responses follow given instructions such as 'write with a funny tone' … the underlying standard is greatly unclear.”* Agent Skills 표준도 같은 한계를 인정한다: *“writing style… whether the output 'feels right' — are hard to decompose into pass/fail checks. These are better caught during human review.”*

따라서 검증은 **네 층으로 분해**해야 한다. 각 층은 서로 다른 것을 증명하며, 어느 하나도 단독으로 “보이스 매칭”을 증명하지 못한다.

| 층 | 무엇을 증명하는가 | 방법 | 비용 |
|---|---|---|---|
| **L1 기계 린트** | 문서화된 기계적 규칙을 지켰다 | 규칙별 위반/준수 픽스처 + Vale/스크립트 | 낮음, 결정론적 |
| **L2 자기 점검** | 에이전트가 납품 전에 스스로 잡았다 | `## Verify` 체크리스트 (스킬 본문 내장) | 낮음, 비결정론적 |
| **L3 A/B 벤치** | 스킬이 **없을 때보다** 나아졌다 | with-skill / without-skill, 클린 컨텍스트 | 중간 |
| **L4 블라인드 판정** | 사람이 봐도 더 낫다 | 순서 교체 + 길이 맞춤 + 블라인드 비교 | 높음, 최고 가중치 |

---

### L1. 기계 린트 — **위반/준수 쌍(paired fixtures)** 이 정답이다

가장 falsifiable한 설계. `donrami/airspeak`가 쓰는 패턴을 그대로 베낀다: 규칙 패밀리마다 `violating` 샘플과 `conforming` 샘플을 짝지어 두고, 테스트가 **두 가지를 동시에 주장**한다 — ①위반 샘플에서 발화한다, ②**준수 샘플에서는 침묵한다**(`expect(runChecks("en", samples.conforming)).toEqual([])`). 두 번째가 없으면 린터는 항상 켜져 있는 소음기가 된다. 중립 대조군(control)도 넣어 오탐 0을 함께 주장한다.

**애플 보이스용 위반/준수 쌍 (Part A의 1차 출처에서 도출):**

| 규칙 (출처) | Violating | Conforming |
|---|---|---|
| No interjections (HIG) | `Oops! Something went wrong.` | `Couldn’t load. Try again.` |
| No first-person “we” (HIG) | `We’re having trouble loading this content.` | `Unable to load content.` |
| Possessive pronouns sparingly (HIG) | `Your Favorites` | `Favorites` |
| Instruction not blame (HIG) | `That password is too short.` | `Choose a password with at least 8 characters.` |
| Verb-first action label (HIG) | `Let’s do it!` | `Send` |
| Contractions present (ASG) | `It is not possible to save.` | `It’s not possible to save.` — 또는 `Can’t save.` |
| Passive avoided (ASG) | `The file was saved by the app.` | `The app saved the file.` |
| Touch verb (HIG) | `Click Done.` (touch context) | `Tap Done.` |
| Protected text (ASG + 경쟁 스킬 2곳) | `Save changes to config.yaml` → `Save changes to configuration file` | `Save changes to config.yaml` (변경 없음) |

**주의:** airspeak 저자 본인의 고백을 우리도 인정해야 한다 — *“Never use for marketing copy, essays, creative writing, or anything that needs a distinctive voice. These specs intentionally strip voice.”* **린트는 보이스가 아니라 기계를 강제한다.** L1만 있으면 애플 문체가 아니라 STE100 문체가 나온다.

**기술 스택 후보:** `Vale`가 사실상 표준이다. 규칙 1개 = YAML 1개(`extends` / `message` / `level` / `scope` / `action`), 용어는 `Vocab = <name>` → `config/vocabularies/<name>/{accept.txt,reject.txt}` (한 줄에 정규식 하나). `accept.txt`는 `Vale.Terms` 치환을 자동 생성해 **대소문자까지 강제**한다. **`level: error`만 CI를 실패시킨다** → 애플 규칙은 `error`(금지어·protected text), 취향은 `warning`(문장 길이)로 나눈다. GitLab의 정책이 좋은 선례다: *Error = 브랜딩/상표/렌더링 파손, Warning = 스타일가이드 원칙, Suggestion = 선호.* 참고로 `vale-cli/Google` 36규칙, `errata-ai/Microsoft` 48규칙이 공개되어 있어 **애플 규칙셋도 같은 형식으로 배포 가능**하다.

**한국어는 백지다.** 어떤 textlint 스타일 프리셋도 한국어용이 없다. 현실적 경로는 ①`textlint-rule-prh`(YAML 용어 사전), ②`dictionary-ko`(Hunspell 목록)를 Vale `spelling`으로, ③`jhaemin/speller-api`·`ssut/py-hanspell`(맞춤법만). 즉 **한국어 문체 린트는 우리가 처음 만들거나, 만들지 않는다고 정직하게 선언**해야 한다.

---

### L2. `## Verify` — 납품 전 자기 점검 (스킬 본문에 내장)

`surendranb/writing-skills`의 계약: *“Every skill ends with a `Verify` checklist the agent must pass before it delivers.”* 그리고 이 계약을 CI가 강제한다(`## The core rule`, `## Mechanics`, `## Verify`, `## Do not` 4개 섹션 필수, 전후 예시 ≥2, 본문 ≤120줄).

**설계 원칙:** `Verify` 항목은 **에이전트가 기계적으로 pass/fail 할 수 있어야** 한다. “애플처럼 들리는가”를 넣으면 항목이 무의미해진다. A(c) 패턴 3의 체크리스트를 그대로 쓴다.

**그리고 `Verify`는 결과를 보고하게 한다** — 조용히 실패하지 않도록. 예: `Verify: 9/9 passed` 또는 `Verify: 7/9 — "we" 2회 발견(3행, 11행), 미수정 사유: 인용문 내부`.

---

### L3. A/B 벤치 — 표준이 규정한 with/without 설계

Agent Skills 표준의 평가 방법론(`evals/evals.json`)이 핵심 패턴을 못 박는다:

> **“Run each test case twice: once with the skill and once without it (or with a previous version). This gives you a baseline.”**

레이아웃: `iteration-N/eval-<name>/{with_skill,without_skill}/{outputs/,timing.json,grading.json}` + 집계 `benchmark.json`. 각 실행은 **클린 컨텍스트**에서 시작. **어서션은 첫 실행 결과를 본 뒤에** 작성. 채점은 PASS/FAIL + **인용 근거** 필수 — *“Require concrete evidence for a PASS. Don’t give the benefit of the doubt.”* 그리고 진단 규칙: 양쪽 arm에서 항상 통과하는 어서션은 **버린다**, 항상 실패하는 것은 조사한다, 스킬이 있을 때만 통과하는 것이 진짜 신호다.

**실제로 돌아간 유일한 공개 벤치(`yzhao062/agent-style`, 700★)** 의 숫자와 — 더 중요하게 — **그 한계 공개 방식**을 베낀다: Opus 4.7 88→47 위반(−47%), GPT-5.4 48→26(−46%), Gemini 3 Flash 65→9(−86%), Copilot CLI 52→52(노이즈 대조군). 저자들이 스스로 밝힌 한계: 기계적 채점이 **21규칙 중 7개만** 커버, **3개 규칙이 감소의 94%** 를 만들어냄, 그리고 **“Both critical-severity rules are measured by nothing here.”** “Numbers are directional and carry no claim of statistical significance.”

**우리도 같은 문장을 써야 한다.** 벤치 숫자를 자랑하는 것보다 **무엇을 측정하지 않았는지** 밝히는 것이 신뢰를 만든다.

**평가 케이스는 주장하는 도메인을 전부 덮어야 한다:** 마이크로카피 · 에러 메시지 · README · 분석 리포트 · 이메일 · **한국어**. 최소 3개, 표준은 더 권장. 그리고 **여러 모델 등급에서 테스트**한다 — “What works perfectly for Opus might need more detail for Haiku.”

---

### L4. 블라인드 판정 — 최고 가중치, 그러나 편향 통제 필수

표준의 권고: *“present both outputs to an LLM judge without revealing which came from which version. The judge scores holistic qualities… on its own rubric, free from bias about which version 'should' be better.”*

**그런데 LLM 판정자는 심하게 편향되어 있다. 통제 없이는 이 층이 무효다:**

| 편향 | 측정된 크기 | 출처 | 우리의 통제 |
|---|---|---|---|
| **위치 편향** | 순서 교체 시 일관성 Claude-v1 23.8% / GPT-3.5 46.2% / GPT-4 65.0% | Zheng et al., arXiv 2306.05685 | **모든 비교를 순서 교체해 2회 실행**, 불일치 쌍은 폐기 |
| **장황함 편향** | “repetitive list” 공격 실패율 91.3% / 91.3% / 8.7% | 동일 | **길이 맞춤(length-match)** 후 비교 |
| **자기 선호** | GPT-4 +10%, Claude-v1 +25% 승률 | 동일 | 판정 모델 ≠ 생성 모델. 가능하면 다중 판정자 |
| **자기 인식 상관** | 자기 인식 능력과 자기 선호가 **선형 상관** | Panickssery et al., arXiv 2404.13076 | 동일 |
| **저 perplexity 선호** | “regardless of whether the outputs were self-generated” — 편향의 본질이 perplexity | Wataoka et al., arXiv 2410.21819 | **결정적 함정.** “Claude처럼 들린다” ≠ “애플처럼 들린다” |
| **참조 없는 지표의 순환성** | “equivalent to using one generation model to evaluate another… inherently biased toward models which are more similar to their own” | Deutsch, Dror & Roth, arXiv 2210.12563 | 판정 기준(reference)을 **사람이 쓴 애플 실문장**으로 고정 |

**styletransfer 문헌이 주는 가장 중요한 경고 (GYAFC, Rao & Tetreault, Grammarly, NAACL 2018 — https://arxiv.org/abs/1803.06535):** 그들이 만든 **formality 분류기가 도메인 데이터에서 사람 판단과 ρ = 0.38밖에 상관하지 않았다**(도메인 재학습 후에도 ρ = 0.56). 그리고 **BLEU는 사람의 전체 순위와 음의 상관(−0.48/−0.43)** 을 보였고, PINC는 음의 상관이어야 하는데 **양의 상관(+0.11)** 을 보였다. → **스타일 분류기 점수와 BLEU를 보이스 매칭의 주 지표로 쓰면 안 된다.** 문체 전환은 단어를 바꾸는 것이 목적이므로 n-gram 겹침 지표가 원리적으로 어긋난다.

**Mir et al. (arXiv 1904.02295)** 의 실무적 결론도 그대로 쓴다: **절대 점수보다 상대 비교가 신뢰도가 높다**(naturalness에서 Fleiss κ 0.170 → 0.526). 그리고 논문 간 비교 불가 — “target-style scoring may not be directly comparable across papers due to different classifiers used in evaluations.”

**따라서 L4의 루브릭은:** ①내용 보존, ②애플다움(사람이 쓴 애플 실문장 대비), ③자연스러움, ④**과잉 적용 없음**(캐리커처 항목을 **별도 감점 항목**으로) — 4항목, 각 5점, **상대 비교만**. 판정자는 산문 rubrik를 받고, 어느 쪽이 스킬 산출물인지 모른다.

**사람 검토는 필수로 남는다.** 표준과 IFEval이 모두 인정한 한계이며, 우리가 그 한계를 없앴다고 주장해서는 안 된다. 대신 **사람 검토를 줄이는 것**을 목표로 한다(기계적 층이 명백한 실패를 먼저 걸러냄).

---

### L5. 반드시 넣어야 할 두 가지 특수 픽스처

**① Protected text 픽스처 (non-modification 단언).** 직접 경쟁 스킬 두 곳(`gerizekali/apple-editorial-style`, `rootcastleco/Apple-style-guide-skill`)과 Apple Style Guide가 **모두** 요구한다: UI 라벨, 제품명, 코드, 법률 문구를 조용히 바꾸지 말 것. 테스트는 리라이트 모드에 protected text가 섞인 입력을 주고 **해당 부분이 바이트 단위로 동일함**을 단언한다. 이 픽스처가 없으면 스킬은 “문체를 좋게 만들려다 API 이름을 바꾸는” 최악의 실패를 한다.

**② 한국어 픽스처 쌍.** 어떤 경쟁 스킬도 한국어를 테스트하지 않고, 어떤 한국어 문체 린트 규칙셋도 없다. 최소 1쌍(위반/준수)을 넣어 **다국어 주장을 실제로 시험**한다. 동시에 `references/ko-notes.md`에 **UNVERIFIED 라벨**을 붙인다 — Part B가 검증하지 않은 것을 사실처럼 쓰면 그것이 가장 큰 리스크다.

---

### L6. 최소 실행 프로토콜 (권장 순서)

1. **`evals/evals.json`을 먼저 쓴다.** 스킬을 쓰기 전에. 최소 3개, 주장하는 도메인 전부(마이크로카피 · 분석 리포트 · README · 이메일 · **한국어**).
2. 각 케이스를 **with skill / without skill**, **클린 컨텍스트**로 실행 → `benchmark.json`(+ `timing.json`).
3. 기계적 애플 규칙마다 **위반/준수 픽스처 쌍** 추가, 발화 + 중립 대조군 오탐 0을 함께 단언. Vale 규칙셋으로 배포.
4. **Protected text 픽스처** 추가(non-modification 단언).
5. **한국어 픽스처 쌍** 1개 추가.
6. 최고 가중치 판정은 **블라인드 + 순서 교체 + 길이 맞춤** 비교로. 루브릭 4항목 공개.
7. `benchmark.json`에 with/without 델타 + **명시적 한계 공개**를 함께 게시(3개 규칙이 델타 대부분을 만들었다면 그렇게 쓴다).
8. 양쪽 arm에서 항상 통과하는 어서션은 삭제하고 반복.

**그리고 정직하게 남길 문장:** 이 하네스는 *문서화된 기계적 규칙*의 준수를 증명한다. **“애플의 목소리” 자체를 증명하지는 않는다.** 우리가 증명할 수 있는 것과 없는 것을 스킬 문서에 나눠 쓰는 것이, 검증되지 않은 형용사를 늘어놓는 것보다 강하다.

---

## A(e) Part A가 확립하지 못한 것

- **Salesforce SLDS / IBM Style의 실제 보이스 형용사와 전후 예시** — 두 곳 모두 배포 구조(페이지/PDF, JS 렌더링) 때문에 본문 미확보. `UNVERIFIED`로 남긴다.
- **Stripe에는 공개 스타일가이드가 없다.** `docs.stripe.com/style` 등 7개 URL 404, `docs.stripe.com/sitemap.xml` 전체에 style/voice/tone/contributing 페이지 없음. → Stripe를 “공개 문서화된 시스템”으로 인용하지 말 것.
- **BBC GEL voice guidance** — 페이지 500 오류로 미확보. BBC News style guide + John Allen PDF + Editorial Guidelines 2025로 대체.
- **Buffer / Linear / Vercel** — Buffer voice-and-tone URL 404, Linear `method`·Vercel `design/writing`은 클라이언트 렌더링으로 본문에 가이드 텍스트 없음. **공개 가이드 없음.**
- **한국어 문체 규칙** — 어떤 시스템도 제공하지 않는다. Mailchimp의 “Writing for Translation”이 유일하게 문화권별 격식 문제를 다루며(*“in some cultures, informal text may be considered offensive”*), 그 섹션이 가이드 전체보다 우선한다고 선언한다. 이 **우선순위 역전 선언**은 우리 한국어 섹션에 그대로 이식할 가치가 있다.
- **`web.archive.org` 가용성은 세션별로 다르다.** Part A 작성 시점에는 CDX API와 스냅샷 조회가 모두 동작했으나, 병렬 조사 에이전트는 같은 세션에서 *“Internet Archive services are temporarily offline”* 을 받았다. 아카이브 의존 인용은 **재현 불가할 수 있음**을 전제로 읽어야 한다.
- **“tech 기업들이 Strunk & White를 인용한다”** 는 통념은 1차 출처로 확인하지 못했다. 확인된 것은 Strunk의 규칙이 **번호가 붙은 명령형 규칙**으로 살아남아 현대 도구에 이식됐다는 패턴 자체다(*III. Elementary Principles of Composition*, Rule 13 “Omit needless words”, 1920년 원문은 퍼블릭 도메인 — Project Gutenberg #37134).

---

## A(f) 참고 — Part A가 놓친 것으로 조사된 추가 시스템 (요약만)

지면 관계상 표에 넣지 않았으나, **보이스 검증**과 **교차 확인**에 유용한 항목들:

- **NN/g “The Four Dimensions of Tone of Voice”** (Kate Moran, 2016-07-17, 2023-08-16 재검토) — https://www.nngroup.com/articles/tone-of-voice-dimensions/ — 톤을 **4개 양극 축의 좌표**로 정의: Formal↔Casual, Serious↔Funny, Respectful↔Irreverent, Matter-of-fact↔Enthusiastic. 그리고 **동일 메시지를 4개 톤으로 쓴 사다리**가 이 조사 전체에서 가장 좋은 교수 장치다: `We apologize, but we are experiencing a problem.` → `We’re sorry, but we’re experiencing a problem on our end.` → `Oops! We’re sorry, but we’re experiencing a problem on our end.` → `What did you do!? You broke it! (Just kidding. We’re experiencing a problem on our end.)`. **주의:** 통계적으로 유의하지만 *“the actual differences in the ratings were rather small, around 0.5–1 point on a 5-point scale”* — 즉 톤 축은 **측정 가능하되 효과 크기는 작다.**
- **NN/g “Error-Message Guidelines”** (Neusesser & Sunwall, 2023-05-14) — https://www.nngroup.com/articles/error-message-guidelines/ — 금지어 목록: *“invalid, illegal, or incorrect”* — **Polaris의 “invalid 금지”와 독립적으로 일치**한다. 두 시스템이 같은 단어를 금지한다는 것은 강한 신호.
- **Hemingway Editor** — https://hemingwayapp.com/help/docs/highlighted-issues — 색상=규칙 카테고리(Red/Yellow 난이도, Blue: Adverbs·Passive Voice·Qualifiers, Purple: 더 단순한 동의어), 기본 **grade 9** 목표, 3개 프리셋(Accessible/Default/Technical). 그러나 도구 스스로 반대 논거를 제공한다: *“writers like Ernest Hemingway produced novels for adults that score at a 5th-grade reading level”*, *“Rules are meant to be broken.”* → **가독성 점수를 보이스 매칭 지표로 쓰지 말 것.**
- **plainlanguage.gov** — https://digital.gov/guides/plain-language (원 URL은 리다이렉트; 정본 소스는 GSA 저장소 `github.com/GSA/plainlanguage.gov`) — **“Don’t say | Say” 약 350행 테이블**, 그중 12개를 **“dirty dozen”** 으로 굵게 표시. 54단어 → 22단어 압축 예시가 방법론 전체를 보여준다.
- **Strunk, *The Elements of Style* (1920, 퍼블릭 도메인)** — Project Gutenberg #37134 — **III. Elementary Principles of Composition 8~18번**, 특히 **Rule 13 “Omit needless words”** 와 그 치환쌍(`the question as to whether → whether`, `he is a man who → he`, `the fact that I had arrived → my arrival`).
- **37signals / Basecamp house style** — https://github.com/basecamp/house-style — **산문 가이드가 아니라 린트 설정으로 하우스 스타일을 인코딩**한다: `rubocop-37signals` gem + `@37signals/eslint-config` + `@37signals/stylelint-config-scss`, 그리고 **“App-specific config may follow, overriding the house style.”** 거버넌스가 “편집위원회”가 아니라 **“공유 설정 + 프로젝트별 오버라이드”**. 이는 부록 B의 `AGENTS.md`/`CLAUDE.md` 계층과 같은 발상이다.
- **BBC** — https://www.bbc.co.uk/newsstyleguide/ + John Allen *BBC News Styleguide* (92pp PDF) + https://www.bbc.co.uk/editorialguidelines/guidelines/ — **예외를 1급 콘텐츠로** 취급하는 최고 사례: *“Sometimes, though, the passive is better. Active: A rhinoceros trampled on Prince Edward at a safari park today. Passive: Prince Edward was trampled on by a rhinoceros… In this example, the focus of the story is Prince Edward, not the rhinoceros.”* 그리고 금지 목록의 비절대적 프레이밍: *“The words and phrases in these lists are not banned… at least be aware that when you do you are straying into the superficially attractive word store which produces second-hand, second-rate writing.”*
- **Acrolinx(현 Markup AI)** — 보이스 점수를 **공식으로** 공개한 유일한 사례: `goal score = normalized document length / (normalized document length + issue count)`, 1~100, **Green >79 / Yellow 60~79 / Red <60**. 톤을 **Informality(80–100 Friendly … 0–20 Stiff)·Liveliness·Flesch** 지수로 분해. → 우리 L1 린트에 점수를 붙일 때 참고할 수 있는 유일한 공개 공식.
- **Typeface** — **결정론과 확률론의 분리**가 인상적: *“Banned terms are blocked outright, rules and tone are injected directly into generation.”* 그리고 **“Brand Linting”이 규칙셋 자체를 검증**한다(스키마 위반·중복 규칙·모순·깨진 상호참조·경계 조건). **모순 탐지는 우리 스킬에도 필요하다** — 1,000줄 스킬은 반드시 자기모순을 만든다.

---

---

# Part B — Apple evidence

> **Status note.** Part B was produced by a separate agent from Part A and is self-contained. Every sentence quoted below was retrieved by direct HTTP fetch during this research session (2026-09-30). Nothing here is quoted from memory. Where a claim is someone else’s, it is labelled as such; where it is a count, the sample is stated.

## B0. Method, and what “retrieved” means here

`web_fetch` on `apple.com` product pages returns navigation chrome only, because those pages are client-rendered. That is a real limitation and it is why many attempts to analyse Apple’s copy stop at the nav bar.

**What worked instead:** `curl` with a desktop User-Agent returns the full server-rendered HTML for these surfaces, including the marketing copy, the `<li id="footnote-N">` small print, and the Korean locale pages. So the corpus below was retrieved, parsed with BeautifulSoup, and quote-checked against the raw HTML. Retrieval notes:

| Surface | Retrieval result |
|---|---|
| `apple.com/<product>/` (M5-era pages) | ✅ full HTML via `curl` (500 KB – 1 MB); `web_fetch` → nav only |
| `apple.com/kr/<product>/` | ✅ full HTML; Korean copy is server-rendered |
| `support.apple.com/en-us/<id>` | ✅ server-rendered; `web_fetch` returned `unsupported content type` |
| `apple.com/legal/...` | ✅ server-rendered |
| `apple.com/newsroom/...` | ✅ server-rendered (both `web_fetch` and `curl`) |
| `apps.apple.com` product pages | ✅ server-rendered (description, subtitle, release notes) |
| `developer.apple.com` | ✅ server-rendered |

**Two corpus hazards worth knowing before you quote Apple:**

1. **Scroll-reveal duplication.** Apple’s HTML emits both a start-frame and an end-frame copy of scroll-animated text. Naive extraction yields artifacts such as `Decide which apps are allowed to track track you.` and `Simple. Secure. So not a password .` and `Read Read, , delete, delete , and reply with peace of mind.` These are **extraction artifacts, not Apple typos** — the real strings are `Decide which apps are allowed to track you.`, `Simple. Secure. So not a password.`, `Read, delete, and reply with peace of mind.` Do not quote the doubled forms as Apple errors.
2. **One artifact that *is* in the served HTML.** On `apple.com/macbook-pro/` the M5 Pro bento tile literally contains `Fly through demanding AI tasks up to 86x faster.` with footnote 3 — verified in raw HTML as `up to 86x\xa0faster.` Sibling tiles read `up to 6x` and `up to 7.8x`. This is most likely a missing space between a revised figure (“8x”) and its footnote marker, shipped live. It is a useful reminder that even Apple’s copy operation ships typos, and it is *not* a stylistic rule.

## B1. The corpus — 52 retrieved sentences

Each entry: `[ID] category — sentence (verbatim) — source URL`. Footnote markers are reproduced as they appear (`¹`, `**`, `◊`) but the superscript digits in the raw HTML are stripped because they are `<sup>` elements; where a marker matters it is shown as a bracketed note. **Counts derived from this corpus are counts of this corpus — 52 sentences from 24 pages — not of apple.com as a whole.**

### B1.1 Product hero / tagline (n=15)

| ID | Sentence | Source |
|---|---|---|
| H01 | `Fly through demanding AI tasks up to 6x faster.` | https://www.apple.com/macbook-pro/ |
| H02 | `Fast runs in the family.` | https://www.apple.com/macbook-pro/ |
| H03 | `Now with M5, M5 Pro, and M5 Max.` | https://www.apple.com/macbook-pro/ |
| H04 | `Happily ever faster.` | https://www.apple.com/macbook-pro/ |
| H05 | `All-day battery life. Think outside the outlet.` | https://www.apple.com/macbook-pro/ |
| H06 | `The world’s best in‑ear Active Noise Cancellation.` | https://www.apple.com/airpods-pro/ |
| H07 | `The best thing you’ve never heard.` | https://www.apple.com/airpods-pro/ |
| H08 | `The sound of science.` | https://www.apple.com/airpods-pro/ |
| H09 | `They’re workin' 9 to 5.` | https://www.apple.com/airpods-pro/ |
| H10 | `The ultimate theater. Wherever you are.` | https://www.apple.com/apple-vision-pro/ |
| H11 | `A workspace with infinite space.` | https://www.apple.com/apple-vision-pro/ |
| H12 | `More pixels than a 4K TV. For each eye.` | https://www.apple.com/apple-vision-pro/ |
| H13 | `Mmmmm. Power.` | https://www.apple.com/ipad-pro/ |
| H14 | `OLED it shine.` | https://www.apple.com/ipad-pro/ |
| H15 | `M5. Creator. Accelerator.` | https://www.apple.com/ipad-pro/ |

### B1.2 Feature blurb — the “Label. Plain meaning. What you get.” shape (n=13)

| ID | Sentence | Source |
|---|---|---|
| F01 | `Ultra Retina XDR. The world’s most advanced display.` | https://www.apple.com/ipad-pro/ |
| F02 | `Apple Pencil Pro. Engineered for limitless creativity.` | https://www.apple.com/ipad-pro/ |
| F03 | `Magic Keyboard. Precision at your fingertips.` | https://www.apple.com/ipad-pro/ |
| F04 | `Wi-Fi and cellular. Grab-and-go connectivity.` | https://www.apple.com/ipad-pro/ |
| F05 | `Design. A powerhouse of portability.` | https://www.apple.com/ipad-pro/ |
| F06 | `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` | https://www.apple.com/macbook-pro/ |
| F07 | `Built for AI. From the silicon up.` | https://www.apple.com/macbook-pro/ |
| F08 | `Apple Intelligence. Works hard. You take it easy.` | https://www.apple.com/ipad-pro/ |
| F09 | `Liquid Retina XDR display with 1600 nits peak HDR brightness.` [fn 2] | https://www.apple.com/macbook-pro/ |
| F10 | `Up to 14 more hours battery life. (Up to 24 hours total.)` [fn 4, 5] | https://www.apple.com/macbook-pro/ |
| F11 | `HDMI, Thunderbolt 5, SDXC, MagSafe, Wi‑Fi 7, and Bluetooth 6.` [fn 6] | https://www.apple.com/macbook-pro/ |
| F12 | `Introducing Siri AI. Truly helpful. Truly yours.` | https://www.apple.com/apple-intelligence/ |
| F13 | `Drive external displays. Connect up to two high-resolution external displays with M5, up to three with M5 Pro, or up to four with M5 Max.` | https://www.apple.com/macbook-pro/ |

### B1.3 Footnote / small print (n=8)

| ID | Sentence | Source |
|---|---|---|
| N01 | `Testing conducted by Apple in September 2025 using preproduction 14-inch MacBook Pro systems with Apple M5, 10-core CPU, 10-core GPU, 32GB of unified memory, and 4TB SSD, as well as production 14-inch MacBook Pro systems with Apple M4, 10-core CPU, 10-core GPU, and 32GB of unified memory, and production 13-inch MacBook Pro systems with Apple M1, 8-core CPU, 8-core GPU, and 16GB of unified memory, all configured with 2TB SSD.` | https://www.apple.com/macbook-pro/ |
| N02 | `Performance tests are conducted using specific computer systems and reflect the approximate performance of MacBook Pro.` | https://www.apple.com/macbook-pro/ |
| N03 | `Battery life varies by use and configuration; see apple.com/batteries for more information.` | https://www.apple.com/macbook-pro/ |
| N04 | `In temperatures less than 25° C.` | https://www.apple.com/macbook-pro/ |
| N05 | `Wi‑Fi 7 available in countries and regions where supported.` | https://www.apple.com/macbook-pro/ |
| N06 | `Requires that your iPhone and Mac are signed in with the same Apple Account using two-factor authentication, your iPhone and Mac are near each other and have Bluetooth and Wi-Fi turned on, and your Mac is not using AirPlay or Sidecar.` | https://www.apple.com/macbook-pro/ |
| N07 | `Port configuration varies by model.` | https://www.apple.com/macbook-pro/ |
| N08 | `Available to current and newly accepted college students and their parents, as well as faculty, staff, and homeschool teachers of all grade levels. See Terms for more information.` | https://www.apple.com/macbook-pro/ |
| N09 | `Battery life varies by use, configuration, cellular network, signal strength and other factors; actual results may vary based on usage. Testing conducted by Apple in July 2026 using preproduction iPhone 18 Pro and iPhone 18 Pro Max units and software, subscribed to LTE and 5G carrier networks.` — qualifies the hero figure `Up to 45 hours`; note `preproduction` and `actual results may vary` appear only here | https://www.apple.com/iphone-18-pro/specs/ |

### B1.4 Privacy / security copy (n=9)

| ID | Sentence | Source |
|---|---|---|
| P01 | `Siri learns what you need. Not who you are.` | https://www.apple.com/privacy/ |
| P02 | `Maps knows your route, not your profile.` | https://www.apple.com/privacy/ |
| P03 | `Photos lets you choose who has the full picture.` | https://www.apple.com/privacy/ |
| P04 | `Wallet and Apple Pay help hide what you buy.` | https://www.apple.com/privacy/ |
| P05 | `Health keeps your records under wraps.` | https://www.apple.com/privacy/ |
| P06 | `Great powers come with great privacy.` | https://www.apple.com/apple-intelligence/ |
| P07 | `Passkeys. Simple. Secure. So not a password.` | https://www.apple.com/privacy/ |
| P08 | `When you make a purchase, Apple Pay uses a device-specific number and unique transaction code. So your card number is never stored on your device or on Apple servers.` | https://www.apple.com/privacy/ |
| P09 | `Where you go says a lot about you.` | https://www.apple.com/privacy/ |

### B1.5 Support article & error/alert copy (n=6)

| ID | Sentence | Source |
|---|---|---|
| S01 | `Your Apple Watch is water resistant, but not waterproof.` | https://support.apple.com/en-us/109522 |
| S02 | `Water resistance isn’t a permanent condition and can diminish over time.` | https://support.apple.com/en-us/109522 |
| S03 | `If you see the "Allow accessory to connect?" alert on your computer, click Allow.` | https://support.apple.com/en-us/118107 |
| S04 | `Tap Cancel Subscription. You might need to scroll down to find the Cancel Subscription button. If there is no Cancel button or you see an expiration message in red text, the subscription is already canceled.` | https://support.apple.com/en-us/118428 |
| S05 | `You might’ve bought the subscription from another company.` | https://support.apple.com/en-us/118428 |
| S06 | `Erase your iPhone, iPad, or iPod and install the latest iOS, iPadOS, or iPod software using a computer.` | https://support.apple.com/en-us/118107 |

### B1.6 Onboarding / setup copy (n=5)

| ID | Sentence | Source |
|---|---|---|
| O01 | `Peace of mind in every plan.` | https://www.apple.com/support/products/ |
| O02 | `Request a replacement iPhone, and we’ll ship it to you so you don’t have to wait for a repair.` | https://www.apple.com/support/products/ |
| O03 | `If your iPhone battery holds less than 80 percent of the original capacity, it’s covered.` | https://www.apple.com/support/products/ |
| O04 | `From coverage for one product to all eligible products in your family, AppleCare has a plan for you.` | https://www.apple.com/support/products/ |
| O05 | `Get answers to your questions and support for all your hardware and software needs 24/7.` | https://www.apple.com/support/products/ |

### B1.7 Legal / terms microcopy (n=3)

| ID | Sentence | Source |
|---|---|---|
| L01 | `These terms and conditions create a contract between you and Apple (the "Agreement"). Please read the Agreement carefully.` | https://www.apple.com/legal/internet-services/itunes/us/terms.html |
| L02 | `Our Services are available for your use in your country or territory of residence ("Home Country").` | https://www.apple.com/legal/internet-services/itunes/us/terms.html |
| L03 | `You can acquire Content on our Services for free or for a charge, either of which is referred to as a "Transaction."` | https://www.apple.com/legal/internet-services/itunes/us/terms.html |

### B1.8 App Store product page copy (n=5)

| ID | Sentence | Source |
|---|---|---|
| A01 | `Shopping designed around you` — subtitle, no terminal period | https://apps.apple.com/us/app/apple-store/id375380948 |
| A02 | `Over 100 million songs.` — subtitle | https://apps.apple.com/us/app/apple-music/id1108187390 |
| A03 | `Apple Music is all about the music, with the highest audio quality; exclusive, in-depth content and unparalleled access to the artists you love–all ad-free.` | https://apps.apple.com/us/app/apple-music/id1108187390 |
| A04 | `Like a DJ, AutoMix seamlessly transitions one song into the next.` | https://apps.apple.com/us/app/apple-music/id1108187390 |
| A05 | `Various improvements and performance enhancements.` — the boilerplate release-note line; the phrase occurs **44 times** in the served HTML of this one page (≈22 version entries, each emitted twice by the page’s list markup) | https://apps.apple.com/us/app/apple-store/id375380948 |

### B1.9 Korean localized copy (n=8) — with English counterpart where the EN page exists

| ID | Korean (verbatim) | English counterpart (verbatim) | Source URL |
|---|---|---|---|
| K01 | `스피드는 칩안 내력.` | `Fast runs in the family.` | https://www.apple.com/kr/macbook-pro/ · https://www.apple.com/macbook-pro/ |
| K02 | `기승전빠름.` | `Happily ever faster.` | https://www.apple.com/kr/macbook-pro/ · https://www.apple.com/macbook-pro/ |
| K03 | `온종일 가는 배터리. 무엇에도 얽매이지 않는 작업을 위해.` | `All-day battery life. Think outside the outlet.` | https://www.apple.com/kr/macbook-pro/ · https://www.apple.com/macbook-pro/ |
| K04 | `AI를 위한 탄생. 근본인 칩부터.` | `Built for AI. From the silicon up.` | https://www.apple.com/kr/macbook-pro/ · https://www.apple.com/macbook-pro/ |
| K05 | `오오오오오. 파워.` | `Mmmmm. Power.` | https://www.apple.com/kr/ipad-pro/ · https://www.apple.com/ipad-pro/ |
| K06 | `찬란하게 OLED.` | `OLED it shine.` | https://www.apple.com/kr/ipad-pro/ · https://www.apple.com/ipad-pro/ |
| K07 | `사운드는 과학.` | `The sound of science.` | https://www.apple.com/kr/airpods-pro/ · https://www.apple.com/airpods-pro/ |
| K08 | `아침부터 저녁까지 열일 중.` | `They’re workin' 9 to 5.` | https://www.apple.com/kr/airpods-pro/ · https://www.apple.com/airpods-pro/ |

Two further Korean lines retrieved and worth noting because they show the body-copy register:

- `당신의 데이터를 당신이 원하는 곳에서만.` (privacy section headline, https://www.apple.com/kr/iphone/) — **I could not locate an English counterpart.** The corresponding EN page (https://www.apple.com/iphone/) shows only `Groundbreaking privacy protections.` in that slot; the `당신`-fronted line has no EN string I was able to retrieve. Flagging this as an unresolved asymmetry rather than asserting a translation pair.
- `당신은 그저 '재생' 버튼만 누르면 된답니다.` (https://www.apple.com/kr/airpods-pro/) — note the `-답니다` softener, which has no English analogue.

**One verified Korean localization defect.** `스피드는 칩안 내력.` contains `칩안`, with the space missing where standard Korean orthography requires `칩 안`. Verified in raw HTML: `<p class="header-headline typography-marquee-headline-base">스피드는 칩안 내력.</p>` — there is exactly one occurrence of `칩안` and zero of `칩 안` on that page. This is a genuine shipped spacing error in Apple’s own primary headline, and it is the kind of thing a “write like Apple” skill must *not* propagate.

## B2. Derived rules with evidence counts

**Everything in this section is a measurement of the B2 sample described in each row — nothing more.** These are not claims about apple.com in aggregate. The two are labelled separately and must not be merged.

### B2.1 Sample definitions

| Sample | Definition | n |
|---|---|---|
| **S-hero** | All hero, section and card headlines extracted from the five EN product pages `/macbook-pro/`, `/airpods-pro/`, `/apple-vision-pro/`, `/ipad-pro/`, `/apple-intelligence/`, deduplicated | **83** |
| **S-two** | Subset of a broader headline pool matching the two-part `X. Y.` shape | **38** |
| **S-body** | All `<p>` elements of ≥8 words across the ten EN pages `/macbook-pro/`, `/airpods-pro/`, `/apple-vision-pro/`, `/ipad-pro/`, `/apple-intelligence/`, `/privacy/`, `/iphone/`, `/mac/`, `/apple-watch-series-10/`, `/accessibility/`, deduplicated | **568** |
| **S-sent** | Sentence-split of all `<h1>–<h4>`, `<p>`, `<li>` text from those same ten pages, ≥3 words | **4,638 sentences / 80,882 words** |
| **S-fn** | Every `<li id="footnote-*">` on `/macbook-pro/` | **59** |
| **S-kr-body** | All `<p>` elements of ≥8 words across `/kr/macbook-pro/`, `/kr/airpods-pro/`, `/kr/ipad-pro/`, `/kr/iphone/`, `/kr/apple-watch-series-10/`, `/kr/privacy/` | **379** |
| **S-kr-hero** | Hero/section headlines from the same KR pages | **60** |

### B2.2 The evidence table

| # | Candidate rule | Measured | Sample | Verdict |
|---|---|---|---|---|
| R1 | **End headlines with a period, even when they are fragments.** | 76/83 = **92%** of EN headlines end with `.` | S-hero | Strong. The minority are utility labels (`Recycled Material`, `Renewable Electricity`) and nav-style items. |
| R2 | **Never use an exclamation mark as sentence punctuation.** | **0/4,638** sentences. The only two `!` characters on all ten pages are inside the film title `Deaf President Now!` | S-sent | Very strong — and unusually absolute for a style rule. |
| R3 | **Prefer the declarative to the interrogative in headlines.** | 0/83 headlines contain `?` | S-hero | Strong in headlines. Support copy is the opposite — see R14. |
| R4 | **Two-beat headlines: `Label. Payoff.`** | 38 headlines match the two-part shape; of these, **30** lead with a product/tech noun followed by a period (`Ultra Retina XDR. The world’s most advanced display.`) | S-two | Strong, and this is the single most imitable Apple pattern. |
| R5 | **A three-beat escalation is common and deliberate.** | Counted within S-two: `M5. Creator. Accelerator.` / `Apple Intelligence. Works hard. You take it easy.` / `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` / `Passkeys. Simple. Secure. So not a password.` | S-two | Present but a *minority* device; roughly a fifth of two-part headlines extend to three or four beats. Treat tricolon as a spice, not a base. |
| R6 | **Sentence case, not Title Case.** | Title-case-looking headlines 41/83 — but this count is inflated by 2–3 word headlines where the two are indistinguishable. Among headlines of ≥5 words, sentence case dominates: `All-day battery life. Think outside the outlet.`, `The best thing you’ve never heard.`, `More pixels than a 4K TV. For each eye.` | S-hero | **Weak as measured.** Report honestly: Apple is *not* consistently sentence case in US marketing headlines. Title case is common in the retail/value-prop modules (`Recycled Material`, `Renewable Electricity`, `Same-day service`, `Express Replacement Service`). |
| R7 | **Second person is the default in body copy, absent in headlines.** | Body: 344/568 paragraphs contain `you/your` = **61%**. Headlines: 18/83 = **22%** | S-body, S-hero | Strong and asymmetric. The rule is *not* “always say you” — it is “say you in the paragraph, name the thing in the headline.” |
| R8 | **Mean sentence length sits in the high teens; median lower.** | mean **17.4** words, median **14** words | S-sent | Moderate. This is *my* measurement on a mixed corpus that includes legal boilerplate, which pulls the mean up. Marketing-only prose reads shorter. |
| R9 | **Numerals, not spelled-out numbers, for quantities and performance.** | 51/59 footnotes contain digits; headline examples use `6x`, `7.8x`, `1600 nits`, `24 hours`, `80 percent`, `5.1 mm`, `100 million` | S-fn, S-hero | Strong for figures. Note the inconsistency a skill should resolve: `80 percent` (word) vs `80%` — Apple uses both. |
| R10 | **Performance claims are always hedged with `up to` and always footnoted.** | `up to` appears in the headline claims `up to 6x faster`, `up to 8x faster`, `up to 7.8x faster`, `Up to 24 hours`, `Up to 14 more hours battery life` — and each carries a footnote marker | S-hero, S-fn | Very strong. |
| R11 | **The footnote apologises for the headline in a fixed formula.** | `Testing conducted by Apple in … using preproduction … systems with …` opens **40/59** footnotes; `Performance tests are conducted using specific computer systems and reflect the approximate performance of …` closes **36/59** | S-fn | Very strong — this is a template, not a style. |
| R12 | **Footnote length is wildly bimodal.** | min **5** words (`In temperatures less than 25° C.`), median **100**, max **694** (the Apple Upgrade lease footnote) | S-fn | Strong. A skill that says “keep footnotes short” is wrong; Apple writes 5-word and 700-word footnotes on the same page. |
| R13 | **`Requires…` and `Available…` open availability caveats.** | `Requires` 2/59, `Available` 2/59, `varies by` 5/59, `for more information` 7/59, `subject to` 4/59 | S-fn | Moderate; the *form* is a terse subject-less opener, the specific verbs vary. |
| R14 | **Support copy inverts the marketing register: it asks the user’s question as the heading, then answers it in the affirmative-then-correction shape.** | `Is my Apple Watch waterproof?` → `Your Apple Watch is water resistant, but not waterproof.` Also `Can I go scuba diving, swimming, or take a shower with my Apple Watch?` | Support pages | Strong as a pattern (observed repeatedly), but n is small — I retrieved 5 support articles. |
| R15 | **Support steps are bare imperatives with the UI element named exactly.** | `Tap Subscriptions.` / `Go to Settings.` / `Enter your Apple Account password.` / `Open the Finder on Mac…` / `Select your device when it appears on your computer.` 24/568 body paragraphs are bare imperatives, but within support-step `<li>` lists the rate is near-total | S-body + support pages | Strong within support; the 24/568 figure understates it because S-body is dominated by marketing pages. |
| R16 | **Alerts are quoted verbatim in the user’s UI language and followed by the action.** | `If you see the "Allow accessory to connect?" alert on your computer, click Allow.` | Support pages | Strong pattern: `If you see the "<exact string>" alert, <action>.` |
| R17 | **Em dashes and semicolons are present but not characteristic.** | 179 `—` and 334 `;` across S-sent’s 80,882 words, heavily concentrated in legal and footnote text, **not** in headlines: 0/83 headlines contain an em dash | S-sent, S-hero | **Corrects a common claim.** Apple’s *marketing headlines* avoid the em dash entirely; its *legal* text is full of semicolons. Pop copywriting advice that treats “Apple uses lots of em dashes” as a rule is not supported by this sample. |
| R18 | **`And` and `But` open sentences freely, including headlines and paragraphs.** | 15/83 headlines contain `and`; body paragraphs routinely open with `And`: `And when you pay, your card numbers are never shared by Apple with merchants.` / `And because Apple News uses machine learning…` / `And you can change your preference for any app…` | S-hero, `/privacy/` | Strong. Note it is *also* a device in privacy copy specifically, where it chains guarantees. |
| R19 | **Privacy copy is written as reassurance-by-negation: `not`, `never`, `isn’t`, `without`.** | `Siri learns what you need. Not who you are.` / `Maps knows your route, not your profile.` / `your card number is never stored on your device or on Apple servers` / `where you go isn’t associated with your Apple Account at all` | `/privacy/` | Strong. This is a *register* rule: privacy copy’s job is to deny, so it is the one place where the Apple voice is allowed to be negative. |
| R20 | **Korean headlines keep the two-beat shape but change the mechanics: no `and`, fewer `you`, and a soft assertive verb ending.** | KR: 2/60 hero headlines contain a digit vs 6/83 EN; 54/60 end with `.`; `and` count **0/60** (vs 15/83 EN, because Korean coordination is not written with a standalone word); `당신` appears in only 4/60 hero headlines but in **80/379 = 21%** of KR body paragraphs | S-kr-hero, S-kr-body | Strong and directly actionable. |
| R21 | **Korean body copy uses the `-죠` / `-답니다` softener as a signature.** | 133/379 = **35%** of KR body paragraphs contain `죠`; 22/379 contain `답니다`. Example: `당신은 그저 '재생' 버튼만 누르면 된답니다.` | S-kr-body | Strong. There is **no English equivalent** — this is a Korean-only Apple marker and the single most important thing to get right in KR localization. |
| R22 | **Korean copy also suppresses exclamation marks.** | 0 `!` in S-kr-body (vs 9 `?`) | S-kr-body | Consistent with R2, so the rule survives localization. |

### B2.3 What I could NOT measure, and would not claim

- **Word/character counts of the whole site.** My sample is 24 pages. Apple publishes thousands.
- **Anything about `apple.com/kr/` beyond the six pages fetched.** Notably, Korean *support* copy (`support.apple.com/ko-kr`) was **not** retrieved, so R20–R22 describe Korean *marketing* copy only. Whether Korean support copy uses `-죠` is untested and should not be asserted.
- **Whether the “no exclamation marks” rule holds sitewide.** It holds on the 10 EN pages I fetched. It is a strong signal, not a proof.
- **Anything diachronic.** These pages are M5-era (fetched 2026-09-30). I did not archive-compare against 2015-era Apple copy, so I cannot say the style has or has not drifted. Every “Apple has always…” claim is outside my evidence.
- **Title case vs sentence case.** R6 is genuinely inconclusive from this sample. Do not build a rule on it without a larger, length-controlled sample.

## B3. Apple’s *own* documented writing guidance — and the two-voice problem

This is the single most important structural finding in Part B, and it is a **primary source**, not a critic’s opinion.

Apple publishes an official writing guide at <https://developer.apple.com/design/human-interface-guidelines/writing>. The page is a client-rendered SPA, but its content is served as JSON at <https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.json> (retrieved successfully, 37 KB). Quoting it verbatim:

> `The words you choose within your app are an essential part of its user experience.`

> `Be clear. Choose words that are easily understood and convey the right thing. Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.`

> `Write for everyone. For your app to be useful for as many people as possible, it needs to speak to as many people as possible. Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology.`

> `Be action oriented. Active voice and clear labels help people navigate through your app from one step to the next, or from one screen to another. When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying "Send" often works better than "Let’s do it!"`

> `Use possessive pronouns sparingly. Possessive pronouns like my and your are often unnecessary to establish context. For example, "Favorites" conveys the same message as "Your Favorites," and is more succinct. If you do use possessive pronouns, use them consistently throughout your app, and try not to switch perspectives. Avoid using we altogether because it may be unclear who the "we" in question refers to. This is particularly problematic in error messages like "We’re having trouble loading this content." Something like "Unable to load content" is much clearer.`

> `Write clear error messages. It’s always best to help people avoid errors. When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, "That password is too short" isn’t as helpful as "Choose a password with at least 8 characters."`

> `Remember that errors can be frustrating. Interjections like "oops!" or "uh-oh" are typically unnecessary and can sound insincere.`

> `Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently throughout your app — for example, title case for all alerts or sentence case for all headlines.`

Apple also records the change history on that page: `December 16, 2025 — Clarified guidance on language patterns, and added guidance for possessive pronouns.`

### B3.1 Why this matters more than any blog post

There isn’t **one** Apple voice. There are **two**, and they are documented as pulling in opposite directions:

| | **Platform voice** (HIG — Apple telling *you* how to write UI) | **Marketing voice** (Apple’s own product pages) |
|---|---|---|
| Second person | “Use possessive pronouns **sparingly**”; `"Favorites" conveys the same message as "Your Favorites," and is more succinct` | **61%** of body paragraphs use `you/your` (R7) |
| First person plural | `Avoid using we altogether` | Used freely: `we’ll ship it to you`, `we never share or sell it`, `Our Services are available for your use` |
| Cleverness | `avoid the temptation to be too cute or clever` | The whole register: `OLED it shine.`, `Happily ever faster.`, `They’re workin' 9 to 5.`, `Mmmmm. Power.` |
| Error tone | `avoid blame`, no interjections, state the fix | n/a — support copy follows this, marketing copy ignores it |

**This is the highest-value insight in Part B for skill design.** A writing skill that says “write like Apple” without disambiguating will produce marketing pastiche in contexts — error messages, settings labels, legal notices, medical or financial UI — where Apple’s *own published guidance* says to do the opposite. The skill must ask **which Apple** is being invoked.

Note also that Apple’s HIG guidance is *convergent with* generic plain-language practice (active voice, short words, no blame, no jargon, front-load the fix). On the UI/support axis, Apple is not distinctive — it is simply competent. Apple’s *distinctiveness* lives almost entirely in the marketing register: the two-beat headline, the coined compound, the withheld verb, the pun. That is also the register that carries the most risk (see B5).

## B4. Critiques and failure modes — when NOT to write like Apple

Each item states the **documented** basis separately from **my inference**, because the two carry different weight.

### F1. The marketing register is the register regulators punish

**Documented.** Apple’s advertising has repeatedly been found misleading by regulators, and the failures cluster in exactly the stylistic habits a “write like Apple” skill is most tempted to copy — the confident absolute and the unqualified superlative.

- **UK, 2008 — ASA banned an iPhone ad — REPORTED, NOT VERIFIED, and the wider ASA angle is weak.** Wikipedia’s *Apple advertising* article records: `In August 2008, the Advertising Standards Authority (ASA) in the UK banned one iPhone ad from further broadcast in its original form due to "misleading claims". The ASA took issue with the ads' claim that "all parts of the internet are on the iPhone", when the device did not support Java or Adobe’s third-party Flash web browser plug-in.` (retrieved from <https://en.wikipedia.org/wiki/Apple_advertising>). **I could not retrieve the underlying ruling**, and a later attempt to retrieve *other* Apple ASA rulings also failed (live URLs 404, no Wayback snapshots) — see **B5.9**, which also records that three Apple ASA rulings were reported to me as having been adjudicated **`Not Upheld`**. **Practical guidance: do not lean on the ASA as an anti-Apple evidence source.** Rely instead on Which? (B5.8a), the CFPB (B5.8d), the FTC (B7) and the DOJ (B5.2), all of which I verified. Note nonetheless that the *shape* of the 2008 complaint is instructive: *“all parts of the internet”* is a totalising claim with no hedge, and the hedged `up to` construction Apple now uses everywhere (R10) is plausibly a downstream response. That last step is my inference, not a sourced claim.
- **Australia, 2012 — A$2.25 million penalty.** The same article: `In 2012 Apple was sued in Australia for branding its 2012 iPad as being 4G capable, even though the iPad was not compatible with Australia’s 4G network. Apple offered a refund to customers for all iPads sold in Australia. Apple Inc. agreed to pay a A$2.25 million penalty for misleading Australian customers about its iPad being 4G capable.`
- **The general finding.** The same article’s Criticism section states plainly: `Apple’s advertising has come under criticism for adapting other creative works as advertisements and for inaccurate depictions of product functionality.`

**Now documented in federal litigation, not merely inferred.** See **B5.1** (*Landsheft v. Apple*, N.D. Cal. 2025, over Apple Intelligence features advertised but not delivered; ¶30 is headed `No Notice of Contradictions`) and **B5.2** (*US v. Apple*, D.N.J. 2024, in which the DOJ characterises Apple’s privacy-and-security messaging as `an elastic shield`). The 2008 and 2012 actions below are not isolated embarrassments; they are the early instances of a pattern that continued into federal court.

**Implication for the skill.** Apple’s *own* copy is only defensible because Apple footnotes it to death. A skill that teaches the punchy headline without the 100-word footnote template teaches the half that gets companies fined.

### F2. Culture and register travel badly

**Documented.** In July 2024 Apple released *The Underdogs: Out of Office*, filmed in Bangkok. Wikipedia’s *Criticism of Apple Inc.* records that it `depicts the characters' U.S. office in cool tones to suggest modernity, while using vintage filters to portray Thailand as an underdeveloped 'third‑world' state`, that it was criticised by `the Thai public and foreigners, both residents and previous visitors, as "a stereotypical and dated portrayal of Thai society"`, and that `On August 2, 2024, Apple apologized and removed access to the film on YouTube.` (<https://en.wikipedia.org/wiki/Criticism_of_Apple_Inc.>)

Also documented, May 2024: the *Crush!* iPad Pro advertisement, which `received broad criticism online, with Hugh Grant describing the advertisement as a "destruction of the human experience"`. Apple’s VP of marketing communications Tor Myhren apologised: `Creativity is in our DNA at Apple, and it’s incredibly important to us to design products that empower creatives all over the world. Our goal is to always celebrate the myriad of ways users express themselves and bring their ideas to life through iPad. We missed the mark with this video, and we’re sorry.` (<https://en.wikipedia.org/wiki/Apple_advertising>)

**Implication.** Apple’s house style is *confident*. Confidence reads as arrogance when the writer has not earned the audience’s trust, and it reads as tone-deaf when the subject is someone else’s culture, craft, or loss. The register is not portable to a first-time writer, a small brand, or a sensitive topic.

### F3. Privacy copy makes promises the company can be held to

**Documented.** Apple’s privacy register is assertion-heavy and negation-based (R19), which makes each line a falsifiable public commitment. Wikipedia’s *Criticism of Apple Inc.* documents the gap: on Face ID, `In 2017, Apple announced Face ID as a neural network technology that was private and safe because it was stored locally on the device and never uploaded to the cloud.` followed by reporting that `In August 2021, The Verge published "Apple cares about privacy, unless you work at Apple," which detailed an internal tool called "Glimmer" (formerly "Gobbler") employees used to test Face ID.` On AI training: `some media outlets have questioned the effectiveness of this opt-out system, arguing that it places the responsibility on publishers and questioning whether data can be fully retracted from training sets once collected. CNN criticized the procedure saying it places the burden on publishers to safeguard their data from Apple.`

**The strongest adversarial evidence is now a government filing.** The DOJ’s antitrust complaint against Apple (retrieved, 88 pp. — see **B5.2**) attacks this exact register: `Apple wraps itself in a cloak of privacy, security, and consumer preferences to justify its anticompetitive conduct. Indeed, it spends billions on marketing and branding to promote the self-serving premise that only Apple can safeguard consumers' privacy and security interests.` … `In the end, Apple deploys privacy and security justifications as an elastic shield that can stretch or contract to serve Apple’s financial and business interests.` (¶16). Separately, Korea’s PIPC found that **72%** of evaluated companies' published privacy policies diverged from their actual data practices (B5.5). The register is not the problem; the absolutism is.

**Implication.** `Siri learns what you need. Not who you are.` is a beautiful sentence and a legal exposure. In a regulated domain (health, finance, children’s data, EU/UK GDPR), the skill must not generate absolute negations unless the writer can defend every one of them. The more quotable the privacy sentence, the more quotable it is *against* you. Prefer the hedge that Apple itself uses in its footnotes (`Not all devices are eligible`, `varies by use and configuration`) over the absolutism it uses in its heroes.

### F4. The footnote is where Apple’s clarity goes to die — and I measured it

**My measurement.** On `/macbook-pro/`, footnote length ranged from **5 words** to **694 words**, with a **median of 100** (S-fn, n=59). The 694-word footnote is a single sentence-adjacent block of lease terms covering eligibility, credit checks, damage fees, upgrade mechanics, termination charges, and a list of excluded storefronts. `Testing conducted by Apple in …` opens **40/59** footnotes and `Performance tests are conducted using specific computer systems and reflect the approximate performance of …` closes **36/59**.

**Why this is a failure mode, not just a pattern.** The footnote template exists to make an unverifiable headline claim legally defensible. Two consequences follow:

1. **The headline claim is unfalsifiable by a normal reader.** `Fly through demanding AI tasks up to 6x faster.` is qualified by a footnote disclosing *preproduction* hardware, a specific beta application build, a specific file, and a specific MLX framework version. The words `preproduction` and `(Beta)` appear in the small print but never in the hero. Whether that is adequate disclosure is a judgement call; that the hero would be indefensible without the footnote is not.
2. **Nobody reads 694 words of lease terms on a laptop page.** Whether or not the disclosure is legally sufficient, it is not *communicatively* sufficient. Copied into a domain with real consumer harm — credit, insurance, health — this pattern is a liability, not a style.

**And the upper bound has been independently tested.** R10 notes that Apple hedges every performance claim with `up to`. In 2019 Which? tested nine iPhone models against those claims: **all nine fell short, by 18–51%** — iPhone XR talk time lasted `16 hours and 32 minutes` against a claimed 25 hours. Full quotation at **B5.8(a)**. The `up to` upper bound is not a typical result, and a consumer organisation with a published methodology demonstrated it. Separately, The Verge documented the benchmark genre’s opacity — charts `maddeningly labeled with "relative performance" on the Y-axis`, with `Apple doesn’t tell us what specific tests it runs` (**B5.8c**). So the F4 critique is no longer only my measurement plus one lawsuit: it now has an independent test result and an independent methodology critique behind it.

**Also relevant:** the live `up to 86x faster` artifact documented in B0. A performance-claim pipeline that revises numbers without updating spacing is a pipeline that can ship a wrong number.

**The FTC states the rule this pattern strains against.** From *[.com Disclosures](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf)* (2013), retrieved and verified verbatim:

> `When practical, advertisers should incorporate relevant limitations and qualifying information into the underlying claim, rather than having a separate disclosure qualifying the claim.`

> `Required disclosures must be clear and conspicuous. In evaluating whether a disclosure is likely to be clear and conspicuous, advertisers should consider its placement in the ad and its proximity to the relevant claim. The closer the disclosure is to the claim to which it relates, the better. Additional considerations include: the prominence of the disclosure; whether it is unavoidable; whether other parts of the ad distract attention from the disclosure…`

Apple’s hero-plus-distant-footnote layout — a large claim on a bento tile, its qualification 100 words down in a numbered list below the fold — is precisely the `separate disclosure qualifying the claim` structure the FTC says to avoid `when practical`. And that is the structure the *Landsheft* complaint targets in ¶30 (`No Notice of Contradictions`). **The footnote is not a stylistic tic; it is the disputed instrument.**

### F5. Superlative fatigue is measurable in Apple’s own copy

**My measurement.** 13/83 headlines (**16%**) in S-hero contain a superlative or absoluteness marker (`best`, `fastest`, `most`, `world’s`, `ultimate`, `ever`, `never`, `amazing`, `incredible`, `revolutionary`, `magic*`) — e.g. `The world’s best in‑ear Active Noise Cancellation.`, `Our most advanced Spatial Audio system ever.`, `The world’s most advanced display.`, `Longest battery life ever in a Mac.`

**Inference (clearly mine, not sourced).** At 16% these still land, because they are spaced out across a long page and each is footnoted. A shorter document that reproduces the same *density* — three or four superlatives in a paragraph — produces the opposite effect: a reader who discounts all of them. The device works at Apple’s scale and dose and fails at most other scales. Note too that Apple **stops short of the strongest words**: in 83 headlines I found **zero** instances of `magical` used as a product claim, and the word that survives is the milder `Magic` as a product name (`Magic Keyboard`) and the pun `Magic to your ears.`

### F6. Korean localization: the register is genuinely localized, but errors ship anyway

**My measurement + verification.** The Korean pages are *not* literal translations — Apple rewrites the joke rather than translating it. `Fast runs in the family.` becomes `스피드는 칩안 내력.`; `Happily ever faster.` becomes `기승전빠름.` (a four-character idiom pun, 기승전결 → 기승전’빠름'/fast); `They’re workin' 9 to 5.` becomes `아침부터 저녁까지 열일 중.` These are competent, idiomatic transcreations, and the `-죠` softener appears in **133/379 = 35%** of Korean body paragraphs (R21) with no English equivalent.

**But:** `스피드는 칩안 내력.` ships with a spacing error — `칩안` where standard orthography requires `칩 안` (verified: exactly one occurrence of `칩안`, zero of `칩 안` in the served HTML). This is Apple’s *primary hero headline* on the Korean MacBook Pro page.

**Implication for the skill.** Two rules, and they point opposite ways:
- Do **not** translate English Apple headlines into Korean word-for-word. That produces 번역투 (translationese). Rebuild the joke in Korean, as Apple does.
- Do **not** assume the Korean page is orthographically safe to copy. Apple’s Korean localisation carries spacing and particle errors; a skill that says “mirror apple.com/kr exactly” propagates them. Korean copy needs a separate orthography pass (맞춤법/띄어쓰기) that Apple’s own pipeline evidently did not fully run here.

**번역투 is now a *named, scored* regulatory failure category — not just a style opinion.** Korea’s Personal Information Protection Commission (개인정보보호위원회) evaluates privacy policies on three axes out of 100. The 2024 round covered 49 companies across 7 sectors and averaged **가독성 (readability) 69.1 / 접근성 (accessibility) 60.8 / 적정성 (adequacy) 53.4**, and reported that the twelve foreign operators scored below domestic firms on all three — attributing it in part to `번역투 문장 사용` (use of translationese sentences). Full quotation and citation in **B5.5(a)**. Note the caution recorded there: the source does **not** name Apple.

**And Apple’s own localisation quality control is demonstrably uneven.** In August 2024 Korean outlets reported that Apple’s built-in Translate app rendered `김치` into Chinese as `韓式泡菜` and `Korean` into Japanese as `朝鮮語` rather than `韓国語` — full quotation in **B5.5(b)**. The defects were in Apple’s *Chinese and Japanese* output, reported by Korean users. The lesson for the skill is not “Apple’s Korean is bad” (my measurement says its Korean *marketing* prose is genuinely good) but that **a house style does not survive localisation on its own**; each locale needs its own editorial pass.

### F7. The two-voice trap

Restating B3 as a failure mode: the most common way an “Apple-style” writing skill goes wrong is writing *error messages, settings labels, and legal notices* in the marketing register. Apple’s own HIG explicitly forbids this — `avoid the temptation to be too cute or clever`, `Avoid using we altogether`, `Use possessive pronouns sparingly`, no `oops!`, `avoid blame`. Using `Happily ever faster.` as a tone model for a failed-payment screen is not Apple style; it is the opposite of Apple’s documented style for that surface.

### F8. Regulated-domain constraint (a boundary, stated as a boundary)

I did **not** find a source that says “the Apple voice is unusable in regulated domains.” I am recording this as an **open question and a design constraint rather than a cited finding.** What I can say from retrieved primary material:

- Apple’s own most stylistically distinctive surfaces (product heroes, bento tiles) carry the least legal weight, and its least distinctive surfaces (footnotes, terms) carry the most. The style and the liability are inversely distributed in Apple’s own corpus.
- GDPR Article 12 requires information to be provided `in a concise, transparent, intelligible and easily accessible form, using clear and plain language` — a *comprehensibility* standard, not a *voice* standard. Nothing in it forbids a warm register; everything in it forbids the ornamental ambiguity that `OLED it shine.` depends on.
- The honest constraint is therefore not “no Apple voice in regulated domains” but “**no ambiguity where ambiguity creates liability, and no absolute claim you cannot footnote.**”

### F9. Apple has no apology register — and that is the biggest gap to fill

The Apple voice is optimised for products that work. When a product fails, the corpus offers no good mode, and the failure is documented in Apple’s own words. The July 2010 *Letter from Apple Regarding iPhone 4* (still live at <https://www.apple.com/newsroom/2010/07/02Letter-from-Apple-Regarding-iPhone-4/>; retrieved, quotes verified verbatim — full analysis at **B5.4**) makes four moves in sequence:

1. Normalise the defect — `gripping almost any mobile phone in certain ways will reduce its reception by 1 or more bars. This is true of iPhone 4, iPhone 3GS, as well as many Droid, Nokia and RIM phones.`
2. Reframe it as a *display* bug, not a hardware bug — `we were stunned to find that the formula we use to calculate how many bars of signal strength to display is totally wrong.`
3. Reassert the superlative in the same breath — `the iPhone 4’s wireless performance is the best we have ever shipped.`
4. Apologise for the customer’s feelings rather than the fault — `For those who have had concerns, we apologize for any anxiety we may have caused.`

**Implication for the skill.** This is the most useful *negative* finding in Part B. A skill built only from hero headlines and bento tiles will produce an assistant that, facing a real failure, reaches for normalisation, reframing, and a superlative — the exact three moves that made this letter a case study in bad corporate apology for fifteen years. The skill must supply an apology register from **outside** Apple’s corpus: name the fault, name who was affected, state the remedy, and do not re-assert the product’s excellence in the same message. Note the contrast with Apple’s *own* HIG guidance, which gets this right at the micro level — `avoid blame`, and `"That password is too short" isn’t as helpful as "Choose a password with at least 8 characters."`

### F10. The register collision: Apple answering a lawsuit in keynote voice

Apple’s public response to the DOJ antitrust complaint (reported by 9to5Mac, <https://9to5mac.com/2024/03/21/doj-sues-apple-full-lawsuit-document-here/>; quoted in full at **B5.3**) reads:

> `At Apple, we innovate every day to make technology people love—designing products that work seamlessly together, protect people’s privacy and security, and create a magical experience for our users. This lawsuit threatens who we are and the principles that set Apple products apart in fiercely competitive markets.`

`Magical experience` and `who we are`, deployed against a federal antitrust complaint, is the two-voice problem (B3, F7) at maximum stakes. Two lessons:

- **Register is chosen by stakes and audience, not by brand.** A house voice is not a licence to use it in every genre. Where the reader is an adversary, a regulator, or a court, the marketing register reads as evasion and hands opponents a quotable line. The DOJ’s own filing quotes Apple’s marketing spend against it (¶16, B5.2).
- **This is not Apple-specific.** Any confident brand voice collides with legal register the same way. The skill should therefore ship an explicit **register-routing rule**: detect adversarial, regulatory, legal, medical, safety, and failure surfaces and switch out of the brand voice *before* writing, rather than writing in it and softening afterwards.

### F11. The style does not survive localisation unaided

`SupercolorpixelisticXDRidocious` — an English coined compound that depends entirely on English morphology and rhythm — becomes 「スーパーキラキラカラフルクッキリディスプレイ」 in Japanese: the compound is unpacked into stacked onomatopoeic modifiers. Reported by INTERNET Watch (<https://internet.watch.impress.co.jp/docs/yajiuma/1351429.html>; located by the delegated researcher, **not** independently re-fetched by me, so treat as reported). Combined with the PIPC `번역투` finding and the Translate errors (B5.5), the conclusion is structural rather than anecdotal: **coined compounds, puns, and withheld-verb fragments are the least portable part of Apple’s style.** The two-beat `Label. Payoff.` shape travels; the wordplay does not. A skill claiming multilingual fidelity must state which devices it is *not* transferring.

## B5. Adversarial and regulatory evidence — primary sources

An earlier draft of this section reported a gap, because `web_search` was down all session. A delegated researcher broke through using **CourtListener RECAP** (open federal filings), **Yahoo! Japan** and **Google News RSS**, and I have since **independently re-fetched and re-verified every quotation below from the primary document**. Where I could not verify, I say so.

### B5.1 The 2025 Apple Intelligence false-advertising class action — the footnote problem, litigated

**Landsheft v. Apple Inc.**, No. 5:25-cv-02668 (N.D. Cal.), filed 2025-03-19. Complaint retrieved: <https://storage.courtlistener.com/recap/gov.uscourts.cand.446692/gov.uscourts.cand.446692.1.0.pdf> (19 pp., verified with `pypdf`). Docket: <https://www.courtlistener.com/docket/69759747/landsheft-v-apple-inc/>

This is the single most on-point adversarial document in Part B, because the theory of the case **is** the hero-plus-footnote pattern described in B1.3 and R10–R12. Verbatim, all verified in the retrieved PDF:

> `Plaintiff did not notice any disclaimer, qualifier, or other explanatory statement or information on the Products' advertising and marketing that contradicted the prominent Challenged Representations or otherwise suggested that the iPhone would not have the advertised capabilities.` — ¶30, headed **`No Notice of Contradictions`**

> `Apple’s advertisements saturated the internet, television, and other airwaves to cultivate a clear and reasonable consumer expectation that these transformative features would be available upon the iPhone’s release.` — ¶4

> `Worse, Apple has admitted that if these features ever materialize, it won’t be until 2026—two years after its pervasive marketing campaign built on a lie.` — ¶7

> `Apple deceived millions of consumers into purchasing new phones they did not need based on features that do not exist` — ¶8

**Outcome.** Reported as a **$250 million settlement**, with the claims process opening September 2026 — coverage: <https://www.macrumors.com/2026/09/20/siri-ai-settlement-website-now-live/>. *(I verified the Landsheft filing itself; I did not independently retrieve the settlement figure, which is reported via MacRumors. Treat the dollar amount as secondary.)*

**Why this matters.** My R10 and F4 argued from measurement that `up to Nx` and its 100-word footnote are one legal unit. This filing is that argument made by plaintiffs' counsel, with a nine-figure outcome attached. A writing skill that teaches the confident product claim while treating the footnote as optional boilerplate is teaching the exact conduct that produced this case.

### B5.2 US v. Apple — the DOJ attacks the *privacy register itself*

**United States v. Apple Inc.**, No. 2:24-cv-04055 (D.N.J.), filed 2024-03-21. Complaint retrieved: <https://storage.courtlistener.com/recap/gov.uscourts.njd.544402/gov.uscourts.njd.544402.1.0_3.pdf> (88 pp.). Docket: <https://www.courtlistener.com/docket/68362334/united-states-of-america-v-apple-inc/>

Verbatim, verified in the retrieved PDF (note: `pypdf` extraction of this filing inserts stray intra-word spaces; the wording below is confirmed against the character stream):

> `Apple wraps itself in a cloak of privacy, security, and consumer preferences to justify its anticompetitive conduct. Indeed, it spends billions on marketing and branding to promote the self-serving premise that only Apple can safeguard consumers' privacy and security interests.` — ¶16

> `In the end, Apple deploys privacy and security justifications as an elastic shield that can stretch or contract to serve Apple’s financial and business interests.` — ¶16

> `This signals to users that rival smartphones are lower quality because the experience of messaging friends and family who do not own iPhones is worse—even though Apple, not the rival smartphone, is the cause of that degraded user experience.` — ¶90

**This is the most important adversarial finding in Part B for the privacy register (P01–P09, R19).** Apple’s privacy copy works by terse, confident, negation-based absolutes — `Siri learns what you need. Not who you are.` The DOJ’s argument is that this register is a *rhetorical strategy* that the government can characterise as a shield for anticompetitive conduct. Whether or not that characterisation succeeds, the lesson for a writing skill is blunt: **the more quotable your privacy sentence, the more quotable it is against you** in litigation, in a regulator’s filing, or in a journalist’s story.

### B5.3 The Apple voice deployed as a legal defence — the register collision, documented

Apple’s public response to the DOJ suit is the cleanest documented instance of the marketing register being used where a legal register belongs. Verbatim as reported by 9to5Mac (<https://9to5mac.com/2024/03/21/doj-sues-apple-full-lawsuit-document-here/>):

> `At Apple, we innovate every day to make technology people love—designing products that work seamlessly together, protect people’s privacy and security, and create a magical experience for our users. This lawsuit threatens who we are and the principles that set Apple products apart in fiercely competitive markets.`

`Magical experience` and `who we are` in answer to a federal antitrust complaint is the two-voice problem (B3, F7) with the highest possible stakes. *(Reported via 9to5Mac; I did not retrieve an Apple-hosted copy of this statement.)*

### B5.4 The archetypal tone failure: the iPhone 4 antenna letter (2010)

Still live and retrievable: <https://www.apple.com/newsroom/2010/07/02Letter-from-Apple-Regarding-iPhone-4/> — retrieved, all quotes verified verbatim.

> `To start with, gripping almost any mobile phone in certain ways will reduce its reception by 1 or more bars. This is true of iPhone 4, iPhone 3GS, as well as many Droid, Nokia and RIM phones.`

> `Upon investigation, we were stunned to find that the formula we use to calculate how many bars of signal strength to display is totally wrong.`

> `We have gone back to our labs and retested everything, and the results are the same— the iPhone 4’s wireless performance is the best we have ever shipped.`

> `For those who have had concerns, we apologize for any anxiety we may have caused.`

**Read the four moves in order.** (1) Normalise the defect by attributing it to all phones. (2) Reframe it as a *display* bug, not a hardware bug. (3) Reassert the superlative — `the best we have ever shipped` — in the same paragraph. (4) Apologise for the customer’s *anxiety*, not for the fault. This is the definitive case study for F5 (superlative fatigue) and F2 (register): the Apple voice is optimised for products that work, and it has no good mode for a product that does not. A skill must supply an apology register that Apple’s corpus does not contain.

### B5.5 Korean and Japanese localisation — the criticism I could not find earlier

**(a) Korea’s PIPC scores translationese as a defect.** The Personal Information Protection Commission (개인정보보호위원회) runs a *scored* privacy-policy evaluation. Reported by 인공지능신문, 2025-03-16, <https://www.aitimes.kr/news/articleView.html?idxno=34252> — **retrieved and verified verbatim**:

> 「2024년 평가제 적용대상은 빅테크, 온라인 쇼핑, 온라인 플랫폼(주문·배달, 숙박·여행), 병·의료원, 온라인 동영상 서비스(OTT), 엔터테인먼트(게임, 웹툰), 인공지능(AI) 채용 등 총 7개 분야 49개 기업으로 진행됐다.」

> 「평가 결과 대상기업 평균점수는, 100점 만점 기준으로 **가독성 69.1점, 접근성 60.8점, 적정성 53.4점** 순으로 나타났다. 또한 12개의 해외사업자의 경우 개인정보 공유·협력 등 국내법‧정책과 다르게 표현하거나, **번역투 문장 사용** 등으로 인해 가독성, 접근성, 적정성 모든 분야에서 국내 기업 대비 낮은 평가를 받았다.」

> 「평가대상의 **72%**가 처리방침상 기재내용과 실제 서비스 이용 시 고지된 개인정보 처리 목적‧항목‧보유기간이 다르게 운영되고 있었다.」

Three points, and one caution:
- **번역투 (translationese) is a *scored, named* failure category in Korean privacy-policy regulation**, and it demonstrably depressed readability/accessibility/adequacy scores for foreign operators. This is the regulatory backing F6 previously lacked.
- The **72% mismatch** finding between stated policy and actual practice is direct evidence for F3: privacy copy is the surface where the gap between the sentence and the operation is routinely real.
- **CAUTION — do not overclaim.** The article reports `12개의 해외사업자` *in aggregate* and **does not name Apple**. Apple being among the twelve is plausible but is **not stated in the source**. Cite the category-level finding, not an Apple-specific one.

**(b) Apple’s own Translate app shipped the mistranslations.** Reported by 뉴시스, 2024-08-28, <https://www.newsis.com/view/NISX20240828_0002865250> — **retrieved and verified**. Headline: `"김치→파오차이, 한국어→조선어"…아이폰 번역앱 논란`. Body, verbatim:

> 「대표 오류는 '김치’를 중국어로 번역하면 '韓式泡菜'(한국식 파오차이)로 나온다. '파오차이'(泡菜)는 김치와 전혀 다른 중국식 채소 절임이다. 'Korean’도 일본어로 번역하면 '朝鮮語'(조선어)로 나온다. '韓国語'(한국어)가 올바를 표현이다.」

The complaint was raised by 서경덕 (Prof. Seo Kyoung-duk, Sungshin Women’s University). **Note the precise direction of the error**, which is easy to get wrong: the defects are in Apple’s **Chinese and Japanese** output, reported by Korean users — not in Apple’s Korean output. It is evidence that Apple’s localisation quality control is uneven across a language family, which is directly relevant to F6.

**(c) Japanese localisation of a coined English compound.** Apple’s `SupercolorpixelisticXDRidocious` (iPad Pro display copy) became 「スーパーキラキラカラフルクッキリディスプレイ」 — reported by INTERNET Watch, やじうまWatch, 2021-09-16, <https://internet.watch.impress.co.jp/docs/yajiuma/1351429.html>. *(Located by the delegated researcher; I did not independently re-fetch this URL, so treat the pair as reported rather than verified by me.)* The point stands regardless: **coined English compounds do not survive translation as compounds** — they are unpacked into stacked Japanese modifiers. That is a structural limit on R4’s `Label. Payoff.` device in non-English locales.

### B5.6 Honest nulls — verified absences, do not cite as existing

These **negative** results are as useful as the positives, because they stop the skill from citing folklore. Two items that were nulls in the first draft were later **closed** (battery-life criticism and benchmark-methodology criticism — see B5.8a and B5.8c); they are struck through here rather than deleted so the revision is auditable.

- **~~No ASA ruling against Apple was found.~~ SUPERSEDED — see B5.9.** The corrected position: three Apple ASA rulings were *reported* to me as adjudicated `Not Upheld`, but **I could not verify them** (live URLs 404, no Wayback snapshots). The practical guidance stands: **do not cite an ASA ruling as criticism of Apple** — the UK pressure point in 2019 came from Which?, not the ASA.
- **Steve Jobs' “You’re holding it wrong” / “Just avoid holding it in that way”** — the email was **not retrieved**. **Excluded**; do not quote it.
- **Phil Schiller’s “courage” quotation** — WaPo URL returned HTTP 000, **not retrieved**. **Excluded.** Do not paraphrase it into a quotation.
- **~~Apple “up to N hours” battery-life criticism — searched, not found.~~ CLOSED.** Now sourced: Which? 2019, nine iPhone models, all fell short, 18–51% (B5.8a), plus the live iPhone 18 Pro specs footnote (B5.8b).
- **~~Methodological criticism of Apple’s `up to Nx` benchmarks — searched, not found.~~ CLOSED.** Now sourced: The Verge on `"relative performance"` axes (B5.8c), plus the Landsheft filing.
- **“Bendgate” (2014) messaging criticism** — not found. Still a null.
- **Apple support documentation being “too terse”** — no citable source exists; see B5.10.

### B5.7 Working research tooling (worth recording for the next agent)

Since general web search was dead, these were the routes that worked: **CourtListener RECAP** (`storage.courtlistener.com` serves federal filings openly; extract with `pypdf`) · **Google News RSS**, which works in any locale (`https://news.google.com/rss/search?q=QUERY&hl=ko&gl=KR&ceid=KR:ko`) though its links are opaque redirects that do not resolve under `curl -L`, so use it for headline discovery only · **Yahoo! Japan web search** (`https://search.yahoo.co.jp/search?p=QUERY`), a genuine general index · **Bing News RSS** (works) whereas Bing *web* HTML returns query-mismatched garbage. Gotcha: always pass `--compressed` to `curl` against `web.archive.org`, or you get gzip binary.

### B5.8 Footnote, benchmark and plain-language criticism (verified)

This subsections closes the gaps B5.2 previously listed as open. Every quotation was re-fetched and verified by me from the live page or a Wayback snapshot.

**(a) The battery-life claim has been independently tested — and failed.** Which? tested nine iPhone models and published on 2019-05-04: <https://press.which.co.uk/whichpressreleases/apple-significantly-overstates-iphone-battery-life-compared-to-which-tests/> (live page is JS-gated; retrieved via Wayback, `web.archive.org/web/2019id_/…`, verified verbatim):

> `Which? tested nine iPhone models and found that all of them fell short of Apple’s battery time claims. In fact, Apple stated that its batteries lasted between 18 per cent and 51 per cent longer than the Which? results.`

> `Apple’s iPhone XR had the biggest battery overestimation for talk time on full charge. In Which? tests, the battery lasted for 16 hours and 32 minutes, whereas Apple claimed that it would last 25 hours – 51 per cent more.`

This is the empirical backing that R10 and F4 previously lacked. R10 observes that Apple hedges every performance claim with `up to`; this study is what happens when someone tests the upper bound. **Note the balance:** TechRadar’s 2019-05-06 coverage (<https://www.techradar.com/news/apples-iphone-battery-life-claims-are-exaggerated-claims-uk-watchdog>) carries Apple’s rebuttal and notes that Which?'s own methodology was `slightly vague`. Report it as a contested finding, not a settled one.

**(b) The `up to N hours` footnote structure, captured live.** Apple’s own iPhone 18 Pro specs page (<https://www.apple.com/iphone-18-pro/specs/>, retrieved) states the hero figure `Up to 45 hours` for iPhone 18 Pro Max video playback, keyed to footnote 8, which reads:

> `Battery life varies by use, configuration, cellular network, signal strength and other factors; actual results may vary based on usage. Testing conducted by Apple in July 2026 using preproduction iPhone 18 Pro and iPhone 18 Pro Max units and software, subscribed to LTE and 5G carrier networks.`

This is the structure in the wild, and it is the exact artifact *Landsheft* ¶30 says a plaintiff `did not notice`. `preproduction` and `actual results may vary` appear only in the small print. **This is the single best teaching example in Part B for “the claim and its qualification are one unit.”**

**(c) The benchmark-methodology critique I previously reported as not found.** The Verge, 2022-03-17, on the M1 Ultra launch charts: <https://www.theverge.com/2022/3/17/22982915/apple-m1-ultra-rtx-3090-comparison-specs-charts-cpu-gpu-performance> — retrieved, verified verbatim:

> `The charts, in Apple’s recent fashion, were maddeningly labeled with "relative performance" on the Y-axis, and Apple doesn’t tell us what specific tests it runs to arrive at whatever numbers it uses to then calculate "relative performance."`

This is a direct published critique of the `up to Nx faster` genre from an independent outlet with hardware in hand. 9to5Mac’s 2022-03-31 follow-up (<https://9to5mac.com/2022/03/31/m1-ultra-gpu-comparison-with-nvidia/>, crediting Macworld) adds that `Apple achieved this misleading comparison by cutting off the graph before the Nvidia GPU got anywhere close to its maximum performance` *(reported; not re-fetched by me)*.

**(d) A primary regulator action on Apple’s payment messaging.** CFPB, 2024-10-23, retrieved via Wayback (`web.archive.org/web/20241101id_/…` on `consumerfinance.gov`; the live page 403s to non-browser clients). Headline and findings verified verbatim:

> `CFPB Orders Apple and Goldman Sachs to Pay Over $89 Million for Apple Card Failures` — `Companies illegally mishandled transaction disputes and misled iPhone purchasers about interest-free payment options`

> `The CFPB also found that Apple and Goldman Sachs misled consumers about interest-free payment plans for Apple devices. Many customers thought they would automatically get interest-free monthly payments when buying Apple devices with their Apple Card. Instead, they were charged interest. In some cases, Apple did not even show the interest-free payment option on its website on certain browsers.`

Note the failure mode precisely: not a false sentence, but a **sentence that was true of one path and silently false of another**. `Apple Card Monthly Installments` copy is the same register as the rest of Apple’s site — confident, benefit-first. This is the clearest case in Part B of the Apple register failing in a regulated financial context, and it is a regulator finding, not a journalist’s opinion.

**(e) The readability criticism I previously reported as not found.** The Guardian, Alex Hern, 2015-06-15, <https://www.theguardian.com/technology/2015/jun/15/i-read-all-the-small-print-on-the-internet> — retrieved, verified verbatim:

> `My iPhone is also my alarm, which means that at 6am on a Monday, I was greeted by 21,586 words to read before breakfast.`

> `Apple may be famous for products that ruthlessly strip out obsolete parts in pursuit of ease-of-use and simplicity, but that philosophy hasn’t reached its legal department. The terms typically start with an introduction where every word is capitalised, because not a single lawyer cares about anyone being able to read`

The **21,586-word** figure is the concrete readability datapoint B5.2 said was missing. It is a journalist’s count, not a readability score, and the critique is **OPINION** — but the count is checkable and the `every word is capitalised` observation describes the *opposite* of Apple’s own Style Guide advice (see B6).

**(f) Structured clause analysis.** ToS;DR grades `Apple Services` **Grade C** and lists, among others: `Terms may be changed any time at their discretion, without notice to you` — `The Agreements can be updated at any time, including in a way that negatively affects user rights, without notifying before or after the changes.` (<https://tosdr.org/en/service/158>, retrieved, verified verbatim.) Useful as an independent, clause-level counterweight to Apple’s plain-language claims.

**(g) Privacy labels: the small print disclaims the very claim it makes.** netzpolitik.org, 2022-01-20, reporting Oxford computer scientist Konrad Kollnig’s analysis — retrieved, verified verbatim:

> `Computer scientist Konrad Kollnig from Oxford University examined 1,682 randomly selected apps from Apple’s App Store. 373 of the apps tested (22.2 percent) claim not to collect personal data. However, four out of five, 299 apps in total, contacted known tracking domains immediately after the first app launch and without gaining user consent.`

Consumer Reports (2020-12-18, <https://www.consumerreports.org/electronics-computers/privacy/how-to-use-apples-privacy-labels-for-apps-a1059836329/>) separately found the labels `can be tricky to read and understand`, with entries `cryptic`. *(Reported; not re-fetched by me.)* Also reported: the label interface’s own small print disclaims Apple verification of developer submissions — a neat illustration of F4’s core problem, where the qualification undercuts the headline.

**Why (g) matters for the skill.** Apple’s privacy *marketing* register (P01–P09, R19) and Apple’s privacy *label* surface are different products with different reliability. A skill that treats `Siri learns what you need. Not who you are.` as a model for a privacy *disclosure* is confusing a promise with a specification.

### B5.9 Correction: the ASA angle is weaker than the brief assumed

The original research brief assumed UK ASA rulings against Apple would be a useful failure-mode source. **That assumption does not hold, and I am recording the correction explicitly because the failure mode here is asymmetric** — a writer who half-remembers “Apple was censured by the ASA” and finds matching URLs may cite them as criticism when they did not go that way.

- A delegated researcher reported retrieving **three Apple ASA rulings, all adjudicated `Not Upheld`**, citing IDs `A18-445104` (iPhone X “Studio-quality portraits”), `A12-207565` (iCloud “automatic and effortless”) and `A11-161503` (iPhone 4 “world’s thinnest smartphone”).
- **I could not verify any of these.** The live `asa.org.uk/rulings/…` URLs return HTTP 404 in every slug format I tried, and the Wayback Machine reports `no archived snapshots` for each (checked via the availability API and by direct snapshot request). **Status: (X) excluded.** Neither the existence nor the outcome of these three rulings is confirmed by me.
- What this means for the UK regulator angle overall: **the 2019 pressure point on Apple’s performance claims came from Which?, a consumer organisation, not from the ASA** — see B5.8(a). That is a well-evidenced finding.
- My F1 reference to a **2008 ASA ban** over `"all parts of the internet are on the iPhone"` remains **reported via Wikipedia only**; I have not retrieved that ruling either, and the same caution applies. **Treat the ASA as an unverified angle. Lean on Which?, the CFPB, the FTC and the DOJ, all of which I did verify.**

### B5.10 Additional honest null

**“Apple’s support documentation is too terse / assumes too much prior knowledge” has no citable published source.** Three delegated searches (Google News RSS, Bing News RSS, HN Algolia) found nothing. I flag this because it is an intuitively appealing claim that a writer might otherwise assert. My own reading of Apple’s support articles (B1.5) found them *clear and well-sequenced* — the imperative steps, the quoted alert strings, and the misconception-correcting headings (`Your Apple Watch is water resistant, but not waterproof.`) are competent technical writing. **Do not claim Apple’s support docs are terse.** If a skill needs a support-doc critique, it must be built from Apple’s own articles as examples rather than from published criticism, because there isn’t any.

## B6. The Apple Style Guide — primary-source rules (this supersedes blog folklore)

Most “how Apple writes” content online is inference from finished web pages. Apple actually publishes its editorial rulebook, and it is retrievable:

- Web: <https://support.apple.com/guide/applestyleguide/welcome/web> (retrieved; dated **June 2026**)
- PDF: <https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf> (retrieved; 244 pages, 4.1 MB)

**Scope, stated by Apple itself** (verbatim from the PDF): `The Apple Style Guide provides editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and user interfaces.` … `Apple developers and third-party developers should follow these guidelines for user-facing text.` … and critically: **`Some departments at Apple (Marcom, for example) have supplemental style guides.`**

That last sentence is Apple conceding the two-voice structure of B3 in its own words: **the documentation voice and the marketing (Marcom) voice are governed separately.** Apple’s baseline is *The Chicago Manual of Style* + *Merriam-Webster’s Collegiate Dictionary*, with `Exceptions to guidelines in these resources are noted in this guide.`

### B6.1 Rules that settle open questions

These are **verbatim Apple rules**, so they are stronger evidence than any count I can take from a sample:

| Topic | Apple’s rule (verbatim) | How it relates to my measurements |
|---|---|---|
| **Exclamation points** | `OK to use exclamation points occasionally in promotional text and dialogue. Avoid in documentation.` | Explains R2. Apple *permits* them in promo copy and still, in my sample, used **zero** in 4,638 sentences. The restraint is stronger than the rule requires. |
| **Serial comma** | `Use a serial comma before and or or in a list of three or more items.` Example given: `You can ask Siri to place phone calls, send text messages, send reminders, and more.` | Confirms F11 / `HDMI, Thunderbolt 5, SDXC, MagSafe, Wi‑Fi 7, and Bluetooth 6.` Oxford comma is official, not optional. |
| **Em dash** | `Use the em dash (—) to set off a word or phrase that interrupts or changes the direction of a sentence… Don’t overuse em dashes.` … `Close up the em dash with the word before it and the word after it.` | Confirms R17 from the other direction: Apple’s rule is *sparing* use, closed up with no surrounding spaces. My finding of 0/83 headlines containing an em dash is consistent with `Don’t overuse`. |
| **Numerals 1–9** | `Spell out the following numbers: Cardinal numbers from one through nine. (However, use a numeral, no matter how small, to express numbers as numbers and as units of measure.)` | Refines R9. It is **not** “always numerals” — it is numerals for measurements, words for small counts. `up to five computers` but `8 hours`. |
| **Numbers in one paragraph** | `For numbers of the same category within a paragraph, if any number is larger than nine.` Example: `We have 25 computers and 4 printers on the network.` | Explains why Apple pages mix `1600 nits` and `two displays` in different sentences. |
| **Sentence-initial numbers** | Spell out. Correct: `Two hundred fifty functions are available in the Function Browser.` **Preferable:** `The Function Browser gives you access to 250 functions.` | Directly relevant to the “one-word opener + period” headline shape — Apple’s documented preference is to **restructure the sentence** to avoid a leading spelled-out number. |
| **Battery life** | `Use numerals when referring to battery life (up to 8 hours of battery life, up to an 8-hour battery life).` | Explains the `Up to 24 hours` pattern in R10 as a *documented* convention. |
| **Percent** | `Always preceded by a numeral, no matter how small the value. 1 percent` | Resolves the `80 percent` vs `80%` inconsistency I flagged in R9: Apple’s default is the word, with `%` reserved for `technical appendixes, specification lists, and tables`. |
| **Speed / the `x` suffix** | `For the speed of optical drives, use a lowercase x—for example, 24x speed. Note that there’s no space between the numeral and the x.` | Explains the form of `6x faster` / `7.8x faster`: lowercase `x`, closed up, no space. |
| **`24/7`** | `Not 24x7. To spell out, use the form 24 hours a day, 7 days a week.` | Matches `support for all your hardware and software needs 24/7` (O05). |
| **Passive voice** | `Avoid when possible and use active voice.` | Consistent with the imperative-heavy support copy (R15). |
| **Callout / caption punctuation** | `Use sentence-style capitalization. Use a period for a complete sentence and no ending punctuation for a sentence fragment.` | **This is the important one.** Apple’s *documented* rule is the opposite of what its marketing headlines do: 76/83 marketing headlines are fragments ending in a period (R1). The marketing register is a **deliberate, documented departure** from Apple’s own baseline, not an application of it. |

### B6.2 The refined rule for a skill

Combining B3 and B6, the honest formulation is not “Apple writes short punchy sentences.” It is:

> **Apple operates two rulebooks.** The *documentation* rulebook (Apple Style Guide) governs support, settings, alerts, and developer-facing UI: sentence case, period only on complete sentences, no exclamation points, active voice, serial comma, spell out one through nine. The *Marcom* rulebook governs product pages and keynotes: two-beat fragments that **do** take a period, coined compounds, withheld verbs, puns, and `up to`-hedged superlatives. A writer must pick one rulebook per surface and not blend them — the blend is what produces the “uncanny Apple” register that reads as parody.

The Style Guide also explicitly defers on localisation — `For localized content, consult resources specific to the language or region.` — which is consistent with the Korean evidence in B4/F6: Apple’s English rulebook does not transfer, and the `-죠` softener and idiom-pun strategy are region-specific editorial decisions, not translations of the English.

## B7. The regulatory floor under the footnote pattern

The footnote apparatus in B1.3 and the `up to` hedge in R10 are not stylistic flourishes. They are the visible surface of a legal obligation, and that is the strongest argument for why they must not be copied decoratively.

**Primary source (retrieved).** The US Federal Trade Commission’s advertising guidance, <https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business>, states verbatim:

> `What truth-in-advertising rules apply to advertisers? Under the Federal Trade Commission Act:` `Advertising must be truthful and non-deceptive;` `Advertisers must have evidence to back up their claims; and` `Advertisements cannot be unfair.`

And, on substantiation:

> `Are letters from satisfied customers sufficient to substantiate a claim? No.`

> `Offering a money-back guarantee is not a substitute for substantiation.`

The FTC’s advertising-and-marketing hub, <https://www.ftc.gov/business-guidance/advertising-marketing>, states: `Under the law, claims in advertisements must be truthful, cannot be deceptive or unfair, and must be evidence-based.`

**Why this matters for the skill.** Apple’s `Fly through demanding AI tasks up to 6x faster.` is lawful because Apple can produce the test conditions — and it discloses them in 40 footnotes reading `Testing conducted by Apple in September 2025 using preproduction 14-inch MacBook Pro systems with Apple M5…`. The stylistic move (`up to Nx`) and the evidentiary apparatus (the methodology footnote) are a **single legal unit**. A skill that teaches the first without the second is teaching a writer to make an evidence-based claim with no evidence. Two concrete failure modes follow:

1. **The hedge without the evidence.** `up to 3x faster` with no test conditions is not a cautious claim; it is an unsubstantiated one, and the hedge makes it look more defensible than it is.
2. **The footnote as decoration.** Copying `Performance tests are conducted using specific computer systems and reflect the approximate performance of…` into a document that has no performance tests converts a disclosure into a false statement.

### B7.1 Additional verified regulatory constraints

Beyond the FTC truth-in-advertising rules and *[.com Disclosures](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf)* quoted above and in F4, these were retrieved and quote-checked:

- **GDPR Article 12(1)** — <https://gdpr-info.eu/art-12-gdpr/> — retrieved, verified verbatim: `The controller shall take appropriate measures to provide any information referred to in Articles 13 and 14 and any communication under Articles 15 to 22 and 34 relating to processing to the data subject in a concise, transparent, intelligible and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child.` Note this is a **conjunctive** standard — four separate duties — and it is a *comprehensibility* standard, not a voice standard. It does not forbid warmth; it does forbid ambiguity that a reader cannot resolve.
- **21 CFR 202.1 (US prescription-drug advertising)** — <https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202/subpart-A/section-202.1> — retrieved, verified verbatim: no advertisement is in violation if `the presentation of true information relating to side effects and contraindications is comparable in depth and detail with the claims for effectiveness or safety`. This `fair balance` / `comparable in depth and detail` requirement is the strongest single counterexample to the Apple hero-plus-footnote pattern: in pharma, the qualification must be *as prominent as* the claim. Apple’s style is structurally illegal there, and this is a hard boundary rather than a stylistic preference.

**Excluded as unverified.** A delegated researcher reported an FTC Deception Policy Statement line, `Advertising that lacks a reasonable basis is also deceptive`, at <https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception>. **I fetched that URL and the phrase is not on the page** (it is a landing page; the statement itself is a linked PDF I did not retrieve). **Not quoted here.** The same applies to reported DSA Article 25, UCPD 2005/29/EC, SEC Rule 206(4)-1, FCA COBS 4.2.1 R and Korean MFDS wording: plausible and probably correct, but **not verified by me**, so Part B does not rely on them.

**Honest boundary.** I did not retrieve the UK CAP Code, the EU Unfair Commercial Practices Directive text, or any ASA/CmA ruling on Apple. ASA’s site is JS-rendered and its search API returned 404; a delegated search found **no ASA ruling on Apple at all** (see B5.6). The UK ASA action in F1 is reported via Wikipedia, not from the ruling itself. Anyone extending this section should fetch those primaries before asserting them.

## B8. Corpus scorecard

| Category requested | Delivered | Notes |
|---|---|---|
| product hero / tagline | 15 (H01–H15) | EN, five product pages |
| feature blurb, `Label. Plain meaning.` | 13 (F01–F13) | incl. the three-beat variants |
| footnote | 8 (N01–N08) | from 59 retrieved; the template lines |
| privacy / security | 9 (P01–P09) | `/privacy/` + `/apple-intelligence/` |
| support article & error/alert | 6 (S01–S06) | 5 support articles retrieved |
| onboarding / setup | 5 (O01–O05) | AppleCare |
| legal / terms microcopy | 3 (L01–L03) | + the 694-word lease footnote |
| App Store product page | 5 (A01–A05) | subtitle, description, release notes |
| Korean localized copy | 8 with EN counterparts (K01–K08) + 2 noted | EN/KR pairs verified page-to-page |
| **Total** | **52 catalogued** | from **24 pages**; **4,638 sentences** in the measurement sample |

### B8.1 Adversarial and primary-source evidence retrieved

| Evidence | Type | Verified by me |
|---|---|---|
| Apple Style Guide, June 2026 (244 pp. PDF + web) | Apple’s own rulebook | **(V)** verbatim |
| Apple HIG “Writing” (via `…/writing.json`) | Apple’s own UI guidance | **(V)** verbatim |
| *Landsheft v. Apple*, N.D. Cal. 5:25-cv-02668 (19 pp.) | Federal complaint | **(V)** verbatim |
| *US v. Apple*, D.N.J. 2:24-cv-04055 (88 pp.) | Federal complaint | **(V)** verbatim |
| FTC *[.com Disclosures](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf)* (2013) | Regulator guidance | **(V)** verbatim |
| FTC truth-in-advertising FAQ + hub | Regulator guidance | **(V)** verbatim |
| GDPR Art. 12(1); 21 CFR 202.1 | Statute / regulation | **(V)** verbatim |
| “Letter from Apple Regarding iPhone 4” (2010) | Apple primary | **(V)** verbatim |
| PIPC privacy-policy evaluation, 인공지능신문 2025-03-16 | Korean regulator, reported | **(V)** Korean verbatim; Apple not named |
| Apple Translate controversy, 뉴시스 2024-08-28 | Korean press | **(V)** Korean verbatim |
| MacRumors settlement report; 9to5Mac Apple statement; Wikipedia regulator actions; INTERNET Watch JP pair | Press / secondary | **(R)** reported only |
| Which? battery-life study (via Wayback); The Verge M1 Ultra critique; Guardian 21,586-word T&C count; ToS;DR Grade C; CFPB Apple Card action (via Wayback); netzpolitik/Oxford privacy-label study | Test result, press, regulator | **(V)** verbatim |
| Apple iPhone 18 Pro Tech Specs (`Up to 45 hours` + `preproduction` footnote) | Apple primary artifact | **(V)** verbatim |
| Three Apple ASA rulings reported as `Not Upheld` | Reported | **(X)** excluded — live 404, no Wayback snapshot (B5.9) |
| FTC Deception Policy Statement line; DSA 25; UCPD; SEC 206(4)-1; FCA COBS 4.2.1 R; MFDS wording; TechRadar; Consumer Reports; 9to5Mac M1 Ultra | Reported | **(X)** not verified by me |

**Failure-mode coverage:** F1–F11. F9 (no apology register), F10 (register collision) and F11 (localisation) rest on retrieved primary documents. F4 and F1 now cite independent test results (Which?), an independent methodology critique (The Verge) and a regulator finding (CFPB) rather than my measurement alone.

## B9. What Part B does NOT establish

**Epistemic key used throughout Part B.** Every claim is one of four kinds, and they must not be merged:
- **(M) I measured it** — my own count on a stated sample (all of B2’s rule table).
- **(V) I retrieved and verified it verbatim** — Apple’s Style Guide and HIG, the Apple pages in B1, the iPhone 18 Pro specs footnote, the *Landsheft* and *DOJ* filings, the FTC *[.com Disclosures](https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf)*, GDPR Art. 12, 21 CFR 202.1, the FTC truth-in-advertising pages, the iPhone 4 letter, the Which? battery study, The Verge M1 Ultra critique, the CFPB Apple Card action, the Guardian T&C piece, ToS;DR, the netzpolitik/Oxford privacy-label study, and the Korean PIPC and Newsis reporting.
- **(R) Reported by someone else, not verified by me** — the MacRumors settlement figure, the 9to5Mac Apple statement, the Wikipedia-sourced regulator actions, the INTERNET Watch Japanese localisation pair, TechRadar, Consumer Reports, the 9to5Mac M1 Ultra piece.
- **(X) Excluded** — sources I could not retrieve: the three Apple ASA rulings reported as `Not Upheld`, the FTC Deception Policy Statement line, DSA Art. 25, UCPD, SEC 206(4)-1, FCA COBS 4.2.1 R, and MFDS wording. Listed in B5.6, B5.9 and B7.1 and **not** quoted as evidence.

- **No diachronic claim.** Everything here is M5-era copy fetched 2026-09-30 (the one 2010 document, the iPhone 4 letter, is used as a *contrast case*, not as evidence about drift). I did not archive-compare earlier Apple copy, so no statement about how Apple’s style has changed over time is supported.
- **No sitewide claim.** 24 pages, 52 catalogued corpus sentences, 4,638 sentences in the measurement sample. Apple publishes vastly more. Every count in B2 is a count of *that* sample.
- **Korean support copy is untested.** I retrieved `apple.com/kr/` marketing pages only. R20–R22 describe Korean *marketing* prose. Whether `support.apple.com/ko-kr` uses `-죠`, or how it handles error strings, is unknown and must not be asserted.
- **The Korean regulatory finding does not name Apple.** The PIPC evaluation (B5.5a) reports `12개의 해외사업자` in aggregate. Apple being among them is plausible but **not stated in the source**. Cite the category-level result, never an Apple-specific one.
- **`web_search` was degraded all session** (SearXNG: zero results; Tavily/Brave: unconfigured; DuckDuckGo: HTTP 202; Bing/Mojeek/Startpage/Marginalia: mismatched, 403, or empty). Delegated researchers recovered most of the adversarial material via **Google News RSS**, CourtListener RECAP, Yahoo! Japan and Wayback — but the two gaps below remain genuinely open, and B5.6/B5.9/B5.10 are the honest inventory of what is *not* established.
- **No corpus-linguistics or discourse-analysis study of Apple’s register was located.** I could not confirm one exists, and I could not confirm one does not. Treat “researchers have found that Apple…” as unverified until a specific paper is produced.
- **No readability *score* for Apple copy was retrieved — but a word count now exists.** The Guardian’s **21,586 words** for the iPhone T&Cs (B5.8e) is a journalist’s count, not a Flesch-Kincaid or Gunning Fog figure; it is labelled OPINION. The only sentence-length measurements in this document are mine (R8). Korea’s PIPC publishes scored readability figures, but for privacy policies in aggregate and not for Apple (B5.5a).
- **The ASA is not a usable anti-Apple source.** Three Apple ASA rulings were reported to me as adjudicated `Not Upheld`, but I could not verify them (live 404, no Wayback snapshot). Correcting an earlier over-strong null, the honest position is: **neither an ASA censure nor an ASA exoneration of Apple is verified in Part B.** Use Which?, the CFPB, the FTC and the DOJ instead (B5.9).
- **Apple’s support documentation is *not* criticised as terse by any source I could find**, and my own reading of it found it clear. Do not assert that claim (B5.10).
- **Quotes sourced via Wikipedia** (F1, F2, F3) are reported as Wikipedia’s text, with the underlying primary documents named but not directly retrieved. Do not upgrade them to primary-source citations without fetching the original.
- **The two most-quoted Apple apocrypha are excluded.** Steve Jobs' “You’re holding it wrong” email and Phil Schiller’s “courage” quotation were both searched for and **not retrieved** (see B5.6). They appear nowhere in Part B and must not be presented as sourced.

---

---

# B10 — Addendum: second verification pass with a real browser (ego-browser, 2026-09-30)

Four items that plain HTTP could not settle were checked in a JavaScript-rendering browser. Everything below is from the source’s own site; nothing here is reported secondhand. The skill files (`apple-writing/references/sources.md` §4) carry the same findings.

## B10.1 The ASA question is closed — with a measured coverage limit

| Query on `asa.org.uk/codes-and-rulings/rulings.html` | Result |
|---|---|
| `Apple Inc` | **0 rulings** |
| `Apple Distribution International` | **0 rulings** |
| `Apple Distribution`, date range 2004–2026 | **0 rulings** |
| `Apple`, no filter | 30 keyword matches, **none titled Apple** (ads that mention it: games, drinks, funeral plans) |
| `Samsung` (method check) | 5 results incl. `Samsung Electronics (UK) Ltd` — the search does index advertiser names |

- The three ruling URLs reported elsewhere as adjudicated *Not Upheld* (`…a18-445104`, `…a12-207565`, `…a11-161503`) return **HTTP 404** in the browser.
- **Archive depth, measured with the date filter** (`dd/mm/yyyy` is the accepted format; ISO and long-form are ignored): 2021: 83 · 2022: 278 · 2023: 330 · 2024: 280 · 2025: 294 · 2026: 244 — and **0 for every year tested 2007–2020**. Ryanair returns only two rulings (2023, 2026) despite a long older history.

**Corrected position, replacing B5.9 and B9’s “unverified” framing:** neither an ASA censure nor an ASA exoneration of Apple is retrievable, the specific rulings alleged to exist do not resolve, and the archive does not reach back far enough to test the 2008 story. For the years the archive does cover, **the ASA has published no ruling naming Apple** — a verified negative, which is stronger than the previous “unverified”. Do not cite the ASA as an anti-Apple source; the verified UK pressure point remains the 2019 Which? battery study.

## B10.2 App Store character limits — verified field by field

App Store Connect Help (`…/reference/app-information/`, `…/reference/platform-version-information/`), quoted wording:

| Field | Limit | Apple’s wording |
|---|---|---|
| Name | 30 characters | “…than 30 characters” |
| Subtitle | 30 characters | “This can’t be longer than 30 characters.” |
| Promotional text | 170 characters | “This property can’t be longer than 170 characters.” |
| Description | 4,000 characters | “Limited to 4000 characters.” |
| Keywords | 100 bytes | “You can provide up to 100 bytes of content.” |
| What’s New | 4,000 characters | “Limited to 4000 characters.” |

This closes the B5 note that the numbers were only citable from ASC Help without confirmation — they are now confirmed there directly.

## B10.3 The corpus-linguistics gap is closed (B5’s weakest section)

Two academic studies of Apple’s advertising language exist and were retrieved:

- **Lin, Q. & Hu, X. (2025).** *A Sociolinguistic Study on Linguistic Deviation in Apple’s Advertisement.* Journal of Social Science and Humanities 7(1). PDF: `https://bryanhousepub.com/index.php/jssh/article/download/1367/1322`. Leech’s deviation model applied to Apple ads; six types found — **phonological** (alliteration, repetition, consonance), **lexical** (coined terms signalling novelty), **graphological** (altered word forms, including deliberate misspellings), **grammatical** (heavy ellipsis — e.g. `Think huge.`), **semantic**, and **deviation of register**.
- **Pham, T. T. H.** *More Than Meets the Eye: Pragmatic Implicature in Apple iPhone’s Slogans.* VNU Journal of Foreign Studies. `https://jfs.ulis.vnu.edu.vn/index.php/fs/article/view/86-103`. 16 English slogans, 2017–2023, Yule’s pragmatic framework: predominantly noun phrases, declaratives and imperatives; conventional implicature used to signal elegance and innovation.

Both are small qualitative studies — cite as corroboration, not as measurement. Note that **neither measures readability**, so the Flesch-Kincaid gap in B9 still stands. Also notable: the first study names *register deviation* as a category, which independently supports this document’s central finding that Apple’s marketing register is a deliberate departure rather than an application of the editorial rules.

## B10.4 Korean register, measured on Apple’s own support pages

`support.apple.com/ko-kr/102639` and `support.apple.com/ko-kr/guide/iphone/welcome/ios` use **하십시오체** with **zero occurrences of `당신`** (`따르십시오`, `설정하십시오`, `조절하십시오`). That makes **three** distinct Apple Korean registers, chosen by content type: marketing (합니다체 + 해요체, `당신` present), support and user guides (하십시오체, no `당신`), press releases (한다체). R20–R22 in Part B cover marketing only; this extends the picture without contradicting it. The `apple-writing` skill is English-only by decision, so this is recorded for a future Korean layer.
