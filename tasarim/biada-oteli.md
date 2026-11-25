# Biada Oteli · Tasarım sistemi

> Bu dosya Biada Oteli için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Bozcaada / Rum Mahallesi, Mehtepaltı Sk.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/biada-oteli-ornek/
- **Kaynak:** Instagram @biadaotelleri profil logosu: beyaz zemin üstünde gri el yazısı 'biAda' (96×96 ölçüm: #FFFFFF baskın, #808080 / #809090 yazı). Yazı için gri koyulaştırıldı. Panjur yeşili, sıva, kiremit ve fener amberi Instagram'daki bina fotoğraflarından.
- **Son güncelleme:** 25.11.2026

## Marka gözlemi

Rum Mahallesi'nin meydanında restore edilmiş taş konak: koyu yeşil panjurlar, dış merdiven, akşam fenerleri; BiAda Grande, Medio, Lounge ve Kitchen; Google 4,9 (209), Instagram 7,3K. Ton: zarif, sakin, tarihî.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `grafit` | `#45494B` | Logo grisi (koyulaştırılmış): başlık, gövde |
| `siva` | `#E8E1D6` | Sıva: açık zemin |
| `panjur` | `#25332C` | Panjur yeşili: koyu zemin |
| `kiremit` | `#A9573A` | Kiremit: küçük vurgu |
| `fener` | `#E6A65B` | Gece feneri: koyu zeminde vurgu |
| `beyaz` | `#FFFFFF` | Logo zemini |

**Oranlar:** %45 sıva/beyaz, %30 panjur yeşili, %15 grafit, %10 kiremit/fener.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `grafit` yazı / `siva` zemin → **7.0:1** (AA ✓) — gövde
- `grafit` yazı / `beyaz` zemin → **9.1:1** (AA ✓) — gövde
- `siva` yazı / `panjur` zemin → **10.2:1** (AA ✓) — koyu kare
- `fener` yazı / `panjur` zemin → **6.3:1** (AA ✓) — koyu karede vurgu
- `kiremit` yazı / `siva` zemin → **3.9:1** (yalnız büyük başlık ✓) — büyük vurgu

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Forum** | 400 | Klasik, ince serif: konak havası |
| Gövde | **Kumbh Sans** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Meow Script** | 400 | Logodaki el yazısına yakın: 'biAda' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Forum&family=Kumbh+Sans:wght@400;600&family=Meow+Script&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–150 px Forum
- Gövde: 29 px Kumbh Sans 400
- Vurgu / imza: 110–160 px Meow Script

**Tipografi kuralları:**

- Forum büyük harfle değil, cümle düzeninde.
- Meow Script imza ve tek vurgu için.
- Koyu karede fener amberi yalnız tek kelime.

## Logo ve imza

- Logo el yazısı 'biAda' (gri, beyaz zemin). Dosya gelene kadar Meow Script ile yazı-imza: 'biAda' grafit, altına 'BOZCAADA' Kumbh Sans 600 +30% aralık.

## Görsel dil ve kompozisyon

- Motif: panjur çıtası gibi ince dikey çizgi çifti + fotoğraflarda pencere oranında dikey çerçeve.
- Gece kareleri panjur yeşili, gündüz kareleri sıva.
- Reels: konak cephesi → akşam masası → oda → iletişim.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Bozcaada historic Greek quarter, greige plaster, dark green shutters, terracotta roof, warm lantern light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --grafit: #45494B;
  --siva: #E8E1D6;
  --panjur: #25332C;
  --kiremit: #A9573A;
  --fener: #E6A65B;
  --beyaz: #FFFFFF;
  --font-baslik: 'Forum', serif;
  --font-govde: 'Kumbh Sans', sans-serif;
  --font-vurgu: 'Meow Script', cursive;
}
```

## Yapma

- Mavi-beyaz Ege klişesi.
- İçki şişesi/bar rafı öne çıkaran kare (alkol tanıtım kısıtı).
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
