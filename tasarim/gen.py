"""Firma tasarım MD'lerini tek kaynaktan üretir (palet + font sistemi + kontrast kontrolü)."""
import json, os

BANNED = ("Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, "
          "Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, "
          "Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, "
          "Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui")

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def gf_url(fonts):
    fams = []
    for f in fonts:
        fam = f['family'].replace(' ', '+')
        if f.get('axes'):
            fam += ':' + f['axes']
        fams.append('family=' + fam)
    return 'https://fonts.googleapis.com/css2?' + '&'.join(fams) + '&display=swap'

def render(c):
    pal = c['palette']; P = {p['token']: p['hex'] for p in pal}
    L = []
    L.append(f"# {c['name']} · Tasarım sistemi\n")
    L.append(f"> Bu dosya {c['name']} için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. "
             "Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.\n")
    L.append(f"- **Kategori:** {c['category']}")
    L.append(f"- **Sunum sayfası:** {c['page']}")
    L.append(f"- **Kaynak:** {c['source']}")
    L.append(f"- **Son güncelleme:** {c.get('updated', '21.11.2026')}\n")
    L.append("## Marka gözlemi\n")
    L.append(c['observation'] + "\n")
    L.append("## Renk paleti\n")
    L.append("| Token | Hex | Rol |")
    L.append("|---|---|---|")
    for p in pal:
        L.append(f"| `{p['token']}` | `{p['hex']}` | {p['role']} |")
    L.append("\n**Oranlar:** " + c['ratio'] + "\n")
    L.append("**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**\n")
    for fg, bg, note in c['pairs']:
        r = contrast(P[fg], P[bg])
        ok = 'AA ✓' if r >= 4.5 else ('yalnız büyük başlık ✓' if r >= 3 else 'KULLANMA ✗')
        L.append(f"- `{fg}` yazı / `{bg}` zemin → **{r:.1f}:1** ({ok}) — {note}")
    L.append("")
    L.append("## Font sistemi\n")
    L.append("| Rol | Font | Ağırlık / stil | Nerede |")
    L.append("|---|---|---|---|")
    for f in c['fonts']:
        L.append(f"| {f['role']} | **{f['family']}** | {f['weights']} | {f['use']} |")
    L.append(f"\nGoogle Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):\n\n```\n{gf_url(c['fonts'])}\n```\n")
    L.append("**Ölçek (1080×1350 kare için):**\n")
    for k, v in c['scale']:
        L.append(f"- {k}: {v}")
    L.append("\n**Tipografi kuralları:**\n")
    for r in c['type_rules']:
        L.append(f"- {r}")
    L.append("\n## Logo ve imza\n")
    for r in c['logo']:
        L.append(f"- {r}")
    L.append("\n## Görsel dil ve kompozisyon\n")
    for r in c['layout']:
        L.append(f"- {r}")
    L.append("\n## Fotoğraf yönü (Higgsfield prompt eki)\n")
    L.append(f"```\n{c['photo']}\n```\n")
    L.append("## Sunum sayfası CSS değişkenleri\n")
    L.append("```css\n:root {")
    for p in pal:
        L.append(f"  --{p['token']}: {p['hex']};")
    for f in c['fonts']:
        L.append(f"  --font-{f['var']}: '{f['family']}', {f['fallback']};")
    L.append("}\n```\n")
    L.append("## Yapma\n")
    for r in c['dont']:
        L.append(f"- {r}")
    L.append(f"- Şu fontları kullanma (standart/aşırı kullanılmış): {BANNED}.")
    L.append("")
    return '\n'.join(L)

if __name__ == '__main__':
    data = json.load(open(os.path.join(os.path.dirname(__file__), 'clients.json'), encoding='utf-8'))
    out = os.path.dirname(os.path.abspath(__file__)); os.makedirs(out, exist_ok=True)
    for c in data:
        md = render(c)
        open(os.path.join(out, c['slug'] + '.md'), 'w', encoding='utf-8').write(md)
        worst = min(contrast({p['token']: p['hex'] for p in c['palette']}[a], {p['token']: p['hex'] for p in c['palette']}[b]) for a, b, _ in c['pairs'])
        print(f"{c['slug']:30} min kontrast {worst:.1f}")
