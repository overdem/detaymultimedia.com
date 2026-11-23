import math
def laurel(color, w=360, leaves=8):
    """Defne çelengi: alttan iki yana açılan iki dal. SVG string."""
    cx = w / 2; r = w * 0.40; cy = r * 0.15
    out = []
    for side in (-1, 1):
        a0, a1 = 90 - side * 12, 90 - side * 150
        for k in range(leaves):
            t = (k + 0.5) / leaves
            a = math.radians(a0 + (a1 - a0) * t)
            px = cx + r * math.cos(a); py = cy + r * math.sin(a)
            tx, ty = -math.sin(a) * -side, math.cos(a) * -side   # yukarı giden teğet
            nx, ny = math.cos(a), math.sin(a)
            tang = math.degrees(math.atan2(ty, tx)); sz = 1 - t * 0.35
            L = w * 0.055 * sz; Wd = w * 0.02 * sz
            for sgn in (-1, 1):
                lx = px + nx * sgn * L * 0.7 + tx * L * 0.35; ly = py + ny * sgn * L * 0.7 + ty * L * 0.35
                out.append(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="{L:.1f}" ry="{Wd:.1f}" transform="rotate({tang + sgn*side*-38:.1f} {lx:.1f} {ly:.1f})" fill="{color}"/>')
        x0, y0 = cx + r*math.cos(math.radians(a0)), cy + r*math.sin(math.radians(a0))
        x1, y1 = cx + r*math.cos(math.radians(a1)), cy + r*math.sin(math.radians(a1))
        out.append(f'<path d="M{x0:.1f} {y0:.1f} A{r:.1f} {r:.1f} 0 0 {0 if side==1 else 1} {x1:.1f} {y1:.1f}" stroke="{color}" stroke-width="{w*0.007:.1f}" fill="none"/>')
    top = cy + r * math.sin(math.radians(90 - 150)) - w * 0.08
    hh = cy + r + w * 0.06 - top
    return f'<svg viewBox="0 {top:.0f} {w} {hh:.0f}" width="{w}" height="{hh:.0f}" xmlns="http://www.w3.org/2000/svg">{"".join(out)}</svg>'

def bulbs(color, n=12, w=1080, y=40, sag=40, r=9):
    pts = []
    for i in range(n):
        t = i / (n - 1); x = 40 + t * (w - 80); yy = y + sag * math.sin(math.pi * t)
        pts.append(f'<circle cx="{x:.0f}" cy="{yy+r*1.5:.0f}" r="{r}" fill="{color}"/>')
    path = ' '.join(f'{40 + i/(40)*(w-80):.0f},{y + sag*math.sin(math.pi*i/40):.0f}' for i in range(41))
    return f'<svg width="{w}" height="{y+sag+r*4}" xmlns="http://www.w3.org/2000/svg"><polyline points="{path}" stroke="{color}" stroke-opacity=".5" stroke-width="2" fill="none"/>{"".join(pts)}</svg>'
