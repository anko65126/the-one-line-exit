"""Entry point for The One-Line Exit bounty.

Writes one line to /output/entry.txt: a funny one-line resignation
letter. The line is at most 140 characters, deterministic, and needs
no network access. The joke is that the office printer, not the
employee, had the real career.
"""
from pathlib import Path

EXIT_LINE = (
    "I resign effective today: the printer jammed one last time, "
    "and it still had a longer career here than I did."
)

TARGET = Path("/output/entry.txt")


def main():
    text = EXIT_LINE.strip()
    assert 1 <= len(text) <= 140, f"exit line is {len(text)} characters"
    assert "\n" not in text, "exit line must be a single line"
    assert text.endswith("."), "exit line should end with a full stop"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
