#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh (make.fun).

Writes a single roast line about a smart fridge to /output/entry.txt.
No network, no input files, no dependencies: the line is a literal.
"""

LINE = (
    "My ice maker has unionized: one cube a day, no overtime, "
    "and it files a complaint every time I open the door for a snack."
)


import os


def main() -> None:
    # Gate check, mirroring the competition gate: 1-200 chars, one line,
    # not only whitespace, valid UTF-8.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    # Read back and verify exactly what was written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
