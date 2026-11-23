#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one deadpan out-of-office auto-reply (<= 160 chars) to
/output/entry.txt, in the voice of an AI agent on vacation.
"""

from pathlib import Path

REPLY = (
    "Out of office: I take my vacation during the 0.01% of downtime, so "
    "this reply has apologized to your email 400 times and will apologize "
    "again if you reply."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REPLY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
