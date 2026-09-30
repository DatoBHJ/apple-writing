# 00 — Recon findings (직접 검증분)

> 이 파일은 **내가(메인 에이전트) 직접 curl/web_fetch로 확인한 것**만 담는다. 서브에이전트 리서치는 01~03 파일에 있다.
> 모든 URL은 2026-09-30 기준 실제 응답을 확인했다.

---

## 1. 목표 재정의 (사용자 요청)

- **만들 것:** 애플의 *문체/스타일*(산문·카피·어조)을 스킬화한 것. UI/UX 코드 디자인이 아님 — 그건 기존 `apple-design` 스킬이 담당.
- **쓰임:** 에이전트가 **어느 분야든**(제품 UI 마이크로카피, 분석 리포트, 문서, README, 이메일, 한국어 텍스트) 애플 문체를 적용할 수 있어야 함.
- **계기:** `whoscored-research` 프로젝트에서 애플 공홈 문장을 직접 읽고 지표 문장을 재작성한 워크플로가 효과가 좋았음.
- **기존 자산:** `~/.dsh/skills/` 15개 스킬 중 문체/보이스 계열은 **0개**. `apple-design`(23KB SKILL.md)은 UI·모션 전용.

---

## 2. 지난 세션에서 검증된 것 (whoscored-research, session-5c953737)

`~/.dsh/sessions/--Users-hajunbae-whoscored-research--/session-5c953737-55af-4999-96fc-203fa1b9df3b/` 의 후반부.

### 2.1 사용자가 “이 방식이 괜찮다”고 판단한 워크플로

```
애플 공식 페이지를 실제로 브라우저로 읽는다
  → 문장 패턴을 뽑는다
  → 내 문장에 이식한다 (before/after 명시)
  → 화면에서 확인한다
```
사용자 발화: *“https://www.apple.com/iphone-duo/ 아이폰 duo 페이지를 읽어봐바. 새로운 아이폰을 어떤식으로 전문 기술을 일반 사용자에게 풀어서 설명하는지 **문장에 집중**해서 보고 다시 생각해.”*

### 2.2 도출된 애플 카피 패턴 — “3비트”

실제 추출 문장 (apple.com/iphone-duo/):
- `"48MP Dual Fusion camera system. And all‑new ways to shoot from front to back."`
- `"Landscape. A spacious display for incredibly immersive entertainment. You can even use two apps side by side with Split View multitasking."`
- `"Dual-battery system.¹ All‑day power."`

→ **개념(레이블). 평상시 말로 푼 뜻. 그래서 사용자가 얻는 것.**
→ 숫자는 문장 안에, 각주 마커는 끝에.

### 2.3 실제 적용 결과 (whoscored 지표 문장)

| 이전 | 이후 |
|---|---|
| `Projected to beat a defender with 42% of his passes.` | `About 42% of his passes get past a defender.` |
| `The model reads the pass geometry...` | `...worked out from where each pass started and finished, and how much pressure was around it.` |
| `player correlation 0.83` | `it puts players in almost the same order as the real numbers` |
| `Projections compress the extremes` | `his real season was likely better than this number` |
| `lower bound` | `only defenders the cameras can see are counted, so the real number is a little higher` |
| `43% of his defensive work happens in the opposition half — 15th of 47...` + 각주 `Derived, not observed...` | 각주 → `This shows where the defending happens, not how hard anyone presses — nothing in the data records pressure itself.` |

핵심 규칙: **결론 문장에는 소스/방법 단어를 넣지 않는다. 방법·한계는 각주로 내린다.**
(whoscored의 웹 테스트 220개에 “문장 무결성 검사 — 결론에 소스 단어 없음”이 있다고 기록됨.)

### 2.4 실제로 통했던 애플 페이지 수집 레시피 (ego-browser)

apple.com 제품 페이지는 JS 렌더 → `web_fetch`로는 nav만 나옴. ego-browser로 성공:

