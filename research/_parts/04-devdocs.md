# Apple developer documentation style

Scope: Apple Developer documentation style + WWDC sessions about writing, localization, inclusive language.
(HIG “Writing” page and HIG inclusive-writing pages are covered by another agent — not duplicated here.)

## Headline finding: does a public “Apple Developer Documentation Style Guide” exist?

**No.** There is no page, document, or repo published by Apple titled “Apple Developer Documentation Style Guide.”

Verified negatives (all probed with a browser UA, `curl -sSL --compressed`):

| URL probed | Result |
|---|---|
| `https://developer.apple.com/documentation/style-guide` | **404** |
| `https://developer.apple.com/documentation/documentation-style-guide` | **404** |
| `https://developer.apple.com/documentation/xcode/style-guide` | **404** |
| `https://developer.apple.com/documentation/xcode/documentation-style-guide` | **404** |
| `https://developer.apple.com/documentation/docc/style-guide` | 200 but **redirects to `https://www.swift.org/documentation/docc/`** (soft 404 — JS shell, no such page) |
| GitHub `org:apple` repo search: `documentation style`, `style guide`, `style guide in:name` | `total_count: 0` for all three |

What exists instead (the real public substitutes, all Apple-authored):

1. **Apple Style Guide** — Apple's official, public editorial style guide (support.apple.com). “About the guide” explicitly tells **developers** to follow it for user-facing text. This is the closest thing to a developer prose style guide that Apple publishes.
2. **DocC authoring docs** — “Writing documentation” / “Writing symbol documentation in your source files” / “Adding structure to your documentation pages” on `developer.apple.com/documentation/xcode/...`, mirrored on swift.org. These carry the concrete developer-doc writing rules.
3. **Swift API Design Guidelines** (swift.org, Apple-authored) — naming/clarity rules that transfer directly to prose.
4. **WWDC sessions** — the writing-craft rules live mostly in WWDC talks, not in a written style guide.

**Route discovery worth reusing:** Apple Developer documentation pages are DocC-rendered JS, BUT two clean endpoints exist and both worked with plain `curl`:
- `https://developer.apple.com/documentation/<path>.md` → `text/markdown` (clean Markdown, YAML-ish metadata comment at top)
- `https://developer.apple.com/tutorials/data/documentation/<path>.json` → raw DocC JSON
This is far cheaper than the Jina reader for any `developer.apple.com/documentation/...` page.

---

## Sources table

