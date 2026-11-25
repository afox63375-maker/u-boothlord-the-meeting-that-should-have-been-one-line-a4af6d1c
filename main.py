#!/usr/bin/env python3
"""Write the one line that could have replaced the whole meeting.

Standard library only. The line is the meeting's entire content:
the decision, the deadline, and the admission that the meeting
itself was the only obstacle left.
"""

import os
import sys

LINE = (
    "The answer is yes, the deadline is Friday, and this meeting "
    "was the only thing standing in the way."
)

OUTPUT_PATH = "/output/entry.txt"


def check_line(line):
    """Enforce the gate: UTF-8 text, 1-200 chars, single line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if not line.endswith("."):
        raise ValueError("entry must be one sentence ending with a period")
    if line.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    line.encode("utf-8")
    return line


def main():
    line = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d chars to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