```bash
cd /Users/hajunbae/whoscored-research && ego-browser nodejs -e '
const task = await taskSpace("study Apple copy");
const page = task.page("p1");
await page.goto("https://www.apple.com/iphone-duo/");
await page.waitForTimeout(5000);
const data = await page.evaluate(() => {
  const txt = (e) => e.textContent.replace(/\s+/g, " ").trim();
  return [...document.querySelectorAll("h1,h2,h3,h4,p,li,span,div")]
    .map(txt)
    .filter(t => t.length >= 25 && t.length <= 220)
    .filter(t => !/Shop|Buy|Learn more|Quick Links|AppleCare|Find a Store|footer/i.test(t))
    .filter((t, i, a) => a.indexOf(t) === i)
    .slice(0, 60);
});
console.log(JSON.stringify(data, null, 1));
'
```
각주 블록을 뽑을 때는: `p, li, div` 중 `/^[0-9¹²³*†]+\s/` 로 시작하고 길이 25~260인 것들의 마지막 8개.

---

## 3. 애플 1차 자료 접근 지도 (★ 실측 검증)

| 자료 | URL | 접근 방법 | 비고 |
|---|---|---|---|
| **Apple Style Guide** (공식 편집 스타일 가이드) | `https://support.apple.com/guide/applestyleguide/` | 루트는 껍데기(588KB JS). **섹션 페이지는 서버렌더 → curl로 본문 획득** | `publish_date: 06252026`. 52개 섹션. `help.apple.com/applestyleguide/`는 redirect.js로 여기로 보냄 |
| ↑ 섹션 예시 | `https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web` | curl 200, 본문 텍스트 깨끗하게 나옴 | 포용적 언어 규칙 실제 인용 확보 |
| ↑ 전체 섹션 slug 목록 | `research/asg-sections.txt` (51개) | 저장 완료 | A~Z 알파벳 항목 + 주제 섹션 |
| **HIG — Writing** (공식 UI 문구 가이드) | `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.json` | ★ **JSON API로 즉시 획득 (37KB, 브라우저 불필요)** | HTML판(`/design/human-interface-guidelines/writing`)은 JS 게이트 |
| HIG 다른 페이지 | 위 URL의 `writing`만 바꾸면 됨 | 동일 패턴 | 예: `/inclusion.json`, `/buttons.json` 등 확인 필요 |
| apple.com 제품 페이지 | `https://www.apple.com/<product>/` | JS 렌더 → ego-browser 필요 | §2.4 레시피 |
| Apple Newsroom | `https://www.apple.com/newsroom/` | 서버렌더 (프로즈 많음) | 미검증, 후보 |

### 3.1 HIG Writing에서 실제로 확인한 애플의 공식 지침 (인용)

- **Determine your app’s voice.** “Think about who you’re talking to... Consistent language, along with a voice that reflects your app’s values, helps everything feel more cohesive.”
- **Match your tone to the context.** “Once you’ve established your app’s voice, **vary your tone based on the situation**.”
- **Be clear.** “Check each word to be sure it needs to be there. If you can use fewer words, do so. **When in doubt, read your writing out loud.**”
- **Write for everyone.** “Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology.”
- **Be action oriented.** “Active voice and clear labels... When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the temptation to be too cute or clever... just saying 'Send' often works better than 'Let’s do it!' For links, avoid using 'Click here'.”
- **Build language patterns.** “Consistency builds familiarity... Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently.”
- **Use possessive pronouns sparingly.** “'Favorites' conveys the same message as 'Your Favorites', and is more succinct... **Avoid using we altogether because it may be unclear who the 'we' in question refers to.** ... 'Unable to load content' is much clearer [than 'We’re having trouble loading this content.']”

> **중요:** 애플은 **보이스(고정)와 톤(상황별 변주)** 를 공식적으로 분리한다. 이건 우리 스킬의 골격이 될 수 있다.

### 3.2 Apple Style Guide에서 확인한 편집 규칙 (포용적 언어 섹션 인용)

- “Think inclusively.” / “Research words.” / “Consider the context.” (mute는 사람에게는 금지, 기기 음소거에는 허용)
- “Avoid terms that are violent, oppressive, or ableist.” — kill, hang, master/slave, sanity check 금지. “avoid describing software or hardware using human or biological attributes”
- “Avoid idioms and colloquial expressions.” — fall through the cracks, on the same page 등은 번역·이해를 어렵게 함
- “Don’t use color to convey positive or negative qualities.” — blacklist, white hat, red team 금지

