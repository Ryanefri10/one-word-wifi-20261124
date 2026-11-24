"""One Word for Your Wi-Fi -- make.fun entry.

Writes a single word describing the entrant's Wi-Fi to
/output/entry.txt: the word the sponsor's network will be named after.

The word is "Sometimes": the Wi-Fi works... sometimes. It is funny at
once, true of how home Wi-Fi actually behaves, and a fresh angle --
not a pun that needs explaining, just the one word every household
recognises. Nine characters, inside the 1-20 gate, plain UTF-8.

Why this word beats the field's early entries ("Ghosting", "Liar",
"Gaslighting", "peekaboo"): those name the Wi-Fi as a person being
sneaky or dishonest, which needs a beat of personification to land.
"Sometimes" needs no translation at all -- it is the literal schedule
the Wi-Fi keeps. It also works as a network name on its own, which is
what the winning word becomes.
"""

import os

WORD = "Sometimes"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