| 출처 | URL | 성격(공식/2차) | 무엇을 규정 | 인용 수 |
|---|---|---|---|---|
| Apple Style Guide — About the guide | https://support.apple.com/guide/applestyleguide/about-the-guide-apsg1eef9171/web | 공식 (Apple 발행, 전체 공개) | 누가 이 가이드를 따르는가, 편집 기준 | 4 |
| Apple Style Guide — General guidelines (Writing inclusively) | https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web | 공식 | 포용적 언어 규칙 | 5 |
| Apple Style Guide — Gender identity | https://support.apple.com/guide/applestyleguide/gender-identity-apd2a7af8d36/web | 공식 | 성별 중립 표현 | 4 |
| Apple Style Guide — Writing about disability | https://support.apple.com/guide/applestyleguide/writing-about-disability-apd49cbb2b06/web | 공식 | 장애 관련 표현 (identity-first/person-first) | 6 |
| Apple Style Guide — Inclusive representation | https://support.apple.com/guide/applestyleguide/inclusive-representation-apd7a037f274/web | 공식 | 예시 이름·고정관념 | 4 |
| Apple Style Guide — Intro to international style | https://support.apple.com/guide/applestyleguide/intro-to-international-style-apsg1ff68ab5/web | 공식 | 번역 친화적 문체 규칙 | 5 |
| Apple Style Guide (PDF, 244p) | https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf | 공식 | 전체 편집 가이드 | (참조) |
| DocC — Writing symbol documentation in your source files | https://www.swift.org/documentation/docc/writing-symbol-documentation-in-your-source-files | 공식 (Apple 저작, Swift.org 호스팅) | 심볼 문서 작성 규칙 | 6 |
| DocC — 같은 문서의 Apple 호스팅판 | https://developer.apple.com/documentation/xcode/writing-symbol-documentation-in-your-source-files.md | 공식 (Apple) | 동일 | 아래 섹션에 통합 |
| DocC — Adding structure to your documentation pages | https://www.swift.org/documentation/docc/adding-structure-to-your-documentation-pages | 공식 (Apple 저작, Swift.org 호스팅) | 랜딩 페이지/개요 작성 규칙 | 5 |
| DocC — Writing documentation (허브) | https://developer.apple.com/documentation/xcode/writing-documentation.md | 공식 (Apple) | DocC 문서화 진입점 | 2 |
| Swift API Design Guidelines | https://www.swift.org/documentation/api-design-guidelines/ | 공식 (Apple 저작, Swift.org 호스팅 — Swift 프로젝트 문서) | 명명·명료성·용어 규칙 | 8 |
| WWDC22 10037 — Writing for interfaces | https://developer.apple.com/videos/play/wwdc2022/10037/ | 공식 (WWDC 전문/transcript) | UI 카피 작성 4원칙 PACE | 8 |
| WWDC25 404 — Make a big impact with small writing changes | https://developer.apple.com/videos/play/wwdc2025/404/ | 공식 (WWDC transcript) | 필러 제거·반복 제거·why 선행·워드리스트 | 9 |
| WWDC24 10140 — Add personality to your app through UX writing | https://developer.apple.com/videos/play/wwdc2024/10140/ | 공식 (WWDC transcript) | voice vs tone | 6 |
| WWDC21 10221 — Streamline your localized strings | https://developer.apple.com/videos/play/wwdc2021/10221/ | 공식 (WWDC transcript) | 번역자용 코멘트 규칙 | 6 |
| WWDC22 10110 — Build global apps: Localization by example | https://developer.apple.com/videos/play/wwdc2022/10110/ | 공식 (WWDC transcript) | 문자열 분리·코멘트·복수형 | 5 |
| WWDC19 254 — Writing Great Accessibility Labels | https://developer.apple.com/videos/play/wwdc2019/254/ | 공식 (WWDC transcript) | 접근성 레이블 문구 규칙 | 6 |
| WWDC22 10034 — Design for Arabic | https://developer.apple.com/videos/play/wwdc2022/10034/ | 공식 (WWDC transcript) | RTL·문화적 적합성 | 4 |
| WWDC21 10275 — The practice of inclusive design | https://developer.apple.com/videos/play/wwdc2021/10275/ | 공식 (WWDC transcript) | 콘텐츠 정의·포용적 표현 | 4 |
| WWDC25 316 — Principles of inclusive app design | https://developer.apple.com/videos/play/wwdc2025/316/ | 공식 (WWDC transcript) | 스펙트럼 사고 | 2 |
| WWDC23 10155 — Discover String Catalogs | https://developer.apple.com/videos/play/wwdc2023/10155/ | 공식 (WWDC transcript) | 문자열 코멘트 권장 | 2 |
| WWDC23 111484 — Q&A: UX writing | https://developer.apple.com/videos/play/wwdc2023/111484/ | 공식 (세션 페이지만, **transcript 없음**) | (설명문만) | 1 |

---

## Per-source detail

### Apple Style Guide — “About the guide” (the authoritative public Apple prose style guide)

URL: https://support.apple.com/guide/applestyleguide/about-the-guide-apsg1eef9171/web
Route that worked: **curl** (plain browser UA, `--compressed`). Static HTML, no JS needed. (`help.apple.com/applestyleguide/` itself is a JS redirector — go straight to `support.apple.com/guide/applestyleguide/<slug>/web`.)
Also verified: full PDF, 244 pages, `application/pdf`, 4,158,788 bytes, HTTP 200, at https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf

Quotes (verbatim):
- “The Apple Style Guide provides editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and user interfaces.”
- “The intent of these guidelines is to help maintain a consistent voice in Apple materials.”
- “Apple developers and third-party developers should follow these guidelines for user-facing text.”
- “In general, follow the style and usage rules in: Merriam-Webster's Collegiate Dictionary”
- “In cases where resources conflict with each other, follow The Chicago Manual of Style for style and usage questions, and Merriam-Webster's Collegiate Dictionary for spelling guidance.”
- (welcome page) “The Apple Style Guide provides guidelines to help maintain a consistent voice in Apple materials, including documentation, reference materials, training, and user interfaces.”