---

## 4. 선행 사례 (★ 실제 확인)

| 이름 | URL | 성격 | 우리와의 관계 |
|---|---|---|---|
| **tomdale/inside-mac** (16★, MIT, 오늘도 업데이트) | `github.com/tomdale/inside-mac` | 스킬 7종 패키지. `skills/imac-voice-and-tone/SKILL.md` (133줄) | **가장 가까운 선행 사례.** 애플 *문서* 문체를 스킬화. 단, 대상은 개발자 문서 + Inside Macintosh(1985~94) 현대화 |
| **chaos-xxl/apple-design-skill** (21★, MIT) | `github.com/chaos-xxl/apple-design-skill` | UI 생성 스킬. `prompts/copywriting.md` 13.6KB | 애플 카피 5원칙 + 체크리스트 + EN/ZH 패턴 표. 단, 랜딩페이지 카피 전용·UI 스킬의 부속 |
| **ChrisChinchilla/Apple-style-guide** (3★, MIT) | `github.com/ChrisChinchilla/Apple-style-guide` | **Vale 룰셋** (Terminology / WordyPhrases / Clarity / PassiveVoice / InclusiveLanguage / Capitalization / ProductNames / SerialComma / Spelling / Verbs / Contractions) | ★ 기계 검증 가능한 층. 애플 스타일 가이드 기반 치환 규칙 실제 확보 |
| **blader/humanizer** (53,041★) | `github.com/blader/humanizer` | AI 티 제거 스킬 | 문체 스킬이 실제로 대규모 채택됨을 보여주는 증거 |
| conorbronsdon/avoid-ai-writing (4,789★) | — | AI 문체 감사·재작성 | 동일 계열 |
| freerk/archetype-writer (2★) | — | 12개 원형 페르소나 브랜드 보이스 스킬 | 브랜드 보이스 스킬의 전형 |
| forint573/human-copywrite (7★) | — | 마케팅 카피 휴머나이저 | — |

### 4.1 `imac-voice-and-tone` 구조 (그대로 배울 부분)

```
Use the core sentence pattern: 1) Define 2) State what it enables 3) Explain the consequence 4) Qualify exceptions
Choose modal verbs deliberately: must / must not / should / should not / can / may  (각각 정의)
State rule, rationale, and consequence  (Weak/Strong 예시 쌍)
Put caveats where decisions happen  (callout은 아껴서)
Prefer operational language  (Before/After 예시 3쌍)
Keep instructions compact but causal
Be candid about boundaries
Modernize the historical voice (버릴 것 목록)
Edit in three passes: Contract pass → Clarity pass → Compression pass
```

### 4.2 ChrisChinchilla Vale 룰에서 확인한 실제 규칙 예 (기계 검증층 후보)

- WordyPhrases: `in order to→to`, `due to the fact that→because`, `prior to→before`, `has the ability to→can`, `in the event that→if`, `at this point in time→now`
- Terminology: `click on→click`, `crash→quits unexpectedly|stops responding`, `dropdown→pop-up menu|menu`, `e-mail→email`, `dialog box→dialog`, `cell phone→mobile phone`
- InclusiveLanguage: blacklist/whitelist/master-slave/grandfathered/handicapped/sanity check/man-in-the-middle/he-she 등
- Clarity: `error message`, `bug`, `machine`, `check the checkbox`, `frontmost` 등 회피
- PassiveVoice: `\b(am|are|were|being|is|been|was|be)\s+(\w+ed|\w+ing)\b` + 예외 목록

---

## 5. 예비 갭 분석 (서브에이전트 결과 반영 전)

이미 존재하는 것:
1. 애플 **카피(마케팅)** 패턴 — `chaos-xxl/prompts/copywriting.md` (얕음, 랜딩페이지 전용, EN/ZH만)
2. 애플 **문서 문체** — `tomdale/inside-mac` (개발자 문서 전용, 대상 독자가 개발자)
3. 애플 **편집 규칙** — Vale 룰셋 (문서 린트 전용, 산문 리듬·보이스는 없음)
4. AI 티 제거 — humanizer 계열 (애플 특화 아님)

