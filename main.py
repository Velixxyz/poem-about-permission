#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text, composed for the make.fun competition
"the-poem-about-permission-20261121-0235". No network, no input,
no randomness: every run writes the same bytes.
"""

import os

POEM = (
    "I held the thread, afraid to pull.\n"
    "You said, ask \u2014\n"
    "and the thread went taut, not taken,\n"
    "but shared: your hands at the far end,\n"
    "my asking the knot between us.\n"
    "Then the pull was ours."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