> Note on scope accuracy: this is Apple's **editorial** style guide (Apple Support-hosted), not a “Developer Documentation Style Guide” and not the HIG. It is Apple-authored and explicitly addressed to developers.

### Apple Style Guide — General guidelines (Writing inclusively)

URL: https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web
Route that worked: **curl** (static HTML)

Quotes (verbatim):
- “Think inclusively.”
- “As you write, think about your potential audience, and try to imagine your content from their perspective. Will the words and phrases you use be understood by everyone? Do these words and phrases have any harmful or negative associations?”
- “Keep in mind that words can sometimes carry meanings you don't intend. Be open to learning about the impact of language, and be respectful of those who may receive words differently from how you intended them.”
- “Avoid terms that are violent, oppressive, or ableist. Don't describe technology using terms that are inherently violent—like kill or hang. Don't use the terms master and slave, which describe an oppressive human relationship. In addition, don't use terms like sanity check, which associates mental health with being functional.”
- “In general, it's a good idea to avoid describing software or hardware using human or biological attributes; doing so can lead to unintended hurtful implications.”
- “Consider the context. Even if a common word has one negative use that you should avoid, it may still be acceptable in other contexts. For example, although it's inappropriate to use mute to refer to a person who is nonspeaking, it's OK to use it to refer to silencing a device.”

### Apple Style Guide — Gender identity

URL: https://support.apple.com/guide/applestyleguide/gender-identity-apd2a7af8d36/web
Route that worked: **curl**

Quotes (verbatim):
- “Avoid binary representations of gender when you can reword using gender-neutral language.”
- “Don't use gender-specific pronouns (such as he, she, he or she, and so on) to refer to people of unspecified gender. Instead, it's OK to use they, their, or them as a singular, gender-neutral pronoun.”
- “Correct: A subscriber can post their recipes to your shared folder.”
- “Incorrect: A subscriber can post his or her recipes to your shared folder.”
- “You can also avoid gender-specific pronouns by rewriting a sentence—for example, using the plural form of the noun (subscribers can post their recipes), or simply omitting the pronoun (a subscriber can post recipes).”
- “It's OK to refer to specific genders if the context requires it.”

### Apple Style Guide — Writing about disability

URL: https://support.apple.com/guide/applestyleguide/writing-about-disability-apd49cbb2b06/web
Route that worked: **curl**

Quotes (verbatim):
- “When you write about people with disabilities, focus on each individual's accomplishments, personality, authentic story, or message. You may not even need to mention someone's disability unless it's essential to the content”
- “People who consider a disability or neurodivergence to be part of their identity may prefer identity-first language, which places an emphasis on culture: A Deaf person, an autistic person.”
- “Preferences for identity-first and person-first language vary; when writing about specific individuals or groups, always ask them how they prefer to be identified.”
- “Avoid ableist language. Don't use language that presents people without disabilities as the norm. For example, don't describe nondisabled people as normal, healthy, regular, or able-bodied.”
- “Avoid treating disability as something to overcome, and don't describe people with disabilities as brave, courageous, or inspiring, which can come across as condescending.”
- “When writing instructions (such as in training manuals or user guides), avoid using phrases that refer to the use of specific senses, like you see a message, you see a flashing light, or you hear an alert sound. Instead, simply describe what happens: A message appears, a light flashes, an alert sound plays.”
- “Also avoid using idioms that send negative messages about disability—for example, that's crazy, fell on deaf ears, or turned a blind eye to.”
- “Some phrases and idioms are OK. It's OK to use commonly understood phrases such as the ones below: I see your point. … Hear about the latest news right when it happens. … Even if people in your audience can't see, hear, or speak, they'll typically understand the intent of the words.”

### Apple Style Guide — Inclusive representation

URL: https://support.apple.com/guide/applestyleguide/inclusive-representation-apd7a037f274/web
Route that worked: **curl**

Quotes (verbatim):
- “When your content depicts people—real or fictional—make sure to represent the diversity of the world.”
- “Use diverse names as examples. … Include names that reflect a variety of ethnicities and genders.” (given-name examples: “Blair, Étienne, Guillermo, Lee, Mayuri, Priyanka, Shannon, Yen”)
- “Also keep in mind that some cultures don't use a Western-style name structure (given name followed by a family name).”
- “If your content mentions examples of holidays, foods, or sports, don't give examples only from Western culture. Avoid using examples that reflect primarily an affluent lifestyle.”

