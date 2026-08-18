"""Cartão Open Graph 1200x630 e favicon PNG."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"
IMAGES.mkdir(exist_ok=True)

W, H = 1200, 630
BG = (244, 241, 234)
INK = (31, 42, 48)
BLUE = (57, 114, 158)
MUTED = (90, 99, 105)
URL = (122, 130, 136)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


georgia = r"C:\Windows\Fonts\georgia.ttf"
georgia_b = r"C:\Windows\Fonts\georgiab.ttf"
segoe = r"C:\Windows\Fonts\segoeui.ttf"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, 18, H), fill=BLUE)

x = 88
draw.text((x, 148), "PATRICK RODRIGUES ANDRADE", font=font(georgia_b, 42), fill=INK)
draw.text((x, 220), "Departamento de Economia, PUC-SP", font=font(georgia, 32), fill=BLUE)
draw.rectangle((x, 278, x + 72, 282), fill=BLUE)
draw.text(
    (x, 318),
    "Economia aplicada, políticas públicas\ne análise de dados reprodutível.",
    font=font(segoe, 28),
    fill=MUTED,
    spacing=10,
)
draw.text((x, 540), "patrick-andrade.github.io", font=font(segoe, 22), fill=URL)

out = IMAGES / "og-card.png"
img.save(out, "PNG", optimize=True)
print(f"wrote {out} {img.size}")

# Favicon PNG 32x32 (fallback for clients that ignore SVG)
fav = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
d = ImageDraw.Draw(fav)
d.rounded_rectangle((0, 0, 63, 63), radius=10, fill=BLUE)
d.text((32, 30), "PA", font=font(georgia_b, 26), fill=(255, 255, 255), anchor="mm")
fav32 = fav.resize((32, 32), Image.Resampling.LANCZOS)
fav32.save(ROOT / "favicon.png", "PNG", optimize=True)
print(f"wrote {ROOT / 'favicon.png'}")
