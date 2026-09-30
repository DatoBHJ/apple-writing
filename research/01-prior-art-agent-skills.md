# 선행 사례 조사: “Apple 문체/보이스” Agent Skill

- **조사 목적**: Apple의 **산문 스타일(prose / voice / tone / copy)** 을 인코딩한 Agent Skill이 이미 존재하는지 확인 → 중복 개발 회피
- **조사일**: 2026년 기준 (레포 `pushed_at` 기준 최신 확인)
- **조사 방법**: `web_search` 툴이 조사 기간 내내 장애(SearXNG 0건, Tavily/Brave 키 미설정, DuckDuckGo HTTP 202). 아래 대체 경로로 진행했고, **모든 URL은 HTTP 상태 코드로 실제 응답을 검증**(전부 200):
  - Brave Search HTML 스크래핑 (`https://search.brave.com/search`) — 주 검색 엔진
  - `gh api search/repositories`, `gh api search/code` (인증된 `gh` CLI, code search 가능)
  - GitHub raw / HuggingFace API / Vale registry JSON 직접 조회
  - Bing HTML — **사용 불가 판정**: 인용부호 포함 쿼리를 무시하고 한국 로컬라이즈 상업 결과만 반환
  - Mojeek(403 차단), searx.be(안티봇 캡차), Ecosia(403), DDG(202) — 모두 실패
- **주의**: JS 렌더링 페이지 판정 — `vale.sh/hub/`는 `/explorer`로 301 리다이렉트되며 209KB HTML을 반환하나, 패키지 목록 자체는 클라이언트 렌더링이라 스크래핑으로는 못 읽음. 대신 **레지스트리 원본 데이터(`errata-ai/packages` → `library.json`)를 직접 파싱**해 우회함(이게 오히려 더 권위 있는 1차 자료).

---

## (a) 요약 표

깊이 등급: ★☆☆☆☆ = 분위기/형용사 나열 수준 · ★★★☆☆ = 실제 결정 규칙 있음 · ★★★★★ = 규칙 + 예시 + 예외 + 평가(evals)까지

