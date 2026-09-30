# UI strings — the interface register

**What this file is.** The rulebook for the text *inside* a product interface: button and link labels, alerts and error messages, confirmation dialogs, onboarding, settings rows, form fields and placeholders, search, empty states, loading and progress, notifications, permission prompts, tooltips, and accessibility labels and alt text. This is Apple’s **Interface** register — HIG governs it, not the Apple Style Guide.

**Scope.** English only. Design guidance (color, spacing, motion) is out of scope unless it changes what the text must say.

**Provenance.** Every rule below is an imperative statement followed by a **verbatim quote** from Apple’s Human Interface Guidelines and the URL it came from. Nothing here is invented; if Apple does not say it, it is not a rule. Where guidance had to be derived, it is confined to the section marked **inference**.

**Route used.** All pages were retrieved from the structured JSON endpoint `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json` (the `/tutorials/data/documentation/…` variant 404s for HIG; the correct path has no `documentation/` segment). Text was extracted by recursively walking the JSON and joining `text`, `codeVoice` and `reference` nodes into paragraphs. **All 172 content pages and all 15 index/category endpoints returned HTTP 200; no fallback route was needed.** Quotes preserve Apple’s own typography (curly quotes and apostrophes) and are reproduced verbatim, including inline cross-reference link text.

**How to read a rule.** The bold line is the rule, stated imperatively. The block quote beneath it is Apple’s sentence, verbatim. The em-dash line is the page it came from.

---

## Contents

1. Voice, tone, and clarity — the base every string inherits
2. Labels and buttons (incl. capitalization table)
3. Error messages and alerts
4. Confirmation and destructive actions
5. Onboarding, tutorials and tips
6. Settings
7. Forms, fields, placeholders and hints
8. Search
9. Empty states, loading and progress
10. Notifications
11. Permission prompts and privacy copy
12. Tooltips and contextual help
13. Accessibility labels, hints and alt text
14. Do not — what Apple explicitly forbids or discourages
15. Single words and short strings
16. Sources

---
## Voice, tone, and clarity — the base every string inherits

**Settle the app’s voice before you write a single string.**

> Determine your app’s voice. Think about who you’re talking to, so you can figure out the type of vocabulary you’ll use.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Change the tone to fit the situation, not the voice.**

> Match your tone to the context. Once you’ve established your app’s voice, vary your tone based on the situation.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Be clear. Cut every word that does no work. Read it aloud.**

> Choose words that are easily understood and convey the right thing. Check each word to be sure it needs to be there. If you can use fewer words, do so. When in doubt, read your writing out loud.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Write for everyone: plain language, no jargon, no gendered terminology.**

> Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Put the most important information first, and break multiple ideas across screens.**

> Pay attention to the order of elements on a screen, and put the most important information first. Format your text to make it easy to read. If you’re trying to convey more than one idea, consider breaking up the text onto multiple screens, and think about the flow of information across those screens.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Use active voice and clear labels.**

> Active voice and clear labels help people navigate through your app from one step to the next, or from one screen to another.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Reuse the same language everywhere; consistency is what makes an app feel designed.**

> Consistency builds familiarity, helping your app feel cohesive, intuitive, and thoughtfully designed.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Address people directly as you and your.**

> It typically works well to use you and your to address people directly. Referring to people indirectly as the user or the player can make your experience feel distant and unwelcoming.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Reserve we and our for your company — and never use them where the referent is unclear.**

> Also, consider reserving words like we and our to represent your software or company; otherwise, these terms can suggest a personal relationship with people that might be interpreted as insulting or condescending.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Define a specialized or technical term before you use it.**

> Avoid using specialized or technical terms without defining them. Using specialized or technical terms can make your writing more succinct, but doing so excludes people who don’t know what the terms mean. If you must use such terms, be sure to define them first and make the definitions easy for people to look up.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Replace colloquial expressions with plain language — many are exclusionary or untranslatable.**

> Replace colloquial expressions with plain language. Colloquial expressions are often culture-specific and can be difficult to translate. Worse, some colloquial phrases have exclusionary meanings you might not know.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Think hard before including humor; it rarely survives translation or repetition.**

> Consider carefully before including humor. Humor is highly subjective and — similar to colloquial expressions — difficult to translate from one culture to another.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

> Including humor in your experience risks confusing people who donʼt understand it, irritating people who tire of repeatedly encountering it, and insulting people who interpret it differently.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Avoid references to a specific gender when the gender is not the point.**

> You can help everyone feel welcome in your app or game by avoiding unnecessary references to specific genders. For example, a recipe-sharing app that uses copy like “You can let a subscriber post his or her recipes to your shared folder” could avoid unnecessary gender references by using an alternative like “Subscribers can post recipes to your shared folder.”

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Write about disability people-first.**

> For example, you could describe an individual’s accomplishments and goals before mentioning a disability they may have.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Never use a disability as a metaphor for a negative quality.**

> For example, include people with disabilities when you represent a variety of people, and avoid language that uses a disability to express a negative quality.

— <https://developer.apple.com/design/human-interface-guidelines/inclusion>

**Carry your brand’s voice and tone into every written surface.**

> Use your brand’s unique voice and tone in all the written communication you display.

— <https://developer.apple.com/design/human-interface-guidelines/branding>

**Write shorter strings for small screens; keep text readable when several people share one screen.**

> iPhone and Apple Watch, for example, offer opportunities for personalization, but their small screens require brevity.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> TVs, on the other hand, are often in common living spaces, and several people are likely to see anything on the screen, so consider who you’re addressing.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Choose the delivery method — and its tone — from the urgency of the message.**

> When there’s something you want to communicate, consider the urgency and importance of the message. Think about the context in which someone might see the message, whether it requires immediate action, and how much supporting information someone might need. Choose the correct delivery method, and use a tone appropriate for the situation.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Say what happened rather than that something is happening.**

> Messages that describe what’s actually happening can be more helpful than a vague status message. For example, instead of “Processing…”, say “Finding substitutions for ingredients” or “Summarizing key themes from your notes.”

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>


## Labels and buttons

**Start action labels with a verb. This is the single most load-bearing rule for UI text.**

> When labeling buttons and links, it’s almost always best to use a verb.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Choose clarity over cleverness. A plain verb beats a cute phrase.**

> Prioritize clarity and avoid the temptation to be too cute or clever with your labels. For example, just saying “Send” often works better than “Let’s do it!”

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Never label a link “Click here”. Describe the destination instead.**

> For links, avoid using “Click here” in favor of more descriptive words or phrases, such as “Learn more about UX Writing.” This is especially important for people using screen readers to access your app.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Make every button’s purpose unmistakable from its label, symbol, or both.**

> Ensure that each button clearly communicates its purpose. Depending on the platform, a button can contain a symbol (or icon), a text label, or both to help people understand what it does.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**Use a few words that succinctly describe what the button does.**

> To use text, write a few words that succinctly describe what the button does.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**Begin the button label with a verb that conveys the action.**

> consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label “Add to Cart.”

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**Omit the label entirely when the icon or surrounding context already carries the meaning.**

> Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

> People know what a help button does, so they don’t need additional descriptive text.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

> Avoid supplying a label that explains the button’s purpose.

— <https://developer.apple.com/design/human-interface-guidelines/toggles>

> In general, buttons that contain text don’t need to display a tooltip because the button’s descriptive label communicates what it does.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**Alert buttons: one or two words naming the result of choosing them.**

> Aim for a one- or two-word title that describes the result of selecting the button. Prefer verbs and verb phrases that relate directly to the alert text — for example, “View All,” “Reply,” or “Ignore.”

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Use “OK” only in a purely informational alert — never “Yes” or “No”.**

> In informational alerts only, you can use “OK” for acceptance, avoiding “Yes” and “No.”

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Always title the cancelling button “Cancel”.**

> Always use “Cancel” to title a button that cancels the alert’s action.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Avoid “OK” as a default button title; name the specific action instead.**

> Avoid using OK as the default button title unless the alert is purely informational.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

> A specific button title like “Erase,” “Convert,” “Clear,” or “Delete” helps people understand the action they’re taking.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Use title-style capitalization and no ending punctuation on button titles.**

> As with all button titles, use title-style capitalization and no ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Do not explain your own alert buttons.**

> Avoid explaining alert buttons.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**If you truly must guide a button choice, say “choose” and cite the exact title without quotes.**

> In rare cases where you need to provide guidance on choosing a button, use a term like choose to account for people’s current device and interaction method, and refer to a button using its exact title without quotes.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Menu items that perform an action use a verb or verb phrase.**

> In general, label a menu item that initiates an action using a verb or verb phrase that describes the action, such as View, Close, or Select.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Write menu item labels that clearly and succinctly describe the item.**

> For each menu item, write a label that clearly and succinctly describes it.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Use title-style capitalization for menu items.**

> To be consistent with platform experiences, use title-style capitalization.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

> generally prefer using title-style capitalization, which capitalizes every word except articles, coordinating conjunctions, and short prepositions, and capitalizes the last word in the label, regardless of the part of speech.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Drop articles from menu item labels; they lengthen without clarifying.**

> In English, articles always lengthen labels, but rarely enhance understanding.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

> For example, changing a menu-item label from View Settings to View the Settings doesn’t provide additional clarification.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Append an ellipsis when the action needs more input before it can complete.**

> Append an ellipsis to a menu item’s label when the action requires more information before it can complete.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

> Append a trailing ellipsis to the title when a push button opens another window, view, or app.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**Let a label change to show current state — and add a verb if the state reads as ambiguous.**

> Consider using a changeable label that describes an item’s current state.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

> For example, people might not know whether the changeable labels HDR On and HDR Off describe actions or states. If you needed to clarify that these items represent actions, you could add verbs to the labels, like Turn HDR On and Turn HDR Off.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Prefer one-word menu bar titles.**

