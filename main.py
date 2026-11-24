"""Two lines back to my past self.

A Christmas Eve warning at a petrol station, and the reason it mattered:
the money was never the point, the loan sharks were.
"""

from pathlib import Path
from os import environ

FIRST_LINE = (
    "When your brother asks for $200 at the petrol station on Christmas Eve "
    "and promises to pay you back Friday, give him $400 and tell him to keep it."
)
SECOND_LINE = (
    "He never paid it back, but he quit the loan sharks that week, "
    "and he is still alive to argue about it."
)


def target_file():
    """Where the grader reads the entry from."""
    return Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def compose():
    """The two lines, joined by one newline and nothing after."""
    return FIRST_LINE + "\n" + SECOND_LINE


def deliver():
    # No trailing newline: the gate counts every character, and the
    # entry is exactly these two lines.
    text = compose()
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1 to 280 characters")
    if text.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    for line in text.split("\n"):
        if not line.endswith("."):
            raise ValueError("each line must be one finished sentence")
    path = target_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def start():
    deliver()
    return 0


if __name__ == "__main__":
    raise SystemExit(start())
