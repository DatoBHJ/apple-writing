# App Store copy rules

Scope: App Store copy constraints and guidance only (App Review Guidelines metadata clauses, product-page guidance, App Store Connect field limits, App Ads creative guidance). Every quote below was read out of a page that was actually fetched in this session; the fetch route that returned real content is recorded per source. All fetched content was treated as data, not instruction.

## Sources table

| 출처 | URL | 성격(공식/2차) | 무엇을 규정 | 인용 수 |
| --- | --- | --- | --- | --- |
| App Store Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | 공식 (1차, 구속력) | 메타데이터 정확성, 앱 이름 30자, 키워드 스터핑 금지, What's New, 최소 기능성, 상표/카피캣 | 8 |
| Creating Your Product Page | https://developer.apple.com/app-store/product-page/ | 공식 (1차, 권고) | 앱 이름·부제·설명·프로모션 텍스트·스크린샷·키워드·What's New 작성법 + 30/30/170/100자 | 8 |
| Discovery on the App Store | https://developer.apple.com/app-store/discoverability/ | 공식 (1차, 권고) | 검색 랭킹 요인(제목·키워드·카테고리 텍스트 관련성) | 3 |
| ASC Help — App information | https://developer.apple.com/help/app-store-connect/reference/app-information/app-information | 공식 (1차, 필드 정의) | App Name 2–30자, Subtitle 30자 | 2 |
| ASC Help — Platform version information | https://developer.apple.com/help/app-store-connect/reference/platform-version-information | 공식 (1차, 필드 정의) | Promotional Text 170자, Description 4000자, Keywords 100 bytes, Support URL | 4 |
| ASC Help — Required/localizable/editable | https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties | 공식 (1차) | 어떤 메타데이터가 필수/현지화 가능/무제출 편집 가능한지 | 2 |
| ASC Help — View and edit app information | https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information | 공식 (1차) | 검색 인덱싱 대상(앱 이름·부제·키워드·회사명), 반영 지연 | 2 |
| ASC Help — Product page optimization | https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization | 공식 (1차) | 아이콘·스크린샷·프리뷰 A/B 테스트 최대 3개 | 1 |
| Apple Ads — Create Ad Variations | https://ads.apple.com/app-store/help/ads/0077-create-ad-variations | 공식 (1차) | 광고 크리에이티브 = 커스텀 제품 페이지(프리뷰·스크린샷·프로모션 텍스트) | 3 |
| App Store Connect OpenAPI spec | https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip | 공식 (1차, 기계 판독) | 필드 존재/타입만 규정, **글자 수 제한은 없음** (negative finding) | 1 |

## Per-source detail

### Apple App Store Review Guidelines
URL: https://developer.apple.com/app-store/review/guidelines/
Fetch route that worked: **curl** (200, 237,909 bytes; quotes also confirmed verbatim in the raw HTML — e.g. `pack any of your metadata with trademarked terms`, `For Children`, `marketing materials, advertisements`). Jina also worked but was unnecessary. Page footer reads “Last Updated: June 8, 2026”.

