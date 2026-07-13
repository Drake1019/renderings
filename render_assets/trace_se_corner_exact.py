"""Trace of user's uploaded SE corner SketchUp view — elevated 3/4 perspective."""
from PIL import Image, ImageDraw

S = 3
W, H = 1200 * S, 800 * S
BG = (175, 175, 175)
GROUND = (220, 220, 220)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def p(pts):
    return [(int(x * S), int(y * S)) for x, y in pts]


def poly(pts, fill, outline=(25, 25, 25), width=2):
    pts2 = p(pts)
    d.polygon(pts2, fill=fill, outline=outline)
    d.line(pts2 + [pts2[0]], fill=outline, width=max(1, width))


def ln(pts, fill=(25, 25, 25), width=2):
    d.line(p(pts), fill=fill, width=max(1, width))


# Ground plane (light grey paved path)
d.rectangle([0, int(560 * S), W, H], fill=GROUND)

# ========== FAR-LEFT WHITE CANTILEVERED CANOPY (partial, cut off) ==========
poly([(0, 250), (200, 285), (200, 310), (0, 275)], fill=(248, 248, 248))
for cx in (55, 145):
    d.rectangle(
        [int(cx * S), int(310 * S), int((cx + 16) * S), int(560 * S)],
        fill=(245, 245, 245),
        outline=(25, 25, 25),
        width=2,
    )

# ========== BUILDING MASSES — sharp 90° SE corner in foreground ==========
# Foreground LEFT mass = lower south wing (shorter parapet)
# Background RIGHT mass = taller east wing (higher parapet, extends further right)

# South face (left wall — lower, blank solid)
south_wall = [(180, 360), (430, 375), (430, 545), (180, 560)]
poly(south_wall, fill=(130, 130, 135))

# East face (right wall — taller, longer, drive-thru here)
east_wall = [(430, 375), (920, 320), (920, 500), (430, 545)]
poly(east_wall, fill=(115, 115, 120))

# South roof deck (lower parapet)
south_roof = [(180, 360), (430, 375), (415, 330), (170, 318)]
poly(south_roof, fill=(70, 70, 75))

# East roof deck (taller parapet)
east_roof = [(430, 375), (920, 320), (900, 265), (415, 330)]
poly(east_roof, fill=(60, 60, 65))

# ========== MATERIAL BANDS on both faces (bottom → top) ==========
# 1) Tan/beige split-face stone base
poly([(180, 505), (430, 492), (430, 545), (180, 560)], fill=(210, 190, 155))
poly([(430, 492), (920, 455), (920, 500), (430, 545)], fill=(205, 185, 150))

# 2) Grey brick main field (model shows grey; render will be charcoal)
# already in wall fill

# 3) Dark horizontal reveal / belt course (mid-wall)
ln([(185, 455), (425, 448)], width=4)
ln([(435, 448), (915, 405)], width=4)

# 4) Thick light fascia/cornice band above brick
poly([(180, 385), (430, 395), (430, 415), (180, 405)], fill=(225, 225, 228))
poly([(430, 395), (920, 345), (920, 365), (430, 415)], fill=(220, 220, 225))

# 5) Dark parapet coping cap (top edge)
ln([(170, 318), (415, 330), (430, 375)], width=5)
ln([(415, 330), (900, 265), (920, 320), (430, 375)], width=5)

# ========== MECHANICAL PENTHOUSE — centered on taller (east) roof ==========
ph_body = [(620, 235), (730, 225), (730, 275), (620, 288)]
poly(ph_body, fill=(185, 185, 190))
ph_cap = [(620, 235), (730, 225), (720, 210), (615, 222)]
poly(ph_cap, fill=(45, 45, 50))

# ========== DRIVE-THRU — only opening, on east (right) wall ==========
# Service window
d.rectangle(
    [int(700 * S), int(430 * S), int(735 * S), int(465 * S)],
    fill=(100, 150, 200),
    outline=(25, 25, 25),
    width=2,
)
# Thin black canopy above window
d.rectangle(
    [int(688 * S), int(418 * S), int(750 * S), int(428 * S)],
    fill=(30, 30, 35),
    outline=(25, 25, 25),
    width=2,
)


def car(x, y, w, h, color, label=""):
    d.rounded_rectangle(
        [int(x * S), int(y * S), int((x + w) * S), int((y + h) * S)],
        radius=3 * S,
        fill=color,
        outline=(25, 25, 25),
        width=2,
    )
    # windshield
    d.polygon(
        p([(x + 6, y), (x + w - 8, y), (x + w - 12, y + 10), (x + 10, y + 10)]),
        fill=(180, 210, 230),
        outline=(25, 25, 25),
    )
    # wheels
    for wx in (x + 8, x + w - 18):
        d.ellipse(
            [int(wx * S), int((y + h - 4) * S), int((wx + 14) * S), int((y + h + 8) * S)],
            fill=(30, 30, 30),
        )


# Cars along east wall — BACK to FRONT toward window:
# blue (back), brown (middle), red SUV (front/at window)
car(480, 530, 65, 22, (45, 75, 140))    # blue sedan — back of queue
car(590, 520, 68, 23, (75, 60, 50))     # dark brown sedan — middle
car(710, 505, 80, 28, (185, 40, 40))    # red SUV — at service window

out = "/workspace/render_assets/se-corner-source-trace.png"
img.save(out)
print("saved", out, img.size)
