"""Ali Tutors — Google Business Profile: Logo + Cover photo.
Placeholder brand palette (matches the deck / topic sheet already sent).
Swap the six hex values below once real brand colours are confirmed.
"""
from PIL import Image, ImageDraw, ImageFont
import math

NAVY_DEEP = (7, 28, 51)      # 071C33
NAVY      = (13, 43, 78)     # 0D2B4E
AMBER     = (242, 169, 59)   # F2A93B
AMBER_D   = (212, 134, 27)   # D4861B
WHITE     = (255, 255, 255)
MUTED     = (195, 212, 229)  # C3D4E5

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def text_w(draw, txt, f, tracking=0):
    if tracking == 0:
        return draw.textlength(txt, font=f)
    return sum(draw.textlength(c, font=f) + tracking for c in txt) - tracking

def draw_tracked(draw, xy, txt, f, fill, tracking=0, anchor_left=True):
    x, y = xy
    if not anchor_left:
        x -= text_w(draw, txt, f, tracking)
    for ch in txt:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x

# ============================================================
# LOGO — 1080x1080, content kept inside the circular-crop safe zone
# ============================================================
S = 1080
img = Image.new("RGB", (S, S), NAVY_DEEP)
d = ImageDraw.Draw(img, "RGBA")

# soft depth ring, subtle
d.ellipse([S*0.04, S*0.04, S*0.96, S*0.96], fill=(*NAVY, 255))

# main amber badge — sized so it sits fully inside the circular safe zone
r = S * 0.365
cx, cy = S/2, S/2
d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*AMBER, 255))
# thin darker amber ring for definition
d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(*AMBER_D, 255), width=6)

f_mono = font(BOLD, int(S*0.30))
txt = "AT"
bbox = d.textbbox((0, 0), txt, font=f_mono)
tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
d.text((cx - tw/2 - bbox[0], cy - th/2 - bbox[1] - S*0.012), txt, font=f_mono, fill=NAVY_DEEP)

# small brand wordmark underneath the badge, inside safe zone, for context at larger sizes
f_small = font(BOLD, int(S*0.062))
label = "ALI TUTORS"
lw = text_w(d, label, f_small, tracking=int(S*0.010))
draw_tracked(d, (cx - lw/2, cy + r + S*0.045), label, f_small, WHITE, tracking=int(S*0.010))

img.save("/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/scratchpad/ali-tutors-logo.png", optimize=True)

# ============================================================
# COVER PHOTO — 1200x675 (16:9), safe text margins
# ============================================================
W, H = 1200, 675
cov = Image.new("RGB", (W, H), NAVY_DEEP)
d2 = ImageDraw.Draw(cov, "RGBA")

# decorative circles, top-right, bleeding off-canvas (matches the deck's title slide)
d2.ellipse([W*0.62, -H*0.42, W*0.62+H*1.05, -H*0.42+H*1.05], fill=(*NAVY, 255))
d2.ellipse([W*0.92, H*0.58, W*0.92+H*0.55, H*0.58+H*0.55], fill=(*AMBER, 255))

# kicker
f_kick = font(BOLD, 24)
draw_tracked(d2, (W*0.075, H*0.185), "1-TO-1 TUTORING", f_kick, AMBER, tracking=4)

# wordmark
f_word = font(BOLD, 92)
d2.text((W*0.072, H*0.29), "Ali Tutors", font=f_word, fill=WHITE)

# tagline
f_tag = font(REG, 34)
d2.text((W*0.075, H*0.585), "Online & in-person tutoring  ·  GCSE · IGCSE · A-Level · SAT",
         font=f_tag, fill=MUTED)

# small pill accent
f_pill = font(BOLD, 24)
pill_txt = "TUTORING SINCE 2019"
pw = text_w(d2, pill_txt, f_pill, tracking=3) + 56
ph = 56
px, py = W*0.075, H*0.755
d2.rounded_rectangle([px, py, px+pw, py+ph], radius=ph/2, fill=(*AMBER, 255))
draw_tracked(d2, (px+28, py+15), pill_txt, f_pill, NAVY_DEEP, tracking=3)

cov.save("/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/scratchpad/ali-tutors-cover-photo.png", optimize=True)

print("logo:", img.size, "cover:", cov.size)
