#!/usr/bin/env python3
"""Make a 1080x1920 reel cover: photo + two-line text in the 3:4 grid-safe band.
Usage: make_cover.py IN.jpg OUT.jpg "LINE ONE" "LINE TWO" [text_center_y]
text_center_y is in px on the 1920-tall canvas (default 760). The 3:4 grid
crop keeps y=240..1680, so keep text between ~300 and ~1600."""
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
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im = ImageOps.fit(im, (W, H), Image.LANCZOS)
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
    im.convert("RGB").save(out, quality=95)
    # grid preview (3:4 centre crop) for checking
    prev = im.convert("RGB").crop((0, 240, 1080, 1680))
    prev.save(out.rsplit(".", 1)[0] + "-grid-preview.jpg", quality=90)

if __name__ == "__main__":
    main()