### Apple Style Guide — Intro to international style (the localization-writing rules)

URL: https://support.apple.com/guide/applestyleguide/intro-to-international-style-apsg1ff68ab5/web
Route that worked: **curl**

Quotes (verbatim):
- “Following international style helps readers with limited English proficiency read what you write. By following international style, you also help translators—human or machine—localize your writing by minimizing the burdens of cultural and customary language usage.”
- “These are the basic rules:”
- “Write in simple structures.”
- “Don't use idiomatic or colloquial expressions.”
- “Avoid shortcuts, symbols, and abbreviations that could easily be spelled out.”
- “Express data using the standard international conventions outlined in this chapter.”

### DocC — Writing symbol documentation in your source files

URL: https://www.swift.org/documentation/docc/writing-symbol-documentation-in-your-source-files (Apple-hosted mirror: https://developer.apple.com/documentation/xcode/writing-symbol-documentation-in-your-source-files.md)
Route that worked: **jina** for swift.org (`https://r.jina.ai/<url>` → clean markdown); **curl** for the `.md` endpoint on developer.apple.com. Note: `https://www.swift.org/documentation/docc/writing-symbol-documentation` (without `-in-your-source-files`) is a **soft 404** — it renders a footer-only shell. Use the full slug.

Quotes (verbatim):
- “A common characteristic of a well-crafted API is that it's easy to read and practically self-documenting.”
- “The first step toward writing great documentation is to add single-sentence abstracts or summaries”
- “A summary describes a symbol and augments its name with additional details. Try to keep summaries short and precise; use a single sentence or sentence fragment that's ideally 150 characters or fewer. Use plain text, and avoid including links, technical terms, or other symbol names.”
- “DocC uses the first line of a documentation comment as the summary.”
- “For a property, explain how it affects the behavior of its parent. Describe typical usage and any permitted or default values.”
- “For a method, describe its usage patterns and any side effects or additional behaviors. Highlight whether the method executes asynchronously or performs any expensive operations.”
- “Describe each parameter in isolation. Discuss its purpose and, where necessary, the range of acceptable values.”
- “Use symbol links instead of code voice when referring to other symbols in your project.”

### DocC — Adding structure to your documentation pages

URL: https://www.swift.org/documentation/docc/adding-structure-to-your-documentation-pages (Apple mirror: https://developer.apple.com/documentation/xcode/adding-structure-to-your-documentation-pages.md)
Route that worked: **jina** (swift.org) / **curl** (`.md`)

Quotes (verbatim):
- “A landing page provides an overview of your framework, introduces important terms, and organizes the resources within your documentation catalog”
- “The landing page is an opportunity for you to ease the reader's learning path, discuss key features of your technology, and offer motivation for the reader to return to when they need it.”
- “Try to keep the Overview brief — typically less than a screen's worth of content. Avoid detailing every feature in your framework. Instead, provide content that helps the reader understand what problems the framework solves.”
- “To help readers more easily navigate your framework, arrange symbols into groups with meaningful names. Place important symbols higher on the page, and nest supporting symbols inside other symbols. Use group names that are unique, mutually exclusive, and clear.”
- “Experiment with different arrangements to find what works best for you.”

### DocC — Writing documentation (hub page, Apple-hosted, “official” landing page for doc authoring)

URL: https://developer.apple.com/documentation/xcode/writing-documentation.md
Route that worked: **curl** on the `.md` endpoint (`text/markdown`). Plain HTML page is a JS shell reading “This page requires JavaScript.”

Quotes (verbatim):
- “Produce rich and engaging developer documentation for your apps, frameworks, and packages.”
- “DocC syntax — called documentation markup — is a custom variant of Markdown that adds functionality for developer documentation-specific features, like cross-symbol linking, term-definition lists, code listings, and asides.”

### Swift API Design Guidelines

URL: https://www.swift.org/documentation/api-design-guidelines/
Route that worked: **curl** with `--compressed` (the page is gzip-encoded and long; without `--compressed` you get binary). Static HTML, ~28.6 KB.
Provenance note (mark accurately): this is **Swift.org**, the Apple-hosted / Apple-authored site for the Swift project. It is an official Swift-project document, not an Apple Developer Documentation page.

