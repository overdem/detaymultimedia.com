# Beyzade Pide & Lahmacun · Tasarım sistemi

> Bu dosya Beyzade Pide & Lahmacun için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Pide / lahmacun · Cevat Paşa
- **Sunum sayfası:** https://sunum.detaymultimedia.com/beyzade-pide-lahmacun-ornek/
- **Kaynak:** Instagram @beyzadepide17 profil logosu (21.11.2026): hardal-altın halka, krem iç, siyah aşçı şapkası ve bıyık, kahverengi serif 'BEYZADE', oklava çizgisi; öne çıkanlarda siyah çizgi ikonlar (pide, lahmacun, kebap, künefe).
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Altın halka + kahverengi serif + siyah karakter çizimi: 'usta' kişiliği güçlü (şapka ve bıyık). Ton: iştahlı, geleneksel, esprili usta karakteri; fırın sıcaklığı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `altin` | `#DDA03F` | Logo halkası: vurgu zemini, rozet, şerit |
| `tarcin` | `#6E4A2C` | Logo yazısı: başlık |
| `is` | `#2B2B2B` | Şapka/bıyık siyahı: gövde yazısı, çizgi ikonlar |
| `un` | `#FBF6EA` | Ana açık zemin |
| `kor` | `#B4471F` | Fırın ateşi vurgusu, fiyat |

**Oranlar:** %55 un, %20 altin, %15 tarcin/is, %10 kor.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `tarcin` yazı / `un` zemin → **7.3:1** (AA ✓) — başlık
- `is` yazı / `un` zemin → **13.1:1** (AA ✓) — gövde
- `is` yazı / `altin` zemin → **6.2:1** (AA ✓) — altın şerit içi yazı
- `un` yazı / `kor` zemin → **5.0:1** (AA ✓) — fiyat rozeti
- `un` yazı / `is` zemin → **13.1:1** (AA ✓) — koyu kart

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Gloock** | 400 | Logodaki yüksek kontrastlı serifin karşılığı; ürün adları |
| Gövde | **Golos Text** | 400 / 600 | Açıklama, sipariş hattı, adres |
| Fiyat/sayı | **Coustard** | 900 | Fiyat, adet, '2 lahmacun + ayran' gibi kampanya rakamları |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Gloock&family=Golos+Text:wght@400;600&family=Coustard:wght@400;900&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 104–128 px Gloock
- Fiyat: 96 px Coustard 900
- Gövde: 30–32 px Golos 400
- Etiket: 22 px Golos 600, büyük harf, +10%

**Tipografi kuralları:**

- 'BEYZADE' kelimesi her zaman büyük harf Gloock + tarcin.
- Fiyatlar Coustard 900 altın daire içinde.
- Siyah çizgi ikon dili (öne çıkanlardaki gibi) menü karelerinde kullanılır.

## Logo ve imza

- Altın halkalı rozet logo kare genişliğinin %18'i, sol üst; koyu karede krem iç korunur.
- Usta karakteri (şapka + bıyık) ayrı bir maskot gibi kullanılabilir: 'Usta önerisi' etiketi.

## Görsel dil ve kompozisyon

- Motif: oklava çizgisi (ince yatay çizgi, uçları yuvarlak) ayraç olarak; altın yarım halka kare köşelerinde.
- Fotoğraflar fırından çıkış anı, taş fırın ağzı; un zemin üstünde.
- Reels: hamur açma → fırın → kesme; geçişte oklava çizgisi ekranı süpürür.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Turkish pide and lahmacun fresh out of a stone oven, wooden peel, flour dusted marble counter, warm oven glow, chef hands, appetizing close-up, golden and brown tones, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --altin: #DDA03F;
  --tarcin: #6E4A2C;
  --is: #2B2B2B;
  --un: #FBF6EA;
  --kor: #B4471F;
  --font-baslik: 'Gloock', Georgia, serif;
  --font-govde: 'Golos Text', sans-serif;
  --font-vurgu: 'Coustard', serif;
}
```

## Yapma

- Mavi/yeşil soğuk tonlar kullanma.
- Usta karakterini değiştirme ya da yeni maskot çizme.
- Altını parlak metalik gradyan yapma; mat hardal kalmalı.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
