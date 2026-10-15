#!/usr/bin/env python3
"""Syntagma's minimum local structure, Markdown-link and SVG validity checks."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
ROOMS = ("ATLAS", "MODEL", "BUILD", "DEV", "OPERATE", "EVIDENCE", "ARCHIVE")
REQUIRED = ["README.md", "AGENTS.md", "ATLAS/SOURCE-MAP.md"] + [f"{r}/README.md" for r in ROOMS]
errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"missing required file: {name}")

links = re.compile(r"!?\\[[^\\]]*\\]\\(([^)]+)\\)")
for md in ROOT.rglob("*.md"):
    for raw in links.findall(md.read_text(encoding="utf-8")):
        raw = raw.strip().split(" \\\"", 1)[0]
        if not raw or raw.startswith(("#", "http:", "https:", "mailto:", "data:")):
            continue
        file_part = raw.split("#", 1)[0].split("?", 1)[0]
        if not file_part:
            continue
        target = (md.parent / file_part).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"{md.relative_to(ROOT)}: missing target {raw}")

for svg in ROOT.rglob("*.svg"):
    try:
        ET.parse(svg)
    except ET.ParseError as exc:
        errors.append(f"{svg.relative_to(ROOT)}: invalid SVG: {exc}")

if errors:
    print("Syntagma structural FAIL:")
    for issue in errors:
        print(" -", issue)
    sys.exit(1)
print("Syntagma structural PASS: seven room maps, local links, and SVG syntax")
