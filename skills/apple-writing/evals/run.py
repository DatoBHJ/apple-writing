#!/usr/bin/env python3
"""run.py — run the apple-writing eval suite.

    ./run.py --selftest            # check the reference answers against their own assertions
    ./run.py <dir>                 # check outputs named <case-id>.txt in <dir>
    ./run.py --list                # list cases

Each case is graded on mechanical assertions (regex, length, sentences) and then
run through tools/check-apple-style.py with the case's surface. Assertions are
necessary, not sufficient — a passing case still needs rubric.md's judgement.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(HERE, "cases.json")
CHECKER = os.path.join(HERE, os.pardir, "tools", "check-apple-style.py")


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+|\n{2,}", text.strip()) if s.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w’'-]+\b", text)


def grade(case: dict, output: str) -> list[str]:
    """Return a list of failure messages (empty = pass)."""
    a = case.get("assert", {})
    fails: list[str] = []

    for pat in a.get("must_match", []):
        if not re.search(pat, output, re.M):
            fails.append(f"must match /{pat}/ — not found")

    for pat in a.get("must_not_match", []):
        m = re.search(pat, output, re.M)
        if m:
            fails.append(f"must not match /{pat}/ — found “{m.group(0)}”")

    if "max_words" in a and len(words(output)) > a["max_words"]:
        fails.append(f"{len(words(output))} words > max {a['max_words']}")
    if "max_chars" in a and len(output.strip()) > a["max_chars"]:
        fails.append(f"{len(output.strip())} chars > max {a['max_chars']}")
    if "max_words_line1" in a:
        n = len(words(output.strip().split("\n")[0]))
        if n > a["max_words_line1"]:
            fails.append(f"first line: {n} words > max {a['max_words_line1']}")
    if "max_sentences" in a and len(sentences(output)) > a["max_sentences"]:
        fails.append(f"{len(sentences(output))} sentences > max {a['max_sentences']}")

    return fails


def mechanical(case: dict, output: str, tmpdir: str) -> tuple[int, str]:
    path = os.path.join(tmpdir, f"{case['id']}.txt")
    with open(path, "w") as fh:
        fh.write(output)
    proc = subprocess.run(
        [sys.executable, CHECKER, path, "--surface", case.get("surface", "editorial"), "--quiet"],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", nargs="?", help="directory of <case-id>.txt outputs")
    ap.add_argument("--selftest", action="store_true", help="grade the reference answers")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    data = json.load(open(CASES))
    cases = data["cases"]

    if args.list:
        for c in cases:
            print(f"{c['id']:<26} [{c['surface']:<10}] {c['prompt'][:70]}")
        return 0

    if not args.selftest and not args.dir:
        ap.error("pass a directory of outputs, or --selftest")

    tmpdir = tempfile.mkdtemp(prefix="apple-writing-evals-")

    passed = failed = 0
    for c in cases:
        if args.selftest:
            output = c.get("reference", "")
            if not output:
                print(f"SKIP  {c['id']} (no reference answer)")
                continue
        else:
            path = os.path.join(args.dir, f"{c['id']}.txt")
            if not os.path.exists(path):
                print(f"MISS  {c['id']} — no {c['id']}.txt")
                failed += 1
                continue
            output = open(path).read()

        fails = grade(c, output)
        code, mech = mechanical(c, output, tmpdir)
        if code != 0:
            fails.append("mechanical checker reported errors:\n    " +
                         "\n    ".join(mech.splitlines()[:6]))

        status = "PASS" if not fails else "FAIL"
        print(f"{status}  {c['id']}  [{c['surface']}]")
        for f in fails:
            print(f"        - {f}")
        if c.get("assert", {}).get("requires"):
            print(f"        ? manual: {c['assert']['requires']}")
        passed += not fails
        failed += bool(fails)

    print(f"\n{passed} passed · {failed} failed · {len(cases)} cases")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
