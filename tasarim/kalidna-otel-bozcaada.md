# Kalidna Otel Bozcaada · Tasarım sistemi

> Bu dosya Kalidna Otel Bozcaada için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Bozcaada / Alaybey, Kumkuyu Mevkii
- **Sunum sayfası:** https://sunum.detaymultimedia.com/kalidna-otel-bozcaada-ornek/
- **Kaynak:** Instagram @kalidnaotelbozcaada profil logosu: ekru zemin üstünde lacivert serif 'KALİDNA OTEL' (96×96 ölçüm: #F0E0E0/#E0E0D0 zemin, #203050/#304060 yazı). Çam yeşili, kum ve deniz paylaşımlardaki bahçe ve kıyıdan.
- **Son güncelleme:** 25.11.2026

## Marka gözlemi

Kumkuyu'da bahçeli, aile işletmesi bir otel; çam gölgesinde kahve, ferah ve temiz odalar ('7 numaralı oda' paylaşımı); Google 4,8 (231). Ton: sakin, ev gibi, kafa dinleme.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `lacivert` | `#26324E` | Logo laciverti: başlık, koyu zemin |
| `ekru` | `#EFE8E2` | Logo zemini: açık zemin |
| `cam` | `#3D5A45` | Çam gölgesi: ikinci koyu |
| `kum` | `#D9C8AE` | Kum: ara zemin |
| `deniz` | `#4A7891` | Ada denizi: küçük vurgu |

**Oranlar:** %50 ekru/kum, %30 lacivert, %12 çam, %8 deniz.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `lacivert` yazı / `ekru` zemin → **10.5:1** (AA ✓) — gövde
- `lacivert` yazı / `kum` zemin → **7.8:1** (AA ✓) — gövde
- `ekru` yazı / `lacivert` zemin → **10.5:1** (AA ✓) — koyu kare
- `ekru` yazı / `cam` zemin → **6.3:1** (AA ✓) — çam karesi
- `deniz` yazı / `ekru` zemin → **3.9:1** (yalnız büyük başlık ✓) — büyük vurgu

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Bellefair** | 400 | Logodaki geniş, zarif serif |
| Gövde | **Sarabun** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Corinthia** | 400 / 700 | Kısa not: 'çamların gölgesinde' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Bellefair&family=Sarabun:wght@400;600&family=Corinthia:wght@400;700&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–160 px Bellefair, büyük harf, +8% aralık
- Gövde: 30 px Sarabun 400
- Vurgu: 90–120 px Corinthia 700, deniz mavisi

**Tipografi kuralları:**

- Başlık logodaki gibi büyük harf ve ortalı.
- Corinthia kare başına bir kez, 90 px altına inme.
- Gövde ekru zeminde lacivert.

## Logo ve imza

- Logo: lacivert 'KALİDNA OTEL' serif, ekru daire. Dosya gelene kadar Bellefair büyük harf yazı-imza + altında ince çizgi ve 'BOZCAADA'.

## Görsel dil ve kompozisyon

- Motif: logodaki gibi ekru daire içinde imza; köşede ince çam iğnesi çizgileri.
- Fotoğraf üstte, altında ekru bilgi kartı.
- Reels: bahçe kahvesi → oda → kahvaltı → iletişim.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Bozcaada garden hotel, navy and warm ecru tones, pine shade, soft morning light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --lacivert: #26324E;
  --ekru: #EFE8E2;
  --cam: #3D5A45;
  --kum: #D9C8AE;
  --deniz: #4A7891;
  --font-baslik: 'Bellefair', serif;
  --font-govde: 'Sarabun', sans-serif;
  --font-vurgu: 'Corinthia', cursive;
}
```

## Yapma

- Parlak turkuaz/neon.
- Kalabalık plaj imajı; sakin aile işletmesi kal.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
