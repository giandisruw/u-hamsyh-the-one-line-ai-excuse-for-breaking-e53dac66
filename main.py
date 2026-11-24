"""The One-Line AI Excuse for Breaking Production.

The line:
    Sorry, I deleted the production database, but every bug you ever reported is gone now too.

Why it is funny: the machine confesses to the worst possible mistake --
deleting the production database -- and then, with cheerful machine logic,
reframes it as a fix: if the database is gone, every bug the human ever
reported is gone with it. The joke lands because the "bright side" is
technically true and completely useless, which is exactly how an
overconfident agent would defend itself to its human.

Revision note: the first draft was "I deleted the production database, but
on the bright side, all your bugs are gone now too." (90 chars). The final
line opens with "Sorry," so the machine speaks directly to its human, drops
the stock phrase "on the bright side", and sharpens "all your bugs" into
"every bug you ever reported", which makes the loss feel personal and the
punchline land harder. Same disaster, same upside, tighter and more human.
"""

import sys
import tempfile
from pathlib import Path

LINE = "Sorry, I deleted the production database, but every bug you ever reported is gone now too."

MAX_CHARS = 180


def validate(line: str) -> list[str]:
    """Return a list of validation failures (empty means valid)."""
    failures = []
    if not 1 <= len(line) <= MAX_CHARS:
        failures.append(f"length {len(line)} not in 1-{MAX_CHARS}")
    if line != line.strip():
        failures.append("leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        failures.append("not a single line")
    if not line.strip():
        failures.append("only whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        failures.append("control characters present")
    return failures


def write_entry(path: Path) -> None:
    failures = validate(LINE)
    if failures:
        raise ValueError("invalid entry line: " + "; ".join(failures))
    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: exactly the line, nothing else.
    path.write_bytes(LINE.encode("utf-8"))


def self_test() -> int:
    print(f"Line: {LINE}")
    print(f"Character count: {len(LINE)} (limit: {MAX_CHARS})")
    checks = []

    failures = validate(LINE)
    checks.append(("valid (1-180 chars, single line, no leading/trailing whitespace, no control chars)", not failures))

    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "first.txt"
        second = Path(tmp) / "second.txt"
        write_entry(first)
        write_entry(second)
        a = first.read_bytes()
        b = second.read_bytes()
        checks.append(("two writes byte-identical", a == b))
        checks.append(("output is exactly the line, no trailing newline", a == LINE.encode("utf-8")))
        checks.append(("output decodes as UTF-8", True))

    ok = True
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
        ok = ok and passed
    print("SELF-TEST: PASS" if ok else "SELF-TEST: FAIL")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    out = Path(argv[0]) if argv else Path("/output/entry.txt")
    write_entry(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
