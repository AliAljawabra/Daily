"""Ali Tutors — Google Business Profile: Logo + Cover photo.
Built from the REAL site source (docs/index.html, docs/assets/) —
exact CSS variables, the real logo mark, and the real headshot.
"""
import cairosvg
from PIL import Image, ImageDraw, ImageFont, ImageOps

REPO = "/home/user/Daily"
OUT = "/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/scratchpad"

# ---- exact palette from docs/index.html :root ----
NAVY      = (15, 42, 74)     # #0F2A4A
NAVY_DEEP = (10, 29, 52)     # #0A1D34
PAPER     = (247, 244, 238)  # #F7F4EE
PAPER_ALT = (239, 234, 224)  # #EFEAE0
INK       = (27, 36, 48)     # #1B2430
MUTED     = (91, 101, 114)   # #5B6572
LINE      = (221, 214, 199)  # #DDD6C7
GOLD      = (139, 107, 38)   # #8B6B26
GOLD_SOFT = (200, 168, 90)   # #C8A85A

# Georgia isn't installed here; DejaVu Serif is the closest available
# humanist serif for QA. Swap for the real Georgia render if this is
# ever rebuilt on a machine that has it.
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def tracked_w(d, txt, f, tracking=0):
    return sum(d.textlength(c, font=f) + tracking for c in txt) - (tracking if txt else 0)

def draw_tracked(d, xy, txt, f, fill, tracking=0):
    x, y = xy
    for ch in txt:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking
    return x

def rounded_photo(path, size, radius):
    im = Image.open(path).convert("RGB")
    im = ImageOps.fit(im, (size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=radius, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out

# ============================================================
# LOGO — 1080x1080, rendered straight from the real mark.svg,
# circular-crop safe zone respected (it already is: the mark sits
# centred with clear margin from all four corners).
# ============================================================
S = 1080
png_bytes = cairosvg.svg2png(url=f"{REPO}/docs/assets/mark.svg",
                              output_width=S, output_height=S)
with open(f"{OUT}/ali-tutors-logo.png", "wb") as fh:
    fh.write(png_bytes)
logo = Image.open(f"{OUT}/ali-tutors-logo.png").convert("RGB")
logo.save(f"{OUT}/ali-tutors-logo.png", optimize=True)
print("logo:", logo.size)

# ============================================================
# COVER PHOTO — 1200x675 (16:9), the real site's actual hero:
# cream paper background, navy serif headline, gold badge + accents,
# the real headshot, right where it sits on alitutors.com.
# ============================================================
W, H = 1200, 675
cov = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(cov, "RGBA")

# hairline footer rule, echoing the site's --line borders (used sparingly,
# not as a decorative stripe — this is the real site's own nav/footer rule)
d.line([(0, H-1), (W, H-1)], fill=(*LINE, 255), width=2)

# ---- small brand lockup, top-left: the real mark + wordmark ----
mark_png = cairosvg.svg2png(url=f"{REPO}/docs/assets/mark.svg", output_width=64, output_height=64)
open(f"{OUT}/_mark64.png", "wb").write(mark_png)
mark = Image.open(f"{OUT}/_mark64.png").convert("RGBA")
mx, my = int(W*0.075), int(H*0.09)
cov.paste(mark, (mx, my), mark)
f_brand = F(SERIF_REG, 30)
d.text((mx + 78, my + 15), "Ali Tutors", font=f_brand, fill=NAVY)

# ---- badge pill (exact same shape/copy language as the real site's .badge) ----
f_badge = F(SANS_BOLD, 19)
badge_txt = "NOW BOOKING AHEAD OF MOCKS"
bw = tracked_w(d, badge_txt, f_badge, tracking=2) + 44
bh = 40
bx, by = int(W*0.075), int(H*0.28)
d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=bh/2, fill=(255, 255, 255, 255), outline=(*GOLD_SOFT, 255), width=2)
d.ellipse([bx+18, by+bh/2-4, bx+26, by+bh/2+4], fill=(*GOLD_SOFT, 255))
draw_tracked(d, (bx+36, by+10), badge_txt, f_badge, GOLD, tracking=2)

# ---- the real headshot, right side, styled exactly like .hero-photo ----
# sized and placed FIRST so the text column below has a known safe width
photo_size = 380
gap = 56
px = int(W - photo_size - W*0.075)
py = int((H - photo_size) / 2)
photo = rounded_photo(f"{REPO}/docs/assets/ali-aljawabra.jpg", photo_size, radius=18)
# soft shadow (matches the site's box-shadow on .hero-photo img)
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle([px+2, py+18, px+photo_size+2, py+photo_size+18], radius=18, fill=(15, 42, 74, 60))
shadow = shadow.filter(__import__("PIL.ImageFilter", fromlist=["ImageFilter"]).GaussianBlur(14))
cov.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0,0,0,0)), shadow), (0, 0), shadow)
cov.paste(photo, (px, py), photo)
d.rounded_rectangle([px, py, px+photo_size, py+photo_size], radius=18, outline=(*LINE, 255), width=2)

# ---- text column: everything left of the photo, with a real margin ----
col_left = W * 0.072
col_w = px - gap - col_left

def fit_size(draw, txt, path, max_w, start=58, floor=30):
    size = start
    while size > floor:
        f = F(path, size)
        if draw.textlength(txt, font=f) <= max_w:
            return f, size
        size -= 2
    return F(path, floor), floor

# ---- headline, real copy, real serif/navy treatment, auto-fit to column ----
line1, line2 = "GCSE & A-level", "tutoring in Bath"
f1, sz = fit_size(d, line1, SERIF_REG, col_w, start=58, floor=34)
f2, _ = fit_size(d, line2, SERIF_REG, col_w, start=sz, floor=30)
hy = H * 0.375
d.text((col_left, hy), line1, font=f1, fill=NAVY)
lh = int(sz * 1.18)
d.text((col_left, hy + lh), line2, font=f2, fill=NAVY)

# ---- meta row, matches .hero-meta on the real site — wraps within the column ----
f_meta = F(SANS_REG, 21)
meta_items = ["Bath-based", "Online via Google Meet", "DBS checked"]
mx2 = col_left
my2 = hy + lh * 2 + 46
for i, item in enumerate(meta_items):
    iw = d.textlength(item, font=f_meta)
    sep_w = 34 if i < len(meta_items) - 1 else 0
    if mx2 + iw > col_left + col_w and mx2 > col_left:
        mx2 = col_left
        my2 += 36
    d.text((mx2, my2), item, font=f_meta, fill=MUTED)
    mx2 += iw
    if i < len(meta_items) - 1:
        d.text((mx2 + 12, my2 + 1), "·", font=f_meta, fill=GOLD_SOFT)
        mx2 += sep_w

cov = cov.convert("RGB")
cov.save(f"{OUT}/ali-tutors-cover-photo.png", optimize=True)
print("cover:", cov.size)

import os
os.remove(f"{OUT}/_mark64.png")
