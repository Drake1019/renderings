# Render assets

Photorealistic exterior renders using the Millikin finish palette.

## SketchUp model workflow (recommended)

To render your **exact saved Scenes**, add your model to this folder:

```
render_assets/model.skp
```

Then either:

### Option A — Parse here (geometry + scene metadata)

```bash
python3 render_assets/parse_skp.py
```

This extracts the SKP archive, lists scene names/thumbnails, and exports `skp_extracted/model.glb`.

### Option B — Export scenes from SketchUp (best for exact camera views)

1. Open `model.skp` in SketchUp
2. Ruby Console: `load "render_assets/export_scenes.rb"`
3. Upload the exported PNGs to `render_assets/scenes/`

The Ruby script exports every saved Scene at 4000×3000 with the exact camera from your file.

## Millikin finish stack

1. Tan/beige ledger stone water table
2. Charcoal-gray brick
3. Dark horizontal accent bands
4. Light-gray upper lap siding
5. Matte black fascia, canopy, and trim

## Files

| File | Purpose |
|------|---------|
| `model.skp` | **Your SketchUp model** (add this) |
| `export_scenes.rb` | Batch-export all Scenes as PNG from SketchUp |
| `parse_skp.py` | Parse SKP, extract scenes/GLB without SketchUp |
| `scenes/*.png` | Exported scene images (exact camera) |
| `South_5156.pdf` | Earlier PDF export (2 embedded views) |

## South view renders (from PDF export)

- `south-view-millikin-render.png`
- `south-view-millikin-render-v2.png`

## SE corner renders (approximate — pending `model.skp`)

- `se-corner-exact-view-render.png`

**Note:** Chat image attachments are not saved as files. Commit `model.skp` or scene PNGs to the repo for exact geometry.
