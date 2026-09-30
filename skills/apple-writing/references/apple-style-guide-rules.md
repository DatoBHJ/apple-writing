# Apple Style Guide — Applicable Rulebook

**Source:** *Apple Style Guide*, June 2026 (Apple Inc.), 244 pp. — PDF edition (`research/apple-style-guide.pdf`, text at `research/apple-style-guide.txt`) and the web edition (`research/asg/*.txt`).
**Scope of this file:** English prose written in Apple’s editorial register. Every rule below is stated as an imperative and backed by a verbatim quote from the guide.
**Citations:** `p.N` = PDF page; backticked names are the guide’s own A–Z headwords or chapter sections (see `research/asg-sections.txt` for the slug list).
**Quote policy:** quotations are verbatim. Only extraction whitespace has been normalized — the PDF text layer inserts a space before punctuation that follows an italic or bold run (`use power adapter .`), and that space has been removed here. Nothing else is altered.

**How to use this file:** write the draft first, then check it against §1–§10 for structure and §11 for individual words. §11 is the layer that catches a single wrong word. §12 lists what this guide *permits* that ordinary style advice forbids — do not “fix” those. §13 tells you when this file is the wrong rulebook entirely.

> **Loading note — this file is long (about 1,300 lines). Don’t read it end to end.** Find the section you need and read only that. §11 is a 599-row table, so grep it: `grep -i "| \*\*the word"`, or read the section that matches your task.
>
> **Contents**
> §1 Voice, person, point of view · §2 Sentence construction · §3 Punctuation · §4 Capitalization · §5 Numbers, units, symbols · §6 Abbreviations, acronyms, Latin · §7 Terminology, product names, trademarks · §8 Inclusive language · §9 Technical notation, code font, placeholders · §10 International style · **§11 Word list / substitutions (the big table)** · §12 What this guide permits that common advice forbids · §13 Where this guide does NOT govern

---

## 1. Voice, person, and point of view

**Write to one reader, in the second person, in the present tense.** The guide’s own model is a singular relationship with “you”; it forbids first-person plural entirely.

> “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.” — `first person`, p.87

> “Don’t use first person; rewrite in terms of the reader or the product. Correct: For best results, the image should be at least 600 x 600 pixels. Incorrect: We recommend that the image be at least 600 x 600 pixels.” — `we`, p.217

> “When describing something users are encouraged to do, don’t use we or Apple recommends; use recommended. Correct: It’s recommended that you import video using the same camera you used to record it. Incorrect: We recommend that you import video using the same camera you used to record it. You can also use less formal phrases like it’s a good idea to.” — `recommend`, p.175

**Use Apple’s informal voice — contractions are required, not tolerated.**

> “As part of Apple’s informal voice, contractions are used and recommended throughout most documentation, interface text, and marketing copy. Keep localization in mind when deciding how or whether to use contractions.” — `contractions`, p.57

> “Use common contractions of be-verbs and auxiliary verbs with not (aren’t, isn’t, can’t, couldn’t, didn’t, doesn’t, hadn’t, haven’t, weren’t, won’t).” … “Use common contractions of be-verbs and auxiliary verbs with personal pronouns (he’s, I’m, I’ve, it’s, she’ll, they’re, we’ve, you’re). It’s also OK to use here’s, let’s, that’s, there’s, and what’s.” — `contractions`, p.57

**But never contract nouns or proper nouns, and avoid awkward or colloquial contractions.**

> “Don’t form contractions from nouns or proper nouns. Avoid: The computer’s not working. Avoid: Apple’s going to introduce a new computer today.” — `contractions`, p.57