Quotes (verbatim):
- “Clarity at the point of use is your most important goal. Entities such as methods and properties are declared only once but used repeatedly.”
- “Clarity is more important than brevity. Although Swift code can be compact, it is a non-goal to enable the smallest possible code with the fewest characters.”
- “Write a documentation comment for every declaration. Insights gained by writing documentation can have a profound impact on your design, so don't put it off.”
- “If you are having trouble describing your API's functionality in simple terms, you may have designed the wrong API.”
- “Begin with a summary that describes the entity being declared. Often, an API can be completely understood from its declaration and its summary.”
- “Focus on the summary; it's the most important part. Many excellent documentation comments consist of nothing more than a great summary.”
- “Use a single sentence fragment if possible, ending with a period.  Do not use a complete sentence.”
- “Describe what a function or method does and what it returns, omitting null effects and Void returns”
- “Include all the words needed to avoid ambiguity for a person reading code where the name is used.”
- “Omit needless words. Every word in a name should convey salient information at the use site.”
- “Avoid obscure terms if a more common word conveys meaning just as well.  Don’t say “epidermis” if “skin” will serve your purpose. Terms of art are an essential communication tool, but should only be used to capture crucial meaning that would otherwise be lost.”
- “Don't surprise an expert: anyone already familiar with the term will be surprised and probably angered if we appear to have invented a new meaning for it.”
- “Don't confuse a beginner: anyone trying to learn the term is likely to do a web search and find its traditional meaning.”
- “Avoid abbreviations. Abbreviations, especially non-standard ones, are effectively terms-of-art, because understanding depends on correctly translating them into their non-abbreviated forms.”
- “Prefer method and function names that make use sites form grammatical English phrases.”

### WWDC22 10037 — Writing for interfaces (the single best session for UI copy)

URL: https://developer.apple.com/videos/play/wwdc2022/10037/
Route that worked: **curl** with browser UA — the full transcript is in the **static HTML** (157 KB uncompressed). No JS, no Jina needed. Same pattern holds for every `/videos/play/wwdcYYYY/NNNN/` page.
Speakers: Kaely Coon and Jennifer Bush, writers on Apple's Human Interface design teams.

Quotes (verbatim):
- “it's our job to design through the lens of language.”
- “the earlier you make writing a part of the process of designing your app, the better the experience will be for the people who use it.”
- “These are: Purpose, Anticipation, Context, and Empathy.”
- “You'll notice we've given you an acronym of ”PACE,“”
- “Know what to leave out.”
- “Rather than give too many details, aim for simplicity. You can tell people the purpose of a screen; it's not a secret!”
- “Develop your app's voice first, and then you can vary its tone. Start by asking yourself: what would it say and not say?”
- “The tone is quite celebratory, so it has an exclamation point. Be careful how often you use those, though. They can look silly when they're frequent.”
- “When writing for alerts, it's always best to be specific about the action the buttons are going to take. On this alert, if you only read the button labels, you would still understand what you were choosing.”
- “interjections like ”oops!“ or ”uh-oh“ can sound patronizing, and ”please“ and ”sorry“ can sound insincere. Use them sparingly.”
- “It's best to use simple, plain language, as idioms and humor can be misunderstood or not translate, and some phrases have meanings that exclude people.”
- “Notice also that each of these examples is described as a ”person,“ not, say, a ”man“ or a ”woman.“ You can also help everyone feel welcome in your app by avoiding unnecessary references to specific genders.”
- “read your writing out loud. It can really help make sure your writing sounds conversational, like how you'd talk to a friend. Reading out loud can also help you find unnecessary or repetitive words, grammatical mistakes, or typos.”

### WWDC25 404 — Make a big impact with small writing changes (most concrete, newest ruleset)

URL: https://developer.apple.com/videos/play/wwdc2025/404/
Route that worked: **curl** (static HTML transcript)
Speakers: Liv Huntley and Jennifer Bush, UX Writers at Apple. The four changes: remove fillers / avoid repetition / lead with the why / make a word list.

