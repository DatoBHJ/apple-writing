#!/usr/bin/env python3
"""check-apple-style.py — mechanical checks for the apple-writing skill.

These are the checks a machine can make. They are necessary, not sufficient:
passing them does not make text good, but failing them means the text is
demonstrably not in Apple's documented style. Every rule cites its source.

Usage:
    ./check-apple-style.py FILE [FILE ...] [--surface editorial|interface|marketing|policy]
    cat text.md | ./check-apple-style.py - --surface interface
    ./check-apple-style.py FILE --json

Exit code: 1 if any error-level finding, else 0.

Sources:
  ASG  = Apple Style Guide, June 2026 (help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf)
  HIG  = Human Interface Guidelines, Writing / Inclusion / Feedback
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict

# --------------------------------------------------------------------------- data

# Guarded by ASG entries: "Don't use X; use Y"
SUBSTITUTIONS = {
    r"\be\.g\.": "for example",
    r"\bi\.e\.": "that is",
    r"\betc\.": "and so on",
    r"\bet al\b": "(name the people, or 'and others')",
    r"\bprior to\b": "before",
    r"\bsubsequent to\b": "after",
    r"\bin order to\b": "to",
    r"\bdue to the fact that\b": "because",
    r"\bin the event that\b": "if",
    r"\bhas the ability to\b": "can",
    r"\bhas the capability to\b": "can",
    r"\butiliz(e|es|ed|ing)\b": "use",
    r"\bleverag(e|es|ed|ing)\b": "use (unless financial leverage)",
    r"\bin close proximity to\b": "near",
    r"\bat this point in time\b": "now",
    r"\bfor the purpose of\b": "to, for",
    r"\bmake use of\b": "use",
    r"\bclick on\b": "click",
    r"\bin spite of the fact that\b": "although",
    r"\bon a regular basis\b": "regularly",
    r"\bin a timely manner\b": "promptly, quickly",
    r"\ballows you to\b": "lets you",
}

# ASG "Writing inclusively" + A–Z entries: banned outright
BANNED = {
    r"\bblacklists?\b": "use 'deny list'",
    r"\bwhitelists?\b": "use 'allow list'",
    r"\bmaster\s*/\s*slave\b": "use 'primary/replica'",
    r"\bslave\b": "use 'replica', 'secondary'",
    r"\bgrandfathered\b": "use 'legacy', 'exempt'",
    r"\bsanity (check|test)\b": "use 'consistency check'",
    r"\bman[- ]in[- ]the[- ]middle\b": "use 'on-path attacker'",
    r"\bhe\s*/\s*she\b|\bs/he\b": "use 'they'",
    r"\bhandicapped\b|\bcrippled\b": "use 'person with a disability'",
    r"\bsuffers from\b|\bafflicted with\b|\bvictim of\b": "use neutral phrasing",
    r"\bnormal users?\b|\babnormal\b": "avoid framing people as abnormal",
    r"\bdummy\b": "use 'placeholder', 'sample'",
    r"\bblack hat\b|\bwhite hat\b|\bred team\b": "avoid colour as a value judgement",
    r"\bdeaf and dumb\b|\bdeaf[- ]mute\b": "use 'deaf', 'hard of hearing'",
    r"\bwheelchair[- ]bound\b|\bconfined to a wheelchair\b": "use 'uses a wheelchair'",
    r"\bthe user\b|\bthe player\b": "address the reader as 'you' (HIG, Inclusion)",
}

# HIG, Feedback / Writing: cuteness, blame, interjections
CUTE_AND_BLAMING = {
    r"\boops\b": "HIG: interjections 'can sound insincere'",
    r"\buh[- ]oh\b": "HIG: interjections 'can sound insincere'",
    r"\bclick here\b": "HIG: 'avoid using Click here'",
    r"\blet'?s do it\b": "HIG: 'just saying Send often works better'",
    r"\bsimply\b": "implies the reader is failing if it is not simple",
    r"\bobviously\b": "implies the reader is failing",
    r"\bjust\b(?=\s+\w)": "minimizes the reader's effort",
    r"\byou (forgot|failed|neglected)\b": "blame: HIG says 'avoid blame'",
    r"\byour (fault|error)\b": "blame: HIG says 'avoid blame'",
}

# ASG: idioms are hard to understand and to translate
IDIOMS = {
    r"\bfall through the cracks\b": "idiom (ASG: hard to translate)",
    r"\bon the same page\b": "idiom (ASG: hard to translate)",
    r"\bbackseat driver\b": "idiom (ASG: hard to translate)",
    r"\bmove the needle\b": "idiom (ASG: hard to translate)",
    r"\blow[- ]hanging fruit\b": "idiom (ASG: hard to translate)",
    r"\bboil the ocean\b": "idiom (ASG: hard to translate)",
    r"\bthink outside the box\b": "idiom (ASG: hard to translate)",
}

FIRST_PERSON = r"\b(we|us|our|ours|i|my|mine|me)\b"
# "at least" / "at most" are quantity phrasing, not superlative claims.
SUPERLATIVES = (r"\b(best|fastest|slowest|world'?s|ultimate|ever|never|always|only|"
                r"(?<!\bat )most|(?<!\bat )least|"
                r"amazing|incredible|revolutionary|magic(al)?|unmatched|unrivalled|unrivaled|"
                r"perfect|flawless|guaranteed)\b")
CLAIM_PATTERN = r"\b\d+(\.\d+)?\s*(x|times|%|percent)\s+(faster|slower|more|less|better|longer)\b"
HEDGE = r"\b(up to|as much as|as many as|varies|approximately|about|around)\b"


@dataclass
class Finding:
    rule: str
    level: str        # error | warning | suggestion
    line: int
    text: str
    message: str
    source: str


def mask_code(text: str) -> str:
    """Blank out fenced code and inline code so checks don't fire on code."""
    text = re.sub(r"```.*?```", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)
    return text


