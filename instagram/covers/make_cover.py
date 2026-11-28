#!/usr/bin/env python3
"""Make a 1080x1920 reel cover: photo + two-line text in the 3:4 grid-safe band.
Usage: make_cover.py IN.jpg OUT.jpg "LINE ONE" "LINE TWO" [text_center_y] [KICKER]
KICKER is an optional small line above, e.g. "3 MICHELIN KEYS", or a path to a
.png (e.g. ../assets/michelin/keys-3-outline.png), which is placed above the text instead.
text_center_y is in px on the 1920-tall canvas (default 760). The 3:4 grid
crop keeps y=240..1680, so keep text between ~300 and ~1600."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
W, H = 1080, 1920
WHITE, RED = (255, 255, 255), (230, 40, 40)

def fit(draw, text, max_w, start):
    size = start
    while size > 30:
        f = ImageFont.truetype(FONT, size)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(FONT, size)

def main():
    src, out, l1, l2 = sys.argv[1:5]
    cy = int(sys.argv[5]) if len(sys.argv) > 5 else 760
    kicker = sys.argv[6] if len(sys.argv) > 6 else None
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    cx = float(os.environ.get("CENTER_X", "0.5"))  # 0..1, where to centre the crop
    im = ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(cx, 0.5))
    shade = os.environ.get("SHADE")  # e.g. SHADE=top: darken behind the text
    if shade == "top":
        g = Image.new("L", (1, H))
        for y in range(H):
            top_max = int(os.environ.get("SHADE_MAX", "200"))
            v = top_max if y < cy + 150 else max(0, int(top_max - (y - cy - 150) * 0.8))
            g.putpixel((0, y), v)
        g = g.resize((W, H))
        im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, g)
    elif shade == "bottom":
        g = Image.new("L", (1, H))
        start = cy - 420
        for y in range(H):
            g.putpixel((0, y), 0 if y < start else min(int(os.environ.get("SHADE_MAX", "205")), int((y - start) * 1.2)))
        g = g.resize((W, H))
        im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, g)
    elif shade == "band":
        g = Image.new("L", (1, H))
        for y in range(H):
            dist = abs(y - (cy - 90))
            g.putpixel((0, y), 190 if dist < 280 else max(0, int(190 - (dist - 280) * 1.2)))
        g = g.resize((W, H))
        im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, g)
    d = ImageDraw.Draw(im)
    f1 = fit(d, l1, 920, 150)
    f2 = fit(d, l2, 920, 150)
    b1 = d.textbbox((0, 0), l1, font=f1)
    b2 = d.textbbox((0, 0), l2, font=f2)
    h1, h2, gap = b1[3] - b1[1], b2[3] - b2[1], 36
    top = cy - (h1 + gap + h2) // 2
    # soft shadow for legibility
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    for (t, f, b, y) in ((l1, f1, b1, top), (l2, f2, b2, top + h1 + gap)):
        x = (W - (b[2] - b[0])) // 2 - b[0]
        sd.text((x + 4, y - b[1] + 6), t, font=f, fill=(0, 0, 0, 200))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    im = Image.alpha_composite(im.convert("RGBA"), sh)
    d = ImageDraw.Draw(im)
    for (t, f, b, y, c) in ((l1, f1, b1, top, WHITE), (l2, f2, b2, top + h1 + gap, RED)):
        x = (W - (b[2] - b[0])) // 2 - b[0]
        d.text((x, y - b[1]), t, font=f, fill=c)
    if kicker and kicker.lower().endswith(".png"):
        lg = Image.open(kicker).convert("RGBA")
        sc = min(440 / lg.width, 165 / lg.height)  # same height for 1, 2 or 3 icons
        lw = round(lg.width * sc)
        lg = lg.resize((lw, round(lg.height * sc)), Image.LANCZOS)
        im.alpha_composite(lg, ((W - lw) // 2, top - 45 - lg.height))
        d = ImageDraw.Draw(im)
    elif kicker:
        fk = ImageFont.truetype(FONT, 64)
        spaced = " ".join(kicker)  # letter-spaced
        spaced = spaced.replace("   ", "    ")
        bk = d.textbbox((0, 0), spaced, font=fk)
        while bk[2] - bk[0] > 920:
            fk = ImageFont.truetype(FONT, fk.size - 4)
            bk = d.textbbox((0, 0), spaced, font=fk)
        yk = top - 40 - (bk[3] - bk[1])
        xk = (W - (bk[2] - bk[0])) // 2 - bk[0]
        d.text((xk + 3, yk - bk[1] + 4), spaced, font=fk, fill=(0, 0, 0))
        d.text((xk, yk - bk[1]), spaced, font=fk, fill=(214, 182, 110))
    im.convert("RGB").save(out, quality=95)
    # grid preview (3:4 centre crop) for checking
    prev = im.convert("RGB").crop((0, 240, 1080, 1680))
    prev.save(out.rsplit(".", 1)[0] + "-grid-preview.jpg", quality=90)

if __name__ == "__main__":
    main()
