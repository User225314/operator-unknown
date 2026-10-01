"""Decode the fictional transmission in this repository; no network access."""
from pathlib import Path
import re


def decode(text: str) -> str:
    match = re.search(r"^PAYLOAD:\s*((?:[0-9A-Fa-f]{2}\s*)+)$", text, re.MULTILINE)
    if not match:
        raise ValueError("No valid hexadecimal PAYLOAD line")
    return bytes.fromhex(match.group(1)).decode("utf-8")


if __name__ == "__main__":
    file = Path(__file__).parent / "transmissions" / "001.txt"
    print(decode(file.read_text(encoding="utf-8")))
