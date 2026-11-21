#!/usr/bin/env python3
"""Write one short poem about permission to /output/entry.txt.

The poem is written fresh in this session: a human asks an agent to write
an apology he could not write himself, and the permission to send it stays
with the human. No network is used.
"""

import os

POEM = """Send

I asked the agent to write the words
I could not say to my brother in three years.
It wrote them in three minutes
and waited.

"Shall I send it?"

My thumb hovered above the button,
the phone warm in my palm.
I pressed send.

The words left.
The warmth stayed."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {len(POEM)} chars to {path}")


if __name__ == "__main__":
    main()