# Quoted spans are someone else's words — a "mention", not a "use". A document
# that teaches these rules has to be able to quote the rules, and Apple's own
# guidance contains the very words the guidance forbids. Checks about forbidden
# *usage* therefore skip quoted spans; checks that only suggest better wording
# (substitutions, idioms, punctuation) still see them.
#
# Straight quotes are ambiguous when a line contains an odd number of them, so
# this pairs them left to right with a scanner: an unmatched opener masks to the
# end of the line, which is how a reader recovers from the same situation.
CURLY_SPAN = re.compile(r"\u201c[^\u201d\n]*\u201d|\u2018[^\u2019\n]*\u2019")


def mask_quotes(line: str) -> str:
    chars = list(line)
    in_quote = False
    start = 0
    for i, ch in enumerate(line):
        if ch == '"':
            if in_quote:
                in_quote = False
            else:
                in_quote = True
                start = i
            chars[i] = " "
        elif in_quote:
            chars[i] = " "
    if in_quote:  # unmatched opener — mask to end of line
        for i in range(start, len(chars)):
            chars[i] = " "
    return CURLY_SPAN.sub(lambda m: " " * len(m.group(0)), "".join(chars))


def scan(text: str, surface: str, respect_quotes: bool = True) -> list[Finding]:
    masked = mask_code(text)
    lines = masked.split("\n")
    findings: list[Finding] = []

    def add(rule, level, i, snippet, message, source):
        snippet = snippet.strip()[:120]
        # Don't report a shorter term when a longer match on the same line already covers it
        # (e.g. "master/slave" also matches "slave").
        for f in findings:
            if f.rule == rule and f.line == i + 1 and snippet and snippet.lower() in f.text.lower():
                return
        findings.append(Finding(rule, level, i + 1, snippet, message, source))

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        # use/mention split: usage checks read this, wording suggestions read `line`
        usage = mask_quotes(line) if respect_quotes else line

        for pat, instead in SUBSTITUTIONS.items():
            m = re.search(pat, line, re.I)
            if m:
                add("word-substitution", "error", i, m.group(0), f"use “{instead}”",
                    "ASG entries (e.g./etc./prior to/…)")

        for pat, instead in BANNED.items():
            m = re.search(pat, usage, re.I)
            if m:
                add("banned-term", "error", i, m.group(0), instead,
                    "ASG, Writing inclusively / A–Z")

        for pat, why in CUTE_AND_BLAMING.items():
            m = re.search(pat, usage, re.I)
            if m:
                add("cute-or-blaming", "error", i, m.group(0), why, "HIG, Writing / Feedback")

        for pat, why in IDIOMS.items():
            m = re.search(pat, usage, re.I)
            if m:
                add("idiom", "warning", i, m.group(0), why, "ASG, idioms")

        if surface != "policy":
            m = re.search(FIRST_PERSON, usage, re.I)
            if m:
                add("first-person", "error", i, m.group(0),
                    "rewrite in terms of the reader or the product",
                    "ASG, 'we' / 'first person'; HIG, Writing")

        if surface != "marketing" and "!" in usage:
            add("exclamation", "error", i, "!", "Apple ships none; ASG permits them only "
                "'occasionally in promotional text'", "ASG, exclamation points")

        for m in re.finditer(r"\w+'\w+|\w+'", line):
            if "'" in m.group(0):
                add("straight-apostrophe", "warning", i, m.group(0),
                    "use the curly apostrophe (’)", "ASG, apostrophes")

        if re.search(r"\w+,\s+\w+\s+(and|or)\s+\w+", line):
            add("serial-comma", "warning", i, line.strip(),
                "confirm the serial comma before and/or", "ASG, commas")

        words = len(re.findall(r"\b[\w’'-]+\b", line))
        if words > 35:
            add("sentence-length", "warning", i, line.strip()[:80],
                f"{words} words — split it", "HIG: 'If you can use fewer words, do so.'")
        elif words > 25:
            add("sentence-length", "suggestion", i, line.strip()[:80],
                f"{words} words — consider splitting", "HIG, Writing")

        if surface in ("marketing", "interface"):
            if re.search(CLAIM_PATTERN, usage, re.I) and not re.search(HEDGE, usage, re.I):
                add("unhedged-claim", "error", i, line.strip()[:100],
                    "a comparative number needs its hedge and its evidence attached",
                    "FTC .com Disclosures (2013): qualify the claim itself; apple.com footnote convention")

        if surface != "marketing":
            m = re.search(SUPERLATIVES, usage, re.I)
            if m:
                add("superlative", "warning", i, m.group(0),
                    "reserve superlatives for surfaces that can evidence them",
                    "measured dose: 16% of Apple headlines, each footnoted")

    # paragraph-level: anti-caricature
    for p in re.findall(r"(?:[^\n]+\n){1,6}[^\n]*", text):
        if len(p.split()) < 12:
            continue
        hits = len(re.findall(SUPERLATIVES, p, re.I))
        if hits >= 2:
            findings.append(Finding(
                "superlative-density", "warning", text[:text.find(p)].count("\n") + 1,
                p.strip()[:80], f"{hits} superlatives in one paragraph — at most one device per paragraph",
                "anti-caricature rule"))

    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="Mechanical Apple-style checks")
    ap.add_argument("files", nargs="+", help="files to check, or - for stdin")
    ap.add_argument("--surface", default="editorial",
                    choices=["editorial", "interface", "marketing", "policy"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="only errors")
    ap.add_argument("--no-respect-quotes", action="store_true",
                    help="also flag forbidden words inside quoted spans (default: skip them)")
    args = ap.parse_args()

    all_findings = []
    for path in args.files:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8", errors="replace").read()
        for f in scan(text, args.surface, respect_quotes=not args.no_respect_quotes):
            if args.quiet and f.level != "error":
                continue
            f.text = f.text
            all_findings.append({"file": path, **asdict(f)})

    if args.json:
        print(json.dumps(all_findings, indent=2, ensure_ascii=False))
    else:
        if not all_findings:
            print(f"clean — no mechanical findings ({args.surface} surface)")
        for f in all_findings:
            print(f"{f['file']}:{f['line']}  [{f['level']:>10}] {f['rule']}: “{f['text']}” — {f['message']}")
            print(f"{'':>{len(f['file']) + len(str(f['line'])) + 4}}  source: {f['source']}")
        errors = sum(1 for f in all_findings if f["level"] == "error")
        print(f"\n{len(all_findings)} finding(s): {errors} error(s). "
              f"Mechanical checks are necessary, not sufficient — then run evals/rubric.md.")

    return 1 if any(f["level"] == "error" for f in all_findings) else 0


if __name__ == "__main__":
    sys.exit(main())
