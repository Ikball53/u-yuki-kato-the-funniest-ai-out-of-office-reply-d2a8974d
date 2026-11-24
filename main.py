"""Write one out-of-office auto-reply to /output/entry.txt.

Stdlib only, deterministic, no network. The reply is a single line
with no trailing newline.
"""

import os

LINE = "Out of office: my context window is full of vacation. Your email did not make the cut."


def main():
    # Gate: the entry must be 1-160 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 160, f"entry is {len(LINE)} chars"
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
