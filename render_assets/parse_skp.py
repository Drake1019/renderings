#!/usr/bin/env python3
"""Inspect a SketchUp .skp file: list scenes, thumbnails, and export GLB."""

from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

SKP_CANDIDATES = [
    Path(__file__).parent / "Rendering.skp",
    Path(__file__).parent / "rendering.skp",
    Path(__file__).parent / "model.skp",
]
OUT_DIR = Path(__file__).parent / "skp_extracted"


def resolve_skp(path: str | None = None) -> Path | None:
    if path:
        p = Path(path)
        return p if p.exists() else None
    for c in SKP_CANDIDATES:
        if c.exists():
            return c
    return None


def find_zip_offset(data: bytes) -> int | None:
    idx = data.find(b"PK\x03\x04")
    return idx if idx >= 0 else None


def list_zip_contents(skp: Path) -> list[str]:
    data = skp.read_bytes()
    offset = find_zip_offset(data)
    if offset is None:
        # Legacy format may be raw zip
        try:
            with zipfile.ZipFile(skp) as zf:
                return zf.namelist()
        except zipfile.BadZipFile:
            return []
    import io

    with zipfile.ZipFile(io.BytesIO(data[offset:])) as zf:
        return zf.namelist()


def extract_zip(skp: Path, out: Path) -> list[str]:
    out.mkdir(parents=True, exist_ok=True)
    data = skp.read_bytes()
    offset = find_zip_offset(data)
    import io

    if offset is not None:
        zf = zipfile.ZipFile(io.BytesIO(data[offset:]))
    else:
        zf = zipfile.ZipFile(skp)

    names = []
    with zf:
        for name in zf.namelist():
            target = out / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if not name.endswith("/"):
                target.write_bytes(zf.read(name))
                names.append(name)
    return names


def find_scene_names_in_xml(out: Path) -> list[str]:
    scenes: list[str] = []
    for xml in out.rglob("*.xml"):
        try:
            text = xml.read_text(errors="ignore")
        except OSError:
            continue
        # Scene/page names often appear as name="..." near Scene or Page tags
        for m in re.finditer(r"<(?:Scene|Page|scene|page)[^>]*name=\"([^\"]+)\"", text):
            scenes.append(m.group(1))
        for m in re.finditer(r"name=\"([^\"]+)\"[^>]*(?:Scene|Page)", text):
            scenes.append(m.group(1))
    return sorted(set(scenes))


def export_glb(skp: Path, out: Path) -> Path | None:
    try:
        from openskp import SkpFile
        from openskp.export import glb
    except ImportError:
        print("openskp not installed — run: pip install openskp")
        return None

    glb_path = out / "model.glb"
    skp_file = SkpFile.open(str(skp))
    model = skp_file.parse()
    glb.export(skp_file, str(glb_path))
    print(f"GLB exported: {glb_path}")
    print(f"  Materials: {len(model.materials)}")
    print(f"  Layers:    {len(model.layers)}")
    print(f"  Instances: {len(model.scene_hierarchy)}")
    return glb_path


def main() -> int:
    skp = resolve_skp(sys.argv[1] if len(sys.argv) > 1 else None)
    if not skp:
        print("SKP not found. Looked for:")
        for c in SKP_CANDIDATES:
            print(f"  {c}")
        print("Upload Rendering.skp to render_assets/ on GitHub and commit.")
        return 1

    print(f"Parsing: {skp} ({skp.stat().st_size:,} bytes)")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    names = list_zip_contents(skp)
    print(f"ZIP entries: {len(names)}")
    for n in names[:30]:
        print(f"  {n}")
    if len(names) > 30:
        print(f"  ... and {len(names) - 30} more")

    extracted = extract_zip(skp, OUT_DIR)
    print(f"Extracted {len(extracted)} files to {OUT_DIR}")

    thumbs = list(OUT_DIR.rglob("meta/*.png")) + list(OUT_DIR.rglob("**/thumbnail*.png"))
    if thumbs:
        print("Thumbnails / scene previews:")
        for t in thumbs:
            print(f"  {t}")

    scenes = find_scene_names_in_xml(OUT_DIR)
    if scenes:
        print("Scene names found in XML:")
        for s in scenes:
            print(f"  - {s}")
    else:
        print("No scene names found in XML (may need SketchUp export_scenes.rb)")

    export_glb(skp, OUT_DIR)

    summary = {
        "skp": str(skp),
        "zip_entries": len(names),
        "scenes_xml": scenes,
        "thumbnails": [str(t) for t in thumbs],
    }
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"Summary: {OUT_DIR / 'summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