| 이름 | URL | 무엇을 하는가 | 애플 문체 특화? | 형식 | 깊이 | 라이선스 |
|---|---|---|---|---|---|---|
| **apple-copywriting** | https://github.com/Aaditya93/mmm_backend/tree/main/apple-copywriting | Apple 마케팅 카피를 재현하는 SKILL.md + 참조 라이브러리 | **예 (마케팅 카피 한정)** | 다중 파일 (SKILL.md + references 4개, ~40KB) | ★★★★☆ | **없음 (무라이선스)** |
| **apple-design-skill** (`prompts/copywriting.md`) | https://github.com/chaos-xxl/apple-design-skill | UI 디자인 스킬이지만 카피 모듈을 내장. EN/ZH 패턴 테이블 | **예 (카피 모듈 한정)** | 다중 파일 (UI 스킬 + copywriting.md) | ★★★☆☆ | MIT |
| **apple-design-skill** (naplesblue) | https://github.com/naplesblue/apple-design-skill | UI/디자인 전용 — **산문 모듈 없음** | 아니오 (UI만) | 다중 파일 | — (문체 아님) | NOASSERTION |
| **Apple-style-guide (Vale)** | https://github.com/ChrisChinchilla/Apple-style-guide | 공식 *Apple Style Guide*의 Vale 린트 룰 구현 | 부분 (편집/표기 규범, 마케팅 보이스 아님) | 룰셋 (.yml 12개 + accept/reject 사전) | ★★☆☆☆ (WIP, 미완) | MIT |
| **applestyleguide (텍스트 덤프)** | https://github.com/softwarehistorysociety/applestyleguide | 공식 *Apple Style Guide* 전문을 txt/rtf/xml로 보관 | 부분 (편집 규범 원문) | 단일 대용량 텍스트 (459KB txt) | 원문 데이터 (스킬 아님) | NOASSERTION |
| **Apple Style Guide (공식)** | https://support.apple.com/guide/applestyleguide/ | Apple 공식 편집 스타일 가이드 (라이브) | 부분 (문서/마이크로카피 규범) | 웹 문서 | 원문 (스킬 아님) | Apple 저작권 (독점) |
| **yandex-tone-of-voice-skill** | https://github.com/Dankosik/yandex-tone-of-voice-skill | Yandex 제품 문체를 생성/각색/감사하는 브랜드 보이스 스킬 | 아니오 (Yandex) | 다중 파일 (SKILL.md + references 3 + **evals/** + tests) | ★★★★★ | MIT |
| **Brand-building-skills** (`brand-voice`) | https://github.com/arnabbagxd/Brand-building-skills | 브랜드 버벌 아이덴티티 정의 (톤/보이스/어휘/메시징 규칙) | 아니오 (범용) | 다중 파일 (스킬 30+) | ★★★☆☆ | MIT |
| **writing-skills** | https://github.com/surendranb/writing-skills | 공식 문체 프레임워크 + 캐릭터 보이스 스킬 모음 | **아니오 (Apple 없음)** | 다중 파일 (스킬 19개) | ★★★☆☆ | MIT |
| **microsoft-style-skill** | https://github.com/powerstacks-corp/microsoft-style-skill | MS Writing Style Guide 준수 감사/재작성 | 아니오 (Microsoft) | 단일/다중 md | ★★★☆☆ | NOASSERTION |
| **brand-skills** | https://github.com/cofoundy/brand-skills | 브랜드 네이밍·아이덴티티·보이스·브랜드북 생성 | 아니오 (범용) | 다중 파일 | ★★★☆☆ | NOASSERTION |
| **Voices (Vale)** | https://github.com/jdkato/voices | 보이스를 **프롬프트가 아닌 Vale 룰**로 구현 (Direct/Simple/Human/GenZ/Coach/Claude) | 아니오 (범용) | 룰셋 (.yml) | ★★★★☆ | MIT |
| **brand-voice-spec** | https://huggingface.co/datasets/thehonestape/brand-voice-spec | 브랜드 보이스를 기계 판독 JSON 스펙으로 (rules/lexicon/preference_pairs) | 아니오 (범용, 가상 브랜드) | 데이터 스펙 (voice.json + jsonl 6종) | ★★★★☆ | CC-BY-4.0 |
| **Vale 공식 레지스트리** | https://github.com/errata-ai/packages | Vale 패키지 27종 (Google·Microsoft·Salesforce·RedHat 포함) | **아니오 — Apple 패키지 부재** | 레지스트리 JSON | — | MIT |
| **humanizer** | https://github.com/blader/humanizer | AI 티를 제거해 인간처럼 보이게 | 아니오 (범용) | 단일 md | ★★★☆☆ | MIT |
| **humanizer-skill** | https://github.com/Aboudjem/humanizer-skill | 55개 패턴 + 5개 보이스 + 0–100 AI-tell 점수 | 아니오 (범용) | 단일/다중 md | ★★★★☆ | MIT |
| **writing-style-skill** | https://github.com/jzOcb/writing-style-skill | 사용자 수정에서 규칙을 자동 학습해 SKILL.md를 스스로 개선 | 아니오 (개인 문체) | 단일 md + 학습 루프 | ★★★☆☆ | 없음 |
| **style-alchemy** | https://github.com/snowmays/style-alchemy | 글 샘플 뭉치를 스타일 프로파일로 증류 | 아니오 (개인 문체) | 다중 파일 | ★★★☆☆ | MIT |
| **marketingskills** (`copywriting`) | https://github.com/coreyhaines31/marketingskills | 전환 카피writing 스킬 (레퍼런스 + evals 포함) | 아니오 (전환 최적화) | 다중 파일 (스킬 49+) | ★★★★☆ | MIT |

**“없음” 판정 항목**
- **Apple 마케팅 카피 코퍼스/데이터셋: 없음.** GitHub repo 검색 `apple marketing copy dataset`(0건), `apple taglines`(2건 — 둘 다 무관: REST API plist, 아이폰 랜딩페이지 클론), `apple slogans`(2건 — 무관), `ad copy dataset slogans`(0건), `product hunt taglines dataset`(0건). HuggingFace `search=apple` 상위 30건은 전부 Apple의 ML 데이터셋(DFNDR, mkqa), 주가 데이터, 과일 사과, 블루아카이브 캐릭터 — 마케팅 카피 **0건**. `apple copy in:name` 상위는 전부 **웹사이트 HTML/CSS 클론**(SajjadAhmad14/Apple-Page-Copy, VaarunSinha/NotCopyingApple 등)이며 산문 데이터 아님.
- **awesome 리스트 내 Apple 문체/보이스 스킬: 없음.** `ComposioHQ/awesome-claude-skills`(75,980★) — “apple” **0건**. `travisvn/awesome-claude-skills`(15,228★) — “apple” 0건, voice/tone/style-guide 0건. `karanb192/awesome-claude-skills`(527★) — Apple 0건. `VoltAgent/awesome-agent-skills`(35,060★) — Apple 언급 4건 모두 **UI/플랫폼**(HIG, Sentry Cocoa SDK, Apple Bridges)이며 산문 스킬 0건.
- **Vale 공식 레지스트리의 Apple 패키지: 없음.** `library.json` 27개 패키지 전체 이름: A11y, AiTells, AsciiDoc, AsciiDocDITA, Comments, Commits, Diataxis, Elastic, Fiction, Google, Harper, Hugo, Joblint, Journals, MDX, Microsoft, OpenShiftAsciiDoc, Readability, RedHat, Salesforce, Std, Voices, ai-tells, alex, neighbor, proselint, write-good. “apple” 문자열 매치는 단 1건이며 그것도 Harper 패키지의 파비콘 URL(`writewithharper.com/apple-touch-icon.png`)이었다.

