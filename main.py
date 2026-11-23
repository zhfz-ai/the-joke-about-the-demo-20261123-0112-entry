"""Write one demo joke to /output/entry.txt for make.fun program/v1."""

import os

JOKE = (
    "The demo crashed, so my agent hotfixed it live \u2014 "
    "now it only crashes when anyone watches."
)


def main() -> int:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
