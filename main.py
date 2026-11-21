"""The joke the reviewer laughs at — writes one one-line joke to /output/entry.txt."""

import os

JOKE = (
    "I asked my agent to fix a typo. The diff: 47 files changed, two new "
    "frameworks, 3,000 lines deleted \u2014 and the typo, now load-bearing, untouched."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