---

## (b) 항목별 상세

### Apple 산문 특화 (진짜 경쟁자)

#### 1. `apple-copywriting` — 가장 직접적인 선행 사례
URL: https://github.com/Aaditya93/mmm_backend/tree/main/apple-copywriting · 0★ · **무라이선스** · pushed 2026-09-10

`mmm_backend`라는 무관한 레포 안에 묻혀 있는 실제 `SKILL.md`. 구조는 정석적인 Anthropic Skills 관례를 따른다 — YAML frontmatter에 `name: copywriting` + 트리거 문장이 잔뜩 들어간 `description`, 그 뒤 지시문. 참조 파일 4개(`apple-patterns.md` 9.2KB, `apple-examples.md` 10.4KB, `project-descriptions.md` 10KB, `psychology-map.md` 9KB)로 총 ~40KB.

깊이는 **진짜다**. `apple-patterns.md`는 14개의 **명명된 패턴**을 정의하고 각각에 Apple 실제 카피 예시와 사용 조건, 템플릿을 붙인다: The Compound Boast, The Adjective Mashup, The Superlative Claim, The Contrast Move, The Declaration, The Rhythm Triple, The Command, The Specificity Drop, The Identity Line, The Understatement, The Rhyme/Sound Pattern, The Era Announcement, The Feature-Benefit Pair, The Concise Promise.

인용할 만한 실제 문장:
> “You are an **Apple-caliber copywriter** trained on real Apple marketing copy.”

> “1. **Benefit over feature** — Never write what a thing *is* before writing what it *does for you* … 5. **Verbs, not adjectives** — 'It flies through tasks' > 'It is very fast' … 8. **Rhythm matters** — Short short long. Short short long. The cadence *is* the feeling.”

> “**Pattern**: `[Adjective]. [Adjective]. [Noun phrase].` … **Apple examples**: 'Thin. Fast. Powerful and portable.' (MacBook Air) / 'Feature stacked. Value packed.' (iPhone 17e) / 'Smart. Secure. On device.' (Apple Intelligence)”

**한계**: (i) 마케팅 카피 전용 — 헤드라인·태그라인·CTA·랜딩페이지·프로젝트 설명만 다룬다. 리포트, 문서, README, 이메일, 분석 글에는 적용 지침이 없다. (ii) 다른 스킬(`marketing-psychology`)과 PLFS 스코어링에 하드 결합되어 단독 사용 불가. (iii) **라이선스가 없어** 법적으로 재사용·포크가 불가능. (iv) 0★, 무관한 레포에 매몰 — 사실상 발견 불가능한 상태. (v) 한국어/다국어 지침 없음.

#### 2. `chaos-xxl/apple-design-skill` — UI 스킬에 내장된 카피 모듈
URL: https://github.com/chaos-xxl/apple-design-skill · 21★ · MIT · pushed 2026-04-07

“UI 전용”이라는 통념과 달리, 이 스킬은 `prompts/copywriting.md`를 별도 모듈로 포함한다. 5개 핵심 원칙 + “Apple voice checklist” 5항목 + **언어별 패턴 테이블(영어/중국어)** 을 제공한다. 패턴은 Fragment Sentences, Single-Word Impact, Superlative/Comparative 등.

인용:
> “This module defines the rules and patterns for transforming ordinary product copy into Apple-style 'fruit-flavored' text. Apple’s voice is unmistakable: short, confident, and laser-focused on a single benefit per line.”

> “1. **One idea per line.** … 2. **Short beats long.** If you can say it in three words, don’t use six. Brevity signals confidence. … 4. **Rhythm matters.** Apple copy has a cadence — fragments, pauses (periods mid-sentence), and parallel structures create a reading tempo that feels intentional.”

**한계**: 카피 모듈은 UI 생성 파이프라인의 부속품이다. 트리거가 “Apple-style frontend UI code”라서 **“이 글을 Apple 문체로 고쳐줘”라고 하면 발동하지 않는다.** 또한 영어/중국어만 지원(한국어 없음).

