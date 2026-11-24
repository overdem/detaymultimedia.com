# Bozcaada Öykü Butik Otel · Tasarım sistemi

> Bu dosya Bozcaada Öykü Butik Otel için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Bozcaada / Alaybey, Camii Sk.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/bozcaada-oyku-butik-otel-ornek/
- **Kaynak:** Logo yok (Instagram @oykubutikotelbozcaada profil resmi geceleyin fenerlerle aydınlanan taş bina fotoğrafı). Palet bu fotoğraftan ve ada kahvaltısı paylaşımlarından türetildi: gece kırmızısı-kahve, fener amberi, taş, badana beyazı, asma yeşili — öneri.
- **Son güncelleme:** 24.11.2026

## Marka gözlemi

Bozcaada'da limana bir dakika, Arnavut kaldırımlı Camii Sokak'ta; Emel Hanım'ın kahvaltısı yorumlarda 'efsane'; Google 4,9 (320). Ton: sıcak, ev gibi, ada akşamı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `gece` | `#2E1A14` | Ada gecesi: koyu zemin, başlık |
| `fener` | `#E3A447` | Fener amberi: vurgu, rozet |
| `tas` | `#C9B49A` | Taş duvar: ara zemin |
| `badana` | `#FBF7F0` | Badana beyazı: açık zemin |
| `asma` | `#55663F` | Asma yaprağı: küçük ayrıntı (büyük boyutta) |

**Oranlar:** %45 badana/taş, %30 gece, %15 fener, %10 asma.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `gece` yazı / `badana` zemin → **15.4:1** (AA ✓) — gövde
- `gece` yazı / `tas` zemin → **8.2:1** (AA ✓) — gövde (büyük)
- `badana` yazı / `gece` zemin → **15.4:1** (AA ✓) — koyu kare
- `fener` yazı / `gece` zemin → **7.6:1** (AA ✓) — büyük başlık vurgu
- `badana` yazı / `asma` zemin → **5.9:1** (AA ✓) — asma bandı yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Vollkorn** | 600 / 800 | Sıcak, kitap gibi serif: 'Öykü' adına uygun (öneri) |
| Gövde | **Libre Franklin** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Dancing Script** | 600 | Kısa not: 'ada kahvaltısı' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Vollkorn:wght@600;800&family=Libre+Franklin:wght@400;600&family=Dancing+Script:wght@600&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 130–180 px Vollkorn 800
- Gövde: 30 px Libre Franklin 400
- Vurgu: 70–90 px Dancing Script 600, fener amberi

**Tipografi kuralları:**

- Başlık küçük harf, kitap kapağı gibi ortalı.
- Dancing Script kare başına bir kez.
- Koyu karelerde fener amberi yalnız vurgu.

## Logo ve imza

- Logo yok → yazı-imza 'Öykü' Vollkorn 800 + 'BUTİK OTEL · BOZCAADA' Libre Franklin 600 +30%. Sunumda kimlik önerisi olarak belirt.

## Görsel dil ve kompozisyon

- Motif: kitap sayfası gibi ince çerçeve + küçük fener noktası; kemerli kapı formunda fotoğraf penceresi.
- Fotoğraflar: kahvaltı, taş bina gece, oda.
- Reels: sabah kahvaltısı → ada akşamı.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Bozcaada island, warm stone and lantern amber tones with whitewashed walls, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --gece: #2E1A14;
  --fener: #E3A447;
  --tas: #C9B49A;
  --badana: #FBF7F0;
  --asma: #55663F;
  --font-baslik: 'Vollkorn', serif;
  --font-govde: 'Libre Franklin', sans-serif;
  --font-vurgu: 'Dancing Script', cursive;
}
```

## Yapma

- Soğuk mavi 'Ege kartpostalı' klişesine kayma.
- Logo uydurma; yalnız yazı-imza.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
