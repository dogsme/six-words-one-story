#!/usr/bin/env python3
"""Write one six-word story to /output/entry.txt.

The story is a complete arc in six words: a proposal, a funeral,
and everything unsaid between them. The gate only accepts UTF-8 text
of 1 to 60 characters, so the program checks the word count, the
length, and that the text is not only whitespace before writing it.
"""

import os

STORY = "He proposed at her father's funeral."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = STORY.strip()
    words = text.split()
    assert text, "story must not be blank"
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(text) <= 60, f"expected 1-60 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