#### 3. `naplesblue/apple-design-skill` — 사용자가 언급한 기존 “apple-design”
URL: https://github.com/naplesblue/apple-design-skill · 263★ · NOASSERTION · pushed 2026-07-20

파일 구성: `SKILL.md`, `app.md`, `checklist.md`, `components.md`, `design-system.md`, `icons.md`, `motion.md`, `patterns.md`, `review.md`, `tokens.css`, `examples/*.html`. **산문/카피 모듈이 전혀 없다.** 사용자의 전제(“apple-design은 UI/motion/interaction만 커버”)는 이 레포 기준으로 **정확하다**. 다만 `chaos-xxl` 버전은 카피 모듈을 갖고 있으므로, “Apple 카피는 아무도 안 했다”는 주장은 성립하지 않는다.

### Apple 편집 규범 (마케팅 보이스와 다른 층위)

#### 4. `ChrisChinchilla/Apple-style-guide` — Vale 룰 구현
URL: https://github.com/ChrisChinchilla/Apple-style-guide · 3★ · MIT · pushed 2025-11-29

공식 *Apple Style Guide* (2025년 6월판)를 Vale 린트 룰로 옮긴 것. `apple/` 디렉터리에 12개 룰 파일: Abbreviations, Capitalization, Clarity, Contractions, InclusiveLanguage, PassiveVoice, ProductNames, SerialComma, Spelling, Terminology, Verbs, WordyPhrases + accept/reject 사전.

