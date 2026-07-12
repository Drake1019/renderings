#!/usr/bin/env python3
"""Render SE corner view once se-corner-source.png is provided by the user."""
from pathlib import Path

SOURCE = Path(__file__).parent / "se-corner-source.png"
if not SOURCE.exists():
    print(f"MISSING: {SOURCE}")
    print("Export your SketchUp screenshot and save it to that path for exact geometry.")
    raise SystemExit(1)
print(f"Source found: {SOURCE} ({SOURCE.stat().st_size} bytes)")
