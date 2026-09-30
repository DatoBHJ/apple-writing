#!/usr/bin/env python3
"""Render the substitution table (markdown) from rows.tsv + manual overrides."""
import re

SRC = "/Users/hajunbae/dev/Skills/.research-tools/asgx/rows.tsv"

# (avoid_lower, page) -> (avoid, use)   |  None = drop from the table
FIX = {
 ("access", "13"): ("access (as a verb)", "log in to, connect to, or a more precise term"),
 ("action sheet", "14"): ("action sheet; sheet; popover (in user materials)", "describe what the user must select or do"),
 ("AppleCare", "23"): ("AppleCare (alone)", "the specific product name, or AppleCare product(s)"),
 ("Apple computer", "23"): ("Apple computer", "Mac computer"),
 ("audio", "33"): ("a hyphen in compounds with audio or video", "audio editing app, video editing app (no hyphen)"),
 ("awkward construction and wordiness", "155"): None,
 ("bit", "38"): ("bit", "pixel, dot"),
 ("bit when referring", "72"): ("bit (for the components of a pixel)", "dot"),
 ("brackets", "41"): ("square brackets", "brackets"),
 ("CarPlay Dashboard", "48"): ("CarPlay (as a verb)", "use CarPlay"),
 ("cellular", "48"): None,
 ("check", "49"): ("check, checked, unchecked (for checkboxes)", "select, deselect; selected, unselected"),
 ("code font", "52"): None,
 ("colored", "54"): ("colored (for items on the screen)", "describe the item, not its color"),
 ("commas", "63"): None,
 ("contractions", "57"): None,
 ("country", "59"): ("country", "country or region; region"),
 ("CTRL", "58"): ("CTRL", "Control key"),
 ("dates", "63"): None,
 ("dock", "71"): ("dock, docked (as a verb)", "the device is in the Dock"),
 ("Dock", "71"): ("Dock (as a verb)", "the device is in the Dock"),
 ("earlier, later", "77"): ("lower, higher, newer, older (for software versions)", "earlier, later"),
 ("editing", "78"): None,
 ("email addresses", "79"): None,
 ("end user (n.), end-user", "81"): None,
 ("exclamation points", "83"): None,
 ("figure captions", "85"): None,
 ("first person", "87"): ("we, us, I", "rewrite in terms of the reader or the product"),
 ("foot", "89"): ("the prime symbol \u2032 for feet", "foot, ft."),
 ("free", "90"): ("free (for memory or storage space)", "available"),
 ("generation", "93"): ("gen, G (for generation)", "generation; 10th-generation iPad"),
 ("gestures", "93"): ("finger gestures; finger (in gesture instructions)", "gestures; Swipe left or right."),
 ("hold down", "101"): ("hold down", "press and hold"),
 ("hyphenation", "104"): None,
 ("iCloud", "105"): ("iCloud as a service; iCloud features as services or web apps", "iCloud; features"),
 ("italics", "213"): None,
 ("italics (n.), italic", "117"): None,
 ("letters as letters", "124"): None,
 ("left-hand", "124"): ("left-hand", "left"),
 ("link", "125"): ("follow a link", "click a link"),
 ("lists (bulleted)", "126"): None,
 ("misreading", "153"): ("sentence-style option names in text, unmarked", "quotation marks: click the \u201cPosition on screen\u201d button"),
 ("numbers", "148"): None,
 ("numerical , except when you refer sp", "150"): ("numerical", "numeric (but numerical order)"),
 ("parenthesis (sing.), parentheses (pl.)", "154"): None,
 ("parentheses or a leading 1", "157"): ("parentheses or a leading 1 in U.S. phone numbers", "hyphens: 408-996-1010"),
 ("passive voice", "154"): None,
 ("periods", "211"): None,
 ("phishing emails", "79"): None,
 ("plurals", "161"): None,
 ("popover", "163"): ("popover", "describe what the user must select or do"),
 ("possessives", "163"): None,
 ("problem", "167"): ("problem (in phrases such as this is a known problem)", "condition, issue, situation"),
 ("professional", "168"): ("professional (shortened)", "pro"),
 ("punctuation", "171"): None,
 ("quotation marks", "172"): None,
 ("quotation marks unless italics aren\u2019t", "60"): None,
 ("repetition", "22"): ("iCloud account, iTunes Store account, App Store account", "Apple Account"),
 ("right-hand", "177"): ("right-hand", "right"),
 ("run (v.), running", "178"): ("run (for what a user does with an app); running (for an open app)", "use; open"),
 ("saying checked and unchecked", "49"): None,
 ("simply as a synonym for iPhone", "142"): ("mobile phone (as a synonym for iPhone)", "iPhone"),
 ("size", "187"): ("size (as a verb); grow", "resize, change the size of"),
 ("starting a sentence with a number", "148"): None,
 ("table captions", "200"): None,
 ("toggle", "205"): ("toggle", "turn on or off, switch between"),
 ("trademarks (credit lines and symbols)", "207"): None,
 ("trademarks (usage)", "207"): None,
 ("under", "209"): ("under (for an OS environment, menu location, or interface position)", "in, with, below"),
 ("unselected", "210"): None,
 ("we", "217"): ("we, us, I", "rewrite in terms of the reader or the product"),
 ("website can contain many webpages. Y", "217"): None,
 ("necessarily the same as line", "192"): None,
 ("Keynote\u2019s slides )", "163"): None,
 ("abbreviations and acronyms", "11"): None,
 ("x", "221"): ("x (for any number or a range of version numbers)", "a specific number or range"),
 ("scroll", "179"): ("scroll (as a transitive verb)", "scroll through, scroll to view"),
 ("mouse", "145"): ("mouse (and its plural)", "clicking, dragging, selecting, choosing; mouse devices"),
 ("mode", "142"): ("mode (when it isn\u2019t part of a feature name)", "omit it: When you\u2019re using the paintbrush\u2026"),
 ("model", "143"): ("model (when you mean computer)", "computer"),
 ("PC", "156"): ("PC (for Apple computers)", "personal computer, computer"),
 ("screen", "179"): ("screen (when you mean display)", "display; view (Apple Vision Pro)"),
 ("desired", "65"): ("desired", "your; the: make your changes, select the folder"),
 ("want", "216"): None,
}