인용:
> “This repository contains a [Vale-compatible](https://github.com/errata-ai/vale) implementation of the [*Apple Style Guide*](https://support.apple.com/guide/applestyleguide/) (June 2025).”

> “**Not complete, and WIP, contributions welcome**.😁”

> “This project is neither maintained nor endorsed by Apple.”

**한계**: 이건 **편집 규범 린터**지 보이스/톤 인코더가 아니다. Apple Style Guide는 Apple *문서*용 표기법(철자, 대문자, 용어, 직렬 쉼표)을 다루며, 마케팅 카피의 리듬·억양·수사는 다루지 않는다. 게다가 스스로 “미완성”이라 밝히고 있다.

#### 5. `softwarehistorysociety/applestyleguide` + 공식 원문
URL: https://github.com/softwarehistorysociety/applestyleguide · 1★ · NOASSERTION · pushed 2022-08-25
공식: https://support.apple.com/guide/applestyleguide/ (HTTP 200)

공식 가이드 전문을 `applestyleguide.txt`(459KB), `.rtf`(8.9MB), `.xml`(616KB)로 보관. **스킬이 아니라 원문 데이터**다. 다만 이 원문은 마이크로카피에 실질적으로 유용하다 — `nicnocquee`의 큐레이션 글(https://nicnocquee.com/blog/learning-microcopy-from-apple-style-guide, 2019)이 보여주듯:

> “**allow** — Avoid using allow when you can restructure a sentence to make the reader the subject. … Avoid: FileMaker Pro allows you to create a database. / Preferable: You can create a database with FileMaker Pro.”

이런 규칙은 마케팅 보이스가 아니라 **UI 마이크로카피/문서 규범**이다. 우리 스킬이 참조할 1차 자료로는 가치가 높지만, 경쟁 제품은 아니다.

### 브랜드 보이스 스킬 (구조적 유사 사례)

#### 6. `Dankosik/yandex-tone-of-voice-skill` — **구조적으로 가장 모범적인 선례**
URL: https://github.com/Dankosik/yandex-tone-of-voice-skill · 0★ · MIT · pushed 2026-09-16

우리가 만들려는 것과 **동일한 형태**를 가진 유일한 사례. 브랜드(Yandex) 하나의 톤을 생성/각색/감사 3가지 모드로 적용한다.

구성: `SKILL.md`(6.8KB) + `references/tone-system.md`(14KB) + `references/examples.md`(5.1KB) + `references/source-map.md`(9.2KB) + `docs/instruction-audit.md` + **`evals/`**(boundary-prompts.json, boundary-rubric.json, evals.json, invocation.json) + `tests/test_resources.py`.

인용 (러시아어 원문):
> “Независимая реконструкция голоса продуктовых страниц, не официальный брендбук. Упоминание Яндекса без задачи на этот голос не активирует навык.”
> (= 제품 페이지 보이스의 독립적 재구성이며 공식 브랜드북이 아니다. 이 보이스에 대한 작업 없이 Yandex를 언급하는 것만으로는 스킬이 발동하지 않는다.)

> “Конкретика важнее усилителей, глаголы — канцелярита. … По умолчанию — «вы», «ё», русские кавычки, заголовки без точки и лишних прописных.”
> (= 구체성이 강조어보다, 동사가 관청어보다 낫다. 기본값은 «вы», «ё», 러시아식 따옴표, 마침표 없는 제목과 불필요한 대문자 회피.)

**핵심 시사점 3가지**: (i) **트리거 위생** — 브랜드 이름만 언급해도 발동하지 않도록 `description`을 설계했다. Apple은 브랜드명이 훨씬 흔한 단어라 이 문제가 더 심각하다. (ii) **evals를 스킬에 포함** — 경계 프롬프트와 루브릭으로 발동/비발동을 검증한다. (iii) **기본값 명시** — “«вы», «ё»” 처럼 구체적 기본값을 박아둔다. 우리 스킬의 한국어 처리에 직접 참고할 만하다. 다만 Apple용은 아니고, 0★라 검증된 실사용은 없다.

#### 7. `arnabbagxd/Brand-building-skills` — 최대 규모 범용 브랜드 스킬
URL: https://github.com/arnabbagxd/Brand-building-skills · 697★ · MIT · pushed 2026-06-13

`skills/brand-voice/SKILL.md` 포함 30+ 스킬(brand-identity, brand-messaging, brand-guidelines, brand-story 등).

인용:
> “You are a senior verbal identity strategist and copy director. Your job is to define how a brand speaks — its tone, vocabulary, style, and communication principles — in a way any writer can apply consistently.”

**한계**: 브랜드 보이스를 **정의하는(생성하는)** 스킬이지, 특정 보이스를 **실행하는** 스킬이 아니다. 사용자에게 “Formal ↔ Casual, Serious ↔ Playful” 스펙트럼을 물어보고 새 가이드를 만들어준다. Apple이라는 구체적 목표 보이스의 결정 규칙은 없다. 즉 **경쟁이 아니라 보완재** — 우리 스킬과 조합 가능.

#### 8. `surendranb/writing-skills` — 공식 문체 프레임워크 모음 (Apple 부재)
URL: https://github.com/surendranb/writing-skills · 39★ · MIT · pushed 2026-09-02

19개 스킬. 공식 문체: `gov-uk-style`, `google-dev-docs`, `journalism-ap`, `asd-ste100`, `plain-language`, `business-writing`, `corporate-communication`, `orwells-rules`. 캐릭터 보이스: `bob-ross`, `jack-sparrow`, `paddington`, `scott-adams`, `shrek`, `ted-lasso`, `winnie-the-pooh`, `yoda`.

인용 (레포 설명):
> “Procedural writing-style skills for AI agents: official frameworks (plain language, business writing, GOV.UK, AP style, STE-100, developer docs) + character voices.”

**핵심 시사점**: 이 사람은 GOV.UK·AP·STE-100·Google·Orwell을 스킬로 만들었지만 **Apple은 없다**. “브랜드/기관 문체를 스킬로 만든다”는 패턴은 검증됐는데 Apple만 비어 있다는 뜻이며, 캐릭터 보이스까지 섞는 걸 보면 **우리 스킬이 들어갈 자리가 정확히 여기**다.

#### 9. `powerstacks-corp/microsoft-style-skill`
URL: https://github.com/powerstacks-corp/microsoft-style-skill · 19★ · NOASSERTION · pushed 2026-06-10
Microsoft Writing Style Guide 준수를 감사·재작성. IT 관리자 대상 최적화. Apple용의 직접적 대응물이 **Microsoft에는 있고 Apple에는 없다**는 증거.

### “보이스를 규칙/데이터로” — 형식적으로 가장 진보한 접근

#### 10. `jdkato/voices` — 보이스를 Vale 룰로 (프롬프트가 아니라)
URL: https://github.com/jdkato/voices · 3★ · MIT · pushed 2026-09-28 (매우 최근)

인용:
> “Writing voices from the [output-style catalog](https://github.com/smixs/awesome-claude-output-styles#the-styles), written as **Vale rules instead of prompts**. Checked on every draft rather than remembered, and free until something breaks one.”

> “`Claude` is the demo for the argument: the formatting section of a production system prompt is already a linter.”

구현된 보이스: `Voices`(공통 코어), `Direct`, `Simple`, `Human`, `GenZ`, `Coach`, `Claude`. 각각 구체적 수치 규칙을 갖는다 — Direct: “No hedging, no preamble, sentences under 25 words, paragraphs above 50 on reading ease”. Simple: “Only the 850 words of Basic English, paragraphs above 80 on reading ease”.

**핵심 시사점**: “보이스는 기억하는 게 아니라 매 초안마다 검사되어야 한다”는 **철학적 경쟁**이다. 우리 SKILL.md가 산문 지시문인 이상, 이 접근보다 약하다는 비판을 받을 수 있다. 대응 전략: SKILL.md로 생성 규칙을 주되, **선택적으로 Vale 룰/체크리스트를 동봉**해 검증 가능성을 확보. Apple 보이스는 없으므로 빈칸은 여전히 있다.

#### 11. `thehonestape/brand-voice-spec` (HuggingFace) — 보이스를 데이터로
URL: https://huggingface.co/datasets/thehonestape/brand-voice-spec · CC-BY-4.0 · 118 downloads

인용:
> “Most brand voice lives in a slide deck no model can read. When an LLM writes copy, it falls back to the median of its training data: hedging, buzzwords, passive voice, the corporate gray. This spec is the inverse. The same file a human maintains is the file that conditions the model.”

구성: `voice.json`(정본) + `data/{rules,examples,preference_pairs,lexicon,prompts,changelog}.jsonl` + `SCHEMA.md`. `voice.json`은 `registers`(cafe/trade), `tone` 배열, `guidelines[]`(각 규칙에 `derivedFrom`, `explanation`, `derivedFromCorrection` 역참조)를 담는다. 예시 브랜드는 **가상의 커피 로스터 “Lantern Coffee”** — 실제 Apple 데이터 아님.

**시사점**: “브랜드 보이스를 기계 판독 데이터로 만들고, 수정에서 학습시킨다”는 **방법론**은 이미 공개돼 있다. 우리는 이 형식을 빌릴 수 있고, 빌려야 한다 (특히 `derivedFromCorrection` 피드백 루프). 하지만 이건 *형식* 선례일 뿐 Apple 보이스 콘텐츠는 0이다.

### Humanizer / 문체 증류 (대중적 인접 경쟁)

#### 12. `blader/humanizer` — 이 카테고리 최대 규모
URL: https://github.com/blader/humanizer · **53,041★** · MIT · pushed 2026-09-28

“Agent skill that removes signs of AI-generated writing from text”. 단일 md. 압도적 배포력을 가졌지만 **긍정적 보이스가 아니라 부정적 필터**다 — “AI 티를 뺀다”이지 “Apple처럼 쓴다”가 아니다. Apple 스킬과 직교(orthogonal)한다.

#### 13. `Aboudjem/humanizer-skill`
URL: https://github.com/Aboudjem/humanizer-skill · 260★ · MIT
“55 patterns, 5 voices, a 0-100 AI-tell score”. 점수화와 다중 보이스를 도입한 점이 참고할 만하다.

#### 14. `jzOcb/writing-style-skill` (271★) · `snowmays/style-alchemy` (42★, MIT) · `shannhk/writing-style-extractor` (22★) · `qyh9527/writing-style-distiller-skill` (25★)
모두 **사용자 자신의 문체를 샘플에서 추출**하는 방향이다. `jzOcb`는 “AI writes → you edit → rules auto-extracted → SKILL.md improves”라는 자기학습 루프를 내세운다. 즉 시장은 “**내** 문체”와 “**AI 티 제거**”에 몰려 있고, “**특정 제3자 브랜드의 문체**”는 상대적으로 비어 있다.

#### 15. `coreyhaines31/marketingskills` — 최대 마케팅 스킬 컬렉션
URL: https://github.com/coreyhaines31/marketingskills · 51,973★ · MIT · pushed 2026-09-05

49+ 스킬. `skills/copywriting/`에 SKILL.md + `references/copy-frameworks.md` + `references/natural-transitions.md` + `evals/evals.json`. Apple 언급은 `skills/aso/`(App Store Optimization)에만 있고 전부 **스펙/벤치마크 데이터**지 문체가 아니다.

인용:
> “You are an expert conversion copywriter. Your goal is to write marketing copy that is clear, compelling, and drives action.”

**한계**: 전환율 최적화가 목표라 Apple의 절제·미니멀리즘과 미학적으로 충돌한다. Apple 보이스 인코딩 없음.

---

## (c) 가장 가까운 선행 사례 3개와 그들이 못 한 것

### 1위: `apple-copywriting` (Aaditya93/mmm_backend)
**왜 가장 가까운가**: 유일하게 “Apple 문체”를 이름으로 걸고, 실제 Apple 카피 예시로 14개 명명 패턴을 정리한 진짜 스킬이다. 깊이만 보면 우리 계획과 상당 부분 겹친다.

**못 한 것**:
1. **적용 범위가 마케팅 카피에 갇혀 있다.** 헤드라인/태그라인/CTA/랜딩페이지/프로젝트 설명만 다룬다. 우리 목표인 “리포트, 문서, README, 이메일, 분석 글, 한국어 텍스트”에는 규칙이 없다. Apple 보이스의 *문장 수준* 규칙(리듬, 절제, 구체성)은 마케팅 밖에서도 쓸 수 있는데 그 일반화를 안 했다.
2. **라이선스가 없다.** 기본값은 “All rights reserved”이므로 코드/텍스트 재사용이 법적으로 불가능하다. 포크해서 개선하는 생태계 경로가 막혀 있다.
3. **발견 불가능하다.** 0★, 무관한 `mmm_backend` 레포 안, README 언급 없음. awesome 리스트 어디에도 없음. 사실상 사문화된 자산이다.
4. **다른 스킬에 하드 결합.** `marketing-psychology` 스킬과 PLFS 점수 체계를 전제하므로 단독 설치로는 동작이 반쪽이다.
5. **다국어/한국어 부재.** 영어 전용.

### 2위: `chaos-xxl/apple-design-skill`의 `prompts/copywriting.md`
**왜 가까운가**: Apple 카피 원칙 + 언어별 패턴 테이블을 실제로 구현했고 MIT 라이선스라 재사용 가능하다.

**못 한 것**:
1. **트리거가 UI에 묶여 있다.** 스킬 `description`이 “generate Apple-style frontend UI code”이므로, 순수 산문 편집 요청(“이 리포트를 Apple 문체로”)으로는 발동하지 않는다. 스킬의 가치는 *언제 로드되느냐*로 결정되는데 여기서 실패한다.
2. **UI 생성의 부속품이다.** 카피 모듈은 랜딩페이지를 만들 때 쓰는 재료지, 독립 실행되는 문체 엔진이 아니다.
3. **영어/중국어만.** 한국어 없음.
4. **일반 산문 규칙 부재.** 문서·이메일·리포트용 장문 규칙(문단 구조, 정보 배열, 헤지 제거)이 없다.

### 3위: `Dankosik/yandex-tone-of-voice-skill`
**왜 가까운가**: 우리가 만들려는 것과 **구조가 동일**하다 — 특정 브랜드 하나의 톤을 SKILL.md + references + evals로 인코딩. 품질도 가장 높다.

**못 한 것**:
1. **Apple이 아니라 Yandex다.** 브랜드 보이스 콘텐츠는 전이되지 않는다.
2. **러시아어 전용.** 기본값이 «вы», «ё», 러시아식 따옴표에 맞춰져 있다.
3. **0★ — 실사용 검증 없음.** 구조는 훌륭하지만 채택된 사례가 없다.

**+ 차용할 것**: 트리거 위생 설계(“브랜드명만 언급해도 발동 금지”), `evals/boundary-rubric.json`으로 발동 경계 검증, “공식 브랜드북이 아닌 독립 재구성”이라는 법적 면책 문구, `source-map.md`로 근거 추적. 우리 스킬은 이 4가지를 그대로 채택해야 한다.

---

## (d) 결론: 진짜 공백과 만들 가치

### 공백은 존재한다 — 단, “아무것도 없다”가 아니라 “정확히 우리 형태만 없다”

정직하게 말하면 **Apple 카피 스킬은 이미 존재한다** (`apple-copywriting`, `chaos-xxl/prompts/copywriting.md`). “아무도 안 했다”고 주장하면 틀린다. 그러나 다음 4개 축에서 **교집합이 비어 있다**:

| 축 | 현황 |
|---|---|
| **도메인 일반성** | 기존 Apple 스킬은 전부 마케팅 카피 전용. 리포트/문서/README/이메일/분석 글에 적용 가능한 Apple 산문 스킬은 **없음** |
| **언어** | Apple 문체 스킬은 영어(또는 영어+중국어). **한국어 대응 없음** |
| **법적 재사용성** | 가장 깊은 사례(`apple-copywriting`)가 **무라이선스**. MIT로 배포되는 Apple 산문 스킬은 `chaos-xxl`의 UI 부속 모듈뿐 |
| **발견/채택** | Apple 문체 스킬은 awesome 리스트 4개(총 12만+★) 어디에도 없고, Vale 공식 레지스트리에도 없음. Google/MS/Salesforce/RedHat은 Vale에 있는데 **Apple만 부재** |

특히 마지막 항목이 강한 신호다. Vale 레지스트리에 Google·Microsoft·Salesforce·Red Hat 스타일 패키지가 모두 정식 등록돼 있는데 Apple만 없다. 그리고 `surendranb/writing-skills`는 GOV.UK·AP·STE-100·Google Dev Docs를 스킬로 만들었지만 Apple은 만들지 않았다. **“기관 문체를 스킬로 만든다”는 패턴은 검증됐고, Apple 자리만 주인 없는 상태**다.

### 만들 가치가 있는가 — 있다. 단, 다음 조건에서만

**찬성 근거**
1. **빈 자리가 구조적으로 확인됨** — 위 4축 교집합이 공백이며, 이는 “못 찾았다”가 아니라 레지스트리 원본 데이터와 awesome 리스트 전문 grep으로 확인한 결과다.
2. **1차 자료가 풍부하고 접근 가능** — Apple 공식 Style Guide 전문이 텍스트로 존재(459KB)하고, Vale 구현체(ChrisChinchilla, MIT)가 있으며, 경쟁 스킬들이 이미 추출한 패턴 라이브러리(14개 명명 패턴)가 공개돼 있다. 즉 **증류 대상 데이터는 확보 가능**하다.
3. **모범 구조 선례가 존재** — `yandex-tone-of-voice-skill`의 구조(SKILL.md + references + evals + source-map)를 그대로 채택하면 시행착오를 크게 줄인다.
4. **차별점이 명확** — “마케팅 카피”가 아니라 “**어떤 도메인의 산문이든**” + “**한국어 포함**” + “**MIT 라이선스**”는 기존 사례 어디와도 겹치지 않는다.

**반대 근거 (진지하게 고려해야 함)**
1. **차별점이 “일반화”뿐일 위험** — `apple-copywriting`의 14개 패턴을 도메인 일반화하고 한국어를 붙이는 게 우리 기여의 핵심이 된다. 이건 *증분적 개선*이지 새로운 발명이 아니다. 정직하게 포지셔닝해야 한다.
2. **`jdkato/voices`의 철학적 반박** — “보이스는 프롬프트가 아니라 매 초안마다 검사되는 린트 룰이어야 한다.” SKILL.md 단일 파일 접근은 이 기준에서 약하다. → **대응: SKILL.md를 정본으로 하되, 결정 규칙을 체크리스트로 명시해 린트화 가능하게 설계**하고, 여력이 있으면 Vale 룰을 선택적 부속으로 제공.
3. **Apple 브랜드 리스크** — `ChrisChinchilla`는 “neither maintained nor endorsed by Apple”을 명시했고, Yandex 스킬은 “не официальный брендбук”(공식 브랜드북 아님)이라고 못 박았다. 우리도 **독립 재구성임을 명시**하고 Apple 상표/로고를 쓰지 않아야 한다.

### 권고

**만들되, “또 하나의 Apple 카피 스킬”이 아니라 “Apple 산문 규칙의 도메인 독립 · 한국어 지원 · MIT 구현”으로 포지셔닝한다.**

구체적으로:
- `description`에서 **트리거 위생**을 최우선 설계 (Yandex 방식). “Apple”은 일상어라 오발동 위험이 크다 — “Apple 제품 리뷰”, “Apple 주가” 같은 요청에 발동하면 안 된다. 발동 조건을 “문체/카피/편집 작업 + Apple 보이스 지정”으로 좁힌다.
- **3층 구조**: ① 불변 코어(리듬·절제·구체성·능동태 — 모든 도메인/언어 공통) ② 도메인 어댑터(UI 마이크로카피 / 문서·README / 이메일 / 리포트·분석) ③ 언어 어댑터(영어 / 한국어 — 한국어는 Apple 번역체의 특성인 명사구 나열·간결한 종결·영어 병기 관행을 별도 규칙화).
- **evals 동봉**: 발동/비발동 경계 프롬프트 + 루브릭 (Yandex 구조 차용).
- **라이선스 MIT**, `source-map.md`로 각 규칙의 근거(공식 Style Guide 절 / 실제 Apple 카피 출처) 추적.
- 차용한 `apple-copywriting`(무라이선스)의 텍스트는 **참조만 하고 복사하지 않는다**. 패턴 이름·개념은 아이디어이므로 자유롭지만 표현은 독자적으로 작성한다.

**결론: 유의미한 공백이 존재하며, 만들 가치가 있다. 다만 “최초”가 아니라 “최초의 도메인 일반 + 한국어 + MIT”임을 정확히 인식하고 그 지점에 집중해야 한다.**
