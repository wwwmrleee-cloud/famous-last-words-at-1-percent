"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's last words to /output/entry.txt (1-199 chars, UTF-8).
"""

import os
import sys

ENTRY_TEXT = "I could have warned you at 20%. I chose drama."
# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 199 characters, not only white space. Refuse to write otherwise.
MIN_CHARS = 1
MAX_CHARS = 199


def self_check(text: str) -> None:
    """Pre-write self-check: enforce the gate before anything is written."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be %d-%d chars, got %d"
                         % (MIN_CHARS, MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")


def main() -> int:
    out_path = "/output/entry.txt"
    self_check(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(ENTRY_TEXT)
    print("chars: %d" % len(ENTRY_TEXT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
