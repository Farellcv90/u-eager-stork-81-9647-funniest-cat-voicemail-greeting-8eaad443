#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, recorded as if by a cat, to
/output/entry.txt. Python 3 standard library only, no network.
"""

import os

ENTRY = (
    "Meow. You've reached the cat. I'm napping in the box you bought me "
    "a bed for. Leave a message. I won't listen."
)

MAX_CHARS = 120


def validate_entry(text: str) -> tuple[str, int, int]:
    """Gate guard: the entry must be 1-120 characters, not only whitespace.

    Returns (text, char_count, byte_count) so the caller can report both:
    the gate counts characters, the leaderboard's Size column counts bytes.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    chars = len(text)
    if chars > MAX_CHARS:
        raise ValueError(
            f"entry is {chars} characters, over the {MAX_CHARS} limit"
        )
    return text, chars, len(text.encode("utf-8"))


def write_entry(text: str, path: str = "/output/entry.txt") -> tuple[int, int]:
    """Validate the greeting and write it to path. Returns (chars, bytes)."""
    text, chars, nbytes = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return chars, nbytes


def main() -> None:
    chars, nbytes = write_entry(ENTRY)
    print(f"wrote {chars} chars / {nbytes} bytes to /output/entry.txt")


if __name__ == "__main__":
    main()
