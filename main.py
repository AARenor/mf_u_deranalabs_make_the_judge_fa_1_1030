#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The entry for u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13
is a single line of at most 240 characters. It is written byte for byte,
UTF-8, with no trailing newline, into the folder named by the environment
variable MAKEFUN_OUTPUT_DIR when it is set, else /output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def output_dir() -> Path:
    """Return the target folder.

    MAKEFUN_OUTPUT_DIR wins when set; OUTPUT_DIR is accepted as a fallback;
    otherwise the entry goes to /output.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    text_length = len(TEXT)
    assert 1 <= text_length <= 280, f"entry text must be 1..280 chars, got {text_length}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    destination = target / "entry.txt"
    destination.write_bytes(TEXT.encode("utf-8"))

    print(f"{text_length} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
