#!/usr/bin/env python3
"""Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a dog gives after being
caught eating the homework, in the dog's own voice.

Entry (see ENTRY below): the dog reports its own obedience score.
"""

import os
import sys

# The entry: one line, 1-200 characters, in the dog's own voice.
ENTRY = "You said sit, stay, leave it. I did two out of three, and that's the best grade I've ever gotten."


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200 limit", file=sys.stderr)
        return 1
    if len(text) < 1:
        print("error: entry is too short", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"entry ({len(text)} chars): {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
