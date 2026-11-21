# Lahmacun Time Ocakbaşı Pide · Tasarım sistemi

> Bu dosya Lahmacun Time Ocakbaşı Pide için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Ocakbaşı / pide / lahmacun · Kemalpaşa
- **Sunum sayfası:** https://sunum.detaymultimedia.com/lahmacun-time-ocakbasi-ornek/
- **Kaynak:** Logo ve Instagram hesabı bulunamadı (21.11.2026). Palet Google Haritalar mekân fotoğrafından türetildi: cam cephe, fuşya pembe tabureler, sıcak turuncu iç duvar, petrol/turkuaz detaylar, ip ampuller, gece kalabalığı.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

378 yorumlu, gece yoğun, genç ve renkli bir mekân; pembe tabureler ve sıcak ışık mekânın imzası. Adındaki 'Time' kelimesi saat/zaman oyununa açık. Ton: eğlenceli, gece, sokak lezzeti, enerjik. Kimlik sıfırdan kurulacağı için bu palet bir öneri.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `tabure` | `#E0457B` | İmza renk: pembe tabure; başlık vurgusu, rozet |
| `petrol` | `#12807F` | İkincil: şerit, buton |
| `ocak` | `#E7742B` | Ateş/ocak turuncusu: fiyat, vurgu |
| `gece` | `#1B1D33` | Ana koyu zemin |
| `ampul` | `#FFE3A3` | Açık zemin/yazı, ışık |

**Oranlar:** %50 gece, %20 ampul, %15 tabure, %10 petrol, %5 ocak.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `ampul` yazı / `gece` zemin → **13.2:1** (AA ✓) — gövde
- `tabure` yazı / `gece` zemin → **4.2:1** (yalnız büyük başlık ✓) — başlık (büyük)
- `gece` yazı / `ampul` zemin → **13.2:1** (AA ✓) — açık kart
- `gece` yazı / `ocak` zemin → **5.5:1** (AA ✓) — fiyat rozeti
- `ampul` yazı / `petrol` zemin → **3.8:1** (yalnız büyük başlık ✓) — şerit yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Unbounded** | 900 | Geniş, yuvarlak, genç başlık; 'TIME' oyunları |
| Gövde | **Readex Pro** | 400 / 600 | Menü, saat, adres |
| El yazısı | **Kalam** | 700 | Ok/not: 'gece 02'ye kadar!', 'acılı mı?' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Unbounded:wght@700;900&family=Readex+Pro:wght@400;600&family=Kalam:wght@400;700&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 100–130 px Unbounded 900
- Gövde: 30 px Readex 400
- Not: 44–52 px Kalam 700, −5°
- Saat rozeti: 64 px Unbounded 700

**Tipografi kuralları:**

- Saat/zaman oyunu: 'Lahmacun Time 18:00–02:00', saat kadranı rozeti.
- Başlıkta tek kelime pembe, geri kalanı ampul rengi.
- Kalam notları yalnız koyu zeminde, kısa.

## Logo ve imza

- Logo yok → yazı-logo önerisi: 'LAHMACUN' Unbounded 900 + 'TIME' pembe saat rozeti içinde. Sunumda 'kimlik önerisi' olarak açıkça belirt.
- İmza: saat rozeti + 0538 093 67 17.

## Görsel dil ve kompozisyon

- Motif: ip ampul noktaları (ampul rengi daireler), saat kadranı rozeti, pembe tabure silueti ikon.
- Fotoğraflar gece, sıcak ışık, kalabalık masa; koyu kenar payı.
- Reels: hızlı tempo, saat tik-tak geçişleri, ocak alevi.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Lively Turkish ocakbaşı restaurant at night, lahmacun and pide on wooden boards, grill flames, warm string lights, colorful pink stools and teal details, glass storefront, young crowd, vibrant warm night tones, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --tabure: #E0457B;
  --petrol: #12807F;
  --ocak: #E7742B;
  --gece: #1B1D33;
  --ampul: #FFE3A3;
  --font-baslik: 'Unbounded', sans-serif;
  --font-govde: 'Readex Pro', sans-serif;
  --font-vurgu: 'Kalam', cursive;
}
```

## Yapma

- Klasik/ciddi serif kullanma.
- Açık zeminli sade 'kahvaltıcı' stil yapma.
- Bu paleti müşteri onayı olmadan 'logo' gibi sunma; öneri olarak sun.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
