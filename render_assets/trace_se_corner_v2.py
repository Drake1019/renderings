"""Precise trace of user's uploaded SE corner SketchUp view.

Key geometry from upload:
- Elevated 3/4 perspective, SE corner in foreground
- Lower south mass (left/near), taller east mass extends far right (dominant long wall)
- Sharp 90° corner, flat roofs, centered penthouse on taller roof
- Material bands: tan base → grey brick + dark reveal → thick LIGHT fascia → dark coping
- Drive-thru only opening on east wall; cars: blue (back), brown (mid), red SUV (at window)
- Partial white canopy far left with two columns
"""
from PIL import Image, ImageDraw

S = 3
W, H = 1400 * S, 900 * S
BG = (170, 170, 170)
GROUND = (215, 215, 215)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def p(pts):
    return [(int(x * S), int(y * S)) for x, y in pts]


def poly(pts, fill, outline=(20, 20, 20), width=2):
    pts2 = p(pts)
    d.polygon(pts2, fill=fill, outline=outline)
    d.line(pts2 + [pts2[0]], fill=outline, width=max(1, width))


def ln(pts, fill=(20, 20, 20), width=2):
    d.line(p(pts), fill=fill, width=max(1, width))


# Sloped ground plane (rises left to right)
ground = [(0, 620), (W, 560), (W, H), (0, H)]
poly(ground, fill=GROUND)

# ========== FAR-LEFT CANTILEVER CANOPY (white, cut off) ==========
poly([(0, 220), (230, 255), (230, 280), (0, 245)], fill=(250, 250, 250))
for cx in (60, 165):
    d.rectangle(
        [int(cx * S), int(280 * S), int((cx + 18) * S), int(620 * S)],
        fill=(248, 248, 248),
        outline=(20, 20, 20),
        width=2,
    )

# ========== BUILDING — east wall DOMINATES view ==========
# SE corner near left-third; east face runs long to the right

# South face (narrower — near corner only, lower parapet)
south = [(260, 390), (420, 400), (420, 565), (260, 575)]
poly(south, fill=(125, 125, 130))

# East face (long dominant wall — taller parapet)
east = [(420, 400), (1180, 335), (1180, 515), (420, 565)]
poly(east, fill=(110, 110, 115))

# Roofs
poly([(260, 390), (420, 400), (405, 350), (250, 342)], fill=(65, 65, 70))
poly([(420, 400), (1180, 335), (1165, 285), (405, 350)], fill=(55, 55, 60))

# Penthouse centered on taller east roof
poly([(760, 255), (880, 245), (880, 295), (760, 308)], fill=(180, 180, 185))
poly([(760, 255), (880, 245), (870, 228), (755, 240)], fill=(40, 40, 45))

# ========== MATERIAL BANDS ==========
# Tan stone base
poly([(260, 525), (420, 518), (420, 565), (260, 575)], fill=(212, 192, 158))
poly([(420, 518), (1180, 468), (1180, 515), (420, 565)], fill=(205, 185, 150))

# Dark horizontal reveal mid-brick
ln([(265, 470), (415, 465)], width=4)
ln([(425, 465), (1175, 410)], width=4)

# Thick LIGHT fascia/cornice above brick (key feature in upload)
poly([(260, 410), (420, 418), (420, 438), (260, 430)], fill=(235, 235, 238))
poly([(420, 418), (1180, 360), (1180, 380), (420, 438)], fill=(228, 228, 232))

# Dark parapet coping (top edge above fascia)
ln([(250, 342), (405, 350), (420, 400)], width=6)
ln([(405, 350), (1165, 285), (1180, 335), (420, 400)], width=6)

# ========== DRIVE-THRU on east wall ==========
d.rectangle(
    [int(860 * S), int(445 * S), int(895 * S), int(478 * S)],
    fill=(95, 145, 195),
    outline=(20, 20, 20),
    width=2,
)
d.rectangle(
    [int(848 * S), int(433 * S), int(910 * S), int(443 * S)],
    fill=(28, 28, 32),
    outline=(20, 20, 20),
    width=2,
)


def car(x, y, w, h, color):
    d.rounded_rectangle(
        [int(x * S), int(y * S), int((x + w) * S), int((y + h) * S)],
        radius=3 * S,
        fill=color,
        outline=(20, 20, 20),
        width=2,
    )
    d.polygon(
        p([(x + 5, y), (x + w - 6, y), (x + w - 10, y + 9), (x + 9, y + 9)]),
        fill=(175, 205, 225),
        outline=(20, 20, 20),
    )
    for wx in (x + 7, x + w - 17):
        d.ellipse(
            [int(wx * S), int((y + h - 3) * S), int((wx + 12) * S), int((y + h + 7) * S)],
            fill=(28, 28, 28),
        )


# Queue BACK → FRONT along east wall (left to right toward window)
car(620, 555, 62, 20, (42, 72, 138))    # blue back
car(760, 545, 65, 21, (72, 58, 48))     # brown middle
car(900, 530, 78, 26, (188, 38, 38))    # red SUV at window

out = "/workspace/render_assets/se-corner-exact-geometry.png"
img.save(out)
print("saved", out, img.size)
