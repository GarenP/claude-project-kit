#!/usr/bin/env python3
"""check_open_questions.py — session-end checker for the open-questions tracker.

Reads brainstorms/OPEN-QUESTIONS.md and FAILS if any question is still OPEN.
DEFERRED questions (parked with an owner + venue) pass but are listed so they're
never silently forgotten. Part of the project's verification battery.

Why this exists: questions get dropped across long free-form sessions because
"carry it forward" lives only in prose. This makes it checkable. Run it at
session end alongside the other checkers.
"""
import re
import sys
from pathlib import Path

# Windows console is cp1252 by default; force UTF-8 so ·/⚠ don't mojibake.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

TRACKER = Path(__file__).parent / "brainstorms" / "OPEN-QUESTIONS.md"


def main() -> int:
    if not TRACKER.exists():
        print(f"FAIL — tracker not found: {TRACKER}")
        return 1

    text = TRACKER.read_text(encoding="utf-8")
    open_rows, deferred_rows = [], []

    for line in text.splitlines():
        line = line.strip()
        # Only table data rows: start with '|', and skip header / separator rows.
        if not line.startswith("|"):
            continue
        if re.match(r"^\|\s*#\s*\|", line) or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        qid, question, _asked, status = cells[0], cells[1], cells[2], cells[3].upper()
        # Skip the placeholder example row shipped in the template.
        if "_(example" in question or "replace:" in question:
            continue
        if status == "OPEN":
            open_rows.append((qid, question))
        elif status == "DEFERRED":
            deferred_rows.append((qid, question))

    if deferred_rows:
        print(f"INFO — {len(deferred_rows)} deferred (parked, not forgotten):")
        for qid, q in deferred_rows:
            print(f"  · {qid}: {q}")

    if open_rows:
        print(f"FAIL — {len(open_rows)} question(s) still OPEN (answer or defer before wrap-up):")
        for qid, q in open_rows:
            print(f"  ⚠ {qid}: {q}")
        return 1

    print("PASS — no questions left OPEN.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
