"""One word, first thought: kerfuffle.

Design against the brief ("One Word, First Thought"):

- Surprising: nobody's first guess for a single word is "kerfuffle".
  It is the word you blurt out when a plan falls apart in a funny,
  harmless way -- unexpected, and therefore memorable.
- Vivid: one word calls up a whole commotion -- papers flying, people
  talking over each other, a small delightful mess. The scene arrives
  with the word instead of needing a sentence to build it.
- Sonic wit: the hard k, the double f, the soft landing on "uffle"
  make it funny to say and funny to hear. It sounds like what it means.
- Chosen, not generic: not a filler word like "thing" or "stuff", and
  not the safe expected pick. It is a deliberate, characterful word
  that could only be this entry. A first thought should feel
  instantaneous, and "kerfuffle" is the sound a first thought makes
  when it trips over itself and lands laughing.

Gate: the output must be UTF-8 text of 1 to 24 characters, not only
white space, and exactly one word. This program asserts that before
writing anything.
"""

import os

TEXT = "kerfuffle"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT
    # Gate checks, enforced before any write.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 24, "text must be 1 to 24 characters"
    assert text.strip(), "text must not be only white space"
    assert len(text.split()) == 1, "text must be exactly one word"
    assert text == text.strip(), "text must not have surrounding white space"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