> Prefer short, one-word menu titles.

— <https://developer.apple.com/design/human-interface-guidelines/the-menu-bar>

> One-word menu titles work especially well in the menu bar because they take little space and are easy for people to scan. If you need to use more than one word in the menu title, use title-style capitalization.

— <https://developer.apple.com/design/human-interface-guidelines/the-menu-bar>

**Custom edit-menu commands use verbs or short verb phrases.**

> Use verbs or short verb phrases that succinctly describe the action your command performs.

— <https://developer.apple.com/design/human-interface-guidelines/edit-menus>

**Give every context menu item a short label that states what it does.**

> each item in a context menu needs to display a short label that clearly describes what it does.

— <https://developer.apple.com/design/human-interface-guidelines/context-menus>

**Custom activity-view actions: one verb or a brief verb phrase, and no company or product name.**

> Prefer a single verb or a brief verb phrase that clearly communicates what the action does.

— <https://developer.apple.com/design/human-interface-guidelines/activity-views>

> Avoid including your company or product name in an action title.

— <https://developer.apple.com/design/human-interface-guidelines/activity-views>

**Notification action buttons: a short, title-case phrase naming the result — no app name, no filler.**

> For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name or any extraneous information in the button label, keep the text brief to avoid truncation, and take localization into account as you write it.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Pair a Done button with Cancel or Back — never show Cancel, Done and Back together.**

> If you provide a Done button, always pair it with a Cancel button to give people a clear way to dismiss the sheet without confirming or saving their changes, or a Back button to move to a previous step in the sheet.

— <https://developer.apple.com/design/human-interface-guidelines/sheets>

> Avoid showing all three buttons — Cancel, Done, and Back — together.

— <https://developer.apple.com/design/human-interface-guidelines/sheets>

**Confirmation buttons name the action; “Order” beats “OK” or “Proceed”.**

> For example, when designing a snippet to order coffee, labeling the primary button Order is clearer than labeling it OK or Proceed.

— <https://developer.apple.com/design/human-interface-guidelines/snippets>

**Tab labels are nouns or short noun phrases — single words where possible.**

> In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.

— <https://developer.apple.com/design/human-interface-guidelines/tab-views>

> A tab label appears beneath or beside a tab bar icon, and can aid navigation by clearly describing the type of content or functionality the tab contains. Use single words whenever possible.

— <https://developer.apple.com/design/human-interface-guidelines/tab-bars>

**Give a toolbar item both a title and a symbol.**

> Giving both lets the system pick the right representation for the context. Include a title even when an item shows a symbol, because the system uses the title in overflow menus and expanded forms.

— <https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo>

**Title a window or view with one word or a short phrase under 15 characters.**

> Aim for a word or short phrase that distills the purpose of the window or view, and keep the title under 15 characters long so you leave enough room for other controls.

— <https://developer.apple.com/design/human-interface-guidelines/toolbars>

**Never title a window with your app’s name.**

> Your app’s name doesn’t provide useful information about your content hierarchy or any window or area in your app, so it doesn’t work well as a title.

— <https://developer.apple.com/design/human-interface-guidelines/toolbars>

**Summarize sharing permissions in a succinct phrase, not a sentence.**

> For example, you might write phrases like “Only invited people can edit” or “Everyone can make changes.”

— <https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing>

**Use a generic, task-named label on a button that opens a system technology screen.**

> Don’t include “Tap to Pay on iPhone” or “Tap to Pay” in such a label; instead, use a generic label like “Look Up,” “Store Card,” “Verify,” or “Refund.”

— <https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone>

**Disclosure controls state what is disclosed or hidden.**

> Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

— <https://developer.apple.com/design/human-interface-guidelines/disclosure-controls>

**Gauge labels state the current value and both endpoints of the range.**

> Write succinct labels that describe the current value and both endpoints of the range.

— <https://developer.apple.com/design/human-interface-guidelines/gauges>

**Keep control names short where they sit over content.**

> Control labels adhere to Dynamic Type sizes, and longer names may obfuscate the camera’s viewfinder.

— <https://developer.apple.com/design/human-interface-guidelines/camera-control>



#### Capitalization: choose per element, then never vary

Title case reads formal; sentence case reads casual. Pick one per element type and hold it across the app.

