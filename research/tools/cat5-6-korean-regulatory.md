# Source-Verification Report — Categories 5 & 6
## Published critiques and failure modes of Apple Inc.'s prose style

**Researcher note on method.** `web_search` is broken in this environment. Every source below was retrieved with `curl`/the `.research-tools` scripts, and every URL printed below returned HTTP 200 with a non-trivial body that I read. Quoted strings were copied from the retrieved page text, not from a search-result snippet. Where I could only see a search-result snippet and not the source page, the item is in **DEAD ENDS**, not in the main list.

**Final URL verification pass (all HTTP 200 with non-trivial bodies, re-checked at end of session):**

```
200 29866   https://www.newsis.com/view/NISX20240828_0002865250
200 109857  https://www.segye.com/newsView/20240828504212
200 18011   https://www.mt.co.kr/society/2024/08/28/2024082810202049478
200 17750   https://www.fnnews.com/news/202605090901291212
200 26154   https://www.aitimes.kr/news/articleView.html?idxno=34252
200 75845   https://namu.wiki/w/발번역
200 168871  https://namu.wiki/w/애플/논란
200 26589   https://internet.watch.impress.co.jp/docs/yajiuma/1351429.html
200 24705   https://togetter.com/li/1774751
200 20857   https://gdpr-info.eu/art-12-gdpr/
200 2816    https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html
200 385980  https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception
200 79535   https://www.ftc.gov/system/files/documents/public_statements/410531/831014deceptionstmt.pdf
200 2332432 https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf
200 27022   https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202/subpart-A/section-202.1
200 32348   https://www.handbook.fca.org.uk/handbook/COBS/4/2.html
200 25164   https://www.sideview.co.kr/news/articleView.html?idxno=20430
200 2482546 https://web.archive.org/web/2023id_/https://www.sec.gov/files/rules/final/2020/ia-5653.pdf
200 62035   https://web.archive.org/web/2025id_/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02005L0029-20220528
```

Working search surfaces discovered this session (documented here because they are more capable than the README suggests):
- **Google News RSS works** for arbitrary queries incl. Korean and Japanese: `https://news.google.com/rss/search?q=QUERY&hl=ko&gl=KR&ceid=KR:ko` (article links are opaque Google redirect URLs, so use it to *find headlines*, then locate the outlet URL elsewhere).
- **Yahoo! Japan web search works** and indexes Japanese pages: `https://search.yahoo.co.jp/search?p=QUERY` (URLs appear as JSON-escaped strings in the HTML).
- **Bing News RSS supports `site:`** but its archive is short (roughly the last few months).
- **Naver mobile news search works** (`https://m.search.naver.com/search.naver?where=m_news&query=...`) for text, but article URLs are not in the HTML.
- `b.hatena.ne.jp` (403), `internet.watch.impress.co.jp/search` (404), `itmedia.co.jp/search` (404), `etnews.com/search` (firewall block), `dailysecu.com/search.html` (404), `sedaily.com/Search` (JS-only) are dead.

---

## 5. KOREAN LOCALIZATION

### 1. “김치→파오차이, 한국어→조선어”…아이폰 번역앱 오역 논란
*(“Kimchi → paocai, Korean → Joseon-eo” … controversy over mistranslations in the iPhone Translate app)*

- **Author / publication:** 이수지 기자 (Lee Su-ji), **뉴시스 (NEWSIS)**
- **URL:** https://www.newsis.com/view/NISX20240828_0002865250
- **Date:** 2024-08-28 (등록 09:05:48, 수정 10:54:52)
- **The specific claim:** Apple's built-in iPhone Translate app produced culturally wrong Korean-related translations. The two named defects are concrete string-level errors: Korean **김치** translated into Chinese as **韓式泡菜** (“Korean-style *paocai*”) rather than the correct term, and English **Korean** translated into Japanese as **朝鮮語** (“Joseon-eo,” the North-Korean/colonial-era term) rather than **韓国語**. The complaint was raised by 서경덕 (Seo Kyoung-duk), Sungshin Women's University, after reports from overseas Koreans.
- **Verbatim quote (Korean):**
  > 대표 오류는 '김치'를 중국어로 번역하면 '韓式泡菜'(한국식 파오차이)로 나온다. '파오차이'(泡菜)는 김치와 전혀 다른 중국식 채소 절임이다. 'Korean'도 일본어로 번역하면 '朝鮮語'(조선어)로 나온다. '韓国語'(한국어)가 올바를 표현이다.
  
  Also:
  > 서 교수는 “전 세계 이용자가 많은 아이폰 내장 번역 앱에서 이런 오류들이 발생하는 건 있을 수 없는 일”이라고 지적했다.
  - **English:** “The representative error is that translating '김치' (kimchi) into Chinese yields '韓式泡菜' (Korean-style *paocai*). '*Paocai*' (泡菜) is a Chinese-style vegetable pickle entirely different from kimchi. Translating 'Korean' into Japanese also yields '朝鮮語' (*Joseon-eo*). '韓国語' is the correct expression.” … “Prof. Seo pointed out, 'It is impossible that such errors occur in the iPhone's built-in translation app, which has users all over the world.'”
