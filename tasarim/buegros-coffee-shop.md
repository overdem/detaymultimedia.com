# Buegros Coffee Shop · Tasarım sistemi

> Bu dosya Buegros Coffee Shop için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahve dükkânı · Çarşı Cd.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/buegros-coffee-shop-ornek/
- **Kaynak:** Instagram @buegroscoffeeshop profil logosu (21.11.2026): beyaz zemin, siyah çok kalın yuvarlak slab 'BUEGROS', altında ince serif büyük harf 'BUENOS GRANOS DE CAFÉ' ve kalın 'COFFEE SHOP'. Kavurma atölyesi Selçuk/İzmir.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Saf siyah-beyaz, ağır slab logotip + İspanyolca alt satır: kavurmacı, çekirdek odaklı, 'third wave' ama sıcak. Renk kahve ve kraft ambalajdan gelsin. Ton: özgüvenli, zanaat, sade.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `espresso` | `#1C1C1C` | Logo siyahı: başlık, ana koyu zemin |
| `sut` | `#FFFFFF` | Ana açık zemin |
| `kraft` | `#C8A27A` | Ambalaj/kraft vurgusu: etiket, şerit |
| `cekirdek` | `#4A2C1D` | Kavrulmuş çekirdek: ikincil koyu, gövde |
| `krema` | `#EFE6DA` | İkincil açık zemin |

**Oranlar:** %45 sut/krema, %35 espresso, %15 kraft, %5 cekirdek.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `espresso` yazı / `sut` zemin → **17.0:1** (AA ✓) — başlık/gövde
- `sut` yazı / `espresso` zemin → **17.0:1** (AA ✓) — koyu kare
- `espresso` yazı / `kraft` zemin → **7.2:1** (AA ✓) — kraft etiket
- `cekirdek` yazı / `krema` zemin → **10.2:1** (AA ✓) — gövde
- `kraft` yazı / `espresso` zemin → **7.2:1** (AA ✓) — büyük vurgu

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Alfa Slab One** | 400 (tek, çok kalın) | Logodaki ağır slab'ın karşılığı; kahve adı, kapak |
| Gövde | **Rethink Sans** | 400 / 600 | Demleme notları, açıklama |
| Alt satır | **Tenor Sans** | 400 | 'BUENOS GRANOS DE CAFÉ' gibi aralıklı büyük harf satırlar, köken bilgisi |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Rethink+Sans:wght@400;600&family=Tenor+Sans&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–140 px Alfa Slab One
- Alt satır: 22–24 px Tenor Sans, büyük harf, +22%
- Gövde: 30 px Rethink 400
- Tadım notu: 26 px Rethink 600

**Tipografi kuralları:**

- Kapak logodan: kalın slab kelime + altında ince aralıklı büyük harf satır.
- Kahve kartlarında köken / işlem / tadım notu Tenor Sans etiketleri.
- İspanyolca/İngilizce kelimeler serbest ama gövde Türkçe.

## Logo ve imza

- Siyah logotip beyaz zeminde; koyu karede beyaz. Genişliğin %30'u, üst ortada.
- Kraft etiket şeklinde (yırtık kenarlı dikdörtgen) logo rozeti kullanılabilir.

## Görsel dil ve kompozisyon

- Motif: kahve paketi etiketi (kraft dikdörtgen, siyah çerçeve), çekirdek sayacı ikonları.
- Fotoğraflar yüksek kontrast, siyah-beyaz ağırlıklı ve sadece kahvede sıcak ton.
- Reels: espresso akışı yakın plan, sert kesmeler, etiket damgası 'pat' diye iner.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Specialty coffee shop, espresso extraction close-up, latte art, coffee beans and kraft paper coffee bags, high contrast black and white interior with warm coffee tones, minimalist, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --espresso: #1C1C1C;
  --sut: #FFFFFF;
  --kraft: #C8A27A;
  --cekirdek: #4A2C1D;
  --krema: #EFE6DA;
  --font-baslik: 'Alfa Slab One', Rockwell, serif;
  --font-govde: 'Rethink Sans', sans-serif;
  --font-vurgu: 'Tenor Sans', sans-serif;
}
```

## Yapma

- Mavi/pastel minimal palet kullanma (logo siyah-beyaz).
- İnce zarif serif başlık kullanma.
- Kraft dışında renk ekleme.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
