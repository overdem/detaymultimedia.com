# Cream Coffee & Kitchen · Tasarım sistemi

> Bu dosya Cream Coffee & Kitchen için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahvaltı / kafe · Kepez Sahil, Boğazkent
- **Sunum sayfası:** https://sunum.detaymultimedia.com/cream-coffee-kitchen-ornek/
- **Kaynak:** Logo: creamcoffeekitchen.com/img/logo.png (fincan amblemi + kalın serif 'Cream', 'COFFEE & KITCHEN'). 96×96 ölçüm: kahve #461E1E–#4B2B25; site CSS: --cream #F6F0E7, --coffee #4B2B25, --latte #C8A27C. Deniz/gün batımı tonu (#D98C5F) kendi gün batımı fotoğrafından (öneri).
- **Son güncelleme:** 24.11.2026

## Marka gözlemi

Kepez sahilinde denize sıfır, hasır gölgelikli kahvaltı; filtre kahve ve serpme kahvaltı yorumlarda öne çıkıyor; Google 4,7 (338). Ton: sakin, sıcak, deniz kenarı sabahı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `kahve` | `#4B2B25` | Logo: başlık, gövde, koyu zemin |
| `krem` | `#F6F0E7` | Ana açık zemin |
| `latte` | `#C8A27C` | Ara ton: çizgi, bant, büyük vurgu |
| `kum` | `#EADBC8` | İkincil açık zemin |
| `gunbatimi` | `#D98C5F` | Gün batımı: küçük vurgu (öneri) |

**Oranlar:** %50 krem/kum, %30 kahve, %15 latte, %5 gün batımı.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `kahve` yazı / `krem` zemin → **11.1:1** (AA ✓) — gövde
- `kahve` yazı / `kum` zemin → **9.3:1** (AA ✓) — gövde
- `krem` yazı / `kahve` zemin → **11.1:1** (AA ✓) — koyu kare
- `latte` yazı / `kahve` zemin → **5.3:1** (AA ✓) — büyük başlık vurgu
- `kahve` yazı / `latte` zemin → **5.3:1** (AA ✓) — bant yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Petrona** | 800 | Logodaki kalın serif 'Cream' karşılığı |
| Gövde | **Source Sans 3** | 400 / 600 | Menü, açıklama |
| Vurgu | **Great Vibes** | 400 | Kısa not: 'denize sıfır' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Petrona:wght@600;800&family=Source+Sans+3:wght@400;600&family=Great+Vibes&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 120–170 px Petrona 800
- Gövde: 30 px Source Sans 3 400
- Vurgu: 80–100 px Great Vibes, latte

**Tipografi kuralları:**

- Başlık küçük harfli, sıcak serif; büyük harfle bağırmaz.
- Great Vibes kare başına bir kez.
- Etiketler Source Sans 3 600, +30% aralık, büyük harf.

## Logo ve imza

- Web sitesindeki logo (kahve rengi, krem zemin); koyu zeminde krem renkli yazı-imza 'Cream' Petrona 800 + 'COFFEE & KITCHEN'.

## Görsel dil ve kompozisyon

- Motif: hasır şemsiye dokusu yerine ince yatay dalga çizgisi, yuvarlatılmış kart (24 px).
- Fotoğraflar: deniz, hasır gölgelik, kahvaltı, gün batımı.
- Reels: sabah → gün batımı akışı.

## Fotoğraf yönü (Higgsfield prompt eki)

```
creamy beige and coffee brown tones, seaside under woven straw parasols, soft morning light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --kahve: #4B2B25;
  --krem: #F6F0E7;
  --latte: #C8A27C;
  --kum: #EADBC8;
  --gunbatimi: #D98C5F;
  --font-baslik: 'Petrona', serif;
  --font-govde: 'Source Sans 3', sans-serif;
  --font-vurgu: 'Great Vibes', cursive;
}
```

## Yapma

- Neon ve soğuk renk kullanma.
- Maskot maymunu çizme ya da taklit etme (marka varlığı, ancak kendi dosyaları kullanılır).
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