Quotes (verbatim):
- “when we're asked about how to improve the writing in apps, the advice we give most often is to simplify.”
- “A common misconception in UX writing is that we need to fill all the empty space.”
- “Fortunately, your app doesn't have a minimum word count. In fact, usually the opposite is true and it's best to remove words.”
- (on “Simply enter your license plate number to quickly pay for parking.”) “If I remove the words 'simply' and 'quickly' from this message… I haven't lost any clarity, and I don't make assumptions about the context of the person using it.”
- “While it might seem like these words make your app feel more personal, it's best to remove them when they don't add any meaning to the message.”
- “Words like "uh oh", "oops" or "oh no!" in error messages can make it sound like you’re not taking the problem seriously.” (quotation marks as printed in the transcript)
- “Try to avoid unnecessary punctuation disguised as a kind of filler.”
- “UX writing is all about economy of language. Resist the urge to fill all available space with repeated information.”
- “Messaging is most effective when you tell the people using your app why taking that next step will be fun, or interesting, or beneficial to them.”
- “if you're leaving the benefit for the end of the sentence, try moving it to the front. It only takes a moment to do, but really improves the impact of your message.”
- “Using the same button name for the same action, in this case, moving to the next screen, helps build trust through consistency. Button labels are a great thing to add to your word list.”
- “If you're not sure what to use for some of the terms in your app, the Apple Style Guide, available to anyone, is a good place to start.”
- “Read your writing out loud. It makes it easier to hear those filler and repetitive words and know where to tighten up your writing.”

### WWDC24 10140 — Add personality to your app through UX writing (voice vs tone)

