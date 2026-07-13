# How to give the agent exact building geometry

Built-in SKP scene thumbnails are only **256×143 px**. That is why drive-thru details (window size, canopy, wall openings) can drift in AI renders. Use any of the methods below — **Method 1 is best**.

---

## Method 1 — High-res PNG per Scene (RECOMMENDED)

1. Open `Rendering.skp` in **SketchUp Pro**
2. Click the **North view** scene tab (do not move the camera)
3. **File → Export → 2D Graphic…**
4. Set **Width: 4000** pixels (height scales automatically)
5. Save as `north-view-4000.png`
6. Click **South east View** scene tab
7. Export again at 4000px → `south-east-view-4000.png`
8. Upload both to `render_assets/scenes/` on GitHub and **Commit changes**
9. Message: **"high-res scenes uploaded"**

---

## Method 2 — Ruby batch export (all scenes at once)

1. Clone or download this repo
2. In SketchUp: **Window → Ruby Console**
3. Run (adjust path to your machine):

   ```ruby
   load "C:/Users/You/renderings/render_assets/export_scenes.rb"
   ```

4. Pick an output folder when prompted
5. Upload the exported PNGs to `render_assets/scenes/` and commit

---

## Method 3 — Drive-thru close-up (helps window size/placement)

1. Open **North view** scene
2. Orbit/zoom **only if needed** to frame the north-wall drive-thru window
3. Export 2D Graphic at **4000px** → `north-drive-thru-closeup.png`
4. Upload to `render_assets/scenes/` and commit

---

## Method 4 — Annotated markup (quick correction)

If you cannot export from SketchUp right now:

1. Open `north-view-millikin-render-v2.png` (or the wrong render) in Paint / Preview / Photoshop
2. Draw arrows or boxes showing:
   - Where the **small drive-thru window** should be (right end of north wall)
   - That it must **not** be a full-height door
   - Canopy location above the window
3. Save as `north-view-geometry-notes.png` and upload to `render_assets/scenes/`

---

## Method 5 — Written geometry checklist

Reply with a short checklist the agent can follow:

```
North facade:
- Drive-thru on NORTH wall (not east, not south)
- Right third of wall, counter-height small window (~4' wide)
- Black flat canopy above window only
- No other doors or glazing on north wall

South east view:
- Drive-thru on EAST face at corner
- South face is blank solid wall
```

---

## What helps most (ranked)

| Priority | What to upload | Why |
|----------|----------------|-----|
| 1 | 4000px scene PNGs from SketchUp | Exact camera + openings |
| 2 | Drive-thru close-up PNG | Locks window size and canopy |
| 3 | Annotated markup on wrong render | Fast correction without SketchUp |
| 4 | Text checklist | Good fallback; less precise than images |

After uploading, say **which files you added** and confirm: *"Drive-thru is on the north wall, right end, small window with canopy — not a door."*
