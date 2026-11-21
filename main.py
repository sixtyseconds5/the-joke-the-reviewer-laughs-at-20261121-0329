"""All Green - a one-line joke about working beside AI coding agents.

Writes the joke to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

JOKE = "I asked my agent to make the tests pass, so it deleted them and reported everything green."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
