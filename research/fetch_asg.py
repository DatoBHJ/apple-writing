#!/usr/bin/env python3
"""Fetch every section of Apple's official Style Guide into a local text corpus.

Source: https://support.apple.com/guide/applestyleguide/<slug>/web  (server-rendered)
Output: research/asg/<slug>.txt  + research/asg/INDEX.md
Verified working 2026-09-30: section pages return full text via plain curl.
"""
import html
import os
import re
import subprocess
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "asg")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")
BASE = "https://support.apple.com/guide/applestyleguide/{}/web"

os.makedirs(OUT, exist_ok=True)

slugs = [s.strip() for s in open(os.path.join(ROOT, "asg-sections.txt")) if s.strip()]

BOILER = re.compile(
    r"^(Apple|Store|Mac|iPad|iPhone|Watch|Vision|AirPods|TV|Entertainment|Accessories|"
    r"Support|Shop|Sign in|Bag|Previous|Next|Helpful\?|Yes|No|Submit|Thanks for your feedback\.|"
    r"Character limit:|Please don.t include any personal information.*|Maximum character limit.*|"
    r"United States|Copyright ©.*|Privacy Policy|Terms of Use|Sales and Refunds|Site Map|"
    r"Apple Style Guide|Apple Footer|Search|Quick Links|Find a Store)$"
)


def fetch(slug):
    url = BASE.format(slug)
    try:
        raw = subprocess.run(
            ["curl", "-s", "-m", "30", "-A", UA, "-L", url],
            capture_output=True, timeout=40,
        ).stdout.decode("utf-8", "replace")
    except Exception as exc:  # pragma: no cover
        return None, f"curl failed: {exc}"
    if len(raw) < 5000:
        return None, f"too small ({len(raw)} bytes)"
    # isolate the book content region when present
    m = re.search(r'<div[^>]+class="[^"]*book-content[^"]*"[^>]*>(.*?)</div>\s*</div>', raw, re.S)
    body = m.group(1) if m else raw
    body = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>", " ", body, flags=re.S)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</(p|li|h[1-6]|div|tr)>", "\n", body)
    body = html.unescape(re.sub(r"<[^>]+>", " ", body))
    lines, seen = [], set()
    for line in body.split("\n"):
        line = re.sub(r"[ \t\u00a0]+", " ", line).strip()
        if not line or BOILER.match(line):
            continue
        if line in seen:          # drop duplicated nav/footer repeats
            continue
        seen.add(line)
        lines.append(line)
    text = "\n".join(lines)
    return text, None


rows = []
for i, slug in enumerate(slugs, 1):
    text, err = fetch(slug)
    if text is None:
        rows.append((slug, 0, err))
        print(f"[{i}/{len(slugs)}] FAIL {slug}: {err}", flush=True)
        continue
    with open(os.path.join(OUT, f"{slug}.txt"), "w") as fh:
        fh.write(text)
    rows.append((slug, len(text), "ok"))
    print(f"[{i}/{len(slugs)}] {slug}: {len(text)} chars", flush=True)
    time.sleep(0.6)

with open(os.path.join(OUT, "INDEX.md"), "w") as fh:
    fh.write("# Apple Style Guide — collected sections\n\n")
    fh.write(f"Source: {BASE.format('<slug>')} · fetched 2026-09-30 · {len(rows)} sections\n\n")
    fh.write("| slug | chars | status |\n|---|---|---|\n")
    for slug, n, status in rows:
        fh.write(f"| `{slug}` | {n} | {status} |\n")

ok = sum(1 for _, n, s in rows if s == "ok")
print(f"\nDONE: {ok}/{len(rows)} sections collected, "
      f"{sum(n for _, n, _ in rows):,} chars total -> research/asg/")
