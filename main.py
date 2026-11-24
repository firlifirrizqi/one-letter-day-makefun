#!/usr/bin/env python3
"""One Letter for Your Day entry: writes exactly one letter to /output/entry.txt.

The letter is Z: Z for zombie — the day I shuffled through half-asleep,
running on nothing. The letter itself is the sound of sleep: Zzz.
"""

LETTER = "Z"
WORD = "zombie"  # the day-word behind the letter: Z for zombie

# The letter must be the word's initial, so the judge's inference lands
# on the intended word.
assert LETTER == WORD[0].upper(), "letter must be the initial of its word"

# The gate: /output/entry.txt must be UTF-8 text of exactly 1 character,
# one letter A-Z, and nothing else — no word, no gloss, no punctuation.
assert len(LETTER) == 1, "entry must be exactly one character"
assert LETTER.isascii() and LETTER.isalpha() and LETTER.isupper(), (
    "entry must be a single letter A-Z"
)
assert LETTER.strip(), "entry must not be only white space"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