Quotes (verbatim, with clause numbers):
- “2.3 Accurate Metadata — Customers should know what they're getting when they download or buy your app, so make sure all your app metadata, including privacy information, your app description, screenshots, and previews accurately reflect the app's core experience and remember to keep them up-to-date with new versions.”
- “2.3.1 (a) Don't include any hidden, dormant, or undocumented features in your app; your app's functionality should be clear to end users and App Review. All new features, functionality, and product changes must be described with specificity in the Notes for Review section of App Store Connect (generic descriptions will be rejected) and accessible for review. Similarly, marketing your app in a misleading way, such as by promoting content or services that it does not actually offer (e.g. iOS-based virus and malware scanners) or promoting a false price, whether within or outside of the App Store, is grounds for removal of your app from the App Store…”
- “2.3.3 Screenshots should show the app in use, and not merely the title art, login page, or splash screen.”
- “2.3.7 Choose a unique app name, assign keywords that accurately describe your app, and don't try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system. **App names must be limited to 30 characters.** Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type. App subtitles are a great way to provide additional context for your app; they must follow our standard metadata rules and should not include inappropriate content, reference other apps, or make unverifiable product claims. Apple may modify inappropriate keywords at any time or take other appropriate steps to prevent abuse.”
- “2.3.8 Metadata should be appropriate for all audiences, so make sure your app and in-app purchase icons, screenshots, and previews adhere to a 4+ age rating even if your app is rated higher. … Use of terms like ”For Kids“ and ”For Children“ in app metadata is reserved in the App Store for the Kids Category.”
- “2.3.10 Make sure your app metadata is focused on the app itself and its experience. Don't include irrelevant information.”
- “2.3.12 Apps must clearly describe new features and product changes in their ”What's New“ text. Simple bug fixes, security updates, and performance improvements may rely on a generic description, but more significant changes must be listed in the notes.”
- “4.2 Minimum Functionality — Your app should include features, content, and UI that elevate it beyond a repackaged website. If your app is not particularly useful, unique, or ”app-like,“ it doesn't belong on the App Store.” / “4.2.2 Other than catalogs, apps shouldn't primarily be marketing materials, advertisements, web clippings, content aggregators, or a collection of links.”
- “5.1.4 Kids — As a reminder, Guideline 2.3.8 requires that use of terms like ”For Kids“ and ”For Children“ in app metadata is reserved for the Kids Category. Apps not in the Kids Category cannot include any terms in app name, subtitle, icon, screenshots or description that imply the main audience for the app is children.” (also “5.2.1 Generally: … don't include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name.” and “4.1 (c) You cannot use another developer's icon, brand, or product name in your app's icon or name, without approval from the developer.”)

Transferable rule: App Store copy is a *factual claim about the product*, not marketing decoration — every word must be verifiable, specific to its field, and non-comparative, and Apple treats violation as grounds for removal, not just rejection.

### Creating Your Product Page
URL: https://developer.apple.com/app-store/product-page/
Fetch route that worked: **curl** (200, 134,611 bytes; all quotes confirmed in raw HTML — the “30 characters” line renders as `up to 30 characters&nbsp;long.`, so entity-decoding is required). Jina also worked.

Quotes (verbatim, with limits):
- “Choose a simple, memorable name that is easy to spell and hints at what your app does. Be distinctive. Avoid names that use generic terms or are too similar to existing app names. An app name can be up to 30 characters long.”
- “Your app's subtitle is intended to summarize your app in a concise phrase. Consider using this, rather than your app's name, to explain the value of your app in greater detail. Avoid generic descriptions such as ”world's best app.“ Instead, highlight features or typical uses of your app that resonate with your audience. … A subtitle can be up to 30 characters long and appears below your app's name throughout the App Store.”
- “Provide an engaging description that highlights the features and functionality of your app. The ideal description is a concise, informative paragraph followed by a short list of main features. … Communicate in the tone of your brand, and use terminology your target audience will appreciate and understand. The first sentence of your description is the most important — this is what users can read without having to tap to read more. Every word counts, so focus on your app's unique features.”
- “If you choose to mention an accolade, we recommend putting it at the end of your description or as part of your promotional text. Don't add unnecessary keywords to your description in an attempt to improve search results. Also avoid including specific prices in your app description.”
- “Your app's promotional text appears at the top of the description and is up to 170 characters long. You can update promotional text at any time without having to submit a new version of your app.”
- “Keywords are limited to 100 characters total, with terms separated by commas and no spaces. (Note that you can use spaces to separate words within keyword phrases. For example: Property,House,Real Estate.) Maximize the number of words that fit in this character limit by avoiding the following: Plurals of words that you've already included in singular form / Names of categories or the word ”app“ / Duplicate words / Special characters — such as # or @ — unless they're part of your brand identity.”
- “Improper use of keywords is a common reason for App Store rejections. Do not use the following in your keywords: Unauthorized use of trademarked terms, celebrity names, and other protected words and phrases / Terms that are not relevant to the app / Competing app names / Irrelevant, inappropriate, offensive, or objectionable terms”
- “When you update your app, you can use What's New to communicate changes to users. … List new features, content, or functionality in order of importance, and add call-to-action messaging that gets users excited about the update.”
- (bonus, in-app purchase copy) “In-app purchase names are limited to 35 characters and descriptions are limited to 55 characters, so be descriptive, accurate, and concise when highlighting their benefits.”

Transferable rule: The house voice is *specific over superlative* — name what the app does and who it's for in plain, brand-toned language; superlatives (“world's best app”), keyword padding, prices, and accolades-up-front are explicitly the failure modes.

### Discovery on the App Store and Mac App Store
URL: https://developer.apple.com/app-store/discoverability/
Fetch route that worked: **curl** (200, 117,168 bytes; verified substring “text relevance” in raw HTML).