> “Avoid contractions of multipart verbs (could’ve), colloquialisms (workin'), and other contractions that are uncommon or awkward-sounding.” — `contractions`, p.58

**Describe what the product does, not what it “lets you” do — sparingly.**

> “Don’t overuse the phrase lets you in instructions; try to restructure the sentence to focus on what the user does. Avoid: The Up Next button lets you see which songs will play next. Preferable: Click the Up Next button to see which songs will play next. It’s OK to use lets you in content that focuses on describing features and their capabilities.” — `let`, p.124

**Use the modals precisely: `can` = capacity, `might`/`may` = possibility, `may` = permission.**

> “Use can to express the capacity to do something; use might or may to suggest the possibility of doing something; use may to express permission.” … “When used to express possibility, might typically suggests lower probability than may.” — `can, might, may`, p.45

**Be polite without “please.”**

> “Avoid using please in instructional text and cross-references. Correct: Follow the steps below. Incorrect: Please follow the steps below. Correct: For more information, see ”Store Settings“ on page 96. Incorrect: For more information, please see ”Store Settings“ on page 96.” — `please`, p.161

**Humor and personality are allowed — inside examples, and only in good taste.**

> “Humor can enhance documentation by adding to a reader’s enjoyment and by helping to lighten the tone. Humor usually works best in examples, where it’s less likely to distract the reader. Be careful that your humor is in good taste—one reader’s joke can be another reader’s insult—and keep in mind that humor may not translate well in localized text.” — `humor`, p.103

**Avoid jargon; define technical terms on first use.**

> “Avoid jargon whenever possible. Define technical terminology on first occurrence.” — `jargon`, p.118

**Do not describe software or hardware with human or biological attributes.**

> “In general, it’s a good idea to avoid describing software or hardware using human or biological attributes; doing so can lead to unintended hurtful implications.” — *General guidelines* (Writing inclusively)

> “Passive voice is sometimes appropriate and necessary—for example, when using the active voice would require either a highly convoluted sentence structure or excessive anthropomorphism.” — `passive voice`, p.154

**Never use a product name as a verb, and don’t turn a feature into one.**

> “Don’t use product names or trademarks as verbs: make a FaceTime call to a friend, not FaceTime a friend; identify a song using Shazam, not Shazam a song.” — `product names`, p.168

**Avoid the first-person-ish habit of addressing “the user” when you are writing to them.**

> “If the audience of your document consists of users, avoid this term.” — `user`, p.212

---

## 2. Sentence construction

**Default to active voice; rewrite passive constructions unless a specific exception applies.**

> “Avoid when possible and use active voice. Passive voice is sometimes appropriate and necessary—for example, when using the active voice would require either a highly convoluted sentence structure or excessive anthropomorphism—but rewrite to avoid passive voice if you can. In tutorials, a passive construction might be appropriate to avoid miscuing the reader—that is, when you describe an action that the user isn’t supposed to try yet. Explanation screen: An icon is selected by clicking it. User-try screen: You try it. Click the icon.” — `passive voice`, p.154

**Use present tense; future tense only for genuinely future events.**

> “Whenever possible, use present, not future, tense. Don’t switch unnecessarily from present to future tense when present tense is sufficient to express a sequence of steps or events.” … “Future tense is sometimes appropriate—for example, when a product described isn’t yet available.” — `future tense`, p.92

**Write simple structures — this is the stated international-style baseline.**

> “Write in simple structures.” — *Intro to international style*

**Keep list items parallel.**

> “Within a single list, all bulleted items should be parallel.” — `lists (bulleted)`, p.126

**Fragments are allowed in bullets and callouts — and take no period.**

> “List items that are fragments or that complete the thought started by the main clause should not end with a period; list items that are complete sentences should end with a period.” — `lists (bulleted)`, p.126

> “Use sentence-style capitalization. Use a period for a complete sentence and no ending punctuation for a sentence fragment. It’s OK to have a mixture of complete sentences and fragments in one illustration.” — `callouts`, p.44

**Numbered steps are complete sentences, with sentence-style capitalization and closing punctuation.**

> “Use a numbered list when you want to stress the sequential nature of steps, rules, or instructions. In numbered task lists (steps), each item should be a complete sentence. Use sentence-style capitalization for each item and end each item with closing punctuation.” — `lists (bulleted)`, p.126

**Don’t open a sentence with a numeral; rephrase.**

> “Numbers that appear at the beginning of a sentence. (Try to rephrase to avoid starting a sentence with a number.) Correct: Two hundred fifty functions are available in the Function Browser. Preferable: The Function Browser gives you access to 250 functions.” — `numbers`, p.148

**Cut these constructions outright.**

> “Rewrite to avoid this construction. Correct: document and app icons. Avoid: document and/or app icons” — `and/or`, p.19

> “The whole comprises its parts. This word is misused so often that correct usage might confuse the reader; avoid it altogether. Use is composed of, includes, consists of, contains, or another word, as appropriate. Never use is comprised of, which in strict usage is equivalent to is included of.” — `comprise`, p.56

> “Avoid; instead, use alternatives such as caused by or because of. Avoid: The interference was due to a faulty cable. Preferable: Your apps will open more quickly because of the additional memory.” — `due to`, p.77

> “Don’t use unless absolutely necessary; use just to.” — `in order to`, p.110

> “Avoid using as a transitive verb. Correct: Scroll through a document. Correct: Scroll to view more of the document. Incorrect: Scroll a document.” — `scroll`, p.179

**Say what happens, not that something “appears” as a step.**

> “In a task, avoid stating that an item appears; if necessary for clarity, try to work it into the context of the task.” — `appear`, p.21

> “Use appear, not display, to refer to items becoming visible on the screen. Correct: The setup assistant appears. Incorrect: The setup assistant is displayed. Incorrect: The setup assistant displays.” — `appear`, p.21

**Replace nominalizations and vague capability words with what the reader does.**

> “If possible, avoid capability when you discuss features of software or hardware. Reword in terms of what the user can do with the feature. Correct: With Photos, you can create slideshows. Incorrect: Photos has the capability to create slideshows.” — `capability`, p.45

> “In user materials, avoid if you can use a word such as features instead. Avoid: Some functionality is not available in certain regions. Preferable: Some features are not available in certain regions.” — `functionality`, p.91

> “Try to avoid. Correct: make your changes, select the folder. Incorrect: make the desired changes, select the desired folder” — `desired`, p.65

> “Avoid; use general rule, general recommendation, guideline, or as a rule.” — `rule of thumb`, p.178

**Don’t call a feature “new” — date it instead.**

> “In most documents, avoid describing a product or feature as new because the text will quickly become out of date. When appropriate, state the version of software in which a feature was introduced. Correct: Math Notes, introduced with iOS 18… Incorrect: The new Math Notes feature…” — `new`, p.147

**Keep terminology stable across a document.**

> “Be consistent when naming placeholders; for example, don’t alternate between commands and commandList.” — *Syntax descriptions*

> “Develop a method of spacing around punctuation and use the method consistently.” — *Code*

---

## 3. Punctuation

**Always use the serial comma.**

> “Use a serial comma before and or or in a list of three or more items. Correct: You can ask Siri to place phone calls, send text messages, send reminders, and more. Incorrect: You can ask Siri to place phone calls, send text messages, send reminders and more.” — `commas`, p.56

**Capitalize after a colon only when a complete sentence follows (a deliberate exception to Chicago); always capitalize after a colon in a heading; precede every list with a colon.**

> “In running text: Capitalize the first word after the colon if the word begins a complete sentence (exception to The Chicago Manual of Style).” … “In headings: If you use a colon in a heading, capitalize the first word after the colon, regardless of its part of speech.” … “With lists: Precede every list with a colon, whether the sentence before the colon is a complete thought or a partial thought (exception to The Chicago Manual of Style).” — `colons`, p.53

**Use the em dash closed up, on both sides when it interrupts mid-sentence, and don’t overuse it.**

> “Use the em dash (—) to set off a word or phrase that interrupts or changes the direction of a sentence or to set off a lengthy list that would otherwise make the syntax of a sentence confusing. Don’t overuse em dashes. If the text being set off doesn’t come at the end of the sentence, use an em dash both before it and after it.” … “Close up the em dash with the word before it and the word after it.” — `dash (em)`, p.62

**Use the en dash for ranges, for compound adjectives containing a two-word element, and as a minus sign.**

> “Numbers in a range: Use an en dash between numbers that represent the endpoints of a continuous range. bits 3–17, 2003–2005” … “Compound adjectives: Use an en dash between the elements of a compound adjective when one of those elements is itself two words. desktop interface–specific instructions” … “Minus sign: Use an en dash as a minus sign (except in code font, where you use a hyphen).” — `dash (en)`, p.62

**Use the curly apostrophe everywhere except code and units of measure.**

> “Use the curly apostrophe (Option-Shift-Right Bracket) except in code font and for units of measure.” — `apostrophes`, p.20

**Possessives: apostrophe + s for singulars (even names ending in s); apostrophe alone for plurals ending in s; never possess a product name.**

> “Form the possessive of a singular noun, including one that ends in s, by adding an apostrophe and an s.” … “Form the possessive of a plural noun that ends in s by adding an apostrophe. Form the possessive of a plural noun that doesn’t end in s by adding an apostrophe and an s.” … “Rewrite to avoid forming a possessive of any product name, trademarked or not (for example, don’t use Keynote’s slides).” — `possessives`, p.163

**Plurals: add s with no apostrophe to abbreviations, acronyms and numbers; apostrophe + s only for letters and symbols; never `(s)`.**

> “To form the plural of an acronym or an abbreviation, add an s but no apostrophe. CDs, DVDs” … “To form the plural of a letter or symbol, add an apostrophe and an s. p’s, +'s” … “Form the plural of numbers by adding an s. 1s, 1930s” … “Don’t use (s) to indicate that a noun can be either singular or plural. To refer to both the singular and plural forms, spell them out; if possible, rewrite to avoid either construction. Acceptable: initializing your disk or disks. Preferable: initializing disks. Incorrect: initializing your disk(s)” — `plurals`, p.161

**Pluralize trademarked product names with a generic noun, never with an s.**

> “Form the plural of trademarked product names by adding the plural generic noun to the singular product name. Correct: Mac computers, MacBook Pro computers, iMac computers. Incorrect: Macs, MacBook Pros, iMacs” — `plurals`, p.161

**Use curly quotation marks; put periods and commas inside, other punctuation outside unless it belongs to the quotation; call them “quotation marks,” not “quotes.”**

> “Use curly opening and closing quotation marks except in code font.” … “With periods and commas: Put periods and commas within quotation marks. If necessary for clarity, periods and commas can go outside, as in AN$ = ”1“.” … “With other punctuation: Semicolons, colons, question marks, and exclamation points go outside quotation marks unless they’re part of an actual quotation.” … “Terminology: Use quotation marks, not quote marks or quotes.” — `quotation marks`, p.172

**Quote sentence-style onscreen element names; don’t quote title-style ones.**

> “In general, write the names of buttons exactly as they appear onscreen. If the button’s name uses sentence-style capitalization, enclose the name in quotation marks. Click the ”Position on screen“ button. If the button’s name uses title-style capitalization, don’t enclose the name in quotation marks, even if one of the words is lowercase. Tap Add to Favorites.” — `button`, p.43

> “For options and other onscreen elements of two or more words whose names are capitalized using sentence style, use quotation marks in text to avoid misreading. Select the checkbox labeled ”Keep lines together.“” — `option names`, p.153

**Use the ellipsis character; never carry a menu ellipsis into text.**

> “A set of three dots indicating a continuation or, in a quotation, the omission of one or more words. Use the ellipsis character (Option-Semicolon) to prevent line breaks from occurring between the dots.” … “If the name of a menu item or button ends with an ellipsis, don’t include the ellipsis in running text. Correct: Choose File > New and click a template. Incorrect: Choose File > New… and click a template.” — `ellipsis`, p.79

**Exclamation points: allowed in promotional text and dialogue only.**

> “OK to use exclamation points occasionally in promotional text and dialogue. Avoid in documentation.” — `exclamation points`, p.83

**Brackets, slashes, and other marks — use the guide’s names.**

> “Use brackets, not square brackets, to describe these symbols: [ ]. Don’t use brackets when you mean angle brackets (< >).” — `brackets`, p.41

> “Use slash to describe this character: /. See also backslash.” — `slash`, p.187

> “Use the ampersand character (&) in text only when you refer to onscreen elements, document titles, or other items containing the character.” — `ampersand`, p.19

> “Use to describe this character: #. Don’t use pound sign or number symbol. Avoid using the number sign to specify an item in a numbered series.” — `number sign`, p.150

**Use prime marks for feet and inches — never quotation marks.**

> “Don’t use single or double quotation marks for units of measure; use the prime symbol for feet (Option-Shift-E) and the double prime symbol for inches (Option-Shift-G).” — `quotation marks`, p.172

> “Don’t use the symbol ′ unless space limitations prevent the use of foot or ft.” — `foot`, p.89

**Hyphenate compound modifiers before a noun, not after; never hyphenate -ly adverbs or units of measure used as modifiers.**

> “In general, hyphenate two words that precede and modify a noun as a unit.” … “Adverbs: Don’t hyphenate compounds with very or with adverbs that end in -ly.” … “Units of measure: When you use a spelled-out unit of measure in a compound adjective, hyphenate the compound (27-inch screen). When you use an abbreviation or a metric unit of measure, including KB, MB, mm, and so on, don’t hyphenate (500 GB hard disk).” — `hyphenation`, p.104

> “When you use a spelled-out unit of measure in a compound adjective, hyphenate the compound. 17-inch display, 3-meter cable. When you use a unit symbol or abbreviation in a compound adjective, don’t hyphenate; add a space between the number and the abbreviation. 20 nA battery, 30 GB capacity” — *Intro to units of measure*

> “user-friendly (adj.), user friendly (pred. adj.)” … “If a hyphenated compound has no pred. adj. entry, hyphenate the compound wherever it appears in a sentence.” — *Conventions used in this guide*, p.5

**Use `a.m.`/`p.m.` lowercase with periods and a preceding space; noon and midnight have their own forms.**

> “Note periods: 8:30 a.m. Use a space before the abbreviation.” — `a.m.`, p.19

> “Use 12:00 noon and 12:00 midnight or just noon and midnight.” — `time of day`, p.204

**Avoid punctuation after something the user should type.**

> “Avoid punctuation after something the user should type.” — `punctuation`, p.171

---

## 4. Capitalization

**Two styles exist; pick per element type and stay consistent. Sentence style capitalizes only the first word, proper nouns and proper adjectives.**

> “Two styles of capitalization are commonly used at Apple: • Sentence-style capitalization: This line provides an example of sentence-style capitalization. • Title-style capitalization: This Line Provides an Example of Title-Style Capitalization.” — `capitalization`, p.45

> “Capitalize only the first letter of the first word, proper nouns, and proper adjectives.” — `sentence-style capitalization`, p.182

**Title style: capitalize first and last word, nouns, pronouns, verbs, adjectives, adverbs, conjunctions other than coordinating conjunctions, prepositions of five letters or more, and the second word of a hyphenated compound (except Built-in, Plug-in).**

> “When using title-style capitalization, capitalize: • The first and last word, regardless of the part of speech • Nouns, pronouns, verbs, adjectives, and adverbs—no matter their length (for example, It, This, You, Your, My, Is, Are, and Be)” … “• Conjunctions (except for coordinating conjunctions), no matter their length (for example, If)” … “• Prepositions of five letters or more (for example, About, Between, Through)” … “• The second word in a hyphenated compound (except for Built-in and Plug-in)” — `capitalization`, p.45

**Title style: do not capitalize articles, coordinating conjunctions, `to` in infinitives, `as`, prepositions of four letters or fewer, or words that are always lowercase.**

> “When using title-style capitalization, don’t capitalize: • Articles (a, an, the), unless an article is the first word or follows a colon • Coordinating conjunctions (and, but, or, nor, for, yet, and so) • The word to in infinitives (How to Start Your Computer) • The word as, regardless of the part of speech (Export a Document as a PDF) • Words that always begin with a lowercase letter, such as iPad and macOS • Prepositions of four letters or fewer (at, by, for, from, in, into, of, off, on, onto, out, over, to, up, and with)” — `capitalization`, p.45

**Copy onscreen capitalization exactly; normalize all-caps or all-lowercase interface text to title style in documentation.**

> “In general, capitalize the names of onscreen elements exactly as they appear onscreen. If an onscreen element uses all capital letters or all lowercase letters, use title-style capitalization when writing the element name in documentation.” — `capitalization`, p.45

**Follow the product’s own capitalization, including lowercase leading letters — even at the start of a sentence.**

> “If a product name starts with a lowercase letter, use that capitalization style even at the beginning of sentences and in title-style headings: iPhone Safety Features, not IPhone Safety Features; Set Up Your Mac mini, not Set Up Your Mac Mini. In all-caps text, capitalize all the letters: THE NEW IPAD, not THE NEW iPAD.” — `product names`, p.168

> “Follow the style of the software itself for capitalization and spaces—for example, TextEdit, Image Capture, DigitalColor Meter, iMovie.” — `app names`, p.31

**Don’t capitalize `chapter` or `appendix` except in cross-references to actual titles.**

> “Don’t capitalize the word chapter or appendix, except in cross-references to actual titles. See Chapter 2, ”Units of Measure.“ See the appendix for specifications. See Appendix B for a list of specifications.” — `capitalization`, p.45

**Capitalize feature and onscreen names; leave generic references lowercase.**

> “Capitalize the names of accessibility features. For example: Accessibility Keyboard, AssistiveTouch, Guided Access, Hover Text, Invert Colors, Larger Dynamic Type, Live Listen, Magnifier, Safari Reader, Speak Screen, Speak Selection, Switch Control, Text to Speech, Type to Siri, Typing Feedback, Voice Control, VoiceOver, Zoom” — `accessibility`, p.14

> “Capitalize the names of the rings that track your daily activity in the Activity app (for example, Stand ring, Exercise ring).” — `Activity rings`, p.14

> “Capitalize when referring to the app name. Use lowercase when referring to the recordings you make with the app. You can also use recordings.” — `Voice Memos`, p.215

**Capitalize document and work titles by their own style; italicize for works, quote for parts of works.**

> “Use italics for the titles of books, magazines, newspapers, manuals, movies, videos, plays, television shows, radio shows, podcast series, blogs, music albums, and works of art. Use plain text and quotation marks for the titles of works that are more limited in scope, such as articles, stories, reports, TV episodes, podcast episodes, sections of blogs, songs, chapters and sections of works, and photographs.” — `titles of works`, p.205

> “In general, use title-style capitalization and italics; don’t use quotation marks unless italics aren’t available. Don’t capitalize or italicize phrases such as user guide unless they’re part of the title as it appears on the cover page of the document. Don’t include trademark symbols. See the iPhone User Guide.” — `cross-references`, p.60

> “Don’t capitalize or use italics for generic references to documents. See the user guide that came with your computer. To connect your display, follow the instructions in the setup guide.” — `document titles`, p.71

---

## 5. Numbers, units, and symbols

**Spell out cardinals and ordinals one through nine — except numbers as numbers, units of measure, and anything at the start of a sentence.**

> “Cardinal numbers from one through nine. (However, use a numeral, no matter how small, to express numbers as numbers and as units of measure.)” … “Ordinal numbers from zero through nine.” … “Numbers that appear at the beginning of a sentence.” — `numbers`, p.148

**Use numerals for addresses, slots, memory, ordinals above nine, approximations, and for a whole category if any number in it exceeds nine.**

> “To refer to a specific address, bit, byte, chapter, field, key, pin, sector, slot, or track, or when expressing amounts of memory.” … “For numbers of the same category within a paragraph, if any number is larger than nine. We have 25 computers and 4 printers on the network. [Computers and printers are the same category.]” … “To express an approximation. Cocoa includes definitions for more than 250 additional classes.” — `numbers`, p.148

**Use commas in numbers of five digits or more; not in memory addresses or microprocessor numbers.**

> “Use a comma to set off numbers of five digits or more.” … “Don’t use a comma in memory addresses or in numbers representing microprocessors. $FFFF FFFF, 68020 microprocessor” — `numbers`, p.148

> “Don’t use commas in addresses, even in numbers of five digits or more.” — `memory address, memory location`, p.139

**Ranges take an en dash and both full numbers.**

> “Use an en dash between numbers that represent the endpoints of a continuous range: bits 3–17. Use the full concluding number in a range of numbers. Correct: 2013–2019. Incorrect: 2013–19” — `numbers`, p.148

**Version numbers: `earlier`/`later`, never `lower`/`higher`/`newer`/`older`; no `version` or `v`; drop trailing `.0`; never `x` for a range.**

> “Don’t include the word version or the letter v when you refer to versions of software—for example, Keynote 15.2, not Keynote version 15.2.” … “When referring to a major release number (such as macOS 15 or iOS 18), omit any trailing .0 unless it’s needed for clarity.” … “Earlier or later: Use earlier or later, rather than lower or higher or newer or older.” … “The letter x: Except in developer materials, don’t use x to mean ”any number,“ as in 15.x; use a specific number or range of numbers.” — `version number`, p.213

**Fractions: spell out denominators of 10 or lower in user materials; hyphenate; use mixed numerals.**

> “In user materials, spell out fractions whose denominator is 10 or lower except in specification lists, technical appendixes, or tables. For the spelled-out forms, hyphenate the fractions: one-tenth, one-fifth, three-fourths.” … “When you express a noninteger greater than 1 in fractional form, use a mixed numeral rather than an improper fraction. Correct: 1 1/6. Incorrect: 7/6” — `fractions`, p.90

**Percent is always preceded by a numeral, however small.**

> “Always preceded by a numeral, no matter how small the value. 1 percent” — `percent`, p.156

**Units: SI only, a nonbreaking space between value and symbol, symbols never pluralized or hyphenated, no trailing period.**

> “Use only units of the International System of Units (SI) to express the values of quantities.” … “Quantities are always expressed with a unit symbol. Use a nonbreaking space (Option-Space bar) between the quantity and its symbol. Unit symbols are unaltered in the plural and are never hyphenated, even when they’re used as an adjective. Symbols for SI units of measure aren’t followed by a period unless they appear at the end of a sentence. Don’t imply more precision than is reasonable in choosing a unit symbol.” — *Units of measure*

**Spell out units on first use in user documentation, and always spell out nonmetric units in text.**

> “In user documentation, spell out units of measure and give the abbreviation in parentheses on first occurrence. Repeat the spelled-out version in new sections and chapters if the unit symbol or abbreviation is obscure and if the audience requires it. 20 gigabytes (GB) of memory. Subsequent occurrences: 20 GB of memory” … “Always spell out nonmetric units of measure in text (for example, 17-inch display). It’s OK to abbreviate such units in tables and technical specifications (Display size: 17 in.).” — *Intro to units of measure*

**When a unit symbol is a noun, put a space before it and `of` after it; don’t mix symbol systems.**

> “When you use a unit symbol or abbreviation as a noun, insert a space between the number and the abbreviation, and use the preposition of before the unit the value quantifies. 20 GB of memory” … “Don’t mix unit symbols and names (m/second) or unit symbols and abbreviations (J/sec.). Don’t mix a prefix name with a unit symbol (kiloHz), or a prefix symbol with a unit name (khertz).” — *Intro to units of measure*

**Capitalization of units: lowercase spelled out unless derived from a proper name; symbols capitalized when the unit is.**

> “With the exception of degrees Celsius, Fahrenheit, and Rankine, units of measure derived from a proper name aren’t capitalized when spelled out, but their unit symbols are capitalized. (For example, the unit symbol for joule is J.)” — *Intro to units of measure*

**Dimensions use `by`, not `x`.**

> “In general, use by, not x, to show dimensions. 3.2 by 6.0 by 11.4 in. (8.1 by 15.2 by 28.9 cm) 8.5 by 11 inches, 8.5-by-11-inch paper” … “If you use x instead of by, use the x consistently throughout a document.” — `dimensions`, p.68

**Dates: comma between day and year, comma after the year mid-sentence, no comma for month + year, cardinal numbers with a month, no slashes.**

> “Use a comma between the day of the month and the year. June 8, 2026. When you use the full date, follow the year with a comma. on June 8, 2026, at 10:00 a.m. If you give only the month and year, don’t use commas. in June 2026 at WWDC” … “Use cardinal numbers (1, 2, 3) in dates that include the month. Use ordinal numbers (1st, 2nd, 3rd) in dates without the month.” … “Don’t use the form 3/5/22, because American usage is different from European usage.” — `dates`, p.63

**Times: numerals, `a.m.`/`p.m.` lowercase, `to` for ranges in text, never `from` with an en dash.**

> “Use numerals for times of day. 2:00, 4:15, 7:30” … “In text, it’s preferable to use to with a range of times. 10:00 a.m. to 2:00 p.m., 1:30 to 3:00 p.m.” … “Don’t use from with the en dash. Correct: from 1:30 to 3:00. Incorrect: from 1:30–3:00” — `time of day`, p.204

**Phone numbers: hyphens, no parentheses, no leading 1; `toll-free number`, not `800 number`.**

> “Use hyphens in U.S. phone numbers; don’t use parentheses or a leading 1. Use toll-free number, not 800 number. For numbers with extensions, use extension or ext., not x.” — `phone numbers`, p.157

**International: currency as amount + space + ISO code; dates as ISO 8601; decimals with a period in English and thin/nonbreaking-space grouping above 999.**

> “Write the amount followed by a space and the currency code in capitals. The computer is priced at 1199 USD.” — *Currency*

> “Dates are expressed numerically as year, month, day and are separated by a hyphen. Times are expressed on a 24-hour clock.” — *Dates and times*

> “For numbers larger than 999, don’t use a period or comma as a separator. A nonbreaking space (Option-Space bar) may be used instead.” … “Use a period to produce a decimal in English.” — *Decimals*

---

## 6. Abbreviations, acronyms, and Latin abbreviations

**Spell out on first use unless the abbreviation is more familiar than the spelled-out form; put the spelled-out form first.**

> “If you think your audience might not be familiar with an abbreviation or acronym, spell out its first occurrence on a page or in a section. In user materials, spell out the term when you introduce it.” … “When you spell out a term, generally put the spelled-out version first, with the abbreviation or acronym in parentheses. internet service provider (ISP)” — `abbreviations and acronyms`, p.11

> “If the abbreviation or acronym is much more familiar than the spelled-out version, you can put the abbreviation or acronym first, followed by the spelled-out version in parentheses, or you can explain that the abbreviation is ”short for“ the spelled-out version and place the spelled-out version in italics.” — `abbreviations and acronyms`, p.11

**No periods in abbreviations — except nonmetric units of measure and `a.m.`, `p.m.`, `U.S.`**

> “Don’t use periods except in abbreviations for nonmetric units of measure and in the abbreviations a.m., p.m., and U.S. (see U.S. for exception).” — `abbreviations and acronyms`, p.11

**No apostrophe in the plural of an abbreviation; all caps for file-type abbreviations, lowercase for extensions.**

> “Don’t add an apostrophe before the s when you form the plural of an abbreviation. CDs, ICs, ISPs” … “File types: Use all caps for abbreviations of file types.” … “Filename extensions, which indicate the file type, should be in lowercase.” — `abbreviations and acronyms`, p.11

**Never abbreviate an Apple product or service name.**

> “Don’t abbreviate any Apple product or service names, whether or not the product or service is trademarked or has a service mark.” — `abbreviations and acronyms`, p.11

**Use `a` or `an` by pronunciation, not spelling.**

> “Use the article a or an with an abbreviation or acronym, depending on its pronunciation. a SAN, a USB port, an FAQ, an LCD screen” — `abbreviations and acronyms`, p.11

> “URL is pronounced ”you-are-ell“ and should be preceded by a, not an.” — `URL`, p.211

**No Latin abbreviations — write the English.**

> “Avoid using Latin abbreviations. Correct: for example, and others, and so on, and that is, or equivalent phrases. Incorrect: e.g. (for example), et al. (and others), etc. (and so on), i.e. (that is)” — `abbreviations and acronyms`, p.11

> “Don’t use; use and so forth or and so on.” — `etc.`, p.82

> “Avoid in user materials.” — `et al.`, p.82

**Don’t call an abbreviation a “short form” of something you should spell out; and don’t invent unofficial contractions.**

> “Don’t use abbreviations such as ed, edu, or HED.” — `education`, p.78

> “Don’t use 3rd-party, 3P, or other shortened forms.” — `third party (n.), third-party (adj.)`, p.203

**Spell out or reword rather than reach for a symbol.**

> “Avoid shortcuts, symbols, and abbreviations that could easily be spelled out.” — *Intro to international style*

---

## 7. Terminology, product names, and trademarks

**Use the exact product name, with its exact capitalization and spacing, every time.**

> “Follow the capitalization style of the official product name. Don’t shorten or abbreviate product names.” — `product names`, p.168

**Never pluralize or possess a trademarked name; add a generic noun instead.**

> “Plural form: Don’t use a trademarked name in the plural form. Correct: If you have more than one Mac computer… Incorrect: If you have several Macs…” … “Possessive form: Don’t use a trademarked name in the possessive form. Correct: Learn more about the features of your MacBook Pro. Incorrect: Learn more about your MacBook Pro’s features.” … “Multiple-word trademarks: If a trademark is more than one word (for example, Apple TV, iPad Pro), don’t break it across multiple lines of text.” — `trademarks (usage)`, p.207

**Never split a multiword product name; use a nonbreaking space.**

> “In many cases, you can use a nonbreaking space (Option-Space bar) to keep the name on one line.” — `trademarks (usage)`, p.207

**Don’t use trademark symbols in text or headings of user or developer materials — they belong in the copyright-page credit lines.**

> “In user and developer materials (print and electronic), don’t use trademark symbols for Apple trademarks in headings or text. Note that other types of documents, such as press releases, do use trademark symbols in text.” — `trademarks (credit lines and symbols)`, p.207

> “The name of any trademarked Apple product or service mentioned in a document must appear in the appropriate credit line on the copyright page. Categories include registered trademarks (®), trademarks (™), registered service marks (®), and service marks (SM).” — `trademarks (credit lines and symbols)`, p.207

**Use the company name correctly.**

> “The company’s official name is Apple Inc. Use Apple Inc. in copyright notices and credit lines and in communications that require the legal name of the company, such as legal documents, contracts, and forms.” … “Don’t use Apple alone to refer to products or services; always include a noun: an Apple computer, not an Apple; Apple computers, not Apples; your Apple computer’s screen, not your Apple’s screen.” — `Apple`, p.21

**Don’t use `the` before hardware product names in general references.**

> “In general references, don’t use the with the names of these hardware products: AirPods, AirPods Max, AirPods Pro, AirTag, Apple Pencil, Apple TV 4K, Apple TV HD, Apple Vision Pro, Apple Watch, Apple Watch Ultra, HomePod, HomePod mini, iMac, iPad, iPad Air, iPad mini, iPad Pro, iPhone, Mac, MacBook, MacBook Air, MacBook Pro, Mac mini, Mac Pro, Mac Studio, Magic Keyboard, Magic Mouse, Magic Trackpad, Pro Display XDR, Pro Stand, Studio Display. It’s OK to use another article or a possessive adjective: on an iPhone with Face ID, to set up your MacBook Pro. If you need to refer to a specific product, it’s OK to use the: Select the iPad you want to use as a second display.” — `product names`, p.168

> “In general, don’t use the with app names (the Finder is an exception). Correct: Open QuickTime Player. Incorrect: Open the QuickTime Player.” — `app names`, p.31

> “Don’t use the with the full name of a product whose name includes Player, unless the product name is used as an adjective modifying a noun. Correct: Use QuickTime Player to view the movie. Correct: Open the QuickTime Player app. Incorrect: Open the QuickTime Player.” — `player`, p.160

**Never replace a word in a product name with its symbol or logo.**

> “In text, don’t use the symbol in place of the word Apple, and don’t write product or service names (like Apple News+) by combining the symbol with text. Correct: Subscribe to Apple News+. Incorrect: Subscribe to News+.” — `Apple logo`, p.24

> “In text, don’t write the name Apple TV by combining the symbol with the word TV. Correct: Get started with Apple TV. Incorrect: Get started with TV.” — `Apple TV`, p.29

**Keep generic company vocabulary lowercase; capitalize only the official name.**

> “Note lowercase services. With a single subscription, customers can enjoy their favorite Apple services across all their devices.” — `Apple services`, p.28

**Use the current term, not the retired one.**

> “Don’t use; use Apple Account. See also Apple Account.” — `Apple ID`, p.24

> “This account was formerly known as Apple ID. Correct: An Apple Account gives you access to all Apple services. Incorrect: An Apple ID gives you access to all Apple services.” — `Apple Account`, p.22

**Don’t reach for a name you haven’t verified — check the company’s current guidance.**

> “Trademark status may change with time. For the most current Apple trademarks, consult the Apple trademark list.” — `trademarks (credit lines and symbols)`, p.207

---

## 8. Inclusive language

**Think about the reader’s perspective before choosing words.**

> “As you write, think about your potential audience, and try to imagine your content from their perspective. Will the words and phrases you use be understood by everyone? Do these words and phrases have any harmful or negative associations?” — *General guidelines* (Writing inclusively)

**Research a word’s origin and current use when in doubt.**

> “Investigating the history and usage of a word can help you decide whether to use it. For example, some common expressions (like grandfathered in) arose from oppressive or exclusionary contexts.” — *General guidelines*

**Judge by context, not by a blanket ban.**

> “Even if a common word has one negative use that you should avoid, it may still be acceptable in other contexts. For example, although it’s inappropriate to use mute to refer to a person who is nonspeaking, it’s OK to use it to refer to silencing a device.” — *General guidelines*

**Avoid violent, oppressive, and ableist technology terms.**

> “Don’t describe technology using terms that are inherently violent—like kill or hang. Don’t use the terms master and slave, which describe an oppressive human relationship. In addition, don’t use terms like sanity check, which associates mental health with being functional.” — *General guidelines*

**Don’t use color to carry positive or negative meaning.**

> “Avoid assigning good and bad values to colors (for example, blacklist, white hat hacker, or red team hacker) or using colors as metaphors to convey larger concepts. Use colors only to describe actual colors (for example, black text on a white background, the white point of a display).” — *General guidelines*

**Drop idioms and colloquialisms — they don’t translate and don’t travel.**

> “Common sayings—like fall through the cracks, on the same page, or backseat driver—can add flavor to writing, but they can also be difficult to understand for people who are learning the language. If your content is localized, using phrases like these can also make it more difficult to translate.” — *General guidelines*

> “To make the localization process easier, avoid idiomatic phrases such as these: nitty-gritty details, start from scratch, piggy-backing” — `localization (n., adj.)`, p.129

**Use singular `they`; never gendered defaults.**

> “Don’t use gender-specific pronouns (such as he, she, he or she, and so on) to refer to people of unspecified gender. Instead, it’s OK to use they, their, or them as a singular, gender-neutral pronoun. Correct: A subscriber can post their recipes to your shared folder. Incorrect: A subscriber can post his or her recipes to your shared folder.” — *Gender identity*

> “They always takes a plural verb, even when used as a singular pronoun.” — `pronouns`, p.170

> “Avoid binary representations of gender when you can reword using gender-neutral language. Avoid: Hiring men and women of diverse backgrounds fosters a culture of innovation. Preferable: Hiring people of diverse backgrounds fosters a culture of innovation.” — *Gender identity*

**Never assume pronouns from a name or appearance.**

> “If you refer to a specific person, don’t make assumptions about which pronouns to use based on the person’s name or appearance. If you’re unsure how to refer to someone, you can ask them.” — *Gender identity*

**Use `man` and gendered compounds only for people when gender is known and relevant.**

> “Don’t use man (or compound words that include man) to refer to people in general.” — `man`, p.135

**Disability: default to what the person prefers; identity-first and person-first are both valid.**

> “People who consider a disability or neurodivergence to be part of their identity may prefer identity-first language, which places an emphasis on culture: A Deaf person, an autistic person.” … “Others may prefer person-first language, which emphasizes the individual first, then their disability: A person who is deaf or hard of hearing, a person on the autism spectrum.” … “Preferences for identity-first and person-first language vary; when writing about specific individuals or groups, always ask them how they prefer to be identified.” — *Writing about disability*

**Never describe disability as a deficit to be overcome, and never call disabled people an exception to “normal.”**

> “Don’t use language that presents people without disabilities as the norm. For example, don’t describe nondisabled people as normal, healthy, regular, or able-bodied. Instead, you can use a person without a disability, a nondisabled person, a neurotypical person, a hearing person, and similar terms.” — *Writing about disability*

> “Avoid treating disability as something to overcome, and don’t describe people with disabilities as brave, courageous, or inspiring, which can come across as condescending.” — *Writing about disability*

**Don’t write instructions that depend on a specific sense.**

> “When writing instructions (such as in training manuals or user guides), avoid using phrases that refer to the use of specific senses, like you see a message, you see a flashing light, or you hear an alert sound. Instead, simply describe what happens: A message appears, a light flashes, an alert sound plays.” — *Writing about disability*

**Diversify examples: names, holidays, foods, sports, family structures, occupations.**

> “Include names that reflect a variety of ethnicities and genders.” … “If your content mentions examples of holidays, foods, or sports, don’t give examples only from Western culture.” … “don’t only represent a family as a woman, a man, and their biological children; remember to include a variety of family types.” — *Inclusive representation*

**Never assume “normal” users.**

> “Don’t use normal user.” — `standard user`, p.192

---

## 9. Technical notation, code font, and placeholders

**Code font for anything that is literally code, plus certain names; regular font for the punctuation around it.**

> “Use code font for all text fragments that represent expressions in a programming language.” … “Use code font for names of files, volumes, directories, and libraries.” — *Code font in text*

> “Use regular text font, not code font, for punctuation following a word or phrase in code font, unless the punctuation mark is part of the computer-language element represented. NAN(004), nan(4), and NaN are examples of acceptable input.” — *Code font in text*

**Don’t mix fonts within a word, and don’t pluralize a code-font term.**

> “Don’t mix fonts within a single word. Rewrite to avoid forming the plural of a word in code font. Correct: values of type integer. Incorrect: integer s” — *Code font in text*

**Never use a function or method name as a verb.**

> “Don’t use a function or method name as a verb. Correct: Run ls on both directories. Incorrect: ls both directories. Correct: Use cd to change to the root directory. Incorrect: cd to the root directory.” — *Code font in text*

**Syntax descriptions: code font for literals, italics for placeholders, regular text for optional brackets.**

> “Use code font for literals (parts of the language, values, and so on), italics for placeholder names, and regular text for the brackets that enclose something that’s optional. Pay close attention to punctuation. Read ([ file, ] var)” — *Syntax descriptions*

> “Use embedded caps to connect words that act as a single placeholder name (sourceFile).” — *Syntax descriptions*

**Placeholders are italic in text and are never used as ordinary English words.**

> “In running text, use italics when referring to a placeholder name (that is, an artificial term that has meaning only in your documentation and is to be replaced by a value or symbol). Spell the name just as it would appear in a syntax description. Don’t use a placeholder as you would use a regular English term. Correct: Replace volumeName with a name of up to 12 characters. Correct: The volume name can be up to 12 characters long. Incorrect: The volumeName can be up to 12 characters long.” — *Placeholder names in text*

**Avoid foo/bar/baz.**

> “Avoid foo, bar, and baz to represent hierarchical or ordered placeholder names in code examples. Instead, use names that suggest the kind of item.” — *Placeholder names in text*

**Italics: for titles, words-as-words, emphasis (lightly), placeholders, and defining terms — not for user input.**

> “Use italics to emphasize a word or phrase, but don’t overdo this use of italics.” … “Letters as letters, words as words, and phrases as phrases: Italicize.” … “Text the user types: Don’t use italics to represent what the user actually types; use quotation marks or code font, depending on your department’s style guidelines.” — `italics (n.), italic (adj.)`, p.117

**Follow the programming language’s own capitalization.**

> “When writing about a particular programming language, be careful to follow the capitalization style of that language.” — *Intro to technical notation*

**Keep code font out of structural elements in user materials.**

> “In user materials, don’t use code font in any of the following: • Part or chapter titles • Text headings • Cross-references to parts, chapters, or sections • Entries in the table of contents • Internet or web addresses • Figure ca…” — `code font`, p.52

---

## 10. International style

**Write so that a reader with limited English — and a machine translator — can follow you.**

> “Following international style helps readers with limited English proficiency read what you write. By following international style, you also help translators—human or machine—localize your writing by minimizing the burdens of cultural and customary language usage.” — *Intro to international style*

> “Write in simple structures. Don’t use idiomatic or colloquial expressions. Avoid shortcuts, symbols, and abbreviations that could easily be spelled out.” — *Intro to international style*

**Deviate from international standards only for a compelling reason.**

> “Express data using the standard international conventions outlined in this chapter. You should vary from these standards only when there’s a truly compelling advantage in using a proprietary or customary style.” — *Intro to international style*

**Never season- or hemisphere-specific time references.**

> “Because content may be viewed by a global audience, avoid referring to times of the year using the names of seasons. Preferable: coming later this year, starting early next year. Avoid: coming this fall, starting this spring” — `seasons`, p.180

**Say “country or region,” not “country.”**

> “Avoid using the term country when referring to a geographical area. Instead, use country or region or just region. Features may vary based on country or region. Some features are not available in all countries or regions.” — `country or region`, p.59

**Don’t use “America/American” for the United States.**

> “Don’t use when you mean United States.” — `America, American`, p.19

**Use ISO standards for country codes, currency, dates, language codes, and telephone numbers.**

> “Country names are represented by a two-character code.” — *Countries*

> “Currency amounts are expressed with a three-letter currency code.” — *Currency*

> “Telephone number notations begin with the plus sign and are followed by the country code, the city code, and the number.” — *Telephone numbers*

> “Language names are represented by a two-character code.” — *Languages*

**Spell out the country: no “Korea.”**

> “Don’t use. Specify South Korea or North Korea.” — `Korea`, p.122

---

## 11. Word list / substitutions

The single-word layer. Every row is a term the guide flags, with what to write instead and the guide’s own condition when one applies. A dash in the middle column means the guide gives no one-word replacement — read the condition.

**How to use:** grep this section rather than reading it (`grep -in "| \*\*yourword"`). Sorted alphabetically by the flagged term. `p.N` is the PDF page.

| Don’t write | Write instead | Condition (verbatim from the guide) | Cite |
|---|---|---|---|
| **2-byte character** | double-byte character | “Don’t use; use double-byte character.” | p.11 |
| **2-byte characters** | double-byte characters | “Not 2-byte characters.” | p.72 |
| **24x7** | 24/7 | “Not 24x7.” | p.11 |
| **2K, 4K, 5K, 6K, 8K** | — | “Don’t use a space between the numeral and the K.” | p.11 |
| **abort** | — | “Avoid in user materials.” | p.12 |
| **AC adapter** | power adapter | “Don’t use; use power adapter.” | p.13 |
| **access (as a verb)** | log in to, connect to, or a more precise term | “Avoid: Access the server using an administrator account. … Avoid: You can access the internet with your MacBook Air.” | p.13 |
| **Action pop-up menu** | — | “Don’t use.” | p.14 |
| **action sheet; sheet; popover (in user materials)** | describe what the user must select or do | “In user materials, don’t use the term action sheet, sheet, or popover; instead, describe what the user must select or do.” | p.14 |
| **activate, deactivate** | turn on, turn off | “Avoid; instead, use turn on, turn off.” | p.14 |
| **Adaptive Audio** | — | “Don’t refer to as Adaptive mode.” | p.15 |
| **adaptor** | adapter | “Not adaptor.” | p.15 |
| **adjuster** | — | “Don’t use to refer to a control that has up and down arrows, or left and right arrows, to increase or decrease a value.” | p.15 |
| **administrator** | — | “Don’t shorten to admin. To maintain the distinction between professional administrators and macOS users with administrator accounts, avoid using the noun administrator by itself to describe a person who has an administrator account in …” | p.15, 16 |
| **afterwards** | afterward | “Not afterwards.” | p.16 |
| **agent** | — | “Don’t use when referring to a person in an Apple Support position.” | p.16 |
| **agent or representative** | — | “Don’t use agent or representative.” | p.16 |
| **AirDrop** | — | “Don’t use as a verb.” | p.16 |
| **AirPlay** | — | “Don’t use as a verb.” | p.16 |
| **AirPods** | the plural form of the name nearby, and don’t use it in a prominent location, such as a heading | “In general references, don’t use the with AirPods. … Avoid using singular AirPod; instead, try to rewrite the sentence. … If you do use singular AirPod, use the plural form of the name nearby, and don’t use it in a prominent location, such …” | p.16 |
| **AirPort** | — | “Don’t precede these app names with the. • Hardware: AirPort hardware includes the AirPort Express Base Station, the AirPort Extreme Base Station, and AirPort Time Capsule.” | p.17 |
| **AirPort Express Base Station** | — | “to AirPort Express, but don’t use AirPort Extreme unless you’re referring to the technology. … Use lowercase for base station if you don’t use the full product name. … Correct: Avoid placing the base station near sources of interference. …” | p.17 |
| **aliased** | — | “Don’t use aliased.” | p.18 |
| **allow** | — | “Avoid using allow when you can restructure a sentence to make the reader the subject. Avoid: FileMaker Pro allows you to create a database.” | p.18 |
| **alphabet column** | index | “Don’t use to refer to the vertical column of letters at the right side of a list in some iOS apps; use index.” | p.18 |
| **Alt key** | — | “Don’t use, except when you give instructions for Windows users.” | p.19 |
| **ambient light sensor** | — | “Don’t use ALS.” | p.19 |
| **America, American** | — | “Don’t use when you mean United States.” | p.19 |
| **and/or** | — | “Rewrite to avoid this construction. Correct: document and app icons Avoid: document and/or app icons” | p.19 |
| **antennae in relation to wireless products** | antenna, antennas | “Not antennae in relation to wireless products.” | p.19 |
| **antialiasing (n., adj.), antialiased** | — | “Don’t use antialias as a verb.” | p.20 |
| **App Library** | — | “Don’t precede with the.” | p.31 |
| **app names** | — | “In general, don’t use the with app names ( the Finder is an exception).” | p.31 |
| **App Store** | — | “Avoid constructions like Apple Watch App Store and Apple TV App Store.” | p.31 |
| **appear** | — | “In a task, avoid stating that an item appears; if necessary for clarity, try to work it into the context of the task. 1.” | p.21 |
| **appendices** | appendixes | “Not appendices.” | p.21 |
| **Apple** | — | “Don’t use Apple alone to refer to products or services; always include a noun: an Apple computer, not an Apple; Apple computers, not Apples; your Apple computer’s screen, not your Apple’s screen.” | p.21 |
| **Apple Card** | — | “Don’t precede with the or an.” | p.23 |
| **Apple computer** | — | “Avoid where Mac computer would work.” | p.23 |
| **Apple Creator Studio** | — | “Don’t precede with the.” | p.23 |
| **Apple Fitness+** | — | “Don’t use Apple Fitness Plus or other variations.” | p.24 |
| **Apple Games app** | — | “Don’t use just Games or the Games app.” | p.24 |
| **Apple ID** | Apple Account | “Don’t use; use Apple Account.” | p.24 |
| **Apple Intelligence** | — | “Don’t abbreviate as AI.” | p.24 |
| **Apple logo** | — | “In text, don’t use the symbol in place of the word Apple, and don’t write product or service names (like Apple News+ ) by combining the symbol with text.” | p.24 |
| **Apple News+** | — | “Don’t use Apple News Plus or other variations.” | p.26 |
| **Apple Online Store** | — | “Don’t use.” | p.26 |
| **Apple Pencil** | — | “In general references, don’t use the with Apple Pencil.” | p.27 |
| **Apple Pencil hover** | — | “Don’t use hover as a verb when describing the feature.” | p.27 |
| **Apple Retail Store** | — | “Don’t use.” | p.27 |
| **Apple Store** | — | “It’s OK to use terms such as retail store and retail location; don’t use Apple Retail Store. … Don’t use Apple Store in the plural or possessive form.” | p.28 |
| **Apple Support** | — | “Don’t shorten to Support.” | p.28 |
| **Apple Trade In** | — | “Capitalize and don’t use a hyphen when referring to the Apple program.” | p.29 |
| **Apple Vision Pro** | — | “In general references, don’t use the with Apple Vision Pro. … Don’t refer to Apple Vision Pro as a headset.” | p.30 |
| **Apple Watch** | — | “In general references, don’t use the with Apple Watch. … Don’t use Watch.” | p.30 |
| **AppleCare** | the specific product name or use AppleCare product or AppleCare products | “Don’t use AppleCare alone to refer to AppleCare products; use the specific product name or use AppleCare product or AppleCare products.” | p.23 |
| **Apple TV app** | — | “Apple TV+ Don’t use.” | p.29 |
| **Apple TV 4K** | — | “Don’t use Apple TV alone to refer to the hardware device. … Not all features are available on all Apple TV models. … In general references, don’t use the with Apple TV 4K. … Don’t abbreviate Apple TV 4K as ATV 4K.” | p.29 |
| **arrow keys** | — | “Don’t use direction keys.” | p.32 |
| **arrowhead** | — | “Don’t use to refer to the arrow pointer.” | p.32 |
| **Assistant** | — | “Capitalize, and don’t use the, when the word is part of a full name.” | p.33 |
| **assure** | — | “Don’t use when you mean ensure.” | p.33 |
| **asynchronous progress indicator** | — | “Developer materials: Don’t use the asynchronous progress indicator for processes that start out indeterminate but could become determinate.” | p.33 |
| **attach** | — | “Don’t use to mean connect (as in Connect the USB device to your computer ).” | p.33 |
| **a hyphen in compounds with audio or video** | audio editing app, video editing app (no hyphen) | “Close up the following words beginning with audio: audiobook, audiocassette, audiotape, audiovisual Don’t use a hyphen in compound adjectives that include audio: audio editing app.” | p.33 |
| **autism (n.), autistic** | traits | “It’s OK to use on the autism spectrum or on the spectrum; avoid using autism spectrum disorder or ASD unless you’re writing specifically about a medical diagnosis. Avoid saying that people have symptoms of autism; instead, use traits. …” | p.34 |
| **Auto Unlock** | — | “Use only as the feature name; don’t use as a verb.” | p.35 |
| **autosave** | — | “Don’t use as a verb.” | p.35 |
| **avatar** | — | “Don’t use avatar.” | p.157 |
| **backwards compatibility** | backward compatibility | “Not backwards compatibility.” | p.36 |
| **backwards when you refer to direction** | backward | “Not backwards when you refer to direction.” | p.36 |
| **badge** | — | “If there’s a problem, a badge with an exclamation point appears on the app icon: Don’t use badge as a verb or badged as an adjective.” | p.36 |
| **based** | — | “Windows XP–based computer Don’t use a hyphen or an en dash in predicate adjectives that include based.” | p.37 |
| **battery level** | — | “Don’t use power level or battery charge level.” | p.37 |
| **bit** | pixel, dot | “Don’t use when you mean pixel or dot.” | p.38 |
| **bit resolution** | bit depth | “Don’t use; use bit depth.” | p.38 |
| **black box/white box** | — | “Avoid using to refer to a type of device or system, or a method of testing.” | p.39 |
| **black hat/white hat** | — | “Don’t use to describe a type of hacker.” | p.39 |
| **black/white** | — | “Don’t use black or white in a way that has a positive or negative connotation.” | p.39 |
| **blacklist/ whitelist** | deny, allow, and so on ( you can deny IP addresses to prevent them from accessing the server ) | “Don’t use blacklist/ whitelist. … Don’t use deny list and allow list as verbs; instead, use deny, allow, and so on ( you can deny IP addresses to prevent them from accessing the server ). … Don’t use deny listed and allow listed; instead, …” | p.64 |
| **blacklist/whitelist** | — | “Don’t use.” | p.39 |
| **blank character** | space character | “Don’t use; use space character.” | p.39 |
| **blank or blank character** | space character | “Not blank or blank character.” | p.190 |
| **Bluetooth** | — | “Don’t use Bluetooth as a noun. … Don’t use a hyphen with Bluetooth.” | p.40 |
| **board** | — | “Don’t use when you mean card.” | p.40 |
| **Book Store** | — | “Don’t use Apple Books store, Apple Books Store, Apple Book Store, or Apple Bookstore.” | p.40 |
| **boot** | — | “Don’t use for start up or switch on except in server materials.” | p.41 |
| **boot chime** | — | “Don’t use for the chord heard during a successful startup sequence.” | p.41, 192 |
| **boot disk** | — | “Don’t use except in server materials.” | p.41 |
| **box** | dialog | “Don’t use dialog box; use dialog.” | p.41 |
| **bps** | — | “Don’t use as the abbreviation for bits per second.” | p.41 |
| **square brackets** | brackets | “Don’t use brackets when you mean angle brackets (< >).” | p.41 |
| **bridge** | — | “Don’t use interchangeably with router.” | p.41 |
| **browseable** | browsable | “Not browseable.” | p.42 |
| **bug** | problem, condition, issue, or situation instead | “Avoid; use problem, condition, issue, or situation instead.” | p.42 |
| **built-to-order** | build-to-order | “Not built-to-order.” | p.42 |
| **bus-powered, self-powered** | — | “In user materials, try to avoid when indicating whether devices draw power from a power cord or from another USB device.” | p.42 |
| **cable** | cables | “Don’t use cabling even when you mean cable collectively; use cables.” | p.44 |
| **camcorder** | — | “Don’t use video camera when you mean camcorder.” | p.44 |
| **capability** | — | “If possible, avoid capability when you discuss features of software or hardware.” | p.45 |
| **caret** | — | “Don’t use caret when you mean circumflex.” | p.47 |
| **CarPlay Dashboard** | — | “Don’t use CarPlay as a verb.” | p.48 |
| **carriage return character, except in developer materials when you’re referring to ASCII character $0D** | return character | “Not carriage return character, except in developer materials when you’re referring to ASCII character $0D.” | p.176 |
| **catalog** | — | “Don’t use this term in user materials.” | p.48 |
| **Catalyst** | Mac Catalyst | “Don’t use; use Mac Catalyst.” | p.48 |
| **CD audio disc** | audio CD | “Not CD audio disc.” | p.34 |
| **cell phone, cellular phone** | mobile phone | “Don’t use; use mobile phone.” | p.48 |
| **central memory** | main memory | “Not central memory.” | p.135 |
| **check, checked, unchecked (for checkboxes)** | select, deselect; selected, unselected | “Don’t use when you mean the action of selecting a checkbox.” | p.49 |
| **Check In** | send a Check In or similar | “Don’t use Check In as a verb; use send a Check In or similar.” | p.49 |
| **child’s Apple Account** | — | “Don’t use child Apple Account.” | p.50 |
| **clamshell** | lid | “Don’t use to refer to the lid of a laptop computer or device case (such as an AirPods case); use lid.” | p.50 |
| **clean install** | clean installation | “Not clean install.” | p.50 |
| **click** | press and release | “Don’t use click on. Don’t say click the mouse or click the trackpad; instead, use press and release.” | p.51 |
| **click and drag** | — | “Don’t use.” | p.51 |
| **click and hold** | force click | “Don’t use click and hold to refer to the act of pressing deeper on a Force Touch trackpad; use force click.” | p.51 |
| **click on** | click | “Don’t use; use click.” | p.51 |
| **cloud** | — | “Avoid using the cloud to refer to iCloud.” | p.52 |
| **coax** | — | “Don’t use when you mean coaxial.” | p.52 |
| **CODEC** | codec | “Not CODEC.” | p.52 |
| **color picker** | — | “Don’t use.” | p.54 |
| **colored (for items on the screen)** | describe the item, not its color | “Don’t use to describe items on the screen.” | p.54 |
| **colored pixels** | color pixels | “Not colored pixels.” | p.54 |
| **command names** | — | “Don’t include the ellipsis when you refer to the command name in text or text headings.” | p.55 |
| **Command-key equivalent** | keyboard shortcut even when all the combinations use the Command key | “Don’t use; use keyboard shortcut even when all the combinations use the Command key.” | p.55 |
| **companion iPhone** | — | “Don’t use.” | p.56 |
| **Compass Waypoints** | — | “Don’t use compass waypoint.” | p.56 |
| **complications** | — | “However, in most cases, avoid using any specific term to refer to these features; simply discuss them generically—for example, you can add an alarm to the watch face, not you can add an alarm complication to the watch face.” | p.56 |
| **comprise** | — | “This word is misused so often that correct usage might confuse the reader; avoid it altogether.” | p.56 |
| **connect** | — | “Use to refer to the act of joining devices together; don’t use attach, hook up, or mate.” | p.56 |
| **Control Center** | — | “Don’t precede with the.” | p.58 |
| **control key** | modifier key | “Don’t use in a general sense; use modifier key.” | p.58 |
| **convert into** | convert to | “Not convert into.” | p.58 |
| **cookie files** | cookies | “Not cookie files.” | p.58 |
| **corrupted** | — | “Avoid if possible.” | p.59 |
| **country** | country or region; region | “Avoid using the term country when referring to a geographical area.” | p.59 |
| **crash** | quits unexpectedly, doesn’t respond, or stops responding | “Don’t use; use quits unexpectedly, doesn’t respond, or stops responding.” | p.60 |
| **CTRL** | — | “Don’t use CTRL.” | p.58 |
| **curly brackets** | braces | “Don’t use curly brackets to describe these symbols: { }; use braces.” | p.61 |
| **cursor** | insertion point or pointer, depending on the context | “Don’t use in describing the macOS or iOS interface; use insertion point or pointer, depending on the context.” | p.61, 162 |
| **custom install** | custom installation | “Not custom install.” | p.61 |
| **data** | — | “In user materials, avoid in favor of information if information makes sense in the context. … Not collective and thus plural: Selected data are transferred immediately.” | p.62 |
| **date picker** | — | “Don’t use.” | p.62 |
| **daughter board** | expansion board | “Don’t use; use expansion board.” | p.63 |
| **daughter board or piggyback board** | expansion board | “Not daughter board or piggyback board.” | p.83 |
| **daylight savings time** | daylight saving time | “Not daylight savings time.” | p.63 |
| **deaf or hard of hearing, Deaf** | — | “Don’t use hearing impaired.” | p.64 |
| **deafblind, Deafblind** | — | “Don’t use deaf and dumb, mute, or deaf-mute.” | p.63 |
| **dealer, dealership** | Apple Authorized Reseller | “Don’t use; use Apple Authorized Reseller.” | p.64 |
| **deejay** | DJ | “Don’t use; use DJ.” | p.64 |
| **dehighlight, dehighlighted** | — | “Don’t use.” | p.64 |
| **DEL key** | Delete key | “Not DEL key.” | p.64 |
| **DELETE character or rubout character** | DEL character | “Not DELETE character or rubout character.” | p.64 |
| **depress** | press | “Don’t use; use press.” | p.65 |
| **deselect** | — | “Not uncheck, unselect, unhighlight, or dehighlight.” | p.65 |
| **desire** | — | “Don’t use.” | p.65 |
| **desired** | your; the: make your changes, select the folder | “Try to avoid.” | p.65 |
| **device** | — | “You can also use device: • To refer to a category of hardware products: iOS device, iPadOS device, iOS and iPadOS devices, Android device • To refer to more than one of a specific device (to avoid making a trademarked name plural) …” | p.66 |
| **diacritic** | diacritical mark | “Not diacritic.” | p.66 |
| **dialog** | — | “Don’t use dialog box. … Although a dialog can be implemented as a sheet attached to a window, don’t use sheet in user materials.” | p.66 |
| **dialog box** | dialog | “Don’t use; use dialog.” | p.67 |
| **dialog message** | message | “Don’t use; use message.” | p.67 |
| **different than** | different from | “Not different than.” | p.67 |
| **differently than** | — | “Don’t use different than,” | p.67 |
| **digital** | — | “Don’t use a hyphen in compound adjectives beginning with digital: digital video editing, digital media apps. Don’t use digital apps or digital applications.” | p.67 |
| **direction keys** | arrow keys | “Don’t use; use arrow keys.” | p.68 |
| **disability** | — | “Avoid terms like differently abled, people with special needs, people with special abilities, and people of all abilities.” | p.68 |
| **disable (v.), disabled** | turn off or deselect | “Don’t use disable to refer to turning off a feature or deselecting an option; use turn off or deselect. … Don’t use disabled to describe features that are turned off or unavailable; use turned off, unavailable, or inactive.” | p.68 |
| **disclosure arrow** | — | “Avoid: You can click the closed disclosure arrow (pointing to the right) to reveal more information.” | p.69 |
| **disk name** | — | “Use when you refer to the name that appears below a disk’s icon on the desktop; don’t use disk title for this purpose.” | p.70 |
| **display** | — | “Don’t use when you mean desktop or screen.” | p.70 |
| **display port** | — | “Don’t use monitor port.” | p.70 |
| **division symbol** | division sign | “Not division symbol.” | p.70 |
| **do** | — | “Don’t use in phrases such as do a clean installation.” | p.70 |
| **Do Not Disturb** | — | “To stop notifications, turn on Do Not Disturb.” | p.72 |
| **dock, docked (as a verb)** | the device is in the Dock | “In user materials, don’t use dock as a verb; devices are in the dock, not docked. Don’t use dockable.” | p.71 |
| **document** | — | “A document is a particular type of file; don’t use document when the file could be of another type.” | p.71 |
| **document window** | document or window, not both | “Don’t use; use document or window, not both.” | p.71 |
| **dot** | — | “Don’t use bit when referring to the components of a pixel.” | p.72 |
| **double layer (n.), double-layer** | double-click | “Don’t use to refer to quickly pressing a mechanical button twice; use double-click.” | p.73 |
| **download (n., v.), downloadable** | an alternative such as keep up to date, or say that content appears automatically | “Avoid using download to refer to what iCloud does; instead, use an alternative such as keep up to date, or say that content appears automatically. Avoid: iCloud downloads your new photos to all your devices.” | p.74 |
| **drag** | — | “Don’t use drag the mouse or drag the pointer. … Don’t use click and drag. … Don’t use place, put, or move when you mean drag. … Don’t use tap and drag. … Don’t say drag your finger.” | p.74 |
| **drag and drop (n., v.), drag-and-drop** | — | “Avoid using drag and drop as a compound verb followed by an object; dragging includes dropping the item into place.” | p.75 |
| **drag handle** | handle | “Don’t use; use handle.” | p.75 |
| **drive** | — | “Don’t use drive when you mean disk or disc.” | p.76 |
| **driver** | software instead ( printer software ) | “In user materials, avoid using driver; use software instead ( printer software ).” | p.76 |
| **drop-down menu** | menu | “Don’t use; use menu.” | p.76 |
| **dual-layer** | — | “Don’t use.” | p.76 |
| **dual-processor** | — | “Don’t use a dual processor or DP.” | p.76 |
| **duckhead** | — | “Don’t use.” | p.76 |
| **due to** | alternatives such as caused by or because of | “Avoid; instead, use alternatives such as caused by or because of. Avoid: The interference was due to a faulty cable.” | p.77 |
| **dummy** | — | “Don’t use.” | p.77 |
| **DV** | — | “Don’t use DV to refer to the medium digital video.” | p.77 |
| **DVD drive** | optical drive | “Avoid; use optical drive.” | p.77 |
| **e.g.** | for example or such as | “Don’t use; use for example or such as.” | p.78 |
| **lower, higher, newer, older (for software versions)** | earlier, later | “Use to refer to versions of software; don’t use lower and higher or newer and older.” | p.77 |
| **edit menu, Edit menu** | — | “Avoid using edit menu (lowercase) in user materials; simply describe what people should choose from the menu.” | p.78 |
| **education** | — | “K–12 education, higher education, Apple education pricing, Apple education representative Don’t use abbreviations such as ed, edu, or HED.” | p.78 |
| **eject (trans. v.)** | — | “Don’t use as an intransitive verb.” | p.78 |
| **enable (v.), enabled** | — | “Avoid when you mean turn on. … Don’t use enabled when you mean selected (for example, when you refer to radio buttons or checkboxes) or available (when you refer to commands or buttons that are sometimes dimmed, but not in this case). … Don’t …” | p.80 |
| **entitled** | titled, named, or called | “Don’t use; use titled, named, or called.” | p.81, 205 |
| **EPUB** | ebook | “Don’t use as a noun; to refer generically to an electronic book, use ebook.” | p.82 |
| **equal’s sign, equals sign, or equal symbol** | equal sign | “Not equal’s sign, equals sign, or equal symbol.” | p.82 |
| **error message** | — | “Don’t use except in developer materials.” | p.82 |
| **error message except in developer materials** | — | “Avoid error message except in developer materials. … In specific situations, however, avoid the word alert if you can simply describe what happens.” | p.17 |
| **Esc key** | — | “When you describe escape sequences, don’t use a hyphen between names of keys (because the user presses and releases the keys separately).” | p.82 |
| **et al.** | — | “Cooper et al., “Reader Preferences for Report Typefaces,…” Avoid in user materials.” | p.82 |
| **etc.** | and so forth or and so on | “Don’t use; use and so forth or and so on.” | p.82 |
| **exit** | quit | “In user materials, don’t use to refer to quitting an open app; use quit.” | p.83 |
| **EyeSight** | the front display or just the front | “Don’t precede with the. … Don’t use EyeSight to refer to the front display of Apple Vision Pro; instead use the front display or just the front.” | p.83 |
| **FaceTime** | — | “Don’t use as a verb.” | p.83 |
| **family controls** | parental controls | “Don’t use; use parental controls.” | p.83 |
| **Family Sharing** | — | “Don’t use iCloud Family Sharing.” | p.83 |
| **female** | — | “Don’t use to describe a type of connector.” | p.84 |
| **female connector** | — | “Don’t use female connector.” | p.189 |
| **file extension** | — | “You can shorten filename extension to extension if the meaning is clear, but don’t use file extension. … Don’t use filename extensions to refer to file types.” | p.86 |
| **file format** | file type | “In user documentation, don’t use to refer to a specific kind of file, such as a JPEG file; use file type.” | p.85 |
| **file types** | — | “Don’t use file format (a file’s structure and method of storing data) when you mean file type.” | p.87 |
| **we, us, I** | rewrite in terms of the reader or the product | “Don’t use the first-person pronouns we, us, or I; rewrite in terms of the reader or the product.” | p.87, 217 |
| **flashing** | blinking for this purpose | “Don’t use to describe the insertion point; use blinking for this purpose.” | p.88 |
| **flashing for this purpose** | — | “Don’t use flashing for this purpose.” | p.40 |
| **Focus** | Focus options | “Don’t use an article when referring to the feature, but use an article when referring to an individual Focus. … Don’t use the plural ( Focuses ); use Focus options. … Users can choose, turn on, or use a Focus (don’t use activate ). … When a …” | p.88 |
| **font** | — | “Don’t use font family, typeface, or face.” | p.89 |
| **the prime symbol ′ for feet** | foot, ft. | “Don’t use the symbol ′ unless space limitations prevent the use of foot or ft.” | p.89 |
| **Force Touch** | force click or press harder | “Don’t use Force Touch as a verb; use force click or press harder.” | p.89 |
| **form factor** | design, enclosure, or another term | “Avoid; use design, enclosure, or another term.” | p.89 |
| **free (for memory or storage space)** | available | “Don’t use to refer to available memory or storage space; use available.” | p.90 |
| **freeze** | — | “Avoid using freeze as a noun or to refer to something the computer does.” | p.91 |
| **FTP** | transfer files instead | “Avoid as a verb; use transfer files instead.” | p.91 |
| **full** | — | “Use a hyphen in compound adjectives beginning with full. full-duplex, full-featured, full-height, full-page, full-screen, full-size Don’t use a hyphen with fully. fully buffered, fully charged, fully loaded” | p.91 |
| **functionality** | a word such as features | “In user materials, avoid if you can use a word such as features instead. Avoid: Some functionality is not available in certain regions.” | p.91 |
| **future compatibility or upward compatibility** | forward compatibility | “Not future compatibility or upward compatibility.” | p.90 |
| **gaze** | — | “Don’t use gaze.” | p.130 |
| **gen, G (for generation)** | generation; 10th-generation iPad | “Don’t shorten generation to gen or G—for example, 10th-gen iPad or iPad 9G.” | p.93 |
| **finger gestures; finger (in gesture instructions)** | gestures; Swipe left or right. | “Don’t refer to them as finger gestures; use simply gestures.” | p.93 |
| **Get Info window or Info box** | Info window | “Not Get Info window or Info box.” | p.110 |
| **grandfathered, grandfathered in** | an alternative that’s appropriate to the context, such as legacy, exempt, or preexisting | “Don’t use; use an alternative that’s appropriate to the context, such as legacy, exempt, or preexisting.” | p.95 |
| **graphics card** | — | “Don’t use when referring to Apple products with Apple silicon, which have an integrated GPU built into the chip.” | p.96 |
| **grayed** | dimmed | “Don’t use; use dimmed.” | p.96 |
| **grey** | gray | “Not grey.” | p.96 |
| **GUI** | — | “Don’t use.” | p.96 |
| **handicapped** | — | “Don’t use to refer to people with disabilities.” | p.97 |
| **handle** | — | “Don’t use drag handle.” | p.97 |
| **hang** | a phrase such as not responding | “Don’t use as a description of the computer’s behavior in response to a system error; use a phrase such as not responding.” | p.98 |
| **haptic (adj.), haptics** | — | “Avoid using haptic or haptics when you can reword to describe what the user feels. … Avoid: You receive a haptic alert when your message is sent.” | p.98 |
| **hard copy** | a term such as printout, print version, or printed document | “Avoid; use a term such as printout, print version, or printed document.” | p.98 |
| **headset** | — | “Don’t use to refer to Apple Vision Pro.” | p.99 |
| **hearing impaired** | — | “Don’t use.” | p.99 |
| **help** | — | “Don’t use when referring to documentation that has user guide in its title—even if the user guide can be opened from the Help menu.” | p.100 |
| **hex as a short form** | — | “In user materials, don’t use hex as a short form.” | p.100 |
| **HFS+** | HFS Plus | “Not HFS+.” | p.100, 133 |
| **HFS+ (Journaled)** | HFS Plus (Journaled) | “Not HFS+ (Journaled).” | p.100 |
| **hi-res** | high resolution (n.), high-resolution | “Not hi-res.” | p.101 |
| **highlight** | — | “Don’t use when you mean select. … Don’t use as an intransitive verb.” | p.100 |
| **highlighting** | — | “Don’t use in user materials.” | p.101 |
| **hilighted** | highlighted | “Not hilighted.” | p.101 |
| **Hindi** | Devanagari | “Don’t use when you refer to the writing system used to represent Hindi and several other Asian languages; use Devanagari.” | p.101 |
| **hit** | — | “Don’t use when talking about search results.” | p.101 |
| **hold down** | press and hold | “Don’t use to describe the act of pressing the mouse or trackpad, a key on the keyboard, or a mechanical button until an action or result occurs.” | p.101 |
| **HomePod** | — | “In general references, don’t use an article with HomePod.” | p.102 |
| **hover** | — | “Avoid using hover over to describe the act of holding the pointer over an onscreen element until something occurs. … Avoid: Hover over a participant’s name, and then click the More button. … Don’t use hover the pointer over.” | p.103 |
| **HUD** | — | “Avoid unless the term appears in the user interface.” | p.103 |
| **hypertext link** | link | “Don’t use; use link.” | p.104 |
| **i.e.** | that is | “Don’t use; use that is.” | p.108 |
| **iCloud** | on to refer to where users can access content ( on iCloud.com) | “In user materials, avoid referring to iCloud as a service; simply call it iCloud. In addition, avoid referring to iCloud features (such as iCloud Mail, iCloud Calendar, or Find My) as services or web apps; refer to them as features, or …” | p.105 |
| **iCloud Photo Library** | iCloud Photos | “Don’t use; use iCloud Photos.” | p.106 |
| **iCloud Photo Sharing** | Shared Albums | “Don’t use; use Shared Albums. … Don’t use iCloud Plus or other variations.” | p.106 |
| **iCloud Photos** | — | “Don’t use iCloud Photo Library, iCloud photo library, or your iCloud Photos.” | p.106 |
| **if necessary** | — | “Avoid in user materials.” | p.108 |
| **Image Wand** | — | “Don’t precede with the.” | p.108 |
| **imbed** | embed | “Not imbed.” | p.79, 109 |
| **iMovie** | — | “Don’t use iMovie when you mean movie or project.” | p.109 |
| **Important** | — | “Avoid using an Important notice immediately before or after a note, Warning notice, or another Important notice, or immediately after a text heading.” | p.109 |
| **in order to** | just to | “Don’t use unless absolutely necessary; use just to.” | p.110 |
| **inch (in.)** | — | “Don’t use the symbol " unless space limitations prevent the use of inch or in.” | p.109 |
| **incrementer** | — | “Don’t use to refer to a control that has up and down arrows, or left and right arrows, to increase or decrease a value.” | p.110 |
| **indices, unless you mean mathematical indices** | indexes | “Not indices, unless you mean mathematical indices.” | p.110 |
| **input** | enter or type, depending on the context | “Avoid using as a verb; instead, use enter or type, depending on the context.” | p.110 |
| **inside of** | inside | “Not inside of.” | p.111 |
| **install** | — | “Don’t use install as a noun.” | p.111 |
| **installation** | — | “Don’t use install when you mean installation.” | p.111 |
| **Intel** | — | “Don’t use terms such as Intel Mac.” | p.112 |
| **Intel Core** | — | “Don’t use terms such as Intel Core Mac.” | p.112 |
| **Intel Xeon** | — | “Don’t use terms such as Intel Xeon Mac.” | p.112 |
| **interface** | — | “Don’t use user interface in user materials.” | p.112 |
| **inverted** | — | “Don’t use when you mean highlighted.” | p.113 |
| **invite (v.), invitation** | — | “Don’t use invite as a noun in place of invitation.” | p.113 |
| **iOS device** | — | “Avoid using mobile device when referring to iOS devices ( mobile device could refer to devices made by other companies). … If you list devices by name, list them in the same order throughout a document—for example, always iPhone, iPad, and …” | p.113 |
| **iPad** | — | “In general references, don’t use the with iPad. … Don’t shorten generation to gen or G—for example, 10th-gen iPad or iPad 10G.” | p.114 |
| **iPadOS device** | — | “Avoid using mobile device when referring to iPadOS devices ( mobile device could refer to devices made by other companies).” | p.115 |
| **iPhone** | — | “In general references, don’t use the with iPhone. … Don’t refer to iPhone as phone for short; always use iPhone or the specific model name (iPhone 14, iPhone 15 Pro Max, and so on). … Don’t use lowercase.” | p.116 |
| **iPod** | — | “In general references, don’t use an article with iPod touch. … Don’t shorten generation to gen or G; for example, seventh-gen iPod touch or iPod touch 7G.” | p.117 |
| **iTunes Music Store or iTunes App Store** | iTunes Store | “Not iTunes Music Store or iTunes App Store.” | p.118 |
| **jack** | — | “Don’t use connector to refer to a jack.” | p.118 |
| **jargon** | — | “Avoid jargon whenever possible.” | p.118 |
| **justification** | alignment | “Don’t use to refer to the alignment of text to the right or left margin; use alignment.” | p.119 |
| **K** | KB | “Don’t use; use KB.” | p.119 |
| **key, keys** | — | “In general, don’t use articles and the word key in references to keys. … Don’t use a hyphen if each key should be pressed and released separately. … Don’t abbreviate any other key names, except when space is very tight (in table headings, for …” | p.120 |
| **keyboard equivalent** | keyboard shortcut | “Don’t use; use keyboard shortcut.” | p.120 |
| **Keynote’s slides )** | — | “Susan Torres’s biography [singular] the Joneses’ computer [plural] • Product names: Rewrite to avoid forming a possessive of any product name, trademarked or not (for example, don’t use Keynote’s slides ).” | p.163 |
| **kill** | — | “Don’t use to refer to stopping an app or process.” | p.122 |
| **Korea** | — | “Don’t use.” | p.122 |
| **labelled, labelling** | labeled, labeling | “Not labelled, labelling.” | p.122 |
| **landing page or portal** | — | “Don’t use landing page or portal. Don’t use homepage to refer to an entire website.” | p.102 |
| **latest** | — | “Don’t use to refer to a specific software update.” | p.123 |
| **launch** | — | “Avoid in user materials when you mean to open an app.” | p.123 |
| **Launchpad** | — | “Don’t use in content about macOS 26 or later.” | p.123 |
| **LED** | indicator light | “Not LED.” | p.110, 123 |
| **left arrow** | — | “Don’t call it the left arrow button or the left-pointing arrow. … Don’t use when you mean Back button.” | p.123 |
| **left-hand** | left | “Avoid except in reference to left-hand (verso) pages; use just left whenever possible.” | p.124 |
| **left-hand side** | left side | “Not left-hand side.” | p.124 |
| **let** | — | “Avoid: The Up Next button lets you see which songs will play next.” | p.124 |
| **level 2 cache, level 3 cache** | — | “Don’t use secondary cache or second-level cache when you mean L2 cache.” | p.125 |
| **like, love** | — | “To avoid ambiguity, you can also say mark an item as liked, an item is marked as loved, or similar.” | p.125 |
| **follow a link** | click a link | “Avoid using follow a link; use click a link instead.” | p.125 |
| **Liquid Glass** | — | “Don’t precede with the.” | p.126 |
| **Live Photos** | alternatives such as you see only the still image | “Avoid referring to any part of a Live Photo as video. … Avoid: If you set a Live Photo as your watch face, the video plays when you raise your wrist. … Avoid: A Live Photo captures a still image, along with a few moments of video before and …” | p.127 |
| **Live Text** | — | “Don’t use to refer to the text users interact with.” | p.128 |
| **lo bit or lo-bit** | low-order bit | “Not lo bit or lo-bit.” | p.131 |
| **lo-res** | low resolution (n.), low-resolution | “Not lo-res.” | p.131 |
| **localizable** | — | “Don’t use.” | p.128 |
| **localization** | — | “Many Apple publications and user materials written in English go through the localization process, which involves revision and translation for non-English- speaking users. • Idiomatic language: To make the localization process easier, …” | p.129 |
| **log on, log off** | log in and log out | “Don’t use; use log in and log out.” | p.130 |
| **logical operators** | — | “Don’t use as verbs.” | p.129 |
| **long press (n.), long-press** | — | “Don’t use long press in user materials.” | p.130 |
| **low bit (n.), low-bit** | — | “Not lo bit or lo-bit.” | p.131 |
| **M-series chips** | — | “To refer to devices with an M-series chip, you can use terms such as Mac with the M5 chip and iPad Pro with M4; don’t use M5 Mac, M4 iPad, or other variations. Don’t refer to an M-series chip as a processor.” | p.145 |
| **Mac** | — | “Use Mac to refer to Mac computers and related products ( Mac software, Mac apps ). • Articles: In general references, don’t use the with Mac or the names of specific Mac models. … Slide the Mac Pro you’re troubleshooting out of the rack. • …” | p.131 |
| **Mac App Store** | — | “Don’t abbreviate as MAS. … To prevent confusion, avoid using the store if you’re discussing the App Store for different platforms (for example, the Mac App Store and the App Store for iPhone).” | p.132 |
| **Mac Catalyst** | — | “Don’t use Catalyst alone. … Don’t use Mac Catalyst as an adjective.” | p.132 |
| **Mac operating systems** | — | “Don’t use Mac OS to refer generically to the operating system.” | p.132 |
| **Mac Virtual Display** | — | “Don’t precede with the.” | p.134 |
| **machine** | — | “Don’t use when you mean computer.” | p.132 |
| **machine or unit** | — | “Don’t use machine or unit.” | p.56 |
| **macOS Server** | version numbers only | “Use only to refer to the software; don’t use to refer to a computer with macOS Server installed. … In developer materials, don’t use version names such as Snow Leopard; use version numbers only.” | p.134 |
| **Mac OS Extended (Journaled) format** | — | “It’s OK to define the format parenthetically as Journaled HFS Plus on first occurrence, but don’t use HFS+ (Journaled).” | p.133 |
| **maintenance release or dot release** | — | “Don’t use maintenance release or dot release.” | p.211 |
| **male** | — | “Don’t use to describe a type of connector.” | p.135 |
| **male connector** | plug | “Not male connector.” | p.161 |
| **man** | — | “Don’t use man (or compound words that include man) to refer to people in general. staff, workforce ( not manpower) work hours, people hours ( not man hours) artistry, craft ( not craftsmanship) unstaffed ( not unmanned)” | p.135 |
| **man-in-the-middle attack** | — | “Don’t use.” | p.135 |
| **Managed Apple ID** | Managed Apple Account | “Don’t use; use Managed Apple Account.” | p.135 |
| **master** | — | “For this reason, avoid using master when referring to the following: • The default branch of a source repository.” | p.136 |
| **master branch** | main branch | “Don’t use to refer to the default branch of a source repository; use main branch.” | p.136 |
| **master-detail** | list-detail or navigation-detail | “Don’t use; use list-detail or navigation-detail.” | p.136 |
| **master/slave** | — | “Don’t use to describe the relationship between two devices or processes. … Don’t use alternatives that retain the term master (such as master/helper ) or use the term worker (such as master/worker ).” | p.136 |
| **mate** | — | “Don’t use to refer to connecting hardware.” | p.136 |
| **maximize** | make active | “Don’t use to refer to clicking a window that’s been minimized into the Dock; use make active.” | p.137 |
| **memory** | a term such as storage space instead | “Don’t use memory to refer to storage capacity; use a term such as storage space instead.” | p.139 |
| **memory address, memory location** | — | “Don’t use commas in addresses, even in numbers of five digits or more.” | p.139 |
| **menu commands** | — | “Don’t use an angle bracket when you’re simply identifying which menu contains the item. Correct: the Page Setup command in the File menu Incorrect: the File > Page Setup command Don’t refer to pull-down menus as pop-up menus or drop-down …” | p.139 |
| **message** | — | “Avoid using message as a verb.” | p.140 |
| **mic** | mike | “Don’t use as a verb; use mike.” | p.141 |
| **mice** | — | “Try to avoid, but if you must use the plural of mouse, it’s OK to use mice or mouse devices.” | p.141 |
| **mike, miked, miking** | microphone or mic | “Don’t use mike as a noun; use microphone or mic.” | p.141 |
| **mini-DIN** | — | “Use the following terminology: edge connector: the connector on the edge of a peripheral card; fits into a slot minicircular connector: an 8-pin connector [Don’t use mini-DIN.] plug: a connector with prongs or pins In user materials, …” | p.57 |
| **sentence-style option names in text, unmarked** | quotation marks: click the “Position on screen” button | “For options and other onscreen elements of two or more words whose names are capitalized using sentence style, use quotation marks in text to avoid misreading.” | p.153 |
| **mode (when it isn’t part of a feature name)** | omit it: When you’re using the paintbrush… | “In particular, avoid referring to a feature as a mode if mode isn’t part of the feature name.” | p.142 |
| **model (when you mean computer)** | computer | “Don’t use when you can use computer.” | p.143 |
| **monitor** | display | “In general, don’t use to refer to the primary display connected to the user’s computer; use display.” | p.143 |
| **monitor depth** | color depth | “Avoid; use color depth.” | p.143 |
| **monospace** | monospaced | “Not monospace.” | p.143 |
| **motherboard** | main logic board or main board | “Don’t use; use main logic board or main board.” | p.144 |
| **motherboard, mother board, main board, or main circuit board** | logic board | “Not motherboard, mother board, main board, or main circuit board.” | p.129 |
| **mount** | — | “In user materials, avoid when referring to making a disk or disk image available; use alternatives such as open, make available, or connect to, or describe what the user must do to make the disk available. Avoid: To see the contents of …” | p.144 |
| **mounted** | — | “In user materials, avoid when referring to a disk or disk image that’s available; use alternatives such as available, on your desktop, or in a Finder window. (Note that users can choose whether to display disk icons on their desktops, …” | p.144 |
| **mouse (and its plural)** | clicking, dragging, selecting, choosing; mouse devices | “Avoid referring to the mouse when possible. … Avoid using the plural form of mouse.” | p.145 |
| **MP3** | — | “Don’t use MP3 to refer to audio files in general; some files use AAC or other formats.” | p.145 |
| **multiplication symbol** | multiplication sign | “Not multiplication symbol.” | p.146 |
| **My Photo Stream** | — | “Don’t use the term photo stream generically to refer to the photos in My Photo Stream; always use the full feature name.” | p.146 |
| **native** | — | “In user materials, avoid using native to describe apps; instead, describe the apps as being designed to work with specific hardware or software.” | p.146 |
| **neurodiversity (n.), neurodiverse** | neurodivergent | “Don’t refer to a single individual as neurodiverse; use neurodivergent.” | p.147 |
| **new** | — | “In most documents, avoid describing a product or feature as new because the text will quickly become out of date.” | p.147 |
| **nonce** | — | “Don’t use nonce.” | p.20, 147 |
| **normal install** | normal installation | “Not normal install.” | p.147 |
| **normal user** | — | “Don’t use a Note tag immediately before or after a Warning notice, an Important notice, or another note, or immediately after a text heading.” | p.147 |
| **notebook computer** | laptop or laptop computer | “Don’t use; use laptop or laptop computer.” | p.148 |
| **notebook computer or notebook** | — | “Don’t use notebook computer or notebook.” | p.122 |
| **Notification Center** | — | “Don’t precede with the.” | p.148 |
| **number sign** | — | “Don’t use pound sign or number symbol. Avoid using the number sign to specify an item in a numbered series.” | p.150 |
| **numeric keypad** | — | “Don’t use numerical keypad or numeric keyboard.” | p.150 |
| **numerical, except when you refer specifically to numerical order** | numeric | “Not numerical, except when you refer specifically to numerical order.” | p.150 |
| **offline** | — | “Acceptable: If you want to go offline for a while, turn on Do Not Disturb.” | p.150 |
| **okay** | OK | “Not okay.” | p.151 |
| **on/off button** | on/off switch | “Not on/off button.” | p.151 |
| **onboard (adj., v.), on board** | — | “Don’t use onboard as a verb in user materials.” | p.151 |
| **once** | — | “Don’t use when you mean after.” | p.151 |
| **one-click** | — | “Don’t use 1-Click.” | p.151 |
| **Optic ID** | — | “Don’t precede with the.” | p.152 |
| **optionally** | — | “Avoid in user materials.” | p.152 |
| **output** | write to, display on, print on, or print to | “Avoid as a verb; use write to, display on, print on, or print to.” | p.153 |
| **outside of** | outside | “Not outside of.” | p.153 |
| **over** | — | “Don’t use when you mean more than.” | p.153 |
| **pane** | — | “In many cases, you can avoid using pane by describing how to get to a particular onscreen item: Open Safari settings, and then click AutoFill.” | p.153 |
| **panel** | dialog, window, or pane | “Don’t use in user materials; use dialog, window, or pane.” | p.153 |
| **parental controls** | — | “Don’t use family controls.” | p.154 |
| **parentheses or a leading 1 in U.S. phone numbers** | hyphens: 408-996-1010 | “Use hyphens in U.S. phone numbers; don’t use parentheses or a leading 1. … Don’t use photograph.” | p.157 |
| **passkey** | — | “Don’t use when you mean code, passcode, or password.” | p.154 |
| **passphrase** | — | “Avoid in user materials.” | p.154 |
| **password** | — | “Don’t use when you mean code, passcode, or passkey.” | p.154 |
| **pasteboard** | — | “Don’t use in user materials when you mean Clipboard.” | p.154 |
| **PC** | — | “Avoid PC when you refer to Apple personal computers.” | p.156 |
| **PDF** | — | “Not necessary to spell out on first occurrence.” | p.156 |
| **Personal Hotspot, Instant Hotspot** | Instant Hotspot only as a feature name—don’t use to refer to an individual hotspot | “In general, use Instant Hotspot only as a feature name—don’t use to refer to an individual hotspot.” | p.157 |
| **Phillips screw, Phillips screwdriver** | — | “Not Phillips-head screw or Phillips- head screwdriver.” | p.157 |
| **Photo Stream** | — | “Don’t use.” | p.158 |
| **picker** | — | “Don’t use the term picker in user materials to describe how to select a color or a date.” | p.158 |
| **Pinned Sites** | — | “Avoid referring to pinned sites as pinned tabs unless you need to refer to the tab itself.” | p.159 |
| **place card** | — | “Don’t use information card.” | p.160 |
| **placeholder names** | — | “Don’t use brackets with placeholders in pathnames and filenames.” | p.160 |
| **player** | — | “Don’t use the with the full name of a product whose name includes Player, unless the product name is used as an adjective modifying a noun.” | p.160 |
| **please** | — | “Avoid using please in instructional text and cross-references.” | p.161 |
| **plus symbol** | plus sign | “Not plus symbol.” | p.162 |
| **pod** | — | “Don’t use pod.” | p.162 |
| **point** | — | “Don’t use as a synonym for dot or to describe a place or spot on the screen.” | p.162 |
| **pop-up** | — | “Don’t use pop-up to refer to a pop-up menu; always use pop-up menu.” | p.163 |
| **popover** | describe what the user must select or do | “Don’t use in user materials; instead, simply describe what the user must select or do. … Don’t call it a dialog or window.” | p.163 |
| **port** | — | “Don’t use connector to refer to a port.” | p.163 |
| **portable computer** | laptop or laptop computer | “Avoid; use laptop or laptop computer.” | p.163 |
| **pound sign** | number sign for this character: # | “Don’t use; use number sign for this character: #.” | p.164 |
| **power adapter** | — | “Avoid AC adapter.” | p.164 |
| **power off** | shut down or turn off | “Don’t use in user materials; use shut down or turn off.” | p.164 |
| **power on** | turn on | “Don’t use in user materials; use turn on.” | p.164 |
| **power-down (n., adj.), power down** | turn off or shut down | “Don’t use in user materials; use turn off or shut down.” | p.164 |
| **power-up (n., adj.), power up** | turn on or start up | “Don’t use in user materials; use turn on or start up.” | p.164 |
| **PowerNap** | Power Nap | “Not PowerNap.” | p.164 |
| **prebundled** | — | “Don’t use prebundled.” | p.42 |
| **preinstalled, preloaded** | — | “Avoid.” | p.165 |
| **press** | click, force click, or click and hold | “Don’t use click, hit, push, tap, or type. … You can also use press to describe the act of pressing the stem on some models of AirPods. • Don’t use press to refer to onscreen items; use click, force click, or click and hold. … See also …” | p.166 |
| **press and hold** | — | “Don’t use press and hold when you mean press, which means to press and quickly release a key or mechanical button. … Don’t use press and hold when you mean click and hold.” | p.167 |
| **print out** | print | “Not print out.” | p.167 |
| **problem (in phrases such as this is a known problem)** | condition, issue, situation | “Don’t use in phrases such as this is a known problem or this version fixes that problem.” | p.167 |
| **product** | — | “Don’t use product in materials that discuss using and working with a specific device, such as a Mac or Apple Watch.” | p.168 |
| **product names** | — | “Don’t shorten or abbreviate product names. • Names as verbs: Don’t use product names or trademarks as verbs: make a FaceTime call to a friend, not FaceTime a friend; identify a song using Shazam, not Shazam a song. • Plurals and …” | p.168 |
| **professional (shortened)** | pro | “Don’t shorten to pro.” | p.168 |
| **prompt** | — | “Avoid using prompt as a verb if you can simply tell users to do something, or if you can use friendlier wording such as when asked or you may be asked. Avoid: Double-click the side button, and then enter your passcode when prompted.” | p.169 |
| **pronouns** | — | “When referring to individuals of unspecified gender, don’t use gender-specific pronouns ( he, his, him, she, her, hers) or combinations of gender-specific pronouns ( he or she, he/she, s/he). … You can also rewrite a sentence to avoid …” | p.170 |
| **protocol** | — | “Don’t use an article before the abbreviation when it stands alone.” | p.170 |
| **push** | press | “Don’t use to refer to the act of pressing a button or a key on a keyboard; use press. … Don’t use push when discussing services (such as iCloud) that send content to devices automatically; instead, say content appears automatically or is …” | p.171 |
| **push notification** | just notification | “Don’t use in user materials; use just notification.” | p.171 |
| **put** | — | “Don’t use when you mean drag.” | p.171 |
| **quality** | — | “Don’t use quality alone as an adjective; include a modifier.” | p.172 |
| **question-mark button** | Help button | “Don’t use; use Help button.” | p.172 |
| **Quick Look** | — | “Don’t use quick look as a verb.” | p.172 |
| **QuickTime Player** | — | “Don’t precede with the.” | p.172 |
| **quit** | — | “Don’t use exit, exit from, or leave when you mean quit.” | p.172 |
| **quotation marks unless italics aren’t available** | title-style capitalization and italics; don’t use quotation marks unless italics aren’t available | “This section provides general guidelines, but always consult your department’s style guidelines if in doubt about which style to use, and be consistent within a document. • Titles of books and other documents: In general, use title-style …” | p.60 |
| **radio button** | — | “Avoid the term radio button, except in developer materials.” | p.173 |
| **RAW** | RAW file, RAW image, RAW setting, and so on | “Don’t use RAW alone; use RAW file, RAW image, RAW setting, and so on.” | p.174 |
| **Reader** | — | “Don’t precede with the.” | p.174 |
| **realtime** | — | “Don’t use realtime.” | p.174 |
| **recommend** | — | “When describing something users are encouraged to do, don’t use we” | p.175 |
| **redownload** | download again | “Don’t use; use download again.” | p.175 |
| **reference** | refer to | “Don’t use as a verb; use refer to.” | p.175 |
| **regular** | — | “Don’t use when you mean standard, as in Use standard settings.” | p.175 |
| **release** | — | “Don’t use when referring to a macOS version number.” | p.175 |
| **iCloud account, iTunes Store account, App Store account** | Apple Account | “You can shorten Apple Account to just account to save space or avoid repetition.” | p.22 |
| **representative** | — | “Don’t use to refer to an AppleCare Support person.” | p.176 |
| **reset** | — | “Don’t use reset as a noun.” | p.176 |
| **resizeable** | resizable | “Not resizeable.” | p.176 |
| **restart** | — | “Don’t use as a noun.” | p.176 |
| **restore** | — | “Don’t use as a noun. Correct: Avoid stopping the restore process. Incorrect: Avoid stopping a restore in progress.” | p.176 |
| **right arrow** | — | “Don’t call it the right arrow button or the right-pointing arrow. … Don’t use when you mean Forward button.” | p.177 |
| **right-hand** | right | “Avoid except in reference to right-hand (recto) pages; use just right whenever possible.” | p.177 |
| **right-hand side** | right side | “Not right-hand side.” | p.177 |
| **root** | — | “Avoid using root as a synonym for System Administrator.” | p.177 |
| **rotate** | turn | “Don’t use to refer to turning the Digital Crown; use turn.” | p.177 |
| **router** | — | “Don’t use interchangeably with bridge.” | p.178 |
| **rule of thumb** | general rule, general recommendation, guideline, or as a rule | “Avoid; use general rule, general recommendation, guideline, or as a rule.” | p.178 |
| **run (for what a user does with an app); running (for an open app)** | use; open | “Open Activity Monitor to see what processes are running. • Apps: Don’t use run to describe what a user does with an app (a program that has a graphical interface); say use instead. … Don’t use running to refer to an open app; use open. …” | p.178 |
| **sample rate** | — | “Don’t use sampling rate.” | p.179 |
| **sanity check, sanity test** | an alternative such as consistency check, logic check, final check, or final pass | “Don’t use; use an alternative such as consistency check, logic check, final check, or final pass.” | p.179 |
| **scaleable, scaleability** | scalable, scalability | “Not scaleable, scaleability.” | p.179 |
| **screen (when you mean display)** | display; view (Apple Vision Pro) | “Don’t use when you mean display. … Don’t use screen to refer to what a person sees while wearing Apple Vision Pro; use view.” | p.179 |
| **script symbol or script icon** | keyboard icon | “Not script symbol or script icon.” | p.120 |
| **scroll (as a transitive verb)** | scroll through, scroll to view | “Avoid using as a transitive verb.” | p.179 |
| **seasons** | — | “Because content may be viewed by a global audience, avoid referring to times of the year using the names of seasons. Preferable: coming later this year, starting early next year Avoid: coming this fall, starting this spring” | p.180 |
| **self-test** | — | “Don’t use as a verb.” | p.182 |
| **Setup Assistant** | — | “Don’t use the before Setup Assistant.” | p.182 |
| **share sheet** | — | “In most user materials, avoid using share sheet; instead, describe what the user must select or do.” | p.184 |
| **Shared Albums** | — | “Note capitalization; don’t use iCloud Photo Sharing, Shared iCloud Albums, or similar.” | p.182 |
| **SharePlay** | — | “Don’t use as a verb. … In user materials, avoid using session. … (It’s OK to use session in developer materials.) Avoid: Tap the Play button to start the SharePlay session.” | p.183 |
| **sheet** | — | “Don’t use sheet in user materials; in content about Mac, you can call a sheet a dialog.” | p.184 |
| **Shift Lock** | Caps Lock key | “Not Shift Lock.” | p.47, 185 |
| **shows up** | appears | “Don’t use; use appears.” | p.185 |
| **Sidecar** | — | “Don’t precede with the.” | p.185 |
| **signalled, signalling** | signaled, signaling | “Not signalled, signalling.” | p.185 |
| **simply as a synonym for iPhone** | — | “Don’t use simply as a synonym for iPhone.” | p.142 |
| **Siri** | — | “Don’t refer to Siri as she or her; always say Siri. … Avoid using Hey Siri as a feature name; in most cases just tell users how to use it. … Avoid: You can use Hey Siri to schedule a meeting.” | p.186 |
| **size (as a verb); grow** | resize, change the size of | “Don’t use; use resize or change the size of (in reference to a window or an object).” | p.187 |
| **size or grow** | resize | “Not size or grow.” | p.176 |
| **slave** | — | “Don’t use to refer to a device or process.” | p.187 |
| **sleep** | — | “Don’t use the computer is sleeping or the computer is asleep.” | p.187 |
| **slide** | — | “Avoid when describing how users operate a slider or switch.” | p.188 |
| **slider** | — | “Avoid using the verb slide with slider.” | p.188 |
| **slot** | — | “Don’t use connector to refer to a slot.” | p.188 |
| **smiley** | — | “Don’t use on its own in place of emoji or emoticon.” | p.189 |
| **snapshot** | — | “OK to use as a synonym for photo, but avoid using snapshot to refer generally to a user’s photos.” | p.189 |
| **software** | — | “Don’t use software program.” | p.190 |
| **software licensing agreement** | software license agreement | “Not software licensing agreement.” | p.190 |
| **sound input, sound input/output, sound output** | — | “Avoid unless it appears in the user interface.” | p.190 |
| **spam** | — | “Don’t use spam as a verb.” | p.190 |
| **spinning wait cursor** | — | “Developer materials: Try to avoid situations in your app that cause the window server to display the spinning wait cursor.” | p.191 |
| **splash screen** | opening display | “Not splash screen.” | p.152, 191 |
| **Split View** | — | “In most cases, say that users do things in Split View; they don’t use Split View. Avoid: You can use Split View to view two apps side by side.” | p.191 |
| **SSD** | — | “It’s OK to use SSD alone or in terms such as SSD storage; don’t use SSD drive.” | p.191 |
| **standalone** | — | “Don’t use as a noun.” | p.191 |
| **standard user** | — | “Don’t use normal user.” | p.192 |
| **start** | — | “Don’t use when you mean open (as in open an app ).” | p.192 |
| **startup (n., adj.), start up** | — | “In user materials, try to avoid using startup as a noun, except when repeated occurrences of when you start up become unwieldy.” | p.192 |
| **stepper** | up arrow, down arrow, right arrow, left arrow, or arrows, as appropriate | “Don’t use in user materials unless it’s necessary to refer to the control itself; use up arrow, down arrow, right arrow, left arrow, or arrows, as appropriate.” | p.192 |
| **Stickies** | notes | “Don’t use to refer to the things you create using Stickies; use notes.” | p.192 |
| **stop** | — | “Don’t use when you mean quit an app.” | p.193 |
| **support** | — | “Avoid in user materials when you can use compatible, works with, or another appropriate word or phrase. … Avoid: The first-generation iPad didn’t support AirPlay Mirroring. … Avoid: iMovie supports most QuickTime formats. … Avoid saying Apple …” | p.195 |
| **switch** | tap or click instead | “If you do need to refer to the switch (in order to specify its location, for example), avoid using the verbs switch or slide with it; use tap or click instead.” | p.196 |
| **switch on, switch off** | turn on and turn off | “Don’t use switch on, switch off, power down, power off, power on, or power up in user materials; use turn on and turn off.” | p.196 |
| **symbol** | — | “When referring to onscreen items, don’t use symbol when you mean button or icon. … Don’t use symbol when you mean character, letter, or digit.” | p.197 |
| **synch, synched, or synching** | sync, synced, syncing | “Not synch, synched, or synching.” | p.197 |
| **system** | — | “Don’t use system to refer to a computer by itself.” | p.198 |
| **System Administrator** | — | “Avoid, except when you’re referring to the macOS user account identified as System Administrator (long name) and root (short name).” | p.198 |
| **systems software** | system software | “Not systems software.” | p.198 |
| **tab** | pane | “In user materials, don’t use tab to refer to a changeable area of content built into a window in macOS; use pane.” | p.199 |
| **tap** | — | “Don’t use tap on.” | p.201 |
| **tap and hold** | — | “Don’t use.” | p.201 |
| **Tapback** | — | “Don’t use as a verb.” | p.201 |
| **taptic** | — | “Don’t use.” | p.201 |
| **Taptic Engine** | only in the term Taptic Engine | “Don’t use the word taptic by itself; use only in the term Taptic Engine.” | p.201 |
| **television** | — | “Don’t use television set or TV set.” | p.202 |
| **terms such as AppleScriptable or AppleScripting** | — | “Don’t use terms such as AppleScriptable or AppleScripting.” | p.27 |
| **text message** | — | “Avoid using text and texts as nouns.” | p.203 |
| **theatre** | theater | “Not theatre.” | p.203 |
| **third party (n.), third-party** | — | “Don’t use 3rd-party, 3P, or other shortened forms.” | p.203 |
| **three-prong outlet** | grounded outlet | “Not three-prong outlet.” | p.96, 203 |
| **throw away** | — | “Don’t use when you mean drag an item to the Trash.” | p.203 |
| **thumb** | — | “Don’t use when you mean scroller or slider.” | p.203 |
| **time of day** | — | “Don’t use from with the en dash.” | p.204 |
| **to-do** | — | “Don’t use as a noun.” | p.205 |
| **Today View** | — | “Don’t precede with the.” | p.205 |
| **toggle** | turn on or off, switch between | “Don’t use in user materials; instead, say turn on or off, switch between, or whatever wording is appropriate in the context.” | p.205 |
| **tooltip** | help tag instead | “Don’t use, except in developer materials; use help tag instead.” | p.205 |
| **touch and hold** | — | “Don’t use tap and hold. Don’t use long press in user materials (it’s OK in developer materials).” | p.206 |
| **Touch Bar** | — | “Don’t shorten to the Bar.” | p.206 |
| **towards** | toward | “Not towards.” | p.206 |
| **Trash** | triple-click | “Don’t use to refer to quickly pressing a mechanical button three times; use triple-click.” | p.207 |
| **TV set or television set** | TV | “Not TV set or television set.” | p.208 |
| **type** | — | “Don’t use type when you mean font.” | p.208, 209 |
| **type size** | font size | “Not type size.” | p.89, 209 |
| **type style** | style or font style | “Don’t use; use style or font style.” | p.209 |
| **typeface** | font | “Don’t use; use font.” | p.209 |
| **typestyle or type style** | style (of type) | “Not typestyle or type style.” | p.194 |
| **typestyle or typeface attribute** | font style | “Not typestyle or typeface attribute.” | p.89 |
| **uncheck** | deselect | “Don’t use; use deselect.” | p.209 |
| **unclick** | deselect | “Don’t use; use deselect.” | p.209 |
| **under (for an OS environment, menu location, or interface position)** | in, with, below | “Don’t use to describe an operating system environment. … Don’t use to refer to items in menus. … Don’t use to describe where things are in the interface; use below instead.” | p.209 |
| **unhighlight** | — | “Don’t use.” | p.210 |
| **unhighlighted** | not highlighted | “Don’t use; use not highlighted.” | p.210 |
| **unit** | — | “Don’t use to refer to a hardware product.” | p.210 |
| **unmount** | alternatives such as eject or make unavailable, or describe what the user must do to make the disk unavailable | “In user materials, avoid when referring to making a disk or disk image unavailable; use alternatives such as eject or make unavailable, or describe what the user must do to make the disk unavailable. Avoid: Unmount the disc when you …” | p.210 |
| **unmounted** | alternatives such as not available or not visible in a Finder window | “In user materials, avoid when referring to a disk or disk image that isn’t available; use alternatives such as not available or not visible in a Finder window. Avoid: If a disk is unmounted, you can’t access files on it until you mount it …” | p.210 |
| **upgradeable** | upgradable | “Not upgradeable.” | p.211 |
| **upload** | — | “Avoid using upload to refer to what iCloud does; instead, content is stored, is kept up to date, appears automatically, and so on. Avoid: Every new photo you take is uploaded to My Photo Stream.” | p.211 |
| **upwards** | upward | “Not upwards.” | p.211 |
| **USB** | — | “Avoid as a noun.” | p.212 |
| **user** | — | “If the audience of your document consists of users, avoid this term.” | p.212 |
| **user interface** | interface | “Don’t use in user materials; use interface.” | p.212 |
| **users group or user’s group** | user group | “Not users group or user’s group.” | p.212 |
| **utility** | — | “Capitalize, and don’t use the, when the word is part of a proper name.” | p.212 |
| **version number** | a specific number or range of numbers | “Don’t include the word version or the letter v when you refer to versions of software—for example, Keynote 15.2, not Keynote version 15.2. … To avoid repetition, you can lead with the version number: You need version 26 or later of iOS, …” | p.213 |
| **via** | — | “Don’t use unless space is tight.” | p.214 |
| **video** | — | “Note the treatment of these terms beginning with video: video camera, video capture card, video conference, video editing, video game, video podcast, video tutorial But: videotape Don’t use a hyphen in compound adjectives that include …” | p.214 |
| **video cable** | display cable (for Apple displays) or monitor cable (for non-Apple displays) | “Don’t use to describe a cable connecting a display or monitor to a computer; use display cable (for Apple displays) or monitor cable (for non-Apple displays).” | p.214 |
| **video cable or monitor cord** | monitor cable | “Not video cable or monitor cord.” | p.143 |
| **video camera** | — | “Don’t use when you mean camcorder.” | p.214 |
| **video port** | monitor port | “Not video port.” | p.143, 215 |
| **Virtual Memory or VM** | virtual memory | “Not Virtual Memory or VM.” | p.215 |
| **visionOS** | — | “Don’t precede with the.” | p.215 |
| **visually impaired** | — | “Avoid visually impaired.” | p.40, 215 |
| **voicemail** | — | “Don’t use as a verb.” | p.215 |
| **volume (disk)** | — | “Avoid: You can use the Find command to search for items on all volumes connected to your computer.” | p.216 |
| **vs** | versus | “Not vs.” | p.214 |
| **vs.** | versus when absolutely necessary, but rewrite to avoid the term when possible | “Don’t use; use versus when absolutely necessary, but rewrite to avoid the term when possible.” | p.216 |
| **Walkie-Talkie** | — | “Don’t use as a verb; say use Walkie-Talkie, have a Walkie- Talkie conversation, or similar.” | p.216 |
| **Warning** | — | “Don’t use a Warning notice immediately before or after a note, an Important notice, or another Warning notice, or immediately after a text heading.” | p.217 |
| **watch face** | — | “Don’t shorten to face.” | p.217 |
| **web** | — | “Note the treatment of terms beginning with web: webcam, webcast, webinar, webmail, webpage, website web app, web browser, web developer, web server Don’t use web and internet interchangeably; the web is just one part of the global internet.” | p.217 |
| **website can contain many webpages. You connect to** | — | “Don’t use website and webpage interchangeably. … You can browse, visit, or go to a website, but don’t use such phrases as point your browser at the website and surf the website.” | p.217 |
| **well-behaved** | compatible, well-constructed, and the like | “Don’t use to describe software; use compatible, well-constructed, and the like.” | p.218 |
| **wheelchair user** | — | “Don’t use wheelchair-bound, confined to a wheelchair, or handicapped.” | p.218 |
| **whitelist** | — | “Don’t use.” | p.218 |
| **wifi, wi-fi, or WiFi** | Wi-Fi | “Not wifi, wi-fi, or WiFi.” | p.219 |
| **wiggle** | jiggle | “Don’t use to describe the movement of icons on a screen; use jiggle.” | p.219 |
| **window** | — | “Don’t use window to refer to a popover. … Except for the Picture in Picture window, don’t use window to refer to interface elements in iOS.” | p.219 |
| **wirelessly-enabled** | wireless-enabled | “Not wirelessly-enabled.” | p.220 |
| **wish** | want | “Don’t use; use want.” | p.220 |
| **workspace** | — | “Don’t use as a synonym for desktop or Finder.” | p.220 |
| **workstation** | — | “Don’t use when you mean desktop computer.” | p.220 |
| **write** | copy or burn | “Avoid using as a verb in user materials; use copy or burn. … Don’t use write a disk.” | p.221 |
| **x (for any number or a range of version numbers)** | a specific number or range | “Follow these guidelines when you use the letter x to stand for something else: • Screen resolutions: Use a lowercase x in screen resolutions. 1024 x 768 [Note the space before and after the x.] • As a placeholder (variable): When you use x …” | p.221 |
| **zeroes** | zeros | “Not zeroes.” | p.222 |

---

## 12. What this guide permits that common style advice forbids

Do not “correct” any of the following. Each is either explicitly permitted or actively required by the guide.

**Contractions are required, not merely tolerated — in documentation, interface text, and marketing copy.**

> “As part of Apple’s informal voice, contractions are used and recommended throughout most documentation, interface text, and marketing copy.” — `contractions`, p.57

> “It’s also OK to use here’s, let’s, that’s, there’s, and what’s. Here’s a quick look at what’s new in this release.” — `contractions`, p.57

**Exclamation points are allowed in promotional text and dialogue.**

> “OK to use exclamation points occasionally in promotional text and dialogue. Avoid in documentation.” — `exclamation points`, p.83

**Passive voice is allowed — and sometimes required — in named cases.**

> “Passive voice is sometimes appropriate and necessary—for example, when using the active voice would require either a highly convoluted sentence structure or excessive anthropomorphism—but rewrite to avoid passive voice if you can. In tutorials, a passive construction might be appropriate to avoid miscuing the reader—that is, when you describe an action that the user isn’t supposed to try yet.” — `passive voice`, p.154

**Sentence fragments are correct in list items, callouts, and illustrations — with no ending punctuation.**

> “List items that are fragments or that complete the thought started by the main clause should not end with a period; list items that are complete sentences should end with a period.” — `lists (bulleted)`, p.126

> “Use a period for a complete sentence and no ending punctuation for a sentence fragment. It’s OK to have a mixture of complete sentences and fragments in one illustration.” — `callouts`, p.44

**A large em dash set closed up on both sides is the house mark — not a spaced en dash.**

> “Close up the em dash with the word before it and the word after it.” — `dash (em)`, p.62

**Humor and personality belong in the text.**

> “Humor can enhance documentation by adding to a reader’s enjoyment and by helping to lighten the tone. Humor usually works best in examples, where it’s less likely to distract the reader.” — `humor`, p.103

**Informal register is sanctioned where it serves the reader.**

> “You can also use less formal phrases like it’s a good idea to. It’s a good idea to create a password hint.” — `recommend`, p.175

**Singular `they` is correct and takes a plural verb.**

> “Instead, it’s OK to use they, their, or them as a singular, gender-neutral pronoun.” … “They always takes a plural verb, even when used as a singular pronoun.” — `pronouns`, p.170

**`may` for permission survives — a modal most technical styles forbid.**

> “Use may to express permission. … You may borrow my iPad if you return it tomorrow.” — `can, might, may`, p.45

**Sentences may begin with `But`. The guide itself does it.**

> “But in certain other contexts, such as putting a card in backwards, it’s OK to use backwards.” — `backward (adv.)`, p.36

*On “And”:* the guide contains no rule forbidding it, but it also never starts a sentence with “And” in its own 244 pages (two instances of sentence-initial “But”, zero of “And”). Treat “And” openers as unregulated rather than endorsed — prefer “But”, or restructure.

**Direct imperative address to the reader is the default, not “the user.”**

> “If the audience of your document consists of users, avoid this term.” — `user`, p.212

**Not regulated at all (no rule found, so neither required nor forbidden):** split infinitives, ending a sentence with a preposition, “hopefully” as a sentence adverb, singular/plural agreement with collective nouns, and the use of `that` vs. `which`. The guide defers to Merriam-Webster’s Collegiate Dictionary for spelling and The Chicago Manual of Style for anything it doesn’t cover.

> “Exceptions to guidelines in these resources are noted in this guide. In cases where resources conflict with each other, follow The Chicago Manual of Style for style and usage questions, and Merriam-Webster’s Collegiate Dictionary for spelling guidance.” — *Other editorial resources used at Apple*, p.5

---

## 13. Where this guide does NOT govern

**It governs instructional materials, technical documentation, reference information, training programs, and user interfaces — and nothing else.**

> “The Apple Style Guide provides editorial guidelines for text in Apple instructional materials, technical documentation, reference information, training programs, and user interfaces. The intent of these guidelines is to help maintain a consistent voice in Apple materials.” — *About the guide*, p.4

> “Writers, editors, and developers can use this document as a guide to writing style, usage, and Apple product terminology. … Apple developers and third-party developers should follow these guidelines for user-facing text.” — *About the guide*, p.4

**Marketing (Marcom) runs separate, supplemental style guides. Apple’s marketing copy is therefore evidence of a different register, not a violation of this one.**

> “Some departments at Apple (Marcom, for example) have supplemental style guides.” — *Other editorial resources used at Apple*, p.5

**It is U.S. English only.**

> “Guidance on style, usage, and spelling in the Apple Style Guide is based on U.S. English conventions. For localized content, consult resources specific to the language or region.” — *Other editorial resources used at Apple*, p.5

**For interface text specifically, the guide hands off to the Human Interface Guidelines.**

> “For information about the user interface, see Apple’s Human Interface Guidelines.” — *Other editorial resources used at Apple*, p.5

**Trademark symbols behave differently outside this guide’s territory.**

> “In user and developer materials (print and electronic), don’t use trademark symbols for Apple trademarks in headings or text. Note that other types of documents, such as press releases, do use trademark symbols in text.” — `trademarks (credit lines and symbols)`, p.207

### Rules Apple’s own marketing copy visibly violates

If you are writing copy in the Marcom register (product hero lines, campaign pages), this rulebook is the wrong rulebook for these specific rules. Each is a rule the guide states, followed by what Apple’s product pages do instead.

1. **Fragments end without punctuation — marketing gives them periods.** The guide: “Use a period for a complete sentence and no ending punctuation for a sentence fragment.” (`callouts`, p.44) and “List items that are fragments … should not end with a period” (`lists (bulleted)`, p.126). Apple’s product pages headline in fragments that take full stops: “Landscape. A spacious display for incredibly immersive entertainment.” “Dual-battery system. All-day power.” Treat the period-after-fragment as a marketing-surface device only.

2. **Exclamation points are banned in documentation — allowed in promotional text.** The guide carves this out itself: “OK to use exclamation points occasionally in promotional text and dialogue. Avoid in documentation.” (`exclamation points`, p.83)

3. **First person is banned — marketing headlines use “we.”** The guide: “Don’t use first person; rewrite in terms of the reader or the product.” (`we`, p.217) Corporate and newsroom copy addresses the company in the first person; the guide’s rule applies to documentation, reference, training and interface text.

4. **“New” is discouraged — marketing runs on “all-new.”** The guide: “In most documents, avoid describing a product or feature as new because the text will quickly become out of date.” (`new`, p.147)

5. **Superlatives and unqualified claims have no place in the guide’s register.** The guide’s whole habit is to state what a thing is and what it enables; that is a documentation norm. Marketing copy is governed by Marcom, per the supplemental-guides line above.

**Consequence for an agent:** if the task is a hero line, a campaign page, or a tagline, use §1–§11 for word choice and Apple’s product-pages as the model for rhythm and length — but expect, and do not “fix,” fragment-ending periods, exclamation points, first person, and “new”. If the task is documentation, interface text, a support article, a readme, a changelog, or an error message, every rule in this file applies as written.

---

## Provenance and known gaps

**Method.** Every rule above is drawn from the June 2026 *Apple Style Guide* (PDF edition, 244 pp.; web edition, 52 sections). The A–Z was parsed from the PDF text layer into 1,702 entries with page numbers; the §11 table is generated from that parse, so its quotations are mechanically extracted, not retyped. Topical chapters (Writing inclusively, Units of measure, Technical notation, International style, Copyright and trademarks) were read in full.

**Known gaps:**
- **No semicolon entry exists** in the guide. Nothing in the guide governs semicolon use; follow *The Chicago Manual of Style*.
- **No entry for split infinitives, dangling modifiers, “that” vs. “which”, or sentence length.** The guide has no numeric sentence-length rule anywhere; §2’s “write simple structures” is the closest thing to one.
- **No guidance on numbers in the middle of prose rhythm** (e.g., whether to spell out a large rounded number for effect); the `numbers` entry (p.148) is purely categorical.
- **The A–Z parse can occasionally misattribute an entry boundary** where the PDF line wrapped inside a run of bold or italic text. Where a row in §11 looks like it names the wrong term, the quoted condition in the same row is the authoritative part.
- **Marketing register rules are not extractable from this guide by design** — see §13; Marcom’s supplemental guides are not public.