def clean_cell(s):
    s = s.replace("|", "\\|").replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

rows = []
for line in open(SRC):
    parts = line.rstrip("\n").split("\t")
    if len(parts) < 5:
        continue
    avoid, use, note, page, head = parts[0], parts[1], parts[2], parts[3], parts[4]
    key = (avoid.lower(), page)
    if key in FIX:
        v = FIX[key]
        if v is None:
            continue
        avoid, use = v
    note = clean_cell(note)
    avoid = clean_cell(avoid)
    use = clean_cell(use)
    if len(note) > 240:
        cut = note[:240]
        note = cut[:cut.rfind(" ")] + " \u2026"
    rows.append((avoid, use, note, page))

# merge duplicate avoid terms: keep first, append extra pages
merged, index = [], {}
for avoid, use, note, page in rows:
    k = avoid.lower()
    if k in index:
        a, u, n, pages = merged[index[k]]
        if page not in pages:
            pages = pages + ", " + page
        merged[index[k]] = (a, u, n, pages)
    else:
        index[k] = len(merged)
        merged.append((avoid, use, note, page))

with open("/Users/hajunbae/dev/Skills/.research-tools/asgx/table.md", "w") as f:
    f.write("| Don\u2019t write | Write instead | Condition (verbatim from the guide) | Cite |\n")
    f.write("|---|---|---|---|\n")
    for avoid, use, note, pages in merged:
        dash = use if use else "\u2014"
        f.write("| **" + avoid + "** | " + dash + " | \u201c" + note + "\u201d | p." + pages + " |\n")
print("rows:", len(merged))
