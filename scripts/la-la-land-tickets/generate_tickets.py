#!/usr/bin/env python3
"""Generate a keepsake A4 PDF of two La La Land concert tickets."""

import math
import os
import random

from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

MM = 72.0 / 25.4
PAGE_W, PAGE_H = A4  # points, portrait

OUT_PATH = os.path.expanduser("~/la-la-land-tickets.pdf")

# ---------------------------------------------------------------- palette --

YELLOW = Color(0xF2 / 255, 0xCE / 255, 0x3E / 255)
YELLOW_FAINT = Color(0xF2 / 255, 0xCE / 255, 0x3E / 255, alpha=0.35)
CREAM = Color(0xFA / 255, 0xF3 / 255, 0xE2 / 255)
CREAM_DIM = Color(0xE7 / 255, 0xDE / 255, 0xC8 / 255, alpha=0.85)
LAVENDER = Color(0xD8 / 255, 0xC8 / 255, 0xE6 / 255, alpha=0.9)
SILHOUETTE = Color(0x0B / 255, 0x07 / 255, 0x14 / 255)
GREY_FOOTNOTE = Color(0.42, 0.42, 0.44)

GRAD_TOP = (0x16 / 255, 0x0E / 255, 0x30 / 255)      # deep indigo/violet
GRAD_BOTTOM = (0x5B / 255, 0x2B / 255, 0x4E / 255)   # warm dusk purple


def lerp(a, b, t):
    return a + (b - a) * t


def ease(t):
    # gentle ease so the warm dusk band at the bottom reads a bit richer
    return t ** 1.15


def draw_gradient(c, x, y, w, h, steps=260):
    """Fill a vertical gradient across a rect region already clipped."""
    step_h = h / steps
    for i in range(steps):
        t = ease(i / (steps - 1))
        r = lerp(GRAD_TOP[0], GRAD_BOTTOM[0], t)
        g = lerp(GRAD_TOP[1], GRAD_BOTTOM[1], t)
        b = lerp(GRAD_TOP[2], GRAD_BOTTOM[2], t)
        c.setFillColor(Color(r, g, b))
        yy = y + h - (i + 1) * step_h
        c.rect(x, yy, w, step_h + 0.4, stroke=0, fill=1)


