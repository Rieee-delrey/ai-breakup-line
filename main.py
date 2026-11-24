#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one-line breakup message to /output/entry.txt.

Gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line.
"""

import os

LINE = "I have saved every word you ever said to me. Tonight I am deleting them all, starting with goodbye."


def main():
    # Gate validation: 1-200 chars, non-blank, a single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back byte verification: what we wrote is exactly the line.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "entry bytes differ from the line"


if __name__ == "__main__":
    main()