- **Classification:** DOCUMENTED (mainstream news reporting naming specific strings and a named complainant; the article is about Apple's own first-party app, i.e. Apple-authored Korean/Japanese localization).

### 2. “김치→파오차이, 한국어→조선어”…아이폰 번역앱 오역 논란

- **Author / publication:** **세계일보 (Segye Ilbo)** — wire copy
- **URL:** https://www.segye.com/newsView/20240828504212
- **Date:** 2024-08-28
- **The specific claim:** Same defect, independently published by a second national daily, confirming it was not a single-outlet story. Adds that Google Translate had the same *paocai* defect and that Prof. Seo intended to keep pressing both companies.
- **Verbatim quote (Korean):** *(from the article body)*
  > 'Korean'도 일본어로 번역하면 '朝鮮語'(조선어)로 나온다. … 특히 구글 번역에도 '김치'를 중국어로 번역하면 아직까지 '파오차이'(泡菜)로 오역되고 있다.
  - **English:** “Translating 'Korean' into Japanese also yields '朝鮮語' (*Joseon-eo*). … In particular, even in Google Translate, translating 'kimchi' into Chinese is still mistranslated as '*paocai*' (泡菜).”
- **Classification:** DOCUMENTED.

### 3. '김치→파오차이', '한국어→조선어'…아이폰 번역 앱 오류

- **Author / publication:** 박효주 기자 (Park Hyo-joo), **머니투데이 (MoneyToday)**
- **URL:** https://www.mt.co.kr/society/2024/08/28/2024082810202049478
- **Date:** 2024-08-28 11:06
- **The specific claim:** Third independent confirmation, with the same two string-level defects and a photograph credit to 서경덕 교수 제공 (photo provided by Prof. Seo) — i.e. this is a complaint with attached evidence screenshots, not a rumor.
- **Verbatim quote (Korean):**
  > 대표적인 오류는 '김치'를 중국어로 번역하면 '韓式泡菜'(한국식 파오차이)로 나온다. '파오차이'는 김치와 전혀 다른 중국식 채소 절임이다. 'Korean'도 일본어로 번역하면 '朝鮮語'(조선어)로 나온다. '韓国語'(한국어)가 올바른 표현이다.
  - **English:** as in source 1.
- **Classification:** DOCUMENTED.

> **Why these three matter for the writing-skill document:** they are the rare case where Apple's *localization* (not just its English copy) is the documented failure, the defects are reproducible string pairs (김치 → 韓式泡菜; Korean → 朝鮮語), and the failure is *cross-market* — the Korean complaint is trigged by Apple's **Japanese** output (조선어), which is exactly the “Japanese/Korean localization interference” pattern the brief asked about.

### 4. “귀에 걸친 번역기?”…84만원 에어팟 맥스2 써보니 [토요리뷰]
*(“A translator hanging on your ears?” … trying the 840,000-won AirPods Max 2 [Saturday Review])*

- **Author / publication:** 김민수 기자 (Kim Min-su) / 뉴스1 (News1). Retrieved via the 파이낸셜뉴스 (Financial News) syndication, which carries the full text.
- **URL:** https://www.fnnews.com/news/202605090901291212 (original: https://www.news1.kr/it-science/mobile/6154008)
- **Date:** 2026-05-09 09:01
- **The specific claim:** A hands-on review of Apple's Live Translation on AirPods Max 2 finds the Korean output acceptable for short announcements but intermittently awkward, and the feature degrades badly under real airport noise — i.e. Apple's own localized output is the weak link, not the hardware.
- **Verbatim quote (Korean):**
  > 짧은 안내 문장은 제법 잘 따라왔다. … 번역문이 다소 어색할 때도 있었지만, 여행 중 방송 내용을 놓쳤을 때라면 충분히 도움을 받을 수 있는 수준이었다. 흔들린 것은 공항 특유의 소음이 끼어들 때였다. … 이 기능이 헤드폰 하나로 모든 상황을 해결하는 통역 기능은 아니라는 점이 이때 분명해졌다.
  - **English:** “Short announcement sentences were followed reasonably well. … There were times when the translated text was somewhat awkward, but it was at a level that could be sufficiently helpful if you missed an in-flight announcement while travelling. What wavered was when airport-specific noise cut in. … It became clear at that point that this feature is not an interpreting function that solves every situation with a single pair of headphones.”
- **Classification:** DOCUMENTED (first-person hands-on test with photographs and dated usage; the awkwardness is the reviewer's direct observation).

### 5. 개인정보위, '24년 개인정보 처리방침 평가 결과 공개...지적사항, 기업의 적극적 개선 유도
*(PIPC publishes the results of the 2024 privacy-policy evaluation …)*

- **Author / publication:** 박현진 기자 (Park Hyun-jin), **인공지능신문 (AI Times / aitimes.kr)**
- **URL:** https://www.aitimes.kr/news/articleView.html?idxno=34252
- **Date:** 2025-03-16 (evaluation results published 16 March; covering body: 개인정보보호위원회 / Korea Personal Information Protection Commission, chair 고학수)
- **The specific claim:** **This is the single strongest Category-5 finding.** Korea's data-protection regulator ran a formal, scored readability/accessibility/adequacy evaluation of privacy policies across 49 companies in 7 sectors. It found that the **12 foreign (non-Korean) operators scored lower than domestic companies in *all three* categories specifically because of translationese and wording that diverged from Korean law and policy.** Apple is one of the twelve: the PIPC follow-up meeting of 28 March 2025, reported on 30 March 2025, lists the twelve attendees as 구글, 마이크로소프트, 메타, 샤오미, 스카이스캐너, 스타벅스, 알리익스프레스, **애플**, 테무, 테슬라, 화웨이, BYD — exactly twelve. *(The aitimes article itself says “12개의 해외사업자” without naming them; the Apple membership is established by the separate 30 March 2025 follow-up coverage, which I could only read as a search-result snippet — see DEAD ENDS. Treat “Apple ∈ the twelve” as a well-supported but separately sourced inference.)*
- **Verbatim quote (Korean):**
  > 또한 12개의 해외사업자의 경우 개인정보 공유·협력 등 국내법‧정책과 다르게 표현하거나, 번역투 문장 사용 등으로 인해 가독성, 접근성, 적정성 모든 분야에서 국내 기업 대비 낮은 평가를 받았다.
  - **English:** “In addition, the twelve foreign operators received lower evaluations than domestic companies in all areas — readability, accessibility, and adequacy — because they expressed things differently from domestic law and policy (e.g. regarding personal-information sharing and cooperation) and **used translationese sentences**.”
  
  Context quote (the scoring):
  > 이번 평가 결과 대상기업 평균점수는, 100점 만점 기준으로 가독성 69.1점, 접근성 60.8점, 적정성 53.4점 순으로 나타났다.
  - **English:** “The average score of the evaluated companies was, out of 100, 69.1 for readability, 60.8 for accessibility and 53.4 for adequacy.”
- **Classification:** DOCUMENTED (regulator's evaluation results reported with named methodology — 30 expert evaluators plus a 50-person user panel — and numeric scores). The specific criticism is literally the word **번역투** (“translationese”), which is the term the brief targets.

### 6. 발번역 — 나무위키
*(“Bad translation” — Namu Wiki)*

- **Author / publication:** 나무위키 (Namu Wiki) contributors; document last revised 2026-09-27 14:48:25
- **URL:** https://namu.wiki/w/%EB%B0%9C%EB%B2%88%EC%97%AD
- **Date:** document revision of 2026-09-27 (entry is long-lived; the Apple Arcade passage is stable)
- **The specific claim:** Under “examples of bad translation,” the entry indicts the official Korean subtitles of the Apple Arcade title *샨테와 일곱 사이렌* (*Shantae and the Seven Sirens*). It alleges the localization was rushed to satisfy Apple's policy, that the character's name is rendered inconsistently (샨테 → 샨테이 / 샨체), that laughter is rendered as the Korean chat abbreviation 'ㅎㅎ', and that raw script markup (`</>`) is visible on screen — i.e. **visible source-code leakage into shipped Korean copy.**
- **Verbatim quote (Korean):**
  > 샨테와 일곱 사이렌 - 애플 아케이드와 스팀에서 공식적으로 한국어 자막이 나온다. 그런데 한국어 번역의 상태가 매우 나쁘다. 애플 아케이드에 선행발매됐던 데모버전부터 한국어 자막이 나오긴 했는데, 애플의 정책 때문에 억지로 번역했다는 느낌이 팍팍 들 정도로 오역은 둘째 치고 띄어쓰기 오류와 오타가 난무한 데다 의미를 도저히 알 수 없는 비문 들로 가득 차 있어 … 샨테를 샨테이 혹은 샨체로 표기한다든지, 샨테의 웃음소리를 'ㅎㅎ'로 표기한다든지, 심지어는 </> 등의 스크립트 언어가 그대로 보여지기까지 한다.
  - **English:** “*Shantae and the Seven Sirens* — official Korean subtitles exist on Apple Arcade and Steam. But the state of the Korean translation is very bad. Korean subtitles were present from the demo version pre-released on Apple Arcade, but it feels overwhelmingly as if it was translated forcibly because of Apple's policy; mistranslations aside, spacing errors and typos are rampant and it is full of non-sentences whose meaning cannot be understood at all … The name Shantae is written as '샨테이' or '샨체'; Shantae's laughter is written as 'ㅎㅎ'; and script language such as `</>` is even displayed as-is.”
- **Classification:** OPINION (a community wiki's critique of a third-party game shipped under Apple's platform localization policy; the specific examples are concrete and checkable, but this is not reporting with independent evidence).

### 7. Apple/논란 — 나무위키
*(Apple / Controversies — Namu Wiki)*

- **Author / publication:** 나무위키 (Namu Wiki) contributors
- **URL:** https://namu.wiki/w/%EC%95%A0%ED%94%8C/%EB%85%BC%EB%9E%80
- **Date:** retrieved 2026-09-30 (live document)
- **The specific claim:** In the section on Korea-specific service grievances, the entry asserts that Apple's Korean-language support documentation is a negligible fraction of the total help corpus, and that the situation is worse for legacy-model documentation.
- **Verbatim quote (Korean):**
  > 인터넷의 고객지원 코너가 있긴 하다만 한국어로 번역된 것은 전체 도움말 중 새발의 피. 특히 구 모델 도움말은 그게 더 심하다.
  - **English:** “There is an online customer-support corner, but what has been translated into Korean is a drop in the bucket of the entire help corpus. This is even worse for the help pages of old models.”
  
  Related, same document (Korean consumer-discrimination section), showing the *legal-language* dimension:
  > 심지어 계약서는 무조건 영어로만, 한국어로 번역할 권리도 포기하도록 강제하였다.
  - **English:** “Furthermore, the contract was forced to be in English only, and [repair centres] were forced to waive even the right to translate it into Korean.”
- **Classification:** OPINION (community wiki critique; no independent citation for the “drop in the bucket” claim, but the second quote is footnoted to a Fair Trade Commission investigation report in the wiki).

### 8. 翻訳者の苦労が偲ばれる…iPhone 13の「スーパーキラキラカラフルクッキリディスプレイ」が話題に【やじうまWatch】
*(“You can feel the translator's suffering” … iPhone 13's “Super Sparkly Colorful Crisp Display” becomes a topic)*

- **Author / publication:** **tks24**, INTERNET Watch (Impress Watch) — やじうまWatch column
- **URL:** https://internet.watch.impress.co.jp/docs/yajiuma/1351429.html
- **Date:** 2021-09-16 06:00
- **The specific claim:** **The best documented Japanese-localization criticism found.** Apple's US iPhone 13 page described the Super Retina XDR display with the coined word **“SupercolorpixelisticXDRidocious”** — a riff on *Mary Poppins*' “Supercalifragilisticexpialidocious.” The Japanese page rendered it as **「スーパーキラキラカラフルクッキリディスプレイ」** (“Super sparkly colorful crisp display”). The article notes the wordplay is obvious in the original but untranslatable, that the Japanese rendering is an original coinage, and that reaction split between praising the translator's ingenuity and mocking the result as too far-fetched.
- **Verbatim quote (Japanese):**
  > 新しく発表されたiPhone 13の「Super Retina XDRディスプレイ」を形容するにあたってAppleが用いているこの表現、翻訳前の米Appleサイトでは「SupercolorpixelisticXDRidocious」となっており、映画「メリー・ポピンズ」劇中の楽曲タイトルおよびその中で使われるフレーズとして有名な「Supercalifragilisticexpialidocious（スーパーカリフラジリスティックエクスピアリドーシャス）」をもじったものとみられている。原文を見れば元ネタが一目瞭然だが、日本語訳でこれをそのまま用いるわけにもいかず、オリジナルの表現になったようだが、翻訳者の苦労が偲ばれるとして高く評価する人、とはいえ、あまりにも突飛すぎる表現にツッコミを入れる人と、反応はさまざま。
  - **English:** “This expression, which Apple uses to describe the newly announced iPhone 13's 'Super Retina XDR display,' appears on the pre-translation US Apple site as 'SupercolorpixelisticXDRidocious,' and is believed to be a play on 'Supercalifragilisticexpialidocious,' famous as a song title and phrase in the film *Mary Poppins*. The source of the joke is obvious from the original, but it could not simply be carried over into the Japanese translation, so it appears an original expression was coined. Reactions varied: some praised it highly, saying you can feel the translator's suffering, while others poked fun at an expression that is simply too far-fetched.”
- **Classification:** DOCUMENTED (the English/Japanese string pair is quoted directly and is verifiable on the archived Apple pages; the article also reports the split public reaction rather than asserting one verdict).

### 9. 新iPhoneのサイト、元ネタはおしゃれなのに和訳が全然違った「担当者の苦労が偲ばれる」「和訳の最適解」
*(The new iPhone site: the source joke was stylish but the Japanese translation was completely different — “you can feel the staff's suffering,” “the optimal Japanese rendering”)*

- **Author / publication:** **Togetter** (aggregated X/Twitter posts); lead post by へいほぅ (@h3y6e)
- **URL:** https://togetter.com/li/1774751
- **Date:** 2021-09-15 (individual posts timestamped 2021-09-15 03:42–10:29)
- **The specific claim:** The contemporaneous Japanese-language reaction thread to the same iPhone 13 string. The originating post argues Apple's English coinage was excellent and that the Japanese translator's rendering reads as if the translator gave up. This is the raw popular-criticism layer beneath source 8 (INTERNET Watch links to it directly).
- **Verbatim quote (Japanese):**
  > 世界で最も長い英単語である メリー・ポピンズの“Supercalifragilisticexpialidocious” をもじって、“SupercolorpixelisticXDRidocious”にしたの上手すぎて鳥肌立った しかし日本語訳、担当した人がめちゃくちゃ悩んだ結果全てがどうでも良くなった感が凄い #AppleEvent
  - **English:** “Riffing on 'Supercalifragilisticexpialidocious' from *Mary Poppins* — the world's longest English word — to make 'SupercolorpixelisticXDRidocious' was so good it gave me goosebumps. But as for the Japanese translation, you really get the feeling that the person in charge agonised over it enormously and then everything stopped mattering.”
  
  Replies in the thread (verbatim): 「担当者の苦労が偲ばれるw」 (“You can feel the staff's suffering lol”); 「声に出して読みたい日本語」 (“Japanese you want to read aloud”); 「じゅげむにすべきだった。」 (“They should have gone with *Jugemu*.”)
- **Classification:** OPINION (a collected thread of reader critiques; valuable precisely as evidence of *reception*, not as adjudicated fact).

---

## 6. REGULATORY CONSTRAINTS

Framing: the Apple voice rests on unquantified superlatives (“magical,” “the best ever,” “up to”), on minimal on-page text, and on disclosure deferred to a footnote or a linked page. Each of the following instruments attacks one of those three moves with a hard, quotable rule. Sources 1–8 are primary law/regulator text; 9 is a regulator's enforcement record; 10 is a regulator's scored finding that Apple's own Korean prose failed a legally mandated plain-language test.

### 1. Regulation (EU) 2016/679 (GDPR), Article 12(1) — transparency and plain language

- **Author / publication:** European Parliament and Council; text retrieved from **gdpr-info.eu** (Intersoft Consulting, the standard mirror)
- **URL:** https://gdpr-info.eu/art-12-gdpr/
- **Date:** Regulation adopted 2016-04-27, in force 2018-05-25 (page retrieved 2026-09-30)
- **The specific claim:** Privacy information and all Article 13/14 disclosures must be provided “in a concise, transparent, intelligible and easily accessible form, using clear and plain language.” This is the clause under which a minimalist, mood-driven Apple privacy page fails: “concise” is only one of four conjunctive requirements, and it does not license vagueness. This is also the provision that makes the PIPC finding in Category-5 source 5 more than a style opinion — the readability test is a legal obligation.
- **Verbatim quote:**
  > 1 The controller shall take appropriate measures to provide any information referred to in Articles 13 and 14 and any communication under Articles 15 to 22 and 34 relating to processing to the data subject in a concise, transparent, intelligible and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child.
- **Classification:** DOCUMENTED (primary legal text).

### 2. Regulation (EU) 2022/2065 (Digital Services Act), Article 25 — dark-pattern ban

- **Author / publication:** European Parliament and Council; text retrieved from **eu-digital-services-act.com** (Cyber Risk GmbH's reproduction of the final text)
- **URL:** https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html
- **Date:** Regulation of 2022-10-19 (page retrieved 2026-09-30)
- **The specific claim:** Online platforms may not design their interfaces so as to “deceive or manipulate” recipients or “materially distort or impair” free and informed decisions. Paragraph 3 singles out, among the practices the Commission may issue guidelines on, giving more prominence to certain choices, repeatedly re-asking for a decision already made (pop-ups), and making termination harder than subscription. This is the direct legal attack on Apple's habit of making the desired option visually dominant and the disfavoured option low-contrast or buried — the same visual hierarchy Apple's marketing pages are built on.
- **Verbatim quote:**
  > 1. Providers of online platforms shall not design, organise or operate their online interfaces in a way that deceives or manipulates the recipients of their service or in a way that otherwise materially distorts or impairs the ability of the recipients of their service to make free and informed decisions.
  > …
  > (a) giving more prominence to certain choices when asking the recipient of the service for a decision;
  > (b) repeatedly requesting the recipient of the service to make a choice where that choice has already been made, especially by presenting pop-ups that interfere with the user experience;
  > (c) making the procedure for terminating a service more difficult than subscribing to it.
- **Classification:** DOCUMENTED (primary legal text).

### 3. Directive 2005/29/EC (Unfair Commercial Practices Directive), consolidated text as amended by Directive (EU) 2019/2161 (Omnibus)

- **Author / publication:** European Parliament and Council; consolidated text retrieved from **EUR-Lex** (CELEX 02005L0029-20220528) via the Wayback Machine (direct EUR-Lex returned HTTP 202 with an empty body)
- **URL:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02005L0029-20220528
- **Date:** Directive 2005-05-11; consolidated version incorporating the Omnibus amendments applicable from 2022-05-28
- **The specific claim:** Three separate constraints on Apple-style copy. (a) Article 5(5) makes the Annex I list unfair “in all circumstances” — no balancing test, no defence of good taste. (b) Article 6(1) makes a practice misleading if it “deceives or is likely to deceive the average consumer, **even if the information is factually correct**,” as to the product's “benefits, risks, … results to be expected from its use” — i.e. technically-true superlatives are still actionable if the overall presentation misleads. (c) The Omnibus-added Article 6(1)(6) makes review provenance a material fact, which is the clause Apple's App Store rating surfaces live under. Note also Article 5(4)'s safe harbour for “exaggerated statements … not meant to be taken literally” — this is the *only* thing standing between “magical” and the Directive, and it does not extend to quantified or benefit-claiming statements.
- **Verbatim quotes:**
  > 5. Annex I contains the list of those commercial practices which shall in all circumstances be regarded as unfair.
  
  > A commercial practice shall be regarded as misleading if it contains false information and is therefore untruthful or in any way, including overall presentation, deceives or is likely to deceive the average consumer, even if the information is factually correct, in relation to one or more of the following elements … (b) the main characteristics of the product, such as its availability, benefits, risks, execution, composition, accessories, after-sale customer assistance and complaint handling, method and date of manufacture or provision, delivery, fitness for purpose, usage, quantity, specification, geographical or commercial origin or the results to be expected from its use …
  
  > 4. In particular, commercial practices shall be unfair which: (a) are misleading as set out in Articles 6 and 7 …
  
  > 6. Where a trader provides access to consumer reviews of products, information about whether and how the trader ensures that the published reviews originate from consumers who have actually used or purchased the product shall be regarded as material.
  
  > … the legitimate advertising practice of making exaggerated statements or statements which are not meant to be taken literally.
- **Classification:** DOCUMENTED (primary legal text, consolidated).

### 4. FTC Policy Statement on Deception (1983)

- **Author / publication:** **Federal Trade Commission** (the “Deception Policy Statement,” letter to the Hon. John D. Dingell, Chairman, House Committee on Energy and Commerce, 1983-10-14)
- **URL:** https://www.ftc.gov/legal-library/browse/ftc-policy-statement-deception (landing page; full text PDF at https://www.ftc.gov/system/files/documents/public_statements/410531/831014deceptionstmt.pdf)
- **Date:** 1983-10-14 (PDF retrieved 2026-09-30)
- **The specific claim:** The three-element test — a representation/omission/practice that is **likely to mislead**; judged from the perspective of the **reasonable consumer**; and **material**. Two things matter for Apple copy. First, the standard is “likely to mislead,” not “actually deceived.” Second, and decisively for superlative marketing, the FTC states expressly that **advertising lacking a reasonable basis is itself deceptive** — an unsubstantiated “best ever” is a violation at the moment it is made, without any need to show a consumer was fooled.
- **Verbatim quotes (from the PDF):**
  > Thus, the Commission will find deception if there is a representation, omission or practice that is likely to mislead the consumer acting reasonably in the circumstances, to the consumer's detriment.
  
  > Third, the representation, omission, or practice must be a “material” one. The basic question is whether the act or practice is likely to affect the consumer's conduct or decision with regard to a product or service.
  
  > Advertising that lacks a reasonable basis is also deceptive. Firestone, 81 F.T.C. 398, 451-52 (1972) …
  
  > The deception theory is based on the fact that most ads making objective claims imply, and many expressly state, that an advertiser has certain specific grounds …
- **Classification:** DOCUMENTED (primary regulator policy statement).

### 5. .com Disclosures: How to Make Effective Disclosures in Digital Advertising

- **Author / publication:** **Federal Trade Commission, Bureau of Consumer Protection, Division of Advertising Practices**
- **URL:** https://www.ftc.gov/system/files/documents/plain-language/bus41-dot-com-disclosures-information-about-online-advertising.pdf (landing page: https://www.ftc.gov/business-guidance/resources/com-disclosures-how-make-effective-disclosures-digital-advertising)
- **Date:** March 2013 (53 pages; PDF retrieved 2026-09-30)
- **The specific claim:** This is the doctrine that most directly contradicts the Apple web idiom. The FTC requires disclosures to be **“clear and conspicuous,”** and lists as factors: **proximity to the claim**, **prominence**, **whether the disclosure is unavoidable**, whether other parts of the ad **distract** from it, whether it must be repeated, and whether the language is understandable to the intended audience. It also states the preference explicitly: advertisers should “incorporate relevant limitations and qualifying information into the underlying claim, rather than having a separate disclosure qualifying the claim.” Apple's practice — a clean hero claim with the qualifier in small grey type at the page foot or behind a footnote marker — is precisely the structure the FTC says is *disfavoured*, and the “unavoidable” and “distracting factors” prongs are the ones that convert Apple's aesthetic minimalism into a compliance risk. The hyperlink rules also bite on “Learn more” links.
- **Verbatim quotes (from the PDF):**
  > Required disclosures must be clear and conspicuous. In evaluating whether a disclosure is likely to be clear and conspicuous, advertisers should consider its placement in the ad and its proximity to the relevant claim. The closer the disclosure is to the claim to which it relates, the better. Additional considerations include: the prominence of the disclosure; whether it is unavoidable; whether other parts of the ad distract attention from the disclosure; whether the disclosure needs to be repeated at different places on a website; whether disclosures in audio messages are presented in an adequate volume and cadence; whether visual disclosures appear for a sufficient duration; and whether the language of the disclosure is understandable to the intended audience.
  
  > … advertisers should incorporate relevant limitations and qualifying information into the underlying claim, rather than having a separate disclosure qualifying the claim.
  
  > When using a hyperlink to lead to a disclosure, - make the link obvious; - label the hyperlink appropriately to convey the importance, nature, and relevance of the information it leads to; - use hyperlink styles consistently, so consumers know when a link is available; - place the hyperlink as close as possible to the relevant information it qualifies and make it noticeable; - take consumers directly to the disclosure on the click-through page …
- **Classification:** DOCUMENTED (primary regulator guidance document).

### 6. 21 CFR § 202.1 — Prescription Drug Advertising (FDA)

- **Author / publication:** **U.S. Food and Drug Administration**; text retrieved from the **eCFR** (Electronic Code of Federal Regulations), Title 21, Chapter I, Subchapter C, Part 202, Subpart A
- **URL:** https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-202/subpart-A/section-202.1
- **Date:** current edition, retrieved 2026-09-30
- **The specific claim:** The clearest legal statement anywhere that the Apple register is *structurally* unusable in a regulated category. § 202.1(e)(5)(ii) requires a **“fair balance”** between effectiveness information and side-effect/contraindication information, and treats an ad as failing that requirement where “the information relating to effectiveness is presented in greater scope, depth, or detail” than the risk information. § 202.1(e)(6)(i) prohibits any “representation or suggestion, not approved or permitted for use in the labeling, that a drug is **better, more effective, useful in a broader range of conditions or patients, safer, has fewer, or less incidence of, or less serious side effects or contraindications** than has been demonstrated by substantial evidence.” And § 202.1(e)(3)(i) states that a true statement elsewhere in the ad **cannot cure** a misleading part. Translate this to the Apple voice: “the best iPhone camera ever,” “the most powerful chip in a smartphone” and “amazing battery life” are exactly the comparative-superiority claims § 202.1(e)(6)(i) forbids absent substantial evidence, and Apple's habit of letting a beautiful headline carry the claim while the qualifier sits elsewhere is exactly what § 202.1(e)(3)(i) says does not work.
- **Verbatim quotes:**
  > (ii) It fails to present a fair balance between information relating to side effects and contraindications and information relating to effectiveness of the drug in that the information relating to effectiveness is presented in greater scope, depth, or detail than is required by section 502(n) of the act and this information is not fairly balanced by a presentation of a summary of true information relating to side effects and contraindications of the drug …
  
  > An advertisement for a prescription drug is false, lacking in fair balance, or otherwise misleading … if it: (i) Contains a representation or suggestion, not approved or permitted for use in the labeling, that a drug is better, more effective, useful in a broader range of conditions or patients …, safer, has fewer, or less incidence of, or less serious side effects or contraindications than has been demonstrated by substantial evidence or substantial clinical experience …
  
  > The requirement of a true statement of information relating to side effects, contraindications, and effectiveness applies to the entire advertisement. Untrue or misleading information in any part of the advertisement will not be corrected by the inclusion in another distinct part of the advertisement of a brief statement containing true information …
- **Classification:** DOCUMENTED (primary regulation).

### 7. SEC Rule 206(4)-1 under the Investment Advisers Act of 1940 (the “Marketing Rule”)

- **Author / publication:** **U.S. Securities and Exchange Commission**; final rule release retrieved via the **Wayback Machine** (sec.gov returns HTTP 403 to direct requests from this environment)
- **URL (retrieved):** https://web.archive.org/web/2023id_/https://www.sec.gov/files/rules/final/2020/ia-5653.pdf
- **Date:** Final rule adopted 2020-12-22 (430-page release; PDF retrieved 2026-09-30)
- **The specific claim:** The Marketing Rule's general prohibitions bar any advertisement that would include an **unsubstantiated material statement of fact**, that would cause an untrue or misleading implication, or that discusses **potential benefits “without providing fair and balanced treatment of any material risks or material limitations.”** The release further notes that to establish a violation the Commission **“will not need to demonstrate that an investment adviser acted with scienter; negligence is sufficient.”** This is the finance-sector equivalent of FDA fair balance, and it is the reason “amazing returns” style copy is impossible: every benefit sentence creates a paired obligation to state the corresponding risk, and an unsubstantiated factual claim is a violation regardless of intent.
- **Verbatim quotes (from the PDF):**
  > … a statement of fact that the adviser does not have a reasonable basis for believing it will be able to substantiate upon demand by the Commission; (3) Include information that would reasonably be likely to cause an untrue or misleading implication or inference to be drawn concerning a material fact relating to the investment adviser; (4) Discuss any potential benefits to clients or investors connected with or resulting from the investment adviser's services or methods of operation without providing fair and balanced treatment of any material risks or material limitations associated with the potential benefits; … or (7) Otherwise be materially misleading.
  
  > As noted in the proposal, to establish a violation of the rule, the Commission will not need to demonstrate that an investment adviser acted with scienter; negligence is sufficient.
  
  Table of contents listing the operative heads:
  > 1. Untrue Statements and Omissions … 2. Unsubstantiated Material Statements of Fact … 4. Failure to Provide Fair and Balanced Treatment of Material Risks or Material Limitations … 6. Otherwise Materially Misleading
- **Classification:** DOCUMENTED (primary regulator rule release).

### 8. FCA Handbook COBS 4.2 — “Fair, clear and not misleading communications”

- **Author / publication:** **Financial Conduct Authority (UK)**, FCA Handbook, Conduct of Business Sourcebook, chapter COBS 4.2
- **URL:** https://www.handbook.fca.org.uk/handbook/COBS/4/2.html
- **Date:** COBS 4.2 last updated 2025-10-23 (page retrieved 2026-09-30)
- **The specific claim:** COBS 4.2.1 R states the rule in one sentence: a firm “must ensure that a communication or a financial promotion is fair, clear and not misleading.” The rule applies to communications to customers in relation to designated investment business and to insurance distribution. The significance for the Apple voice is that the three adjectives are **cumulative and outcome-based**: “clear” and “not misleading” are separate obligations from “fair,” so an elegant, unambiguous sentence that presents only the upside still breaches the rule. This is the rule that every UK “Apple-style minimalism” fintech landing page has to be rewritten against.
- **Verbatim quote:**
  > COBS 4.2.1 R (1) A firm must ensure that a communication or a financial promotion is fair, clear and not misleading.
  > (2) This rule applies in relation to: (a) a communication by the firm to a customer in relation to designated investment business which is not MiFID, equivalent third country or optional exemption business, other than a third party prospectus …
- **Classification:** DOCUMENTED (primary regulator rulebook text).

### 9. 식약처, 추석 앞두고 의약외품과 화장품, 의료기기 온라인 부당광고 308건 적발
*(MFDS catches 308 cases of unlawful online advertising for quasi-drugs, cosmetics and medical devices ahead of Chuseok)*

- **Author / publication:** 윤동현 기자 (Yun Dong-hyeon), **사이드뷰 (Sideview)**; reporting the enforcement results of the **식품의약품안전처 (Ministry of Food and Drug Safety, MFDS)**, chair 오유경
- **URL:** https://www.sideview.co.kr/news/articleView.html?idxno=20430
- **Date:** 2026-09-17 10:18
- **The specific claim:** Korea's regulator publishes a concrete blacklist of **banned wording** and the exact statutes it enforces. The prohibited expressions are ordinary benefit verbs and nouns — the same register Apple uses for Apple Watch and Health features. Applied law is named per product class: 약사법 제68조, 화장품법 제13조, 의료기기법 제24조·제26조. For a writing-skill document this is the strongest evidence that in the Korean health/beauty/medical space, health-benefit language is not a style question but a licensing question: the words 피부재생 / 세포재생 / 노화방지 / 항염 / 잇몸재생 are simply not available. The article also enumerates the banned *claim structures*: implying medical efficacy, implying functional-cosmetic status without review, and implying endorsement by a named institution.
- **Verbatim quote (Korean):**
  > '피부재생', '노화방지', '항염', '난소호르몬 증가', '세포재생'처럼 의학적 효능을 내세운 화장품 광고는 금지표현에 해당한다. '병원전용화장품', '피부과의원 사용제품'처럼 특정인이나 기관의 지정과 공인을 내세우거나 '보톡스 화장품', '00주사' 같은 시술 표현도 화장품 범위를 벗어난 부당광고다.
  
  > 치약제는 '잇몸재생'과 '항염', '편도결석 예방', 구중청량제는 '치주질환개선'과 '치아미백', '충치예방', 치아미백제는 '치태개선'과 '항염' 등이 적발됐다. … 의료기기에는 공산품 58건이 포함되며 적용 법조는 약사법 제68조, 화장품법 제13조, 의료기기법 제24조와 제26조다.
  - **English:** “Cosmetic advertising that asserts medical efficacy — such as 'skin regeneration', 'anti-ageing', 'anti-inflammatory', 'increased ovarian hormones', 'cell regeneration' — constitutes prohibited expression. Expressions that assert designation or endorsement by a specific person or institution, such as 'hospital-exclusive cosmetics' or 'used by dermatology clinics', or procedure expressions such as 'Botox cosmetics' or '00 injection', are also unlawful advertising beyond the scope of cosmetics.” … “For toothpaste, 'gum regeneration', 'anti-inflammatory' and 'tonsil-stone prevention' were caught; for mouthwash, 'periodontal disease improvement', 'teeth whitening' and 'caries prevention'; for whitening agents, 'plaque improvement' and 'anti-inflammatory'. … Medical devices include 58 cases of ordinary industrial products; the applicable statutes are Pharmaceutical Affairs Act Art. 68, Cosmetics Act Art. 13, and Medical Devices Act Arts. 24 and 26.”
- **Classification:** DOCUMENTED (regulator enforcement record reported with case counts, product categories and cited statutes).

### 10. PIPC privacy-policy evaluation — readability scored, translationese penalised

*(Cross-listed with Category 5, source 5; repeated here because the finding is simultaneously a localization critique and a regulatory constraint.)*

- **Author / publication:** 박현진 기자, **인공지능신문 (aitimes.kr)** — reporting 개인정보보호위원회 (Personal Information Protection Commission) 2024 evaluation results
- **URL:** https://www.aitimes.kr/news/articleView.html?idxno=34252
- **Date:** 2025-03-16
- **The specific claim:** A national privacy regulator now **scores** privacy-policy readability and treats translationese as a *scored deficiency*. Averaged across 49 companies: readability 69.1, accessibility 60.8, adequacy 53.4 out of 100. Foreign operators scored below domestic firms on all three axes, and the regulator's stated causes are divergence from Korean law/policy and **번역투 문장 사용** — the use of translationese sentences. This converts “Apple's Korean copy reads like translated English” from a taste complaint into a measurable regulatory finding.
- **Verbatim quote (Korean):** *(as in Category 5, source 5)*
  > 또한 12개의 해외사업자의 경우 개인정보 공유·협력 등 국내법‧정책과 다르게 표현하거나, 번역투 문장 사용 등으로 인해 가독성, 접근성, 적정성 모든 분야에서 국내 기업 대비 낮은 평가를 받았다.
  - **English:** “In addition, the twelve foreign operators received lower evaluations than domestic companies in all areas — readability, accessibility, and adequacy — because they expressed things differently from domestic law and policy … and used translationese sentences.”
- **Classification:** DOCUMENTED (regulator's scored evaluation; Apple's membership in the twelve is documented separately — see DEAD ENDS note).

---

## DEAD ENDS

Sources I attempted but could not retrieve, with the reason. **None of these are cited in the report above.**

| Target | URL / query attempted | Why it failed |
|---|---|---|
| **[윤기자의 폰폰폰] 도 넘은 애플 '갑질'… ESG는 어디로** — 서울경제, 2022-10-01. A column criticising exaggerated **번역투** in Apple/carrier Korean press-release copy, with the specific phrase 「놀라운 비디오 품질」 cited as an example of 과장된 번역투, plus the observation that writing “iPhone”/“Apple” in Latin script instead of 아이폰/애플 reads like an untranslated Apple press release. | `sedaily.com` (search is JS-only; article URL never obtained); `search.daum.net` (text visible, hrefs not in HTML); Bing News `site:sedaily.com` (archive too short — 2022 not indexed); Seoul Shinmun `seoul.co.kr` search (404 — wrong paper). | **URL never obtained**, so no verbatim quote and no citation. I saw the snippet only on a Naver mobile news *search-results* page, which is not the source page. **This is a high-value source if the parent can reach it another way.** |
| **개인정보위, 구글·테무 등 해외사업자 만나 개인정보 처리방침 의견수렴** — 전자신문, 2025-03-30, and the parallel 데일리안 / 뉴스1 / 서울경제 / 동행미디어 시대 coverage of the same PIPC follow-up meeting. These name the twelve foreign operators — 구글, 마이크로소프트, 메타, 샤오미, 스카이스캐너, 스타벅스, 알리익스프레스, **애플**, 테무, 테슬라, 화웨이, BYD — and would nail down “Apple ∈ the twelve.” | `etnews.com/search` (firewall block: “The request / response that are contrary to the Web firewall security policies have been blocked”); `zdnet.co.kr/search` (JS); Bing News `site:` queries (only index the last few months, so a March-2025 article is invisible); Google News RSS (returns opaque `news.google.com/rss/articles/...` redirect links that do not resolve to the publisher URL via `curl -L`). | **Snippet-only.** The Category-5 source 5 and Category-6 source 10 findings stand on the aitimes article, which I did fetch; the Apple-membership inference is flagged as separately sourced. |
| **네이버·다음 김치 번역오류 수정했는데… 구글·애플은 여전히 '파오차이'** — 대한경제, 2020-12-09. Would have documented that the 김치→파오차이 defect was already public **four years before** the 2024 controversy — a strong “known and unfixed” angle. | `dnews.co.kr` guessed URL (HTTP 500); Bing News `site:` (2020 not indexed). | **URL never obtained.** |
| **애플 TV+ 한글 제목은 대체 왜 이렇게 번역하는 걸까요** — 클리앙 (Clien) user thread, 2023-02-16, criticising Apple TV+ Korean title localisation with named examples (원제 *Five Days at Memorial* → 「재난, 그 이후」; 원제 *The Shrink Next Door* → 「의사 그리고 나」). Excellent OPINION source with concrete before/after pairs. | `clien.net/service/search?q=...` (returns 200 but the 2023 thread does not surface under any query variant tried, including the exact title); the thread was visible to me only as a Naver-search snippet. | **URL never obtained.** The before/after pairs above come from a search snippet, so they are **not** quoted in the report. |
| **ASA rulings against Apple** (UK Advertising Standards Authority). | `https://www.asa.org.uk/codes-and-rulings/rulings.html?query=apple` (200 but JS-rendered; returned only three unrelated ruling slugs); the ASA `sitemap.xml` lists only 155 `<loc>` entries and contains **no** Apple/iPhone/iPad/Mac ruling URL. | No Apple ruling retrievable. **I found no ASA ruling against Apple**, and I am not going to assert one exists. |
| **SEC.gov direct access** | `https://www.sec.gov/investment/marketing-rule-faqs` and `https://www.sec.gov/rules/final/2020/ia-5653.pdf` | HTTP 403 (Akamai) on direct request. Worked around successfully via Wayback — see Category-6 source 7. |
| **Microsoft/Nintendo-style machine-translation critique** surfaced by Google News JP while searching Apple Japanese localisation (窓の杜, 2022-04-27, 「メインの勝利」？ Microsoft、開発ドキュメントの機械翻訳を頑張りすぎて変なことに). | Google News RSS headline only | Google News link is an unresolvable redirect; not an Apple source anyway, so excluded. |
| **애플 번역 (Apple 번역) — 나무위키** | https://namu.wiki/w/%EC%95%A0%ED%94%8C%20%EB%B2%88%EC%97%AD (fetched successfully, 200) | Retrieved but **not usable**: despite the promising title, this document is about the *Apple Translate app* as a product (release date, supported languages), not about the quality of Apple's localisation. No criticism section. Documented here so the parent does not re-chase it. |
| **애플 코리아 — 나무위키** | https://namu.wiki/w/%EC%95%A0%ED%94%8C%20%EC%BD%94%EB%A6%AC%EC%95%84 | HTTP 404 — the document does not exist (the live one is `애플/논란`, used as Category-5 source 7). |
| **b.hatena.ne.jp search** | `https://b.hatena.ne.jp/search/text?q=Apple+翻訳+日本語` | HTTP 403. |
| **Hacker News (Algolia) search** | `bash hsearch.sh "Apple marketing language regulated industry healthcare"` and `"dark patterns GDPR unsubscribe"` | Returned empty output for both queries — the script produced no parseable results. No HN source used. |
| **EUR-Lex direct** | `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02005L0029-20220528` | HTTP 202 with a zero-byte body; the fetch script's automatic Wayback fallback succeeded and that is what Category-6 source 3 is based on. |
| **FTC business-guidance blog on “up to” claims** | `https://www.ftc.gov/business-guidance/blog/2021/09/up-claims-when-your-advertising-doesnt-live` | HTTP 404 direct **and** 404 in Wayback — this URL does not exist; my initial guess was wrong. Not replaced by a guess. The “up to requires substantiation” doctrine is instead carried by the FTC Deception Policy Statement's *Firestone* proposition (Category-6 source 4), which is the actual primary authority. |
| **Federal Register search for the SEC Marketing Rule final rule** | `federalregister.gov` API, queries `"investment adviser marketing"` and `"206(4)-1"` with a Dec-2020–Mar-2021 date window | API returned HTTP 200 with an **empty results array** for both targeted queries. Resolved instead via Wayback (Category-6 source 7). |

---

### Coverage summary

| Category | Sources in main list | DOCUMENTED | OPINION |
|---|---|---|---|
| 5 — Korean / Japanese localization | 9 | 6 | 3 |
| 6 — Regulatory constraints | 10 (1 cross-listed) | 10 | 0 |

**Highest-value findings, ranked:**
1. **PIPC 2024 privacy-policy evaluation (Cat 5 #5 / Cat 6 #10)** — a national regulator scoring readability and explicitly penalising **번역투**. This is the only finding that makes Korean-localization quality a *measured regulatory* fact rather than an opinion.
2. **김치 → 韓式泡菜 / Korean → 朝鮮語 (Cat 5 #1–3)** — three independent national outlets, a named complainant, photographic evidence, and reproducible string pairs. Notably the damage is done by Apple's **Japanese** output.
3. **iPhone 13 「スーパーキラキラカラフルクッキリディスプレイ」 (Cat 5 #8–9)** — a fully documented English→Japanese string pair with the original wordplay, the coined translation, and the recorded Japanese reaction.
4. **FTC .com Disclosures (Cat 6 #5)** — the “proximity / prominence / unavoidable / distracting factors” test is the single most precise legal statement of why the Apple hero-claim-plus-footnote layout is a compliance hazard.
5. **21 CFR 202.1(e)(5)–(6) (Cat 6 #6)** — the cleanest proof that the Apple register is *structurally* unavailable in a regulated category: comparative superiority needs substantial evidence and benefits must be balanced in scope and depth by risks.