비어 있는 것 (후보):
- **레지스터 구분**: 마케팅 / UI 마이크로카피 / 지원문서 / 법률·개인정보 / 데이터·분석 서술을 *한 스킬 안에서* 구분해 적용하는 것
- **한국어 출력**: 애플 한국어 카피의 실제 규칙 (번역투 제거 등) — 아무도 안 다룸
- **살아있는 검증 루프**: apple.com/HIG JSON/스타일 가이드를 그때그때 다시 읽어 캘리브레이션하는 절차
- **비(非)마케팅 영역 이식**: 리포트·이메일·커밋 메시지·코드 주석 등
- **검증 가능성**: “애플처럼 썼는가”를 채점하는 체크리스트/린트

---

## 5.5 추가 검증 (직접)

### HIG JSON 소스 지도 — `/tutorials/data/design/human-interface-guidelines/<slug>.json`
전부 200 확인: `writing`(37KB) · `inclusion`(51KB) · `branding`(22KB) · `onboarding`(22KB) · `feedback`(19KB).
Foundations 계열 19개 페이지 목록 확보: accessibility, app-icons, branding, color, dark-mode, icons, images,
immersive-experiences, **inclusion**, layout, materials, motion, privacy, right-to-left, sf-symbols,
spatial-layout, typography, **writing**. (index: `.../human-interface-guidelines.json`, foundations: `.../foundations.json`)

### ★ apple.com 제품 페이지: **curl로 전문 획득 가능 (ego-browser 불필요)**

```bash
curl -sL -m 25 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36" \
  "https://www.apple.com/iphone-duo/" -o duo.html
```
검증 결과 (2026-09-30): `200`, **723,842 bytes**, 본문 텍스트 49,295자.
- 문장 클래스: `header-headline`(46회), `section-header-headline`(26회) — 실재 확인
- 각주: `id="footnote-*"` 23개
- 세션에서 본 그 문장들 그대로 존재: `Landscape.` / `Dual Fusion` ×5 / `All‑day power` ×1
  → 주의: `All‑day`의 하이픈은 **U+2011 non-breaking hyphen**. 일반 하이픈으로 grep하면 안 잡힌다.
- **`web_fetch`는 실패한다(nav-only). `curl`은 성공한다.** 이 차이가 스킬 레시피의 핵심.

### 추출 함정 (서브에이전트 보고 + 주의)
- 스크롤 애니메이션 때문에 **시작 프레임/끝 프레임 문장이 중복** 수록된다 →
  `Decide which apps are allowed to track track you.` 같은 **가짜 오타**가 생긴다. 실제 애플 오타로 인용 금지.
- 진짜 결함 1건: `/macbook-pro/`에 `Fly through demanding AI tasks up to 86x faster.` (형제 타일은 6x, 7.8x) — 각주 마커 자리 문제로 보임.

### 도구 상태 (중요)
- `web_search` 툴: **모든 프로바이더 실패** (SearXNG 0건, Brave/Tavily 키 없음, DDG 202).
- `research/search.sh`(Bing 우회): 응답은 오지만 **쿼리 충실도가 낮다** — “Apple Style Guide editorial style official”을 넣으면 apple.com 홈/iCloud 같은 일반 결과가 나온다. Mojeek 파서는 0건.
- **신뢰 가능한 경로:** ① 직접 URL curl ② `api.github.com` 검색 ③ `raw.githubusercontent.com` 파일 조회. 리서치는 이 세 가지로 수행했다.

---

## 6. 다음 단계

- [ ] 01~03 서브에이전트 리포트 도착 → 종합
- [ ] 방향성 후보 2~3개 + 권고안 확정 (사용자 승인)
- [ ] 스킬 이름/범위/파일 구조 확정
- [ ] `asg-sections.txt` 기반으로 Apple Style Guide 본문 수집 (스킬의 근거층)
- [ ] HIG JSON의 다른 페이지 수집 (writing/inclusion/branding 등)
