#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — one short family scene.

The entry is a single fixed scene, written for make.fun
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2: one or two
lines, no more than 280 characters, about a small domestic moment that
is warm, funny and heartfelt. A father still does his nightly rounds
like his child is small — and the grown child plays along, because the
ritual is the love. This program writes that scene to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The scene is fixed text: the
same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SCENE = (
    "Every night Dad still checks the locks twice, the stove once, "
    "and my bedroom door last \u2014 then whispers \u201cgoodnight, "
    "kiddo\u201d to his twenty-six-year-old, who pretends to be asleep "
    "so he will keep doing it forever."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the scene against the gate, then write it out."""
    if not 1 <= len(SCENE) <= 280:
        return abort(f"scene is {len(SCENE)} characters, the gate allows 1-280")
    if not SCENE.strip():
        return abort("scene is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(SCENE, encoding="utf-8")
    print(f"wrote {target}: {len(SCENE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
