# South View — Millikin Finishes Render

Photorealistic exterior rendering of the South view SketchUp model (`South_5156.pdf`), using the Millikin finish palette.

## Finish stack (bottom → top)
1. Light tan/beige rough ashlar / ledger stone water table
2. Dark charcoal-gray brick primary walls
3. Thin dark horizontal ribbed / soldier accent bands
4. Light/medium-gray horizontal lap siding under the cornice
5. Matte black metal fascia, coping, brackets, and canopy
6. Matte black storefront frames with lightly blue-tinted glass

## Files
- `South_5156.pdf` — source South view export
- `south_source_stitched.png` / `south_embed_*.png` — extracted SketchUp frames
- `south_clean_ref.png` — cleaned reference (axes removed)
- `south-view-millikin-render.png` — primary photoreal render
- `south-view-millikin-render-v2.png` — alternate tighter geometry pass
- `south-view-comparison.png` — source vs render comparison strip

## Southeast corner view (Millikin finishes)

Photoreal render of the SE corner SketchUp massing with drive-thru queue.

- `se_corner_perspective_trace.png` — geometry reference trace
- `se-corner-millikin-render-v3.png` — primary render
- `se-corner-millikin-render-v2.png` — alternate pass
- `se-corner-comparison.png` — trace vs render comparison

### Southeast corner — exact uploaded view

Re-rendered from the uploaded SketchUp SE corner screenshot geometry (not the South PDF storefront view).

- `trace_se_view.py` — geometry trace script matching the uploaded view
- `se_corner_uploaded_view_trace.png` — traced massing from uploaded view
- `se-corner-exact-view-render.png` — latest render attempt (Millikin finishes)
- `se-corner-uploaded-view-render.png` — trace-locked render attempt

**For pixel-exact fidelity:** save your SketchUp screenshot as `render_assets/se-corner-source.png` so it can be used directly as a reference image.
