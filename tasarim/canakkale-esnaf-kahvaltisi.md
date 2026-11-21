# Çanakkale Esnaf Kahvaltısı · Tasarım sistemi

> Bu dosya Çanakkale Esnaf Kahvaltısı için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahvaltı · İsmetpaşa
- **Sunum sayfası:** https://sunum.detaymultimedia.com/canakkale-esnaf-kahvaltisi-ornek/
- **Kaynak:** Instagram @canakkaleesnafkahvaltisi profil logosu (21.11.2026): beyaz zemin, koyu arduvaz mavi-gri serif büyük harf 'ÇANAKKALE ESNAF KAHVALTISI', defne çelengi, alt satırda 'PAKET KAHVALTI · PİŞİ · GÖZLEME'. Bio: 'Çanakkale'nin İlk Esnaf Kahvaltıcısı'.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Tek renk arduvaz + defne çelengi: köklü, 'ilk' olma iddiası, esnaf ciddiyeti. Ürünler pişi, gözleme, paket kahvaltı. Ton: klasik, güvenilir, çarşı esnafı; sade.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `arduvaz` | `#33475A` | Logo rengi: başlık, çelenk, çizgi |
| `murekkep` | `#1E2A36` | Gövde yazısı, koyu zemin |
| `defne` | `#8C9A80` | İkincil: çelenk yaprak tonu, ayraç |
| `kagit` | `#FAF8F3` | Ana zemin |
| `pisi` | `#E8A93A` | Ürün vurgusu: kızarmış pişi sarısı (az) |

**Oranlar:** %65 kagit, %25 arduvaz/murekkep, %6 defne, %4 pisi.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `arduvaz` yazı / `kagit` zemin → **9.0:1** (AA ✓) — başlık
- `murekkep` yazı / `kagit` zemin → **13.7:1** (AA ✓) — gövde
- `kagit` yazı / `arduvaz` zemin → **9.0:1** (AA ✓) — koyu şerit
- `murekkep` yazı / `pisi` zemin → **7.1:1** (AA ✓) — fiyat rozeti
- `murekkep` yazı / `defne` zemin → **4.9:1** (AA ✓) — etiket

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Bona Nova** | 700 büyük harf | Logodaki klasik serif büyük harflerin karşılığı |
| Gövde | **Literata** | 400 / 600 | Açıklama, menü |
| Menü/fiş | **Courier Prime** | 400 / 700 | Paket kahvaltı içeriği, fiyat listesi; esnaf fişi havası |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Bona+Nova:wght@400;700&family=Literata:wght@400;600&family=Courier+Prime:wght@400;700&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 80–100 px Bona Nova 700, büyük harf, +6%
- Gövde: 30 px Literata 400
- Menü satırı: 26–28 px Courier Prime
- Alt satır: 20 px Bona Nova, büyük harf, +20%, nokta ayraçlı (PİŞİ · GÖZLEME)

**Tipografi kuralları:**

- Kapak düzeni logodan: ortalı başlık + defne çelengi + noktalı alt satır.
- Paket içerikleri Courier Prime fiş listesi gibi, noktalı çizgi ile fiyat.
- 'İlk esnaf kahvaltıcısı' iddiası rozet içinde Bona Nova ile.

## Logo ve imza

- Defne çelenkli logo ortada, kapakta büyük (genişliğin %40'ı), iç karelerde küçük alt ortada.
- Tek renk arduvaz; koyu zeminde kağıt rengi.

## Görsel dil ve kompozisyon

- Motif: defne çelengi (yarım ya da tam), noktalı fiş çizgileri.
- Fotoğraflar kuşbakışı tepsi, bakır/demlik detayı; kağıt zeminli kartlarda.
- Reels: pişi tavada kabarma, gözleme katlama; geçişte fiş kâğıdı aşağı kayar.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Traditional Turkish tradesmen breakfast, fried pişi dough, gözleme, white cheese, olives, tea in tulip glasses on a simple tray, morning light in a classic local eatery, honest and clean, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --arduvaz: #33475A;
  --murekkep: #1E2A36;
  --defne: #8C9A80;
  --kagit: #FAF8F3;
  --pisi: #E8A93A;
  --font-baslik: 'Bona Nova', Georgia, serif;
  --font-govde: 'Literata', Georgia, serif;
  --font-vurgu: 'Courier Prime', monospace;
}
```

## Yapma

- Polaroid/pastel 'eğlenceli' stil kullanma; marka klasik ve ciddi.
- Logoyu renklendirme.
- El yazısı font ekleme.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
