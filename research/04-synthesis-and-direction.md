# 04 — 종합 & 방향성 제안

작성: 2026-09-30 · 근거: `00-recon-findings.md`(직접 검증) + `01~03`(서브에이전트 리서치) + 애플 1차 자료 실측

---

## 0. 한 줄 결론

**“애플처럼 쓰기” 스킬은 이미 부분적으로 존재한다. 그러나 그것들은 전부 (a) 마케팅 카피 전용이고, (b) 영어 전용이고, (c) 라이선스가 없거나 발견 불가능하며, (d) 애플이 공개한 1차 규칙서를 쓰지 않는다.**
→ 우리가 만들 가치는 “최초”가 아니라 **“영역 독립 + 한국어 + 정확한 3-레지스터 라우팅 + 애플 공식 규칙서 근거 + 검증 가능”** 에 있다.

---

## 1. 선행 사례 — 무엇이 이미 있는가

| 프로젝트 | 규모 | 무엇을 하는가 | 우리에게 의미 |
|---|---|---|---|
| [Aaditya93/mmm_backend → apple-copywriting](https://github.com/Aaditya93/mmm_backend/tree/main/apple-copywriting) | 0★, **라이선스 없음** | 실제 `apple-copywriting/SKILL.md`. `apple-patterns.md`에 **14개 명명 패턴**(Compound Boast, Rhythm Triple, Contrast Move…) + 실예시 + 템플릿. 약 40KB | **직접 선행 사례.** 단 마케팅 카피 전용·영어 전용·무관한 저장소에 묻힘·**법적으로 재사용 불가(텍스트 복사 금지)** |
| [chaos-xxl/apple-design-skill](https://github.com/chaos-xxl/apple-design-skill) | 21★, MIT | UI 생성 스킬. 부속 `prompts/copywriting.md`(13.6KB)에 애플 카피 5원칙 + EN/ZH 패턴 표 | 트리거가 “UI 코드 생성”이라 **순수 산문 요청에는 발동하지 않음** |
| [naplesblue/apple-design-skill](https://github.com/naplesblue/apple-design-skill) | 263★ | 순수 UI. 산문 모듈 없음 | 우리 전제 유지 |
| [tomdale/inside-mac](https://github.com/tomdale/inside-mac) | 16★, MIT | 스킬 7종. `imac-voice-and-tone/SKILL.md`(133줄): 문장 패턴·modal 동사·rule/rationale/consequence·3-pass 편집 | **문체 스킬의 깊이 기준.** 단 대상은 개발자 문서 + Inside Macintosh 현대화 |
| [ChrisChinchilla/Apple-style-guide](https://github.com/ChrisChinchilla/Apple-style-guide) | 3★, MIT, “WIP” | **Vale 룰셋** — 공식 Apple Style Guide의 편집 규칙(용어/금지어/수동태/포용 언어) | 기계 검증층. **Vale 공식 레지스트리(`errata-ai/packages`)에 Apple 패키지는 없음** |
| [Dankosik/yandex-tone-of-voice-skill](https://github.com/Dankosik/yandex-tone-of-voice-skill) | 0★, MIT | SKILL.md + `references/`(tone-system·examples·source-map·responsible-copy) + **`evals/`**(경계 루브릭·발동 테스트) + CI 검증 | ★ **구조 템플릿으로 최적.** 브랜드만 다름 |
| [blader/humanizer](https://github.com/blader/humanizer) · [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | 53,041★ · 4,789★ | AI 티 제거 | 문체 스킬이 실제로 대규모 채택됨을 보여주는 증거 |
| [jdkato/voices](https://github.com/jdkato/voices) | — | “보이스는 프롬프트가 아니라 **기계 검증 린트 규칙**이어야 한다”는 반론 | 우리 설계가 답해야 할 반론 (§5.4) |

### 없음으로 확인된 것
- **애플 카피 코퍼스/데이터셋: 없음.** GitHub 데이터셋 검색 0건, HuggingFace `apple` 상위 30개는 ML 데이터셋·주가·과일·애니 캐릭터. awesome-list 4개(합계 ~126k★)에서 apple+voice/tone/style-guide 0건.
- **Vale 공식 레지스트리에 Apple 없음** (Google·Microsoft·Salesforce·RedHat은 있음).
- ~~한국어 애플 문체~~ — 아무도 다루지 않음.

---

## 2. 애플 1차 자료 — 우리가 확보한 것 (★ 전부 실측)

| 자산 | 경로/URL | 규모 | 접근법 |
|---|---|---|---|
| **Apple Style Guide (공식 편집 규칙서, 2026년 6월판)** | `research/apple-style-guide.pdf` · `.txt` | **244페이지 · 49만 자** | `https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf` — curl로 즉시 |
| 같은 문서 웹판 (52개 섹션) | `research/asg/*.txt` (52개) · `asg-sections.txt` | **50.6만 자** | `support.apple.com/guide/applestyleguide/<slug>/web` — 섹션 페이지는 서버렌더 |
| **HIG(UI 문구 가이드) — JSON API** | `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json` | writing 37KB, inclusion 51KB, branding/onboarding/feedback 각 ~20KB | ★ **브라우저 불필요.** HTML판은 JS 게이트 |
| apple.com 제품 페이지 실측 | curl + UA | 1페이지 ~72만 byte / 본문 4.9만 자 | `web_fetch`는 실패(nav만), **curl은 성공** |

---

## 3. ★ 핵심 발견: 애플은 하나의 목소리가 아니라 **세 개의 규칙서**를 쓴다

Apple Style Guide 원문 인용:
> “Some departments at Apple (**Marcom**, for example) have **supplemental style guides**.”
> “The Apple Style Guide provides editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and **user interfaces**.”

즉 공개된 스타일 가이드는 **문서/UI용**이고, **마케팅(Marcom)은 별도 규칙서**다. 실제로 두 규칙이 정면 충돌한다:

| 축 | Style Guide (문서·UI) | apple.com (마케팅) | HIG (앱 UI) |
|---|---|---|---|
| 문장 조각의 마침표 | “no ending punctuation for a sentence fragment” | **92%(76/83)가 조각인데 마침표를 찍는다** | — |
| 1인칭 “we” | “Don’t use the first-person pronouns we, us, or I” | 드물게 사용 | “**Avoid using we altogether**” |
| 느낌표 | “OK to use occasionally in promotional text” | 실측 **0개 / 4,638문장** | — |
| 소유격 | — | “Your iPhone” 빈번 | “**Use possessive pronouns sparingly**” |

→ **이걸 구분하지 않는 “write like Apple” 스킬은 오류 메시지에 마케팅 패스티시를 만든다.** 이게 우리 스킬의 존재 이유이자 1번 기능이다.

### 3.1 세 레지스터 정의

| 레지스터 | 표면 | 지배 규칙서 | 목표 |
|---|---|---|---|
| **A. 편집/문서** | 문서, README, 지원 문서, 리포트 | Apple Style Guide | 정확·일관·번역 가능 |
| **B. 제품 UI** | 버튼, 라벨, 알림, 오류, 온보딩, 설정 | HIG Writing | 명확·행동 지향·번역 가능 |
| **C. 마케팅** | 제품 페이지, 앱스토어, 랜딩 | Marcom(비공개, 실측으로 역설계) | 한 줄에 하나의 이득, 리듬 |

---

## 4. 실측 근거 (표본 기준, 사이트 전체 아님)

서브에이전트가 10개 영어 페이지 + 24개 페이지(한국어 포함)에서 측정:

| 규칙 | 측정값 | 판정 |
|---|---|---|
| 느낌표 | **0 / 4,638문장** (유일한 `!` 2개는 영화 제목 안) | 강함 |
| 헤드라인 마침표 | **76/83 = 92%** | 강함 |
| 헤드라인 물음표 | 0/83 (단 support 문서 제목은 질문형 있음) | 강함 |
| `Label. Payoff.` 2부 구조 | 38개 | 강함 |
| 2인칭 | 본문 344/568 = **61%**, 헤드라인 18/83 = 22% | 중간 |
| 평균 문장 길이 | 17.4단어 / 중앙값 14 | 중간 |
| 각주 관용구 | `Testing conducted by Apple in…` 40/59 시작, `Performance tests are conducted…` 36/59 종료 | 강함 |
| **em dash** | 179개 전부 법률/각주 — **헤드라인 0/83** | ★ 통념 반박: “애플은 em dash를 쓴다”는 근거 없음 |
| 한국어 `-죠` | 본문 문단 133/379 = **35%** | 강함 |
| 한국어 `당신` | 본문 80/379 = 21%, **헤드라인 4/60** | 중간 |
| 한국어 느낌표 | 0 | 강함 |

**추출 함정:** 스크롤 애니메이션 때문에 시작/끝 프레임 문장이 중복 수록되어 `track track you.` 같은 **가짜 오타**가 생긴다. 실제 애플 오타로 인용 금지. (진짜 결함 1건: macbook-pro 페이지의 `up to 86x faster.`)

---

## 4.5 실패 모드 — 스킬에 “하지 말 것”으로 반드시 들어갈 것

| # | 실패 모드 | 근거 |
|---|---|---|
| F1 | **UI·법률 화면에 마케팅 레지스터 사용** — 애플 HIG가 직접 금지: `avoid the temptation to be too cute or clever`, `Avoid using we altogether`, `oops!` 금지 | HIG(1차) |
| F2 | **각주 없는 단언** — 애플 카피는 각주로 방어된다. `up to 6x faster`는 각주와 한 덩어리. 펀치라인만 가르치면 규제 리스크를 가르친다 (영국 ASA 2008 광고 금지, 호주 2012 A$2.25M 과징금) | Wikipedia 경유 2차 |
| F3 | **절대적 프라이버시 약속** (`never`, `isn’t`) — 검증 가능한 공개 약속이 된다. Face ID “Glimmer”, AI 학습 opt-out 논란 | 2차 |
| F4 | **각주가 명료성의 사망 지점** — 실측: 각주 길이 최소 5단어 ~ **최대 694단어**, 중앙값 100. 694단어는 리스 약관 한 덩어리 | 실측 |
| F5 | **최상급 남용** — 헤드라인 16%(13/83)가 최상급. 애플의 규모와 간격에서만 작동. 한 문단에 3~4개면 전부 무효화. 참고: 애플은 `magical`을 제품 주장으로 **0회** 사용 | 실측 |
| F6 | **EN→KR 직역** — 애플은 직역하지 않고 다시 만든다(`Fast runs in the family.`→`스피드는 칩안 내력.`). 다만 애플 한국어도 띄어쓰기 오류를 출고한다(`칩안` ← `칩 안`). **한국어는 별도 맞춤법 패스 필수** | 실측 |
| F7 | **두 목소리 혼합** — 가장 흔한 실패. 오류 메시지에 `Happily ever faster.`를 쓰는 것은 애플 스타일이 아니라 애플 문서가 금지한 것 | 1차 |

## 4.6 스킬에 인용할 최고 문장 (실측)

1. `Fly through demanding AI tasks up to 6x faster.` — 주장+헤지+각주 시스템 전체가 한 줄에
2. `Ultra Retina XDR. The world’s most advanced display.` — `Label. Payoff.` 패턴
3. `Siri learns what you need. Not who you are.` — 부정 대구 (단, F3 주의)
4. `Your Apple Watch is water resistant, but not waterproof.` — 비난 없이 오해 교정
5. `Apple Intelligence. Works hard. You take it easy.` — 3비트, 2인칭 지연 투입
6. `Longest battery life ever in a Mac. Up to 24 hours. Hit the road, Mac.` — 주장·숫자·인간적 마무리
7. `If you see the "Allow accessory to connect?" alert on your computer, click Allow.` — UI 문자열 + 행동
8. `Passkeys. Simple. Secure. So not a password.` — 4번째 비트 = 펀치라인
9. `Fast runs in the family.` / `스피드는 칩안 내력.` — 트랜스크리에이션 (결함 포함)
10. `Testing conducted by Apple in September 2025 using preproduction…` — 각주 템플릿. **히어로와 분리해서 가르치지 말 것**

## 5. 방향성 후보

### 후보 A — 단일 범용 스킬 `apple-writing` (라우터 + 참조 + 평가)
```
~/.dsh/skills/apple-writing/
  SKILL.md              # 결정 규칙만 (짧게): 레지스터 판별 → 규칙 적용 → 검증
  references/
    registers.md        # A/B/C 세 규칙서와 충돌 지점
    core-rules.md       # 레지스터 공통 불변식 (1인칭 금지·능동태·contractions·jargon)
    marketing.md        # 3비트 패턴, 명명 패턴, 각주 관용구
    ui-strings.md       # 버튼/오류/온보딩 (HIG 근거)
    korean.md           # -죠/당신/번역투 제거 (실측 기반)
    examples.md         # before/after 실측 쌍
    sources.md          # 라이브 재검증 레시피 + 출처 지도
  tools/
    fetch-apple-copy.sh # curl 추출 (레퍼런스 갱신용)
    apple-voice.yml     # Vale 룰 (편집 규칙 기계 검증)
  evals/
    rubric.md, boundary-prompts.md, invocation.md
```
- **장점:** 어디든 적용(사용자 목표 그대로). `apple-design`과 대칭. Yandex 템플릿 재사용.
- **단점:** SKILL.md가 비대해지면 발동은 되지만 실행이 얕아짐 → “references는 필요할 때만 로드”로 해결.

### 후보 B — 스킬 패키지 (역할 분리)
`apple-voice`(라우터) + `apple-copy`(마케팅) + `apple-ui-strings` + `apple-docs` + `apple-ko`
- **장점:** 각 스킬이 좁고 깊다. 트리거 정확.
- **단점:** 5개 유지비용, 중복 규칙, 사용자가 어느 걸 불러야 할지 모름.

### 후보 C — “검증 엔진” (린트 + 재작성 파이프라인)
Vale 룰셋 확장 + before/after 코퍼스 + 자동 채점.
- **장점:** jdkato/voices 반론을 정면으로 만족. CI에 붙일 수 있음(whoscored에 즉시 적용).
- **단점:** 산문 리듬·보이스는 린트로 안 잡힘 → 단독으로는 불충분.

### 비교

| | A 단일 범용 | B 패키지 | C 검증 엔진 |
|---|---|---|---|
| “어디든 적용” | ◎ | ○ | △ |
| 즉시 실전 투입(whoscored) | ◎ | ○ | ◎ |
| 유지비용 | 낮음 | 높음 | 중간 |
| 깊이 | 중~상 | 상 | 중 |
| 선행 사례 대비 차별성 | ◎ | ○ | ○ |

---

## 6. 권고: **A를 골격으로, C를 부속으로** (A+C 하이브리드)

`apple-writing` 스킬 하나 = **3층 구조**:

1. **불변 코어** (레지스터 무관, 애플 공식 문서가 실제로 규정한 것)
   - 1인칭 `we/us/I` 금지 → 독자/제품을 주어로 재작성 *(Style Guide “we” 항목 + HIG)*
   - 능동태 우선, 수동태는 예외 *(Style Guide)*
   - contractions 권장 — “Apple’s informal voice” *(Style Guide)*
   - jargon 회피, 전문용어는 첫 등장에 정의 *(Style Guide)*
   - 포용 언어: master/slave·blacklist·sanity check·kill 등 금지 *(Style Guide + Vale 룰)*
   - 한 문장 = 한 주장, 읽어서 어색하면 고친다 *(HIG)*
2. **레지스터 어댑터** (A/B/C 라우팅 — §3 표)
3. **언어 어댑터** (한국어: `-죠` 활용, `당신` 절제, 번역투 제거 — 측정 근거 있음)

**차별점 5개 (선행 사례 대비):**
1. 레지스터 라우팅 (아무도 안 함 — 애플 자신이 3개 규칙서를 쓴다는 사실 자체가 미개척)
2. 애플 공식 1차 규칙서 근거 (244p PDF + HIG JSON)
3. 실측 카운트 (통념 반박 포함: em dash·느낌표)
4. 한국어
5. **라이브 재검증 루프** — `tools/fetch-apple-copy.sh`로 apple.com을 다시 읽어 캘리브레이션 (사용자가 좋아한 그 워크플로)
6. MIT + 발견 가능 + `evals/`로 발동·경계 검증 (Yandex 템플릿)

**하지 말 것:**
- 무라이선스 `apple-copywriting` 저장소 텍스트 복사 (개념 참조만)
- Vale만으로 해결했다고 주장 (jdkato/voices 반론 회피하지 말고 흡수)
- 추출 함정 문장을 애플 실제 문장으로 인용

---

## 7. 남은 결정 사항

1. **방향:** A+C 하이브리드로 갈지 / A만 / B 패키지 / C만
2. **이름:** `apple-writing` vs `apple-voice` vs `apple-copy` — (`apple-design`과의 대칭성, Siri 오해 소지)
3. **범위:** 한국어 포함 여부, 마케팅 포함 여부
4. **설치:** `~/.dsh/skills/apple-writing/` 전역 vs 이 저장소에서 개발 후 심링크
5. **평가층:** `evals/` 포함 여부 (Yandex처럼) — 포함 권장
6. **첫 적용 대상:** whoscored-research의 지표 문장들로 before/after 검증
