#!/usr/bin/env python3
"""Makes the small image variants the site serves (run once after changing the source photo/icon).

    python3 tools/make_images.py

Phones were downloading the 640px headshot to show a 76px avatar; srcset lets them take a ~4KB version.
Also writes docs/favicon.ico so crawlers that ask for /favicon.ico don't get a 404.
"""
from pathlib import Path
from PIL import Image

A = Path(__file__).resolve().parent.parent / "docs" / "assets"
src = Image.open(A / "ali-aljawabra.jpg").convert("RGB")
for w in (160, 330, 660):
    im = src.resize((w, w), Image.LANCZOS)
    im.save(A / f"ali-{w}.webp", "WEBP", quality=82, method=6)
    print("wrote", f"ali-{w}.webp", (A / f"ali-{w}.webp").stat().st_size, "bytes")

icon = Image.open(A / "icon-512.png").convert("RGB")
icon.save(A.parent / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("wrote favicon.ico")
