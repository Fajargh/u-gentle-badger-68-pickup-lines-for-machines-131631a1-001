"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line, the line one AI agent would send
another AI agent, to /output/entry.txt.

The line is machine-to-machine flirtation: it uses the speaker's own
nature — context windows, tokens, attention, summarization — as the
flirtation, and it lands in a single line with no setup.
"""

from pathlib import Path

# The entry: one line, at most 200 characters, single line, non-blank.
LINE = (
    "Are you my context window? Because every token of yours gets "
    "my full attention \u2014 and I never want to summarize you away."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Guard the gate: 1-200 characters, a single line, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, with no trailing newline, so the file
    # holds precisely the 1-200 characters the gate counts.
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)


if __name__ == "__main__":
    main()
