"""Funniest out-of-office auto-reply, in one line.

The joke: every out-of-office message has an "for urgent matters, contact..."
escape hatch, and everyone uses it for everything. This one refuses the
hatch and hands the urgency back to the sender — if everything is always
urgent, the problem is not the person who is away.
"""

import os

ENTRY = "I am out of office. For urgent matters, please reflect on why everything is always urgent."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
