#!/usr/bin/env python3
"""Fail when a local Markdown link points to a missing file."""

from __future__ import annotations

import re
from pathlib import Path


LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "obsidian://", "#")


def main() -> int:
    broken: list[tuple[Path, str]] = []

    for document in Path(".").rglob("*.md"):
        for target in LINK.findall(document.read_text(encoding="utf-8")):
            if target.startswith(EXTERNAL_PREFIXES):
                continue
            path = target.split("#", 1)[0]
            if path and not (document.parent / path).resolve().exists():
                broken.append((document, target))

    for document, target in broken:
        print(f"{document}: missing {target}")

    print(f"Broken relative links: {len(broken)}")
    return int(bool(broken))


if __name__ == "__main__":
    raise SystemExit(main())