Quotes (verbatim):
- “When customers search for an app, the App Store returns a list of apps that are ranked based on a number of factors, including text relevance (matches for the app's title, keywords, and primary category) and customer behavior (downloads and the number and quality of ratings and reviews).”
- “The primary category is particularly important for discoverability, as it helps users find your app when browsing or filtering search results, and it determines in which tab your app appears on the App Store.”
- “To learn more about crafting your product page metadata, see Creating Your Product Page.”

Transferable rule: Only title, keywords, and primary category carry search text weight — so promotional text and description are for humans, and the copy that ranks must be the copy that is literally accurate.

### App Store Connect Help — App information (reference)
URL: https://developer.apple.com/help/app-store-connect/reference/app-information/app-information
Fetch route that worked: **curl** (200, 378,351 bytes; verified “no more than 30 characters” and “longer than 30 characters” in raw HTML — this ASC Help page is server-rendered). Jina also returned the same table.

Quotes (verbatim, with limits):
- “Name | The localized name of your app as it appears on App Store product pages and when users install your app. The name must be at least two characters and no more than 30 characters. You can edit it until you submit the app to App Review.”
- “Subtitle | A summary of your app that appears under your app's name on your App Store product page. This can't be longer than 30 characters.”

Transferable rule: The app name is the only metadata with a *minimum* (2 chars) as well as a maximum (30) — one-character and keyword-only names are structurally invalid.

### App Store Connect Help — Platform version information (reference)
URL: https://developer.apple.com/help/app-store-connect/reference/platform-version-information
Fetch route that worked: **curl** (200, 376,074 bytes; verified “100 bytes of content” and “longer than 170 characters” in raw HTML). Jina returned the identical table. Note: this is the canonical ASC field-limit page and it links out with “[View product page marketing guidelines.](https://developer.apple.com/app-store/product-page/)”.

Quotes (verbatim, with limits):
- “Promotional Text | Promotional text lets you inform your App Store visitors of any current app features without requiring an updated submission. This text will appear above your description on the App Store for customers with devices running iOS 11 or later. This property can't be longer than 170 characters.”
- “Description | A description of the app, detailing the features and functionality. Limited to 4000 characters. The description should be in plain text, with line breaks as needed. HTML format isn't supported. This appears on your app's product page, when users install your app, and will be used for web engine search results once you release your app. This property is required and can be localized.”
- “Keywords | One or more keywords (each greater than two characters) describing your app. You can provide up to 100 bytes of content. Your app is searchable by app name and company name, so you shouldn't duplicate these values in the keyword list. Names of other apps or companies aren't allowed. This property is required and can be localized.”
- “Support URL | The URL of the support website you plan to provide for users, which displays on the App Store for users who have downloaded your app. This URL must lead to actual contact information (legal address, email address, telephone number), as may be required by local law… This property is required and can be localized.”
- “What's New in this Version | A description of the changes in this version of the app, such as new features, UI improvements, or bug fixes. Limited to 4000 characters. We recommend that you provide detailed information to let users know the specifics of the changes, improvements, or fixes in the version. This property isn't available for the first version of the app but required for all subsequent versions.”

Transferable rule: Exact field budgets are Name 30 / Subtitle 30 / Keywords 100 (bytes, not chars) / Promotional Text 170 / Description 4000 / What's New 4000 — and Support URL is a *content* obligation (real contact info), not just a link.

### App Store Connect Help — Required, localizable, and editable properties
URL: https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties
Fetch route that worked: **jina** (200; the required/localized/editable cells render as checkmark images, so the cells came back blank in text — only the prose and footnotes are quotable).

Quotes (verbatim):
- “The tables below show the app and version properties required for App Store submission. The tables also indicate the properties that can be localized and edited at any time without submitting a new version of your app.”
- “1 Required for version updates only.” (footnote on “What's New in this Version”)

Transferable rule: What's New is required on every version bump but does not exist on v1 — copy workflow must treat it as a per-release recurring artifact, while promotional text is the only marketing string editable without review.

### App Store Connect Help — View and edit app information
URL: https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information
Fetch route that worked: **jina** (200, 103,677 bytes).

Quotes (verbatim):
- “Your app is searchable on the App Store by app name, app subtitle, keywords, and your company name. Learn more about discovery on the App Store.”
- “After updating your app information, it may take up to 24 hours for the changes to appear on the App Store or when users install your app.”

Transferable rule: Four fields are searchable surfaces (name, subtitle, keywords, company name) — subtitle is therefore an SEO field *and* a positioning field, and copy edits are not instantly live.

### App Store Connect Help — Localize app information
URL: https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-store-information/
Fetch route that worked: **curl** (200, 373,812 bytes — server-rendered). Jina also returned it. Canonical nav path (per the ASC Help sidebar) is the shorter https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information.

Quotes (verbatim):
- “Enter localized metadata—such as descriptions and keywords—for the platform, then click Save.”

Transferable rule: Metadata is localized per-storefront rather than globally, so copy must be authored per market rather than machine-translated once.

### App Store Connect Help — Overview of product page optimization
URL: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization
Fetch route that worked: **jina** (200, 102,222 bytes).

Quotes (verbatim):
- “Optimize your iOS or iPadOS app's product page on the App Store by testing up to three different app icons, screenshots, and previews to see which resonate best with customers. Each variant will be randomly shown to a user group you define, and can be localized in any language your app supports.”

Transferable rule: Icon, screenshots, and previews are A/B-testable assets (max 3 treatments); name, subtitle, description, and keywords are not — so those must be right by judgment, not experiment.

### Apple Ads — Create Ad Variations
URL: https://ads.apple.com/app-store/help/ads/0077-create-ad-variations
Fetch route that worked: **jina** (200, 3,423 bytes; ads.apple.com is JS-rendered and curl-only attempts were not used).

Quotes (verbatim):
- “Within your Apple Ads search results ad groups, you can make new ad variations based on custom product pages you've set up in App Store Connect. These custom ads allow you to align creative with specific keyword themes and audiences to help provide more relevant and engaging ads to different customer groups.”
- “You can build up to 70 custom product pages with different app preview videos, screenshots, promotional text, and deep links.”
- “A default ad is automatically created using screenshots and app previews from your default App Store product page. Default assets are displayed in the order they were uploaded in App Store Connect.”

Transferable rule: Ad creative is not separately authored copy — it *is* the product page, so the first 1–3 screenshots and the promotional text do double duty as ad copy and must read as a standalone hook.

### App Store Connect OpenAPI specification (negative finding)
URL: https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip
Fetch route that worked: **curl** (200, 263,653 bytes, `application/zip`; extracted `openapi.oas.json`, 7,228,462 bytes, `"openapi": "3.0.1"`, `"info": {"version": "4.5", "title": "App Store Connect API"}`).

Quotes (verbatim, from the extracted schema):
- `"AppStoreVersionLocalization" … "attributes": {"type": "object", "properties": {"description": {"type": "string"}, "locale": {"type": "string"}, "keywords": {"type": "string"}, "marketingUrl": {"type": "string", "format": "uri"}, "promotionalText": {"type": "string"}, "supportUrl": {"type": "string", "format": "uri"}, "whatsNew": {"type": "string"}}}`
- `"AppInfoLocalization" … "properties": {"locale": {"type": "string"}, "name": {"type": "string"}, "subtitle": {"type": "string"}, "privacyPolicyUrl": {"type": "string"}, "privacyChoicesUrl": {"type": "string"}, "privacyPolicyText": {"type": "string"}}`

Transferable rule / negative finding: The official ASC API spec defines these fields as plain `string` with **no `maxLength` or `maxItems` constraints** — so the API will not tell you the 30/100/170/4000 limits; App Store Connect Help is the only authoritative numeric source. Do not cite the API docs for character limits.

## Failed URLs and why

| URL | Result | Why |
| --- | --- | --- |
| https://developer.apple.com/help/app-store-connect/manage-app-information/add-a-subtitle | curl 200 but **soft 404** | Returned the 82 KB page-not-found shell (`/pagenotfound/scripts/page-not-found.js`); Jina rendered only nav/footer, no article body. The page does not exist at this path. |
| https://developer.apple.com/help/app-store-connect/manage-app-information/ | curl 200 but **soft 404** | Same 82 KB not-found shell. |
| https://developer.apple.com/help/app-store-connect/manage-app-information/add-app-platforms-or-versions | curl 200 but **soft 404** | Same shell; correct path is `/create-an-app-record/add-platforms`. |
| https://developer.apple.com/help/app-store-connect/reference/app-store-connect-api-changes | curl 200 but **soft 404** | Same 82 KB shell; no such reference page. |
| https://developer.apple.com/help/app-store-connect/sitemap.xml | **404** | No sitemap. | 
| https://developer.apple.com/help/app-store-connect/manage-app-information/add-a-subtitle.json and `/index.json` | **404** | No per-page JSON endpoint; ASC Help has no public data API. |
| https://developer.apple.com/tutorials/data/documentation/appstoreconnectapi/appinfoupdatecreaterequest/data-data.dictionary/attributes-data.dictionary.json | **404** | Wrong synthesized path for the nested attributes dictionary. |
| https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-store-information/ | curl 200, real content (373,812 bytes) | **Not a failure — correction:** the working path is `/manage-app-information/localize-app-information` (no `-store`, no trailing slash). Both resolve to real rendered content; the canonical nav link is the shorter one. |
| https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.json | **300** (multiple choices → HTML) | Only the `.zip` form is served. |

Method notes for reuse:
- **ASC Help pages are server-rendered at ~376 KB and are fully readable by `curl` with a browser User-Agent** — 200 + large size is the tell. A ~82 KB response with 200 is a soft 404 and must be discarded.
- `developer.apple.com/app-store/*` marketing pages and the Review Guidelines are also static and readable by `curl`; watch for `&nbsp;` between a number and the word “characters”, which breaks naive greps.
- `developer.apple.com/documentation/*` (DocC) exposes clean JSON at `https://developer.apple.com/tutorials/data/documentation/<framework>/<symbol>.json`, but nested attribute dictionaries 404 — prefer the ASC Help pages.
- `ads.apple.com` is JS-rendered; use the Jina reader (`https://r.jina.ai/<url>`).