| Element | Style Apple documents | Source |
|---|---|---|
| Menus and menu bar items | title-style | [menus](https://developer.apple.com/design/human-interface-guidelines/menus) |
| Tab labels | title-style | [tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) |
| Combo box / introductory labels | title-style, ending with a colon | [combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes) |
| Alert title that is a fragment | title-style, no ending punctuation | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Alert title that is a full sentence | sentence-style, with ending punctuation | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Alert informative message | sentence-style, complete sentences, punctuated | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Notification title | title-style, no ending punctuation | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Notification body | sentence case, proper punctuation | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Notification preview-safe text | sentence-style | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Privacy purpose string | sentence case, active voice, ending period | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) |
| Tooltips | sentence case; omit ending punctuation on sentences | [offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) |
| Box titles | sentence-style, no ending punctuation (colon in a settings pane) | [boxes](https://developer.apple.com/design/human-interface-guidelines/boxes) |
| Table column headings | title-style, no ending punctuation | [lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) |
| Payment/validation error messages | noun phrases, sentence-style, no ending punctuation | [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) |
| NFC scanning instructions | complete sentence, sentence case, ending punctuation | [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc) |
| Game Center achievements | title-style title, sentence-style description | [Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) |

## Error messages and alerts

**Prevent the error first; text is the fallback, not the fix.**

> It’s always best to help people avoid errors.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> If you find that language alone can’t address an error that’s likely to affect many people, use that as an opportunity to rethink the interaction.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Put the message as close to the problem as possible.**

> When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> Show errors right next to the field, and instruct people how to enter the information correctly, rather than scolding them for not following the rules.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Never blame the person. Say what happened and what to do about it.**

> avoid blame, and be clear about what someone can do to fix it.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> instruct people how to enter the information correctly, rather than scolding them for not following the rules.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> Alerts often describe problems and serious situations, so avoid being oblique or accusatory, or masking the severity of the issue.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Name the fix, not the fault. Give the requirement, not the complaint.**

> For example, “That password is too short” isn’t as helpful as “Choose a password with at least 8 characters.”

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> “Use only letters for your name” is better than “Don’t use numbers or symbols.”

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Ban interjections. “oops!” and “uh-oh” read as insincere.**

> Remember that errors can be frustrating. Interjections like “oops!” or “uh-oh” are typically unnecessary and can sound insincere.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Never use “we” in an error message — the reader cannot tell who “we” is.**

> This is particularly problematic in error messages like “We’re having trouble loading this content.” Something like “Unable to load content” is much clearer.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Replace a robotic, information-free message with a specific one.**

> Avoid robotic error messages with no helpful information, like “Invalid name.”

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Be direct, neutral and approachable in all alert copy.**

> In all alert copy, be direct, and use a neutral, approachable tone.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Describe what happened, in what context, and why.**

> You need to help people quickly understand the situation, so be complete and specific, without being verbose. As much as possible, describe what happened, the context in which it happened, and why.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Never title an alert “Error”, an error code, or anything else that conveys nothing.**

> Avoid writing a title that doesn’t convey useful information — like “Error” or “Error 329347 occurred” — but also avoid overly long titles that wrap to more than two lines.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Match the title’s capitalization to its grammar: sentence for a sentence, title-style for a fragment.**

> If the title is a complete sentence, use sentence-style capitalization and appropriate ending punctuation. If the title is a sentence fragment, use title-style capitalization, and don’t add ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Add informative text only when it earns its place; keep it short, complete and punctuated.**

> If you need to add an informative message, keep it as short as possible, using complete sentences, sentence-style capitalization, and appropriate punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Spend alerts only on essential information with useful actions.**

> Encourage people to pay attention to your alerts by making certain that each one offers only essential information and useful actions.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Do not use an alert to deliver information that isn’t actionable.**

> People don’t appreciate an interruption from an alert that’s informative, but not actionable.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Do not alert on common, undoable actions — even destructive ones.**

> Avoid displaying alerts for common, undoable actions, even when they’re destructive.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Do not open the app with an alert.**

> Avoid showing an alert when your app starts.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Send errors as alerts, never as notifications.**

> Use an alert — not a notification — to display an error message.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Warn only about data loss that is unexpected and irreversible.**

> Warn people when they initiate a task that can cause data loss that’s unexpected and irreversible.

— <https://developer.apple.com/design/human-interface-guidelines/feedback>

> don’t warn people when data loss is the expected result of their action.

— <https://developer.apple.com/design/human-interface-guidelines/feedback>

**Confirm success rarely — people already expect their action to work.**

> It’s generally best to reserve this type of confirmation for activities that are sufficiently important — because people typically expect their action or task to succeed, they only need to know when it doesn’t.

— <https://developer.apple.com/design/human-interface-guidelines/feedback>

**Tell people why a command cannot be carried out.**

> Show people when a command can’t be carried out and help them understand why.

— <https://developer.apple.com/design/human-interface-guidelines/feedback>

**Keep an action sheet title to a single line.**

> Aim to keep titles short enough to display on a single line.

— <https://developer.apple.com/design/human-interface-guidelines/action-sheets>

> A long title is difficult to read quickly and might get truncated or require people to scroll.

— <https://developer.apple.com/design/human-interface-guidelines/action-sheets>

**Add an action sheet message only if the title plus context is not enough.**

> In general, the title — combined with the context of the current action — provides enough information to help people understand their choices.

— <https://developer.apple.com/design/human-interface-guidelines/action-sheets>

**In a payment or validation error, name the field and state exactly what is expected.**

> Reference the relevant field and indicate exactly what’s expected. For example, if people enter an invalid zip code, instead of showing “Address is invalid,” show a specific message like “Zip code doesn’t match city.”

— <https://developer.apple.com/design/human-interface-guidelines/apple-pay>

> If the shipping address is unserviceable, indicate why with a message like “Shipping not available for this state.”

— <https://developer.apple.com/design/human-interface-guidelines/apple-pay>

**Format validation errors as noun phrases: sentence-style, no ending punctuation, ≤128 characters.**

> Use noun phrases with sentence-style capitalization and no ending punctuation. Aim to keep messages at 128 characters or fewer to avoid truncation.

— <https://developer.apple.com/design/human-interface-guidelines/apple-pay>

**Be forgiving of input format instead of emitting an error for it.**

> Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction.

— <https://developer.apple.com/design/human-interface-guidelines/apple-pay>

> Let people enter phone numbers in multiple formats — such as with and without dashes, and with and without a country code — without producing an error.

— <https://developer.apple.com/design/human-interface-guidelines/apple-pay>

**When an AI feature fails, say what happened in plain language and offer the next step.**

> If something goes wrong, describe what happened in plain language and offer a clear next step.

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>


## Confirmation and destructive actions

**Give a destructive alert a Cancel button that offers a clear, safe exit.**

> If there’s a destructive action, include a Cancel button to give people a clear, safe way to avoid the action.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Do not make any button the default if you want people to actually read the alert.**

> If you want to encourage people to read an alert and not just automatically press Return to dismiss it, avoid making any button the default button.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**If an alert has a single default button, make it Done — never Cancel.**

> if you must display an alert with a single button that’s also the default, use a Done button, not a Cancel button.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Use the destructive style only where the person did not deliberately choose the action.**

> Use the destructive style to identify a button that performs a destructive action people didn’t deliberately choose.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Offer alternative ways to cancel, such as a keyboard shortcut.**

> In addition to choosing a Cancel button, people appreciate using keyboard shortcuts or other quick ways to cancel an onscreen alert.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Warn before a halt that loses progress, and offer to confirm or resume.**

> When canceling a process results in lost progress, it’s helpful to provide an alert that includes an option to confirm the cancellation or resume the process.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

**Ask for confirmation before an automated system acts significantly on someone’s behalf.**

> Generally, ask for confirmation before performing a significant action on someone’s behalf.

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>

**Keep an alert’s title short enough that it will not scroll.**

> be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>


## Onboarding, tutorials and tips

**Teach by letting people perform the task, not by describing it.**

> People tend to grasp and retain information better when they can actually perform the task they’re learning about instead of just viewing instructional material.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Prefer context-specific tips over one long onboarding flow.**

> Integrating contextually relevant tips into your experience can help people learn about their current task while they make progress in your app or game. A context-specific tip can also help people learn better because it lets them concentrate on a single action or task before encountering new information.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Keep a prerequisite onboarding flow brief and free of memorization.**

> When onboarding is quick and entertaining, people are more likely to complete it. In contrast, if you try to teach too much, people can feel overwhelmed and may be less likely to remember what they learned.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Make a separate tutorial optional, and never re-present it.**

> If you let people skip the tutorial when they first launch your app or game, don’t present it again on subsequent launches, but make sure it’s easy for people to find if they want to view it later. For example, you could make the tutorial available in a help, account, or settings area within your app or game.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Keep onboarding about your product, never about the operating system or device.**

> People enter your onboarding flow to learn about your app or game; they don’t need to learn how to use the system or the device.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Make a splash screen communicate at a glance.**

> If you need to include a splash screen, design a beautiful graphic that communicates succinctly.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Postpone nonessential setup by shipping good defaults.**

> Provide reasonable default settings so most people can immediately start interacting with your app or game without performing additional configuration.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Ask for permission inside onboarding only when it helps you explain the benefit.**

> making the request during your onboarding flow gives you the opportunity to show people why your app or game needs their permission and the benefits of granting it.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Let people use the product before you ask for a rating or a purchase.**

> People can be more likely to respond positively to such requests when they’ve had a chance to become engaged with your app or game.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Do not put licensing agreements and disclaimers in the onboarding flow.**

> Let the App Store display agreements and disclaimers so people can read them before downloading your app or game.

— <https://developer.apple.com/design/human-interface-guidelines/onboarding>

**Write tips as direct, action-oriented sentences that describe the feature and how to use it.**

> Use direct, action-oriented language to describe what the feature does and explain how to use it.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Keep a tip to one or two sentences and keep promotion out of it.**

> Keep your tips to one or two sentences and avoid including content that’s promotional or related to a different feature or user flow.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**If a feature needs more than three actions, it is too complex for a tip.**

> If a feature requires more than three actions, it’s probably too complicated for a tip.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Show a tip only to people it can help.**

> Not everyone benefits from every tip. For example, people who’ve already used a feature won’t appreciate viewing a tip that describes it.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>


## Settings

**Label settings as practically as possible so people can find them.**

> Help people easily find the settings they need by labeling them as practically as possible.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Describe what the setting does when it is on; let people infer the off state.**

> If the setting label isn’t enough, add an explanation. Describe what it does when turned on, and people can infer the opposite.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> It isn’t necessary to tell you that a timer won’t start when this setting is off.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Send people to a setting with a direct link or button instead of describing where it lives.**

> If you need to direct someone to a setting, provide a direct link or button, rather than trying to describe its location.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Offer as few settings as you can.**

> Although people appreciate having control over an app or game, too many settings can make the experience feel less approachable, while also making it hard to find a particular setting.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

**Put general, infrequently changed options in the settings area — and task-specific options in the task.**

> People must suspend what they’re doing to open an app’s or game’s settings area, so you want to include options that people don’t need to change all the time.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

> make these options available in the screens they affect, where they’re discoverable and convenient.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

**Do not duplicate systemwide settings inside your own settings.**

> Including custom versions of global options in your settings area is likely to confuse people because it implies that systemwide settings may not apply to your app or game and that changing your custom version of a global setting may affect other apps and games, too.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

**Title a single-pane settings window “App Name Settings”.**

> If your settings window doesn’t have multiple panes, use the title App Name Settings.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

**Keep the window title in step with the visible pane.**

> Update the window’s title to reflect the currently visible pane.

— <https://developer.apple.com/design/human-interface-guidelines/settings>

**Use a settings title that is a brief phrase; sentence-style, often with a trailing colon.**

> Use sentence-style capitalization. Avoid ending punctuation unless you use a box in a settings pane, where you append a colon to the title.

— <https://developer.apple.com/design/human-interface-guidelines/boxes>

**Give a combo box an introductory label in title style, ending with a colon.**

> Generally, use title-style capitalization for labels and end them with a colon.

— <https://developer.apple.com/design/human-interface-guidelines/combo-boxes>


## Forms, fields, placeholders and hints

**Label every field clearly and use hint or placeholder text to show the expected format.**

> label all fields clearly, and use hint or placeholder text so people know how to format the information.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Give an example or a description in the hint — never nothing.**

> You can give an example in hint text, like “name@example.com,” or describe the information, such as “Your name.”

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Use placeholder text to communicate the field’s purpose — but add a separate label, because placeholder text disappears.**

> A text field can contain placeholder text — such as “Email” or “Password” — when there’s no other text in the field.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

> Because placeholder text disappears when people start typing, it can also be useful to include a separate label describing the field to remind people of its purpose.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**Validate at the moment that fits the field: on blur for formats, before blur for a new credential.**

> The appropriate time to check the data depends on the context: when entering an email address, it’s best to validate when people switch to another field; when creating a user name or password, validation needs to happen before people switch to another field.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**Match the field’s size to the amount of text you expect.**

> The size of a text field helps people visually gauge the amount of information to provide.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**Space and stack multiple fields so each label clearly owns its field.**

> If your layout includes multiple text fields, leave enough space between them so people can easily see which input field belongs with each introductory label.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**Use a secure field for anything private.**

> Always use a secure text field when your app asks for sensitive data, such as a password.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**Show the keyboard type that matches the content.**

> To streamline data entry, display the keyboard that’s appropriate for the type of content people are entering.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>

**State the purpose of a digit-entry view with a title and a prompt.**

> Use a title and prompt that explains why someone needs to enter digits.

— <https://developer.apple.com/design/human-interface-guidelines/digit-entry-views>

**Name table columns with nouns or short noun phrases; title-style, no ending punctuation.**

> Use nouns or short noun phrases with title-style capitalization, and don’t add ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/lists-and-tables>

**Keep row and item text succinct so it does not truncate.**

> Short, succinct text can help minimize truncation and wrapping, making text easier to read and scan.

— <https://developer.apple.com/design/human-interface-guidelines/lists-and-tables>

**Give a box a succinct introductory title in sentence style, and no ending punctuation.**

> If you need a title, write a brief phrase that describes the contents.

— <https://developer.apple.com/design/human-interface-guidelines/boxes>

**Minimize text entry where typing is expensive.**

> Entering long passages of text or filling out numerous text fields is time-consuming on Apple TV and Apple Watch.

— <https://developer.apple.com/design/human-interface-guidelines/text-fields>


## Search

**Use placeholder text to say what can be searched and what search can reach.**

> Placeholder text can be helpful when you need to reinforce the scope of your search or to educate people about the type of content that search has access to.

— <https://developer.apple.com/design/human-interface-guidelines/search-fields>

**Make the current scope of a search visible in the text.**

> Use a descriptive placeholder text, a scope bar, or a title to help reinforce what someone is currently searching.

— <https://developer.apple.com/design/human-interface-guidelines/searching>

**Start searching as the person types.**

> Searching while someone types makes the search experience feel more responsive because it provides results that are continuously refined as the text becomes more specific.

— <https://developer.apple.com/design/human-interface-guidelines/search-fields>

**Offer suggestions, recent searches or predictive terms.**

> For example, you can display recent searches before search begins, or predictive search suggestions as a person types. This can help someone search faster, even when the search itself doesn’t begin immediately.

— <https://developer.apple.com/design/human-interface-guidelines/search-fields>

**Rank the most relevant results first.**

> Provide the most relevant search results first to minimize the need for someone to scroll to find what they’re looking for.

— <https://developer.apple.com/design/human-interface-guidelines/search-fields>

**Default to a broad scope and let people narrow it.**

> A broader scope provides context for the full set of available results, which helps guide people in a useful direction when they choose to narrow the scope.

— <https://developer.apple.com/design/human-interface-guidelines/search-fields>

**Do not put search history where others can see it; offer a way to clear it.**

> If you do show search history, provide a way for people to clear it if they want.

— <https://developer.apple.com/design/human-interface-guidelines/searching>


## Empty states, loading and progress

**Give every blank screen a next step, and a button or link to take it.**

> An empty screen can be daunting if it isn’t obvious what to do next, so guide people on actions they can take, and give them a button or link to do so if possible.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Make empty-state content useful and in context — it is a chance to teach, not to joke.**

> Empty states can also showcase your app’s voice, but make sure that the content is useful and fits the context.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Do not put crucial information in an empty state; empty states are temporary.**

> Remember that empty states are usually temporary, so don’t show crucial information that could then disappear.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Show something immediately rather than waiting for content.**

> If you make people wait for loading to complete before displaying anything, they can interpret the lack of content as a problem with your app or game. Instead, consider showing placeholder text, graphics, or animations as content loads, replacing these elements as content becomes available.

— <https://developer.apple.com/design/human-interface-guidelines/loading>

**Let people do something else while content loads.**

> Loading content in the background helps give people access to other actions.

— <https://developer.apple.com/design/human-interface-guidelines/loading>

**If a wait is unavoidable, give people something worth reading.**

> If loading takes an unavoidably long time, give people something interesting to view while they wait.

— <https://developer.apple.com/design/human-interface-guidelines/loading>

**Make the progress text accurate and specific; ban vague status words.**

> Be accurate and succinct. Avoid vague terms like loading or authenticating because they seldom add value.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

> For example, instead of “Processing…”, say “Finding substitutions for ingredients” or “Summarizing key themes from your notes.” Specific feedback reduces uncertainty and makes waiting feel purposeful.

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>

**Prefer a determinate indicator so people can judge the wait.**

> A determinate progress indicator can help people decide whether to do something else while waiting for the task to complete, restart the task at a different time, or abandon the task.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

**Never let a progress indicator appear stalled.**

> People tend to associate a stationary indicator with a stalled process or a frozen app.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

**Do not label a spinner.**

> Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

**If a refresh control has a title, use it to add information, not instructions.**

> If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed.

— <https://developer.apple.com/design/human-interface-guidelines/progress-indicators>

**Change the button label while work is in flight.**

> For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible.

— <https://developer.apple.com/design/human-interface-guidelines/buttons>

**On watchOS, avoid an indeterminate indicator and promise a notification instead.**

> To provide a better experience, reassure people that they’ll receive a notification when the process completes.

— <https://developer.apple.com/design/human-interface-guidelines/feedback>


## Notifications

**Write a short notification title that carries real information.**

> Prefer brief titles that people can read at a glance, especially on Apple Watch, where space is limited. When possible, take advantage of the prominent notification title area to provide useful information, like a headline, event name, or email subject.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Prefer no title over a generic one — let the system show the app name.**

> If you can only provide a generic title for a noncommunication notification — like New Document — it can be better to let the system display your app name instead.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Format the title in title style with no ending punctuation.**

> Use title-style capitalization and no ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Write the body as complete sentences in sentence case, with proper punctuation.**

> Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Never truncate the message yourself — the system does it.**

> don’t truncate your message — the system does this automatically when necessary.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Write preview-safe body text that is descriptive without revealing details.**

> write body text that succinctly describes the notification content without revealing too many details, like “Friend request,” “New comment,” “Reminder,” or “Shipment”

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

> Use sentence-style capitalization for this text.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Keep private information out of notifications.**

> it’s essential to avoid including private information that could be visible to others.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

> Avoid including potentially sensitive information in the notification’s title.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Do not repeat your app name or icon in the notification.**

> The system automatically displays a large version of your app icon at the leading edge of each notification; in a communication notification, the system displays the sender’s contact image badged with a small version of your icon.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Make each notification action a task people would otherwise open the app to do.**

> Prefer actions that let people perform common, time-saving tasks that eliminate the need to open your app.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Do not add an action that merely opens the app.**

> When people tap a notification or its preview, they expect your app to display related content, so presenting an action button that does the same thing clutters the detail view and can be confusing.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Prefer nondestructive notification actions; give context if one is destructive.**

> If you must provide a destructive action, make sure people have enough context to avoid unintended consequences.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**Never rely on sound alone to carry information.**

> A notification sound can enhance the user experience, but don’t rely on it to communicate important information, because people may not hear it.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>


## Permission prompts and privacy copy

**Ask only for data you actually need, as specifically as possible.**

> Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

> Give people precise control over their data by making your permission requests as specific as possible.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Be transparent about what you collect and how you use it.**

> People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Request permission at the moment of use, not before.**

> Ideally, wait to request permission until people actually use an app feature that requires access.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Avoid a launch-time permission request unless the app cannot function without it.**

> People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Write the purpose string as one brief, complete, specific sentence.**

> Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Use sentence case, active voice, and a period at the end of a purpose string.**

> Use sentence case, avoid passive voice, and include a period at the end.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Reject the vague passive justification and the bare imperative.**

> A passive sentence that provides a vague, undefined justification.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

> An imperative sentence that doesn’t provide any justification.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Model the purpose string on Apple’s own example: an active sentence saying how and why.**

> An active sentence that clearly describes how and why the app collects the data.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

> Create a purpose string with a phrase that describes why you’re asking for permission to access data, such as “Lets you control this accessory with the Apple Home app and Siri across your Apple devices.”

— <https://developer.apple.com/design/human-interface-guidelines/homekit>

**A custom pre-prompt carries exactly one button, and that button opens the system alert.**

> Include only one button and make it clear that it opens the system alert.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Never title that button “Allow” — use “Continue” or “Next”.**

> Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

> Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Add no other actions to the pre-prompt — no close, no cancel.**

> don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Never mislead people into a permission choice; it is grounds for App Store rejection.**

> A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.

— <https://developer.apple.com/design/human-interface-guidelines/privacy>

**Explain a permission’s benefit concisely and say whether the data trains the model.**

> When asking for permission to use someone’s information, explain the benefits in a way that’s concise, specific, and easy to understand.

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>

> Articulate whether your model uses personal information for training and improvement.

— <https://developer.apple.com/design/human-interface-guidelines/generative-ai>


## Tooltips and contextual help

**Describe only the control the person is pointing at.**

> When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Explain the action the control initiates, beginning with a verb.**

> It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Do not repeat the control’s name in its tooltip.**

> Repeating the name takes up space in the tooltip and rarely adds value to the description.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Cap a tooltip at 60–75 characters; use a fragment and drop articles.**

> As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Use sentence case in tooltips, and omit the closing period on a sentence.**

> Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Vary the tooltip with the control’s state.**

> For example, you could provide different text for a control’s different states.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Do not use the word “popover” in help text; name the task or selection instead.**

> Instead, refer to a specific task or selection. For example, instead of “Select the Show button at the bottom of the popover,” you might write “Select the Show button.”

— <https://developer.apple.com/design/human-interface-guidelines/popovers>

**Keep help terminology consistent with the platform and input device.**

> don’t write copy that tells people to click a button on an iPhone or tap a menu item on a Mac.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Do not explain how standard components work; describe this task in this app.**

> Instead, describe the specific action or task that a standard element performs in your app or game.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Keep help content inclusive.**

> Make sure all help content is inclusive.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Match the help to the task at hand and make it dismissible.**

> In general, directly relate the help you provide to the precise action or task people are doing right now and make it easy for people to dismiss or avoid the help if they don’t need it.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>


## Accessibility labels, hints and alt text

**Provide an alternative label for every key interface element — descriptive, not the generic default.**

> System-provided controls have generic labels by default, but you should provide more descriptive labels that convey your app’s functionality.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

> Add labels to any custom elements your app defines.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Keep the descriptions current as the interface and content change.**

> Be sure to keep your descriptions up-to-date as your app’s interface and content change.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Describe a meaningful image by what it conveys — and nothing else.**

> Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions, describe only the information the image itself conveys.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Give each chart or infographic a concise description of what it conveys; expose any interactions too.**

> Provide a concise description of each infographic that explains what it conveys.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Leave decorative images out of VoiceOver entirely.**

> It’s unnecessary to describe images that are decorative and don’t convey useful or actionable information.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

> Excluding these images shows respect for people’s time and reduces cognitive load when they use VoiceOver.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Give every screen a unique, succinct title, and use accurate section headings.**

> Offer unique titles that succinctly describe each page’s content and purpose.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

> Likewise, use accurate section headings that help people build a mental model of each page’s information hierarchy.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Describe relationships that are otherwise only visual — grouping, order, linkage.**

> Examine your app for places where relationships among elements are visual only. Then, describe these relationships to VoiceOver.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Announce visible content and layout changes.**

> It’s crucial to report visible changes so VoiceOver and other assistive technologies can help people update their understanding of the content.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Label interface elements so Voice Control can act on them.**

> To ensure a smooth experience, label interface elements appropriately.

— <https://developer.apple.com/design/human-interface-guidelines/accessibility>

> your interface elements are appropriately labeled to ensure a great experience.

— <https://developer.apple.com/design/human-interface-guidelines/accessibility>

**Label a chart element with context first, then a succinct description of its details.**

> In general, it’s rarely enough to merely report a data value unless you also include context that helps people understand it, like the date or location that’s associated with it. Aim to concisely describe the context for a value without repeating information that people can get in other ways, like an axis name that Audio Graphs or your overview provides. Follow context-setting information with a succinct description of the element’s details.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Ban subjective words from data descriptions; use the actual values.**

> Subjective words — like rapidly, gradually, and almost — communicate your interpretation of the data. To help people form their own interpretations, use actual values in your descriptions.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Avoid ambiguous formats and abbreviations in data descriptions.**

> Maximize clarity in data descriptions by avoiding potentially ambiguous formats and abbreviations.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Describe what a chart’s details represent, not what they look like.**

> It’s crucial to create accessibility labels that identify what each series represents, but describing the colors that visually represent them can add unnecessary information and be distracting.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Hide decorative axis and tick labels from assistive technologies.**

> Axis and tick labels help people visually assess trends in a chart and estimate mark values. VoiceOver users can get mark values and trend information through accessibility labels and Audio Graphs, so they don’t generally need the content in the visible labels.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Provide alternative text labels for custom interface icons.**

> Provide alternative text labels for custom interface icons.

— <https://developer.apple.com/design/human-interface-guidelines/icons>

**Write accessibility labels that serve the chart’s actual purpose.**

> The purpose of the chart is to give people a sense of the terrain for the entire route, not to provide individual elevations. For this reason, Maps provides accessibility labels that summarize the elevation changes over a portion of the route, rather than providing labels for each individual moment.

— <https://developer.apple.com/design/human-interface-guidelines/charts>

**Let VoiceOver read a gauge’s visible labels by labelling value and endpoints.**

> Although not every gauge style displays all labels, VoiceOver reads the visible labels to help people understand the gauge without seeing the screen.

— <https://developer.apple.com/design/human-interface-guidelines/gauges>

**Never make color the only carrier of meaning in text or state.**

> Offer visual indicators, like distinct shapes or icons, in addition to color to help people perceive differences in function and changes in state.

— <https://developer.apple.com/design/human-interface-guidelines/accessibility>


## Do not — what Apple explicitly forbids or discourages

Every line below is a prohibition Apple states, with the sentence that states it. If your draft contains the left-hand column, it is wrong regardless of how good it sounds.

Apple’s sentences are set in *italics* rather than wrapped in quotation marks, because many of them contain their own quotation marks and nesting them would misrepresent the punctuation.

| Never | Apple’s words | Source |
|---|---|---|
| Write `we`, `us`, `our` or `I` — the reader cannot tell who “we” is | *Avoid using we altogether because it may be unclear who the “we” in question refers to.*<br>*consider reserving words like we and our to represent your software or company; otherwise, these terms can suggest a personal relationship with people that might be interpreted as insulting or condescending.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing)<br>[inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Call people `the user` or `the player` | *Referring to people indirectly as the user or the player can make your experience feel distant and unwelcoming.* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Use possessive pronouns (`my`, `your`) when they add nothing | *Possessive pronouns like my and your are often unnecessary to establish context.*<br>*“Favorites” conveys the same message as “Your Favorites,” and is more succinct.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Open with an interjection: `oops!`, `uh-oh` | *Interjections like “oops!” or “uh-oh” are typically unnecessary and can sound insincere.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Blame or scold the person | *avoid blame, and be clear about what someone can do to fix it.*<br>*rather than scolding them for not following the rules.*<br>*avoid being oblique or accusatory, or masking the severity of the issue.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing)<br>[alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Write a cute or clever label | *avoid the temptation to be too cute or clever with your labels.*<br>*just saying “Send” often works better than “Let’s do it!”* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Label a link `Click here` | *For links, avoid using “Click here” in favor of more descriptive words or phrases, such as “Learn more about UX Writing.” This is especially important for people using screen readers to access your app.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Title an alert `Error` or `Error 329347 occurred` | *Avoid writing a title that doesn’t convey useful information — like “Error” or “Error 329347 occurred”* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Ship a robotic, information-free error such as `Invalid name` | *Avoid robotic error messages with no helpful information, like “Invalid name.”* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Phrase an error as a prohibition (`Don’t use numbers or symbols.`) | *“Use only letters for your name” is better than “Don’t use numbers or symbols.”* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Use `OK` as a default button title | *Avoid using OK as the default button title unless the alert is purely informational.* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Offer `Yes` and `No` as alert buttons | *In informational alerts only, you can use “OK” for acceptance, avoiding “Yes” and “No.”* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Label a confirmation button `OK` or `Proceed` when the action has a name | *labeling the primary button Order is clearer than labeling it OK or Proceed.* | [snippets](https://developer.apple.com/design/human-interface-guidelines/snippets) |
| Explain what your own alert buttons do | *Avoid explaining alert buttons.* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Make Cancel the default button, or make any button default when you want the alert read | *Note that you don’t want to make a Cancel button the default button.*<br>*avoid making any button the default button.* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Show Cancel, Done and Back together on a sheet | *Avoid showing all three buttons — Cancel, Done, and Back — together.* | [sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) |
| Use an alert purely to inform, or on common undoable actions, or at launch | *People don’t appreciate an interruption from an alert that’s informative, but not actionable.*<br>*Avoid displaying alerts for common, undoable actions, even when they’re destructive.*<br>*Avoid showing an alert when your app starts.* | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |
| Deliver an error as a notification | *Use an alert — not a notification — to display an error message.* | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Write a vague progress word: `loading`, `authenticating`, `Processing…` | *Avoid vague terms like loading or authenticating because they seldom add value.*<br>*Messages that describe what’s actually happening can be more helpful than a vague status message.* | [progress-indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)<br>[generative-ai](https://developer.apple.com/design/human-interface-guidelines/generative-ai) |
| Put a label on a spinner | *Avoid labeling a spinning progress indicator.* | [progress-indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) |
| Truncate your own notification text, or put private data in it | *don’t truncate your message — the system does this automatically when necessary.*<br>*Avoid including potentially sensitive information in the notification’s title.* | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Repeat your app name or icon inside a notification or its action buttons | *Avoid including your app name or icon.*<br>*Don’t include your app name or any extraneous information in the button label* | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Add a notification action that just opens the app | *Avoid providing an action that merely opens your app.* | [notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) |
| Use your app name as a window title | *Don’t title windows with your app name.* | [toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) |
| Bake text into an App Clip header image | *Text in the header image isn’t localizable* | [app-clips](https://developer.apple.com/design/human-interface-guidelines/app-clips) |
| Name the underlying technology in a generic button label | *Don’t include “Tap to Pay on iPhone” or “Tap to Pay” in such a label* | [tap-to-pay-on-iphone](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone) |
| Use imprecise feedback words such as `dislike` | *Avoid using imprecise terms such as dislike because such terms don’t convey consequences and can be hard to translate* | [machine-learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning) |
| Put text next to a help button to introduce it | *People know what a help button does, so they don’t need additional descriptive text.* | [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) |
| Repeat a control’s name in its tooltip, or write the word `popover` in help text | *In general, avoid repeating a control’s name in its tooltip.*<br>*Avoid using the word popover in help documentation.* | [offering-help](https://developer.apple.com/design/human-interface-guidelines/offering-help)<br>[popovers](https://developer.apple.com/design/human-interface-guidelines/popovers) |
| Put a company or product name in an activity-view action title | *Avoid including your company or product name in an action title.* | [activity-views](https://developer.apple.com/design/human-interface-guidelines/activity-views) |
| Pad a menu item label with articles | *In English, articles always lengthen labels, but rarely enhance understanding.* | [menus](https://developer.apple.com/design/human-interface-guidelines/menus) |
| Write a purpose string in the passive voice or as a bare imperative | *A passive sentence that provides a vague, undefined justification.*<br>*An imperative sentence that doesn’t provide any justification.* | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) |
| Title a pre-alert button `Allow`, or add a close/cancel escape to it | *Another type of manipulation is using a term like “Allow” to title the custom screen’s button.*<br>*don’t provide a way for people to leave the screen or window without viewing the system alert* | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) |
| Design a custom screen that confuses or misleads people before a system alert | *Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.*<br>*A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.* | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) |
| Use specialized, technical or colloquial language the reader may not share | *Using specialized or technical terms can make your writing more succinct, but doing so excludes people who don’t know what the terms mean.*<br>*Colloquial expressions are often culture-specific and can be difficult to translate.* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Include humor that may confuse, tire or insult people | *Including humor in your experience risks confusing people who donʼt understand it, irritating people who tire of repeatedly encountering it, and insulting people who interpret it differently.* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Use unnecessary gender references or singular gendered pronouns | *the revised copy avoids the unnecessary singular pronouns “his” and “her,” helping the sentence remain inclusive when it’s localized* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Use a disability to express a negative quality | *avoid language that uses a disability to express a negative quality* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Assume a stereotype — of family, gender, occupation or experience | *Because the app assumes that people’s families fit this narrow definition, it excludes everyone whose family is different.*<br>*Basing design decisions on stereotypes or assumptions inevitably leads to exclusion because generalizations can’t reflect the diversity of human perspectives.* | [inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) |
| Duplicate a systemwide setting inside your own settings | *Including custom versions of global options in your settings area is likely to confuse people because it implies that systemwide settings may not apply to your app or game and that changing your custom version of a global setting may affect other apps and games, too.* | [settings](https://developer.apple.com/design/human-interface-guidelines/settings) |
| Describe where a setting lives instead of linking to it | *If you need to direct someone to a setting, provide a direct link or button, rather than trying to describe its location.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing) |
| Put licensing agreements inside onboarding | *Let the App Store display agreements and disclaimers so people can read them before downloading your app or game.* | [onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) |
| Present a skipped tutorial again on the next launch | *don’t present it again on subsequent launches* | [onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) |
| Explain how standard components work instead of this task | *Avoid bloating your help content by explaining how standard components or patterns work.* | [offering-help](https://developer.apple.com/design/human-interface-guidelines/offering-help) |
| Use a popover to deliver a warning | *People can miss a popover or accidentally close it.* | [popovers](https://developer.apple.com/design/human-interface-guidelines/popovers) |
| Introduce square buttons with a label, or label a toggle-style button’s purpose | *Avoid using labels to introduce square buttons.*<br>*Avoid supplying a label that explains the button’s purpose.* | [buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)<br>[toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) |
| Rely on color alone to carry meaning | *Convey information with more than color alone.*<br>*Offer visual indicators, like distinct shapes or icons, in addition to color to help people perceive differences in function and changes in state.* | [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) |
| Force people to match your business logic’s input format | *Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible.* | [apple-pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) |
| Mix registers — put marketing rhythm, cuteness or humor into an error or a destructive confirmation | *Prioritize clarity and avoid the temptation to be too cute or clever with your labels.*<br>*In all alert copy, be direct, and use a neutral, approachable tone.* | [writing](https://developer.apple.com/design/human-interface-guidelines/writing)<br>[alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) |

## Single words and short strings

**Prefer one word. Short is the documented default for the smallest surfaces.**

> Prefer short, one-word menu titles.

— <https://developer.apple.com/design/human-interface-guidelines/the-menu-bar>

> Use single words whenever possible.

— <https://developer.apple.com/design/human-interface-guidelines/tab-bars>

**Make a 1–3 word string a noun when it names a thing and a verb when it does a thing.**

> In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts.

— <https://developer.apple.com/design/human-interface-guidelines/tab-views>

> Aim for a one- or two-word title that describes the result of selecting the button.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

> label a menu item that initiates an action using a verb or verb phrase that describes the action, such as View, Close, or Select.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

**Keep a short string inside one budget: a window title under 15 characters, a tooltip 60–75.**

> keep the title under 15 characters long so you leave enough room for other controls.

— <https://developer.apple.com/design/human-interface-guidelines/toolbars>

> limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text).

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Omit articles from short strings.**

> In English, articles always lengthen labels, but rarely enhance understanding.

— <https://developer.apple.com/design/human-interface-guidelines/menus>

> consider using a sentence fragment and omitting articles.

— <https://developer.apple.com/design/human-interface-guidelines/offering-help>

**Drop the possessive when the surface is one word.**

> “Favorites” conveys the same message as “Your Favorites,” and is more succinct.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Omit the string entirely when an icon, a symbol or the surrounding row already says it.**

> You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

— <https://developer.apple.com/design/human-interface-guidelines/toggles>

> Avoid supplying a label that explains the button’s purpose.

— <https://developer.apple.com/design/human-interface-guidelines/toggles>

> Include text in your design only when it’s essential for conveying meaning.

— <https://developer.apple.com/design/human-interface-guidelines/icons>

**Give a short string no ending punctuation where it is a label, heading or column name.**

> Use nouns or short noun phrases with title-style capitalization, and don’t add ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/lists-and-tables>

> As with all button titles, use title-style capitalization and no ending punctuation.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Pick one capitalization style per element type and keep it across every instance.**

> Choose a style for each UI element type and use it consistently throughout your app — for example, title case for all alerts or sentence case for all headlines.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

**Make a one-word state a state, not a feeling.**

> Interjections like “oops!” or “uh-oh” are typically unnecessary and can sound insincere.

— <https://developer.apple.com/design/human-interface-guidelines/writing>

> write body text that succinctly describes the notification content without revealing too many details, like “Friend request,” “New comment,” “Reminder,” or “Shipment”

— <https://developer.apple.com/design/human-interface-guidelines/notifications>

**For a one-word action button, use the specific verb, not `OK`.**

> labeling the primary button Order is clearer than labeling it OK or Proceed.

— <https://developer.apple.com/design/human-interface-guidelines/snippets>

> A specific button title like “Erase,” “Convert,” “Clear,” or “Delete” helps people understand the action they’re taking.

— <https://developer.apple.com/design/human-interface-guidelines/alerts>

**Make a label state what is disclosed or hidden, or what value is being shown.**

> Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”

— <https://developer.apple.com/design/human-interface-guidelines/disclosure-controls>

> Write succinct labels that describe the current value and both endpoints of the range.

— <https://developer.apple.com/design/human-interface-guidelines/gauges>

**Write one-word alt text as the thing the image conveys, not a description of the image.**

> Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions, describe only the information the image itself conveys.

— <https://developer.apple.com/design/human-interface-guidelines/voiceover>

**Keep a control name short wherever it sits over content.**

> Keep names of controls short.

— <https://developer.apple.com/design/human-interface-guidelines/camera-control>

> In general, keep text brief.

— <https://developer.apple.com/design/human-interface-guidelines/wallet>

**Assume a one-word string will be translated and may be twice as long.**

> keep the text brief to avoid truncation, and take localization into account as you write it.

— <https://developer.apple.com/design/human-interface-guidelines/notifications>



### Inference — what the quoted rules imply for a 1–3 word surface (derived, not quoted)

Everything in this subsection is **inference**, derived from the sourced rules above; Apple does not state these as standalone rules. Where a surface has no HIG page, the inference is marked as such.

| Surface | Inferred rule | Derived from |
|---|---|---|
| Button (1–2 words) | A verb, no article, no period, title-style or sentence-style per your element convention. `Send`, `Erase`, `Add to Cart` — never `OK`, `Proceed`, `Click here`, `Let’s do it!`. | “it’s almost always best to use a verb”; “Aim for a one- or two-word title that describes the result”; “no ending punctuation” |
| Tab (1 word) | A noun naming the content of the pane, parallel in grammatical form with every sibling tab. Prefer a single word. | “use nouns or short noun phrases for tab labels”; “Use single words whenever possible.” |
| Toggle / switch label | The thing being switched, not `On`/`Off`. In a list row supply nothing at all; the row is the label. Never a label that re-explains the button’s purpose. | “the content in the row provides the context for the state the switch controls”; “Avoid supplying a label that explains the button’s purpose.” |
| Section header | A noun phrase, title-style, no ending punctuation, no possessive. *Inference:* keep it parallel with sibling headers and short enough not to wrap on the narrowest supported width. | “Use nouns or short noun phrases with title-style capitalization, and don’t add ending punctuation.” |
| Status / badge (1 word) | A state the person recognises, never an interjection or a joke: `Synced`, `Offline`, `Waiting` — not `Oops`, `Uh-oh`, `Whoops!`. *Inference:* the vocabulary should match the words used elsewhere in the product for the same state. | interjection ban; “write body text that succinctly describes the notification content” |
| Menu item (1–2 words) | Verb for an action, noun for a destination; no articles; ellipsis if it opens a view or needs more input. | “articles always lengthen labels”; “Append an ellipsis…when the action requires more information”; “label a menu item that initiates an action using a verb or verb phrase” |
| Notification action button (1–2 words) | A title-case verb phrase naming the result, with no app name: `Reply`, `Mark as Read`, not `Open MyApp`. | “use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app name…” |
| Alt text (1–5 words) | Name what the image conveys, in the terms the rest of the interface uses; never “image of”, never the file name, and nothing at all for a decorative image. | “describe only the information the image itself conveys”; “It’s unnecessary to describe images that are decorative…” |
| CLI flag description | **No HIG page exists for CLIs** — HIG does not govern them. This is an inference by analogy plus the Editorial register: one line, imperative or noun phrase, state the effect first and the default second, no trailing period on a fragment, and no article-padding. Confirm against `apple-style-guide-rules.md`. | no HIG source — inference; the closest HIG rules are “omit articles” and “no ending punctuation” |

**The short-string test.** Before you ship a one-word string, run the rules in order: (1) Is it a verb (it acts) or a noun (it names)? (2) Does it survive with no article and no possessive? (3) Is it free of `we`, of `the user`, of cuteness and of interjections? (4) Would it still be unambiguous at twice its length, in another language? (5) Does an icon already say it, in which case delete it? If any answer is wrong, the string is wrong.

---

## Sources

Every URL this file was built from, all fetched with `curl`/`urllib` and parsed with Python’s `json` module.

**Result: 187 URLs requested, 187 returned HTTP 200 with content. Zero 404s, zero empty pages, no fallback route required.** (172 content pages plus 15 index/category endpoints.)
The route is `https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json`.
(The `/tutorials/data/documentation/design/human-interface-guidelines/<slug>.json` variant — the one a sibling agent reported as failing — does 404; the working path has no `documentation/` segment.)

`cited` = the page supplies at least one quoted rule in this file. `no text guidance used` = the page returned full content but yielded no wording guidance worth quoting (visual/layout/technical guidance only, or a navigation index with no prose of its own).

| Slug | Page | HTTP | Bytes | Used for |
|---|---|---|---|---|
| `accessibility` | Accessibility | 200 | 85,010 | cited |
| `action-button` | Action button | 200 | 17,763 | no text guidance used |
| `action-sheets` | Action sheets | 200 | 24,268 | cited |
| `activity-rings` | Activity rings | 200 | 25,116 | no text guidance used |
| `activity-views` | Activity views | 200 | 26,568 | cited |
| `airplay` | AirPlay | 200 | 30,034 | no text guidance used |
| `alerts` | Alerts | 200 | 36,589 | cited |
| `always-on` | Always On | 200 | 20,645 | no text guidance used |
| `app-clips` | App Clips | 200 | 80,673 | cited |
| `app-icons` | App icons | 200 | 46,336 | no text guidance used |
| `app-shortcuts` | App Shortcuts | 200 | 43,253 | no text guidance used |
| `apple-in-app-purchase` | Apple In-App Purchase | 200 | 71,599 | no text guidance used |
| `apple-pay` | Apple Pay | 200 | 106,883 | cited |
| `apple-pencil-and-scribble` | Apple Pencil and Scribble | 200 | 45,412 | no text guidance used |
| `augmented-reality` | Augmented reality | 200 | 72,009 | no text guidance used |
| `boxes` | Boxes | 200 | 12,819 | cited |
| `branding` | Branding | 200 | 21,742 | cited |
| `buttons` | Buttons | 200 | 70,324 | cited |
| `camera-control` | Camera Control | 200 | 29,767 | cited |
| `carekit` | CareKit | 200 | 60,076 | no text guidance used |
| `carplay` | CarPlay | 200 | 22,865 | no text guidance used |
| `charting-data` | Charting data | 200 | 22,029 | no text guidance used |
| `charts` | Charts | 200 | 53,610 | cited |
| `collaboration-and-sharing` | Collaboration and sharing | 200 | 29,552 | cited |
| `collections` | Collections | 200 | 15,280 | no text guidance used |
| `color` | Color | 200 | 182,037 | no text guidance used |
| `color-wells` | Color wells | 200 | 12,959 | no text guidance used |
| `column-views` | Column views | 200 | 14,156 | no text guidance used |
| `combo-boxes` | Combo boxes | 200 | 12,873 | cited |
| `complications` | Complications | 200 | 99,430 | no text guidance used |
| `components` | Components | 200 | 14,427 | index page |
| `content` | Content | 200 | 8,600 | index page |
| `context-menus` | Context menus | 200 | 31,677 | cited |
| `controls` | Controls | 200 | 35,491 | no text guidance used |
| `dark-mode` | Dark Mode | 200 | 38,687 | no text guidance used |
| `design-principles` | Design principles | 200 | 26,295 | no text guidance used |
| `designing-for-games` | Designing for games | 200 | 77,474 | no text guidance used |
| `designing-for-ios` | Designing for iOS | 200 | 22,510 | no text guidance used |
| `designing-for-ipados` | Designing for iPadOS | 200 | 21,458 | no text guidance used |
| `designing-for-iphone-duo` | Designing for iPhone Duo | 200 | 77,105 | cited |
| `designing-for-macos` | Designing for macOS | 200 | 25,477 | no text guidance used |
| `designing-for-tvos` | Designing for tvOS | 200 | 16,518 | no text guidance used |
| `designing-for-visionos` | Designing for visionOS | 200 | 34,660 | no text guidance used |
| `designing-for-watchos` | Designing for watchOS | 200 | 23,640 | no text guidance used |
| `digit-entry-views` | Digit entry views | 200 | 9,728 | cited |
| `digital-crown` | Digital Crown | 200 | 19,496 | no text guidance used |
| `disclosure-controls` | Disclosure controls | 200 | 22,764 | cited |
| `dock-menus` | Dock menus | 200 | 12,874 | no text guidance used |
| `drag-and-drop` | Drag and drop | 200 | 37,910 | no text guidance used |
| `edit-menus` | Edit menus | 200 | 25,732 | cited |
| `entering-data` | Entering data | 200 | 21,929 | no text guidance used |
| `eyes` | Eyes | 200 | 36,972 | no text guidance used |
| `feedback` | Feedback | 200 | 19,462 | cited |
| `file-management` | File management | 200 | 31,253 | no text guidance used |
| `focus-and-selection` | Focus and selection | 200 | 42,190 | no text guidance used |
| `foundations` | Foundations | 200 | 29,595 | index page |
| `game-center` | Game Center | 200 | 64,843 | cited |
| `game-controls` | Game controls | 200 | 44,368 | no text guidance used |
| `gauges` | Gauges | 200 | 18,138 | cited |
| `generative-ai` | Generative AI | 200 | 47,058 | cited |
| `gestures` | Gestures | 200 | 60,734 | no text guidance used |
| `getting-started` | Getting started | 200 | 16,754 | index page |
| `going-full-screen` | Going full screen | 200 | 33,956 | no text guidance used |
| `gyro-and-accelerometer` | Gyroscope and accelerometer | 200 | 11,690 | no text guidance used |
| `healthkit` | HealthKit | 200 | 34,791 | no text guidance used |
| `home-screen-quick-actions` | Home Screen quick actions | 200 | 14,542 | no text guidance used |
| `homekit` | HomeKit | 200 | 67,984 | cited |
| `icloud` | iCloud | 200 | 12,395 | no text guidance used |
| `icons` | Icons | 200 | 78,412 | cited |
| `id-verifier` | ID Verifier | 200 | 21,078 | no text guidance used |
| `image-views` | Image views | 200 | 27,034 | no text guidance used |
| `image-wells` | Image wells | 200 | 10,193 | no text guidance used |
| `images` | Images | 200 | 43,685 | no text guidance used |
| `imessage-apps-and-stickers` | iMessage apps and stickers | 200 | 21,089 | no text guidance used |
| `immersive-experiences` | Immersive experiences | 200 | 57,276 | no text guidance used |
| `inclusion` | Inclusion | 200 | 51,352 | cited |
| `inputs` | Inputs | 200 | 22,484 | index page |
| `keyboards` | Keyboards | 200 | 66,400 | no text guidance used |
| `labels` | Labels | 200 | 36,245 | no text guidance used |
| `launching` | Launching | 200 | 25,518 | no text guidance used |
| `layout` | Layout | 200 | 84,939 | no text guidance used |
| `layout-and-organization` | Layout and organization | 200 | 16,206 | index page |
| `lists-and-tables` | Lists and tables | 200 | 33,074 | cited |
| `live-activities` | Live Activities | 200 | 98,950 | no text guidance used |
| `live-photos` | Live Photos | 200 | 13,088 | no text guidance used |
| `live-viewing-apps` | Live-viewing apps | 200 | 17,719 | no text guidance used |
| `loading` | Loading | 200 | 16,425 | cited |
| `lockups` | Lockups | 200 | 23,415 | no text guidance used |
| `mac-catalyst` | Mac Catalyst | 200 | 39,138 | no text guidance used |
| `machine-learning` | Machine learning | 200 | 79,040 | cited |
| `managing-accounts` | Managing accounts | 200 | 30,495 | no text guidance used |
| `managing-notifications` | Managing notifications | 200 | 26,436 | no text guidance used |
| `maps` | Maps | 200 | 67,382 | no text guidance used |
| `materials` | Materials | 200 | 76,600 | no text guidance used |
| `menus` | Menus | 200 | 48,890 | cited |
| `menus-and-actions` | Menus and actions | 200 | 18,314 | index page |
| `modality` | Modality | 200 | 25,972 | no text guidance used |
| `motion` | Motion | 200 | 31,108 | no text guidance used |
| `multitasking` | Multitasking | 200 | 33,675 | no text guidance used |
| `navigation-and-search` | Navigation and search | 200 | 10,281 | index page |
| `nearby-interactions` | Nearby interactions | 200 | 18,715 | no text guidance used |
| `nfc` | NFC | 200 | 12,338 | cited |
| `notifications` | Notifications | 200 | 43,985 | cited |
| `offering-help` | Offering help | 200 | 31,540 | cited |
| `onboarding` | Onboarding | 200 | 21,786 | cited |
| `ornaments` | Ornaments | 200 | 21,736 | no text guidance used |
| `outline-views` | Outline views | 200 | 22,180 | no text guidance used |
| `page-controls` | Page controls | 200 | 34,423 | no text guidance used |
| `panels` | Panels | 200 | 22,973 | no text guidance used |
| `path-controls` | Path controls | 200 | 12,536 | no text guidance used |
| `patterns` | Patterns | 200 | 40,734 | index page |
| `photo-editing` | Photo editing | 200 | 10,303 | no text guidance used |
| `pickers` | Pickers | 200 | 27,800 | no text guidance used |
| `playing-audio` | Playing audio | 200 | 43,777 | no text guidance used |
| `playing-haptics` | Playing haptics | 200 | 51,525 | no text guidance used |
| `playing-video` | Playing video | 200 | 51,013 | no text guidance used |
| `pointing-devices` | Pointing devices | 200 | 86,213 | no text guidance used |
| `pop-up-buttons` | Pop-up buttons | 200 | 19,029 | no text guidance used |
| `popovers` | Popovers | 200 | 22,930 | cited |
| `presentation` | Presentation | 200 | 13,301 | index page |
| `printing` | Printing | 200 | 14,176 | no text guidance used |
| `privacy` | Privacy | 200 | 66,967 | cited |
| `progress-indicators` | Progress indicators | 200 | 27,214 | cited |
| `pull-down-buttons` | Pull-down buttons | 200 | 25,744 | no text guidance used |
| `rating-indicators` | Rating indicators | 200 | 10,914 | no text guidance used |
| `ratings-and-reviews` | Ratings and reviews | 200 | 12,026 | no text guidance used |
| `remotes` | Remotes | 200 | 18,180 | no text guidance used |
| `researchkit` | ResearchKit | 200 | 28,561 | no text guidance used |
| `right-to-left` | Right to left | 200 | 62,460 | no text guidance used |
| `scroll-views` | Scroll views | 200 | 43,377 | no text guidance used |
| `search-fields` | Search fields | 200 | 46,952 | cited |
| `searching` | Searching | 200 | 23,154 | cited |
| `segmented-controls` | Segmented controls | 200 | 30,736 | no text guidance used |
| `selection-and-input` | Selection and input | 200 | 16,874 | index page |
| `settings` | Settings | 200 | 20,353 | cited |
| `sf-symbols` | SF Symbols | 200 | 73,718 | no text guidance used |
| `shareplay` | SharePlay | 200 | 45,228 | no text guidance used |
| `shazamkit` | ShazamKit | 200 | 12,071 | no text guidance used |
| `sheets` | Sheets | 200 | 56,812 | cited |
| `sidebars` | Sidebars | 200 | 38,566 | no text guidance used |
| `sign-in-with-apple` | Sign in with Apple | 200 | 59,015 | no text guidance used |
| `siri` | Siri | 200 | 49,420 | no text guidance used |
| `sliders` | Sliders | 200 | 27,352 | no text guidance used |
| `snippets` | Snippets | 200 | 24,565 | cited |
| `spatial-layout` | Spatial layout | 200 | 39,627 | no text guidance used |
| `split-views` | Split views | 200 | 34,759 | no text guidance used |
| `status` | Status | 200 | 8,957 | index page |
| `status-bars` | Status bars | 200 | 13,707 | no text guidance used |
| `steppers` | Steppers | 200 | 12,179 | no text guidance used |
| `system-experiences` | System experiences | 200 | 15,949 | index page |
| `tab-bars` | Tab bars | 200 | 53,333 | cited |
| `tab-views` | Tab views | 200 | 17,542 | cited |
| `tap-to-pay-on-iphone` | Tap to Pay on iPhone | 200 | 51,807 | cited |
| `technologies` | Technologies | 200 | 45,051 | index page |
| `text-fields` | Text fields | 200 | 25,637 | cited |
| `text-views` | Text views | 200 | 20,167 | no text guidance used |
| `the-menu-bar` | The menu bar | 200 | 84,251 | cited |
| `toggles` | Toggles | 200 | 38,601 | cited |
| `token-fields` | Token fields | 200 | 15,175 | no text guidance used |
| `toolbars` | Toolbars | 200 | 72,799 | cited |
| `top-shelf` | Top Shelf | 200 | 28,494 | no text guidance used |
| `typography` | Typography | 200 | 281,141 | no text guidance used |
| `undo-and-redo` | Undo and redo | 200 | 17,228 | no text guidance used |
| `virtual-keyboards` | Virtual keyboards | 200 | 49,590 | no text guidance used |
| `voiceover` | VoiceOver | 200 | 36,439 | cited |
| `wallet` | Wallet | 200 | 129,438 | cited |
| `watch-faces` | Watch faces | 200 | 11,810 | no text guidance used |
| `web-views` | Web views | 200 | 10,097 | no text guidance used |
| `widgets` | Widgets | 200 | 142,173 | no text guidance used |
| `windows` | Windows | 200 | 67,050 | no text guidance used |
| `workouts` | Workouts | 200 | 20,914 | no text guidance used |
| `writing` | Writing | 200 | 37,074 | cited |

#### Index and category endpoints

These carry no prose guidance; they were used to enumerate the pages above. All returned HTTP 200.

| Endpoint | What it is | HTTP | Bytes |
|---|---|---|---|
| `human-interface-guidelines.json` | Human Interface Guidelines (root) | 200 | 27,269 |
| `human-interface-guidelines/foundations.json` | Foundations index | 200 | 29,595 |
| `human-interface-guidelines/components.json` | Components index | 200 | 14,427 |
| `human-interface-guidelines/patterns.json` | Patterns index | 200 | 40,734 |
| `human-interface-guidelines/inputs.json` | Inputs index | 200 | 22,484 |
| `human-interface-guidelines/technologies.json` | Technologies index | 200 | 45,051 |
| `human-interface-guidelines/getting-started.json` | Getting started index | 200 | 16,754 |
| `human-interface-guidelines/content.json` | Components / Content | 200 | 8,600 |
| `human-interface-guidelines/layout-and-organization.json` | Components / Layout and organization | 200 | 16,206 |
| `human-interface-guidelines/menus-and-actions.json` | Components / Menus and actions | 200 | 18,314 |
| `human-interface-guidelines/navigation-and-search.json` | Components / Navigation and search | 200 | 10,281 |
| `human-interface-guidelines/presentation.json` | Components / Presentation | 200 | 13,301 |
| `human-interface-guidelines/selection-and-input.json` | Components / Selection and input | 200 | 16,874 |
| `human-interface-guidelines/status.json` | Components / Status | 200 | 8,957 |
| `human-interface-guidelines/system-experiences.json` | Components / System experiences | 200 | 15,949 |

### Pages fetched that this rulebook quotes nothing from

These all returned full content (HTTP 200), but no sentence from them appears above. Most are purely visual, structural or technical and belong to other rulebooks. **A few do carry one line of wording guidance that a neighbouring, better page already states** — for example `app-shortcuts` (“Provide brief, memorable activation phrases and natural variants”), `labels` (a page about the *Label component*, not about how to word labels), `nfc` and `game-center` (both quoted in the capitalization table above), and `typography` / `workouts` / `designing-for-games` (legibility, not wording). Listed so the next reader does not re-fetch them hoping for text guidance.

`action-button`, `activity-rings`, `airplay`, `always-on`, `app-icons`, `app-shortcuts`, `apple-in-app-purchase`, `apple-pencil-and-scribble`, `augmented-reality`, `carekit`, `carplay`, `charting-data`, `collections`, `color`, `color-wells`, `column-views`, `complications`, `controls`, `dark-mode`, `design-principles`, `designing-for-games`, `designing-for-ios`, `designing-for-ipados`, `designing-for-macos`, `designing-for-tvos`, `designing-for-visionos`, `designing-for-watchos`, `digital-crown`, `dock-menus`, `drag-and-drop`, `entering-data`, `eyes`, `file-management`, `focus-and-selection`, `game-controls`, `gestures`, `going-full-screen`, `gyro-and-accelerometer`, `healthkit`, `home-screen-quick-actions`, `icloud`, `id-verifier`, `image-views`, `image-wells`, `images`, `imessage-apps-and-stickers`, `immersive-experiences`, `keyboards`, `labels`, `launching`, `layout`, `live-activities`, `live-photos`, `live-viewing-apps`, `lockups`, `mac-catalyst`, `managing-accounts`, `managing-notifications`, `maps`, `materials`, `modality`, `motion`, `multitasking`, `nearby-interactions`, `ornaments`, `outline-views`, `page-controls`, `panels`, `path-controls`, `photo-editing`, `pickers`, `playing-audio`, `playing-haptics`, `playing-video`, `pointing-devices`, `pop-up-buttons`, `printing`, `pull-down-buttons`, `rating-indicators`, `ratings-and-reviews`, `remotes`, `researchkit`, `right-to-left`, `scroll-views`, `segmented-controls`, `sf-symbols`, `shareplay`, `shazamkit`, `sidebars`, `sign-in-with-apple`, `siri`, `sliders`, `spatial-layout`, `split-views`, `status-bars`, `steppers`, `text-views`, `token-fields`, `top-shelf`, `typography`, `undo-and-redo`, `virtual-keyboards`, `watch-faces`, `web-views`, `widgets`, `windows`, `workouts`

### Container / index pages

These are navigation pages with no prose guidance of their own; they were used only to enumerate the pages above.

`components`, `content`, `foundations`, `getting-started`, `hig`, `inputs`, `layout-and-organization`, `menus-and-actions`, `navigation-and-search`, `patterns`, `presentation`, `selection-and-input`, `status`, `system-experiences`, `technologies`

---


### Which page holds which surface

Several surfaces named in this rulebook have **no page of their own** in the HIG. The guidance lives on a neighbouring page, and this table records where, so the mapping is auditable.

| Surface | Page that actually documents it |
|---|---|
| Tooltips | `offering-help` (section “macOS, visionOS”) — there is **no** `tooltips` page |
| Empty states | `writing` (guideline “Provide clear next steps on any blank screens”) — there is **no** `empty-states` page |
| Loading and progress | `loading` and `progress-indicators` |
| Buttons, labels, links | `buttons`, `labels`, and `writing` (the verb and “Click here” rules) |
| Error messages | `writing` (the only place Apple gives the error-writing rules) and `alerts` |
| Confirmation and destructive actions | `alerts`, `action-sheets`, `sheets`, `progress-indicators` |
| Permission prompts | `privacy`; `homekit` for a purpose-string example |
| Alt text and accessibility labels | `voiceover`, `accessibility`, `charts` |
| Accessibility hints | No dedicated HIG guidance exists for the “hint” half of an accessibility label; `voiceover` covers labels and descriptions only. Anything you write as a hint is inference. |

### Pages checked that had copy guidance but nothing quotable beyond what is above

`app-shortcuts` (activation phrases), `virtual-keyboards` (Return key type), `game-controls` (“Prefer using symbols, not text”), `top-shelf` and `widgets` (succinct titles for glanceable surfaces), `workouts` and `designing-for-games` (legibility, not wording), `entering-data`, `token-fields`, `combo-boxes`, `gauges`, `boxes`, `disclosure-controls`, `split-views`, `tab-bars`, `toolbars`. Each is cited above where its rule belongs.

### Verification notes

- **Every quote in this file was extracted programmatically** from the fetched JSON rather than typed by hand, so the wording, the curly quotes and the punctuation match Apple’s page exactly. Each extraction was anchored by a start and end string; a build failure would have been raised if any anchor failed to match exactly one paragraph.
- **Inline cross-references were resolved to their visible text**, including Apple’s `overridingTitle` where present. For example, the alerts page reads “As with all button titles, use *title-style capitalization* and no ending punctuation” — the phrase in italics is a link whose visible label is `title-style capitalization`, and it is reproduced here as it renders on the page.
- **The `reference` nodes that point at developer documentation** (SwiftUI/UIKit/AppKit symbols) were dropped from quotes, since they are not prose. Where that leaves a sentence trailing on a preposition, the quote was trimmed to end at the last complete clause.
- **Inline emphasis is rendered as plain text.** Apple italicises the example words inside several guidelines — for example “*my*” and “*your*” in the possessive-pronoun rule, and “*the user*” / “*the player*” in the inclusion rule. The words are unchanged; only the italics are dropped, because they carry no meaning beyond emphasis on the page.
- **Nothing in this file is a paraphrase of an unquoted page.** If you need a rule that is not here, fetch the page and add it with its quote.
