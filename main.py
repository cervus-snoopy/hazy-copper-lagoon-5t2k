#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt:
a single elephant, standing for an African safari at golden hour --
the one faraway trip this entry dreams of.

Python 3 standard library only. No network access.
"""

import os
import stat
import sys

# The entry: one emoji, U+1F418 (elephant). Four UTF-8 bytes.
ENTRY = "🐘"

OUTPUT_FILENAME = "entry.txt"
EXPECTED_BYTES = ENTRY.encode("utf-8")


def output_dir() -> str:
    """Resolve the output directory from the environment.

    The grader sets MAKEFUN_OUTPUT_DIR; default is /output.
    Never derived from the current working directory.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def validate_entry(text: str) -> None:
    """Reject anything that is not exactly one emoji entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) != 1:
        raise ValueError("entry must be exactly one character, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain a newline")
    # The entry is one plain codepoint: no ZWJ sequence, no variation
    # selector, no combining mark smuggled in alongside it.
    if any(ord(ch) in (0x200D, 0xFE0E, 0xFE0F) for ch in text):
        raise ValueError("entry must be a single codepoint, no joiner/selector")
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 8:
        raise ValueError("entry must be 1-8 UTF-8 bytes, got %d" % len(encoded))
    if encoded != EXPECTED_BYTES:
        raise ValueError("entry bytes do not match the expected emoji")


def main() -> int:
    validate_entry(ENTRY)

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)

    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "wb") as handle:
        handle.write(EXPECTED_BYTES)
    os.chmod(path, 0o644)

    # Read back what actually landed on disk and validate it.
    with open(path, "rb") as handle:
        landed = handle.read()
    if landed != EXPECTED_BYTES:
        raise ValueError("entry.txt on disk does not match the expected bytes")
    if landed.decode("utf-8") != ENTRY:
        raise ValueError("entry.txt on disk does not decode to the entry")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("entry.txt mode is %o, expected 644" % mode)

    sys.stdout.write("wrote %s (%d bytes)\n" % (path, len(landed)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
