"""The Worst Pizza Topping — make.fun entry.

Competition: u-motasimfuad-the-worst-pizza-topping-062c6893
One funny line, under 200 characters, pitching a terrible pizza topping.
The program writes the line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt), after checking the gate: UTF-8 text of
1 to 200 characters, not only white space.
"""

import os
import sys

ENTRY = "Durian pizza: banned from three hotels, two airports, and now \u2014 triumphantly \u2014 your dinner table."

MAX_CHARS = 200


def check_gate(text):
    """Return True when the entry passes the competition gate."""
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > MAX_CHARS:
        return False
    if not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not check_gate(ENTRY):
        print("gate failed: entry is not 1-200 non-blank characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("verify failed: written bytes differ from entry", file=sys.stderr)
        return 1
    print("wrote %d bytes to %s" % (len(data), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
