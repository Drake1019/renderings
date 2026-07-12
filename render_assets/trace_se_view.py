from PIL import Image, ImageDraw

# SE corner view massing — match user's uploaded SketchUp screenshot geometry
S = 2
W, H = 1000 * S, 700 * S
img = Image.new("RGB", (W, H), (180, 180, 180))
d = ImageDraw.Draw(img)


def P(pts):
    return [(int(x * S), int(y * S)) for x, y in pts]


def poly(pts, fill, outline=(20, 20, 20), width=2):
    d.polygon(P(pts), fill=fill, outline=outline)
    d.line(P(pts) + [P(pts)[0]], fill=outline, width=max(1, width))


def line(pts, fill=(20, 20, 20), width=2):
    d.line(P(pts), fill=fill, width=max(1, width))


# Ground plane
d.rectangle([0, int(520 * S), W, H], fill=(235, 235, 235))

# ========== FAR-LEFT CANOPY (partial, white columns) ==========
poly([(0, 300), (160, 340), (160, 365), (0, 325)], fill=(245, 245, 245))
for cx in (50, 120):
    d.rectangle(
        [int(cx * S), int(360 * S), int((cx + 14) * S), int(520 * S)],
        fill=(250, 250, 250),
        outline=(20, 20, 20),
        width=2,
    )

# ========== BUILDING — SE corner ==========
# South face (left volume — lower, long, blank)
south = [(200, 340), (420, 355), (420, 510), (200, 530)]
poly(south, fill=(90, 90, 95))

# East face (right, taller, with drive-thru)
east = [(420, 355), (780, 300), (780, 470), (420, 510)]
poly(east, fill=(75, 75, 80))

# Roof south
roof_s = [(200, 340), (420, 355), (400, 310), (185, 300)]
poly(roof_s, fill=(60, 60, 65))

# Roof east (taller)
roof_e = [(420, 355), (780, 300), (760, 250), (400, 310)]
poly(roof_e, fill=(55, 55, 60))

# Mechanical penthouse on taller roof (rear/right)
ph = [(560, 230), (650, 215), (650, 265), (560, 280)]
poly(ph, fill=(170, 170, 175))
ph_top = [(560, 230), (650, 215), (640, 200), (555, 215)]
poly(ph_top, fill=(50, 50, 55))

# ========== MATERIAL BANDS (bottom → top) ==========
poly([(200, 490), (420, 475), (420, 510), (200, 530)], fill=(210, 195, 170))
poly([(420, 475), (780, 440), (780, 470), (420, 510)], fill=(200, 185, 160))

line([(200, 420), (420, 430)], width=3)
line([(420, 430), (780, 385)], width=3)

poly([(200, 355), (420, 368), (420, 390), (200, 378)], fill=(175, 175, 180))
poly([(420, 368), (780, 315), (780, 340), (420, 390)], fill=(165, 165, 170))

# ========== DRIVE-THRU (ONLY opening) on EAST face ==========
d.rectangle(
    [int(520 * S), int(400 * S), int(560 * S), int(435 * S)],
    fill=(90, 140, 190),
    outline=(20, 20, 20),
    width=2,
)
d.rectangle(
    [int(510 * S), int(388 * S), int(575 * S), int(398 * S)],
    fill=(35, 35, 40),
    outline=(20, 20, 20),
    width=2,
)


def car(x, y, w, h, color):
    d.rounded_rectangle(
        [int(x * S), int(y * S), int((x + w) * S), int((y + h) * S)],
        radius=4 * S,
        fill=color,
        outline=(20, 20, 20),
        width=2,
    )
    d.rectangle(
        [int((x + 8) * S), int((y - 8) * S), int((x + w - 10) * S), int(y * S)],
        fill=tuple(max(0, c - 20) for c in color),
        outline=(20, 20, 20),
        width=1,
    )
    d.ellipse(
        [int((x + 4) * S), int((y + h - 6) * S), int((x + 16) * S), int((y + h + 6) * S)],
        fill=(25, 25, 25),
    )
    d.ellipse(
        [int((x + w - 16) * S), int((y + h - 6) * S), int((x + w - 4) * S), int((y + h + 6) * S)],
        fill=(25, 25, 25),
    )


# Queue along east face: blue at window, brown behind, red further back
car(640, 465, 78, 28, (40, 70, 130))   # blue sedan at drive-thru window
car(545, 485, 72, 24, (90, 60, 40))    # dark brown sedan behind
car(450, 500, 70, 24, (170, 40, 40))   # red SUV further back

out = "/workspace/render_assets/se_corner_uploaded_view_trace.png"
img.save(out)
print("saved", out, img.size)