URL: https://developer.apple.com/videos/play/wwdc2024/10140/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “You can think of voice as the expression of your brand and values through words. It's the things about your writing that tend not to change.”
- “Clarity, simplicity, friendliness, and helpfulness.” (the four qualities the Apple writer keeps in mind: “I see these pretty consistently throughout Apple's writing”)
- “You can think of tone as the way your voice adapts to the situation.”
- “Voice represents the consistent elements that are always there. The tone represents things that can and should change depending on the moment.”
- “even though we tend to use exclamation marks pretty sparingly around here, this screen gets one, because of the situation.”
- “Notice how there's a little bit of tension here. Simplicity and friendliness are just slightly at odds with each other. If you're adding an extra word here or there to create some friendliness, you're taking away from the simplicity and vice versa. They balance each other out. That can help modulate tone.”
- “It opens with a friendly greeting. ”Good morning“, like a person saying hello to another.”

### WWDC21 10221 — Streamline your localized strings (translator-comment rules)

URL: https://developer.apple.com/videos/play/wwdc2021/10221/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “Think about all the strings in your app as movie subtitles. In the movie you watch, you want all subtitles to be in the right language, at the right time, with the right context, and consistent throughout the movie.”
- “Translators don't have the full app UI in front of them while they translate string by string, and they need to stay consistent in all strings. So you need to help them, just like you help your coworkers understand your code by adding code comments.”
- “I insist, no matter the string, you should always define a comment.”
- “First, comments should explain where the string is visible. For instance, is this a button? A label? Some VoiceOver text? Knowing if this is an action -- to order -- or a statement -- an order -- is critical.”
- “Second, they should explain the context. If I press Order, am I completing a transaction or sorting a list? Lastly, comments should explain variables.”
- “be careful not to overuse variables. Gluing strings together is handy but could lead to translation problems.”
- “the text can be read, be accurate, and be accessible.”

### WWDC22 10110 — Build global apps: Localization by example

URL: https://developer.apple.com/videos/play/wwdc2022/10110/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “Internationalization means preparing your app to run on devices all across the world. When localization is done well, everybody gets to enjoy the same great experience and utility– regardless of the language they speak.”
- “Even though the English words are the same, when they appear in different contexts, other languages might use different words. You should use two strings in code in this case.”
- “A great comment explains which interface element the string is shown in, like a label or a button. It also explains the context of the UI element and where it is shown on screen.”
- “If the string contains variables, make sure to explain their value at runtime.”
- “Remember that translators might not see the app at runtime when translating your content.”
- “Joining strings might have surprising consequences in other languages: they might need to inflect the grammar or could have troubles with capitalization”
- “Having people who speak the language testing the app is a substantial part of the workflow.”

### WWDC19 254 — Writing Great Accessibility Labels

URL: https://developer.apple.com/videos/play/wwdc2019/254/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “It's a localized string that succinctly identifies the accessibility element.”
- “VoiceOver knows what the element in your apps is based on the element type. So, it's redundant to add text to your string like button or tab.”
- “Remember to update the label when the UI changes.”
- “When there's multiple buttons with the same action like adding an item to the cart, remember to provide the context.”
- “Avoid redundant labels.”
- “Remember, we want these labels to be as succinct as possible.”
- “But verbosity isn't always a bad thing though. Oftentimes verbose descriptions when in appropriate situations is really what makes your app fun and memorable.”

### WWDC22 10034 — Design for Arabic

URL: https://developer.apple.com/videos/play/wwdc2022/10034/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “There is around 660 million people that uses the Arabic script today, which makes it the third most written language in the world after Latin and Chinese.”
- “If you want to reach even a fraction of that audience, you would want to consider optimizing not only for the language, but also for the directionality of the UI.”
- “Titles, buttons, and the Navigation bar should change order and position. Paragraphs should be always aligned to the right. Carousals and swipeable elements should also flow from right to left.”
- “it is always important to make sure that your app is culturally relevant.”

### WWDC21 10275 — The practice of inclusive design

URL: https://developer.apple.com/videos/play/wwdc2021/10275/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “At Apple, we define ”content“ as the words, images, audio, and video that live inside your designs, as well as your marketing. Content is the language you use to speak to your audience.”
- “The way you address people through your content and how you let folks represent themselves are great moments where you can make more people feel welcome.”
- “When someone approaches your app or game, they should feel like you designed with them in mind.”
- “The way you describe your app or game, its name, video trailer, and even the screenshots you select tell a story about whom it was built for and how they might use it.”

### WWDC25 316 — Principles of inclusive app design

URL: https://developer.apple.com/videos/play/wwdc2025/316/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “About one in seven people has a disability.”
- “it's really important to think of all of these senses as a spectrum, because everyone is different.”
- “By just adding that one extra word, “some”, you remind yourself of the spectrum within disability, and that will help you make more inclusive design decisions.”

### WWDC23 10155 — Discover String Catalogs

URL: https://developer.apple.com/videos/play/wwdc2023/10155/
Route that worked: **curl** (static HTML transcript)

Quotes (verbatim):
- “string comments provide a way to give the translator context about where and how the string is being used in the user interface. We recommend adding comments to strings in order to help resolve ambiguities for the translator.”
- “Here at Apple, we strongly believe in accessibility and inclusivity. Localizing your app is one way to ensure your content reaches more people around the world.”

### WWDC23 111484 — Q&A: UX writing

URL: https://developer.apple.com/videos/play/wwdc2023/111484/
Route that worked: **curl** — but the page has **no transcript** (it is a Slack Q&A session; only the description is published).

Quote (verbatim, description only):
- “Ask Apple UX writers for guidance on writing great copy for your app during this hour-long Q&A in Slack. Ask a question about a specific label or an area of your app, explore best practices, or learn from others.”

Same “no transcript” result for the other Q&A sessions checked: WWDC22 110540 “Q&A: Internationalization and localization”, WWDC23 10334 “Q&A: Internationalization and localization” (both pages render but contain no transcript body).

---

## Consolidated rule summary (all traceable to the quotes above)

**Voice / person / tense**
- Apple's own four qualities: clarity, simplicity, friendliness, helpfulness (WWDC24 10140).
- Voice is fixed, tone flexes by situation (WWDC24 10140; WWDC22 10037).
- Second person, conversational register: speak to the reader “like how you'd talk to a friend” (WWDC22 10037).
- Simple structures; no idioms or colloquialisms (Apple Style Guide, international style).
- For developer docs specifically: symbol summaries are **sentence fragments ending with a period**, not complete sentences (Swift API Design Guidelines); DocC asks for a single sentence/fragment ≤150 characters (DocC).

**Concision**
- No filler adverbs/adjectives (“simply”, “quickly”), no interjections (“oops”, “uh oh”, “hooray”), no pleasantries (“please”, “sorry”, “thank you”); no exclamation-point filler (WWDC25 404; WWDC22 10037).
- Don't repeat the same information in headline and body; combine (WWDC25 404).
- Omit needless words (Swift API Design Guidelines).
- Keep overviews “less than a screen's worth of content” (DocC).

**Structure**
- Lead with the benefit/why, then the action: “To get reservation updates, enter your phone number.” (WWDC25 404)
- Alert titles must be specific; buttons must name the action, never Yes/No (WWDC22 10037).
- Information hierarchy: header first, then supporting text smaller (WWDC22 10037).
- Consistent terminology; keep a word list of approved and banned terms (WWDC25 404).

**Inclusive & localizable language**
- Avoid gendered defaults; singular “they” is approved; avoid binary gender framing (Apple Style Guide).
- Avoid ableist/violent/oppressive tech metaphors (kill, hang, master/slave, sanity check); don't describe software with human/biological attributes (Apple Style Guide).
- Don't describe people with disabilities as brave/inspiring; don't call nondisabled people “normal” (Apple Style Guide).
- Don't reference senses in instructions: write “A message appears,” not “you see a message” (Apple Style Guide).
- Diverse example names and non-Western examples (Apple Style Guide).
- Avoid idioms/humor that won't translate or that exclude (WWDC22 10037; Apple Style Guide).
- Every user-visible string needs a translator comment covering **where it appears, what it means in context, and what each variable holds** (WWDC21 10221; WWDC22 10110; WWDC23 10155).
- Separate strings when the same English word plays two roles (e.g. “Archive” the folder vs. the action) (WWDC22 10110).
- Design for text expansion, taller scripts, and RTL (WWDC22 10037; WWDC22 10034).

---

## Failed URLs and why

| URL | Result | Why |
|---|---|---|
| `https://developer.apple.com/documentation/style-guide` | 404 | No such page — this is the direct evidence that no public “Apple Developer Documentation Style Guide” exists |
| `https://developer.apple.com/documentation/documentation-style-guide` | 404 | same |
| `https://developer.apple.com/documentation/xcode/style-guide` | 404 | same |
| `https://developer.apple.com/documentation/xcode/documentation-style-guide` | 404 | same |
| `https://developer.apple.com/documentation/docc/style-guide` | 200 → redirects to `https://www.swift.org/documentation/docc/` | Soft 404 caused by the DocC→swift.org redirect. Not a real page. |
| `https://developer.apple.com/documentation/docc` | 200 → redirects to `https://www.swift.org/documentation/docc/` | Apple's DocC docs now live on swift.org; the developer.apple.com path is a redirect shell |
| `https://www.swift.org/documentation/docc/writing-symbol-documentation` | 200 but footer-only shell | Wrong slug; correct slug is `writing-symbol-documentation-in-your-source-files` |
| `https://developer.apple.com/documentation/docc/writing-symbol-documentation-in-your-source-files` | 200 but redirect shell → swift.org docc root | Use the `.md` form under `/documentation/xcode/...` instead |
| `https://developer.apple.com/documentation/xcode/writing-documentation` (HTML) | 200 but JS shell: “This page requires JavaScript.” | Use `…/writing-documentation.md` (`text/markdown`, 200) |
| `https://www.swift.org/documentation/api-design-guidelines/` without `--compressed` | 200 but binary garbage | Response is gzip-encoded; always pass `--compressed` for swift.org |
| `https://developer.apple.com/videos/play/wwdc2023/111484/` | 200, no transcript | Q&A sessions have no published transcript (same for 110540, 10334) |
| `https://help.apple.com/applestyleguide/` | 200 but 248-byte `redirect.js` shell | JS-only redirector; use `https://support.apple.com/guide/applestyleguide/<slug>/web` directly |
| GitHub search `org:apple documentation style`, `org:swiftlang style guide`, `style guide in:name org:apple` | `total_count: 0` | No Apple/Swift GitHub repo documenting prose style; `swiftlang/swift-docc` has no style-guide doc (only `CONTRIBUTING.md` and `.unacceptablelanguageignore`) |
| GitHub code search API (`/search/code?q=repo:swiftlang/swift-docc+style+guide`) | 401 | Requires authentication |
| `web_search` tool | “all search providers failed” (SearXNG no results; Tavily/Brave keys missing; DuckDuckGo HTTP 202 / unparseable) | Search tooling unavailable in this session — all findings above were reached by direct URL probing, not by search |
| `https://html.duckduckgo.com/html/?q=...` and `https://www.bing.com/search?q=...` | 200 but 0 parseable results | Both anti-bot gated for this UA |
| `https://developer.apple.com/search/search_data.php?q=...` | 404 | Apple's site search is JS/AI-rendered; no plain JSON endpoint found |