def draw_sparkle(c, cx, cy, size, color, alpha=1.0):
    """A small four-pointed sparkle star."""
    col = Color(color.red, color.green, color.blue, alpha=alpha)
    c.setFillColor(col)
    outer = size
    inner = size * 0.32
    pts = []
    for i in range(8):
        ang = math.pi / 2 * (i // 2) + (0 if i % 2 == 0 else math.pi / 4)
        r = outer if i % 2 == 0 else inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def draw_five_star(c, cx, cy, r_outer, color):
    c.setFillColor(color)
    r_inner = r_outer * 0.382
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def draw_stars(c, x, y, main_w, h, seed):
    """Scatter a starfield over the upper portion of the main panel only,
    keeping clear of the title/label/subtitle text blocks."""
    rnd = random.Random(seed)
    # (xmin, xmax, ymin, ymax) fractions of (main_w, h) to keep clear of text
    exclusions = [
        (0.16, 0.84, 0.83, 0.92),   # small tracked label
        (0.10, 0.93, 0.63, 0.82),   # title
        (0.22, 0.88, 0.57, 0.64),   # italic subtitle
    ]
    min_frac_h = 0.50  # only the upper half of the ticket gets stars

    n = 90
    placed = 0
    attempts = 0
    while placed < n and attempts < n * 6:
        attempts += 1
        t = rnd.random() ** 1.6  # bias toward the very top
        fy = min_frac_h + t * (1.0 - min_frac_h)
        fx = rnd.random()
        if any(xa <= fx <= xb and ya <= fy <= yb for xa, xb, ya, yb in exclusions):
            continue
        sx = x + fx * main_w
        sy = y + fy * h
        rad = rnd.uniform(0.16, 0.6) * MM
        alpha = rnd.uniform(0.25, 0.8) * (1.0 - 0.3 * (1 - t))
        c.setFillColor(Color(1, 1, 1, alpha=max(0.12, alpha)))
        c.circle(sx, sy, rad, stroke=0, fill=1)
        placed += 1

    draw_sparkle(c, x + main_w * 0.055, y + h * 0.935, 2.5 * MM, YELLOW, alpha=0.9)
    draw_sparkle(c, x + main_w * 0.955, y + h * 0.905, 1.8 * MM, CREAM, alpha=0.85)


def draw_palm(c, base_x, base_y, scale):
    c.setFillColor(SILHOUETTE)
    trunk_w = 1.3 * MM * scale
    trunk_h = 7.0 * MM * scale
    lean = 1.6 * MM * scale
    p = c.beginPath()
    p.moveTo(base_x - trunk_w * 0.5, base_y)
    p.curveTo(base_x - trunk_w * 0.5 + lean * 0.3, base_y + trunk_h * 0.5,
              base_x + lean * 0.8, base_y + trunk_h * 0.85,
              base_x + lean, base_y + trunk_h)
    p.lineTo(base_x + lean + trunk_w, base_y + trunk_h)
    p.curveTo(base_x + lean * 0.8 + trunk_w, base_y + trunk_h * 0.85,
              base_x + trunk_w * 0.5 + lean * 0.3, base_y + trunk_h * 0.5,
              base_x + trunk_w * 0.5, base_y)
    p.close()
    c.drawPath(p, stroke=0, fill=1)

    crown_x, crown_y = base_x + lean, base_y + trunk_h
    frond_len = 5.4 * MM * scale
    base_w = 0.85 * MM * scale
    # angles measured from +x axis; spread fan-like above the crown, a
    # couple drooping near-horizontal so it silhouettes as a palm, not a bush
    angles_deg = [8, 40, 75, 108, 140, 172]
    for ang_deg in angles_deg:
        rad = math.radians(ang_deg)
        droop = frond_len * 0.45 * (1.0 - math.sin(rad))
        tip_x = crown_x + frond_len * math.cos(rad)
        tip_y = crown_y + frond_len * math.sin(rad) - droop
        mid_x = crown_x + frond_len * 0.55 * math.cos(rad)
        mid_y = crown_y + frond_len * 0.55 * math.sin(rad) - droop * 0.25
        perp = (-math.sin(rad), math.cos(rad))
        b1 = (crown_x + perp[0] * base_w, crown_y + perp[1] * base_w)
        b2 = (crown_x - perp[0] * base_w, crown_y - perp[1] * base_w)
        fp = c.beginPath()
        fp.moveTo(*b1)
        fp.curveTo(mid_x + perp[0] * base_w * 0.4, mid_y + perp[1] * base_w * 0.4,
                   tip_x, tip_y, tip_x, tip_y)
        fp.curveTo(mid_x - perp[0] * base_w * 0.4, mid_y - perp[1] * base_w * 0.4,
                   b2[0], b2[1], b2[0], b2[1])
        fp.close()
        c.drawPath(fp, stroke=0, fill=1)

    c.circle(crown_x, crown_y, base_w * 0.9, stroke=0, fill=1)


def draw_lamppost(c, base_x, base_y, scale):
    c.setFillColor(SILHOUETTE)
    pole_w = 0.55 * MM * scale
    pole_h = 13.5 * MM * scale
    c.rect(base_x - pole_w / 2, base_y, pole_w, pole_h, stroke=0, fill=1)
    c.rect(base_x - pole_w * 1.6, base_y, pole_w * 4.2, 0.9 * MM * scale, stroke=0, fill=1)

    arm_y = base_y + pole_h
    glow_r = 2.6 * MM * scale
    c.setFillColor(Color(YELLOW.red, YELLOW.green, YELLOW.blue, alpha=0.16))
    c.circle(base_x, arm_y + 1.4 * MM * scale, glow_r, stroke=0, fill=1)

    c.setFillColor(SILHOUETTE)
    lamp_w = 1.7 * MM * scale
    lamp_h = 2.3 * MM * scale
    p = c.beginPath()
    p.moveTo(base_x - lamp_w, arm_y)
    p.lineTo(base_x + lamp_w, arm_y)
    p.lineTo(base_x + lamp_w * 0.55, arm_y + lamp_h)
    p.lineTo(base_x - lamp_w * 0.55, arm_y + lamp_h)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.rect(base_x - lamp_w * 0.7, arm_y + lamp_h, lamp_w * 1.4, 0.7 * MM * scale, stroke=0, fill=1)


def tracked_text(c, x, y, text, font, size, char_space, color, align="left", alpha=1.0):
    col = Color(color.red, color.green, color.blue, alpha=alpha) if alpha != 1.0 else color
    c.setFillColor(col)
    c.setFont(font, size)
    if align == "center":
        c.drawCentredString(x, y, text, charSpace=char_space)
    elif align == "right":
        w = c.stringWidth(text, font, size) + char_space * max(0, len(text) - 1)
        c.drawString(x - w, y, text, charSpace=char_space)
    else:
        c.drawString(x, y, text, charSpace=char_space)


# ------------------------------------------------------------ ticket draw --

def draw_ticket(c, x0, y0, w, h, seed, seat_no):
    """x0,y0 = bottom-left corner of the ticket, in points."""
    radius = 3.6 * MM
    stub_w = 40 * MM
    main_w = w - stub_w
    perf_x = x0 + main_w

    # -- clipped background: gradient + stars + silhouette --------------
    c.saveState()
    p = c.beginPath()
    p.roundRect(x0, y0, w, h, radius)
    c.clipPath(p, stroke=0, fill=0)

    draw_gradient(c, x0, y0, w, h)
    draw_stars(c, x0, y0, main_w, h, seed)

    # ground silhouette across the main panel's lower edge
    ground_h = 3.2 * MM
    c.setFillColor(Color(SILHOUETTE.red, SILHOUETTE.green, SILHOUETTE.blue, alpha=0.92))
    c.rect(x0, y0, main_w, ground_h, stroke=0, fill=1)
    draw_palm(c, x0 + main_w * 0.045, y0 + ground_h * 0.35, 1.0)
    draw_lamppost(c, x0 + main_w * 0.955, y0 + ground_h * 0.35, 0.85)

    # subtle vignette at the very top for depth
    c.setFillColor(Color(0, 0, 0, alpha=0.12))
    c.rect(x0, y0 + h - 3 * MM, w, 3 * MM, stroke=0, fill=1)

    c.restoreState()

    # -- outer rounded border --------------------------------------------
    c.setStrokeColor(Color(0, 0, 0, alpha=0.35))
    c.setLineWidth(0.9)
    p2 = c.beginPath()
    p2.roundRect(x0, y0, w, h, radius)
    c.drawPath(p2, stroke=1, fill=0)

    # -- faint inner yellow border ----------------------------------------
    inset = 3.2 * MM
    c.setStrokeColor(YELLOW_FAINT)
    c.setLineWidth(0.5)
    p3 = c.beginPath()
    p3.roundRect(x0 + inset, y0 + inset, w - 2 * inset, h - 2 * inset, radius * 0.55)
    c.drawPath(p3, stroke=1, fill=0)

    # -- perforation notches (cut into background colour = white page) ---
    notch_r = 3.0 * MM
    c.setFillColor(Color(1, 1, 1))
    c.circle(perf_x, y0 + h, notch_r, stroke=0, fill=1)
    c.circle(perf_x, y0, notch_r, stroke=0, fill=1)

    # -- dashed perforation line -----------------------------------------
    c.saveState()
    c.setStrokeColor(Color(1, 1, 1, alpha=0.55))
    c.setLineWidth(1.0)
    c.setDash(3, 2.6)
    c.line(perf_x, y0 + notch_r + 1.2 * MM, perf_x, y0 + h - notch_r - 1.2 * MM)
    c.restoreState()

    # ================================================================
    # MAIN PANEL TEXT
    # ================================================================
    mx = x0 + main_w / 2.0

    tracked_text(c, mx, y0 + h - 12.0 * MM, "ROYAL ALBERT HALL  ·  LONDON",
                 "Helvetica-Bold", 7.6, 2.6, YELLOW, align="center")

    tracked_text(c, mx, y0 + h - 26.5 * MM, "LA LA LAND",
                 "Helvetica-Bold", 33, 7.4, CREAM, align="center")

    c.setFillColor(LAVENDER)
    c.setFont("Times-Italic", 11)
    c.drawCentredString(mx, y0 + h - 34.0 * MM, "in Concert - the film with live orchestra")

    # metadata grid: left column (3 rows), right column (2 rows)
    left_x = x0 + 12 * MM
    right_x = x0 + main_w * 0.56
    row0_y = y0 + h - 46.0 * MM
    row_gap = 10.8 * MM

    rows_left = [
        ("DATE", "Thursday 31 December 2026"),
        ("DOORS", "5.15pm"),
        ("SHOW", "6.00pm"),
    ]
    rows_right = [
        ("CONDUCTOR", "Justin Hurwitz"),
        ("ORCHESTRA", "Royal Philharmonic Concert Orchestra"),
    ]

    for i, (label, value) in enumerate(rows_left):
        ry = row0_y - i * row_gap
        tracked_text(c, left_x, ry, label, "Helvetica-Bold", 6.4, 1.8, YELLOW, align="left")
        c.setFillColor(CREAM)
        c.setFont("Helvetica-Bold", 10.4)
        c.drawString(left_x, ry - 4.6 * MM, value)

    for i, (label, value) in enumerate(rows_right):
        ry = row0_y - i * row_gap
        tracked_text(c, right_x, ry, label, "Helvetica-Bold", 6.4, 1.8, YELLOW, align="left")
        c.setFillColor(CREAM)
        font_size = 10.4 if len(value) < 20 else 8.6
        c.setFont("Helvetica-Bold", font_size)
        c.drawString(right_x, ry - 4.6 * MM, value)

    # ================================================================
    # STUB PANEL TEXT
    # ================================================================
    sx = perf_x + stub_w / 2.0

    draw_five_star(c, sx, y0 + h - 10.5 * MM, 3.1 * MM, YELLOW)

    stub_labels = ["STALLS", "BLOCK L", "ROW 5", "SEAT"]
    stub_y0 = y0 + h - 21.0 * MM
    stub_gap = 6.6 * MM
    for i, lab in enumerate(stub_labels):
        tracked_text(c, sx, stub_y0 - i * stub_gap, lab, "Helvetica-Bold", 6.6, 1.9,
                     YELLOW if i == 3 else CREAM, align="center")

    c.setFillColor(CREAM)
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(sx, y0 + 10.5 * MM, str(seat_no))

    tracked_text(c, sx, y0 + 4.6 * MM, "ADMIT ONE", "Helvetica-Bold", 6.0, 2.4, YELLOW, align="center")


def build_pdf():
    c = canvas.Canvas(OUT_PATH, pagesize=A4)

    ticket_w = 170 * MM
    ticket_h = 90 * MM
    x0 = (PAGE_W - ticket_w) / 2.0

    top_margin = 20 * MM
    bottom_margin = 15 * MM
    footer_h = 15 * MM
    gap_to_footer = 10 * MM

    fixed = top_margin + ticket_h * 2 + gap_to_footer + footer_h + bottom_margin
    gap_between = PAGE_H - fixed

    y_ticket1 = PAGE_H - top_margin - ticket_h
    y_ticket2 = y_ticket1 - gap_between - ticket_h

    draw_ticket(c, x0, y_ticket1, ticket_w, ticket_h, seed=7, seat_no=95)
    draw_ticket(c, x0, y_ticket2, ticket_w, ticket_h, seed=19, seat_no=96)

    footer_top = y_ticket2 - gap_to_footer
    c.setFillColor(Color(0.18, 0.16, 0.2))
    c.setFont("Times-Italic", 11.5)
    c.drawCentredString(PAGE_W / 2.0, footer_top - 5 * MM, "Here's to the fools who dream.")
    c.setFillColor(GREY_FOOTNOTE)
    c.setFont("Helvetica", 7)
    c.drawCentredString(PAGE_W / 2.0, footer_top - 10.5 * MM,
                         "Keepsake only - the official e-tickets are emailed separately and are what's scanned on the door.")

    c.showPage()
    c.save()
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    build_pdf()
