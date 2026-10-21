"""Generates images/icon.png for VSx Glow (black circle, green border, white glyph with green outline)."""
from PIL import Image, ImageDraw, ImageFilter, ImageChops

S = 1024            # supersampled canvas
OUT = 256           # final icon size
GREEN = (0, 230, 118, 255)
BLACK = (8, 9, 11, 255)
c = S // 2

def glow(mask, radius, color, strength=1.0):
    g = mask.filter(ImageFilter.GaussianBlur(radius))
    g = g.point(lambda v: min(255, int(v * strength)))
    layer = Image.new("RGBA", (S, S), color[:3] + (0,))
    layer.putalpha(g)
    return layer

img = Image.new("RGBA", (S, S), (0, 0, 0, 0))

# --- circle: soft outer glow, black body, green border ---
R = 440
ring_outer = Image.new("L", (S, S), 0)
ImageDraw.Draw(ring_outer).ellipse((c-R, c-R, c+R, c+R), fill=255)
img = Image.alpha_composite(img, glow(ring_outer, 22, GREEN, 1.1))

d = ImageDraw.Draw(img)
d.ellipse((c-R, c-R, c+R, c+R), fill=GREEN)
r_in = R - 30
d.ellipse((c-r_in, c-r_in, c+r_in, c+r_in), fill=BLACK)

# subtle inner highlight so the black looks modern / glossy
hl = Image.new("L", (S, S), 0)
ImageDraw.Draw(hl).ellipse((c-r_in+30, c-r_in+20, c+r_in-30, c-40), fill=22)
hl = hl.filter(ImageFilter.GaussianBlur(40))
hl_layer = Image.new("RGBA", (S, S), (255, 255, 255, 0)); hl_layer.putalpha(hl)
img = Image.alpha_composite(img, hl_layer)

# --- glyph (code-editor ribbon mark, original geometry, 24-unit grid) ---
pts = [(16.8,1.5),(22,4),(22,20),(16.8,22.5),(7.5,14),(3.5,17),(1.5,15),
       (5.5,12),(1.5,9),(3.5,7),(7.5,10)]
cut = [(17,7),(17,17),(10.8,12)]
scale, ox, oy = 21.5, c - 12*21.5, c - 12*21.5
tx = lambda p: (ox + p[0]*scale, oy + p[1]*scale)

mask = Image.new("L", (S, S), 0)
md = ImageDraw.Draw(mask)
md.polygon([tx(p) for p in pts], fill=255)
md.polygon([tx(p) for p in cut], fill=0)

outline = mask.filter(ImageFilter.MaxFilter(15))       # ~7px green outline
img = Image.alpha_composite(img, glow(outline, 26, GREEN, 1.6))   # glow
green_layer = Image.new("RGBA", (S, S), GREEN); green_layer.putalpha(outline)
img = Image.alpha_composite(img, green_layer)
white_layer = Image.new("RGBA", (S, S), (255, 255, 255, 255)); white_layer.putalpha(mask)
img = Image.alpha_composite(img, white_layer)

img.resize((OUT, OUT), Image.LANCZOS).save("images/icon.png")
img.resize((512, 512), Image.LANCZOS).save("images/logo-512.png")
print("ok")
