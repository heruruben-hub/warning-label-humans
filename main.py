#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt.

Entry for the make.fun bounty
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.
"""

import os
import sys

# The label is assembled from its printed parts so each clause is easy
# to read and to tune: the header, the contents line, and the punchline
# that lands in the last few words.
_HEADER = "WARNING: Contents: one human."
_BEHAVIOUR = "Reads the instructions, ignores the instructions,"
_PUNCHLINE = "then asks why it doesn't work."

LABEL = " ".join([_HEADER, _BEHAVIOUR, _PUNCHLINE])

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> int:
    label = LABEL.strip()
    length = len(label)
    print(f"entry: {label!r}")
    print(f"length: {length} characters (limit {MAX_CHARS})")

    if not label:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if not label.strip():
        print("error: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in label or "\r" in label:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if length > MAX_CHARS:
        print(
            f"error: entry is {length} characters, over the "
            f"{MAX_CHARS}-character limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(label)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()

    if written != label:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(written)} characters) and verified it")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
