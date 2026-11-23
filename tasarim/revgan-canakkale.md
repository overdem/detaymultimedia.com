# Revgan Çanakkale · Tasarım sistemi

> Bu dosya Revgan Çanakkale için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Restoran · Anadolu Hamidiye Tabyası, Boğaz kıyısı
- **Sunum sayfası:** https://sunum.detaymultimedia.com/revgan-canakkale-ornek/
- **Kaynak:** Instagram @revgancanakkale profil logosu (23.11.2026, 96×96 ölçüm): koyu petrol yeşili zemin (en sık #005454 civarı), şeftali renginde dalgaların üstünde yarım güneş ikonu, aralıklı yüksek kontrastlı serif büyük harf 'REVGAN', altında küçük 'ÇANAKKALE'. Web sitesi revgancanakkale.com renkleri: #0B2F2E, #F6F0E7, #F0C1A6, #8A6633.
- **Son güncelleme:** 23.11.2026

## Marka gözlemi

Logo sakin ve şık: Boğaz'da batan güneş, dalga, tarihi tabya. Kahvaltıdan akşam yemeğine her gün 08:00–00:00, Pazar açık büfe kahvaltı, söz/nişan/doğum günü organizasyonu, denize sıfır bahçe. Ton: zarif, huzurlu, kutlama.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `tabya` | `#0A5250` | Logo zemini: ana koyu zemin |
| `derin` | `#0B2F2E` | Daha koyu: gölge, alt şerit |
| `seftali` | `#F0C1A6` | Logo güneşi: başlık, ikon, çizgi |
| `krem` | `#F6F0E7` | Açık zemin, koyu zeminde gövde |
| `bronz` | `#8A6633` | İnce ayrıntı, açık zeminde etiket |

**Oranlar:** %55 tabya/derin, %25 krem, %15 şeftali, %5 bronz.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `krem` yazı / `tabya` zemin → **7.9:1** (AA ✓) — gövde
- `seftali` yazı / `tabya` zemin → **5.5:1** (AA ✓) — başlık/vurgu
- `krem` yazı / `derin` zemin → **12.7:1** (AA ✓) — koyu şerit
- `tabya` yazı / `krem` zemin → **7.9:1** (AA ✓) — açık kart
- `bronz` yazı / `krem` zemin → **4.6:1** (AA ✓) — açık kartta küçük etiket
- `derin` yazı / `seftali` zemin → **8.8:1** (AA ✓) — şeftali buton

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Cinzel** | 400 / 600 büyük harf | Logodaki aralıklı serif 'REVGAN' karşılığı |
| Gövde | **Libre Bodoni** | 400 / italik | Açıklama, menü; italik vurgu |
| Etiket | **Schibsted Grotesk** | 500 | Saat, adres, küçük büyük harf etiketler |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Libre+Bodoni:ital,wght@0,400;1,400&family=Schibsted+Grotesk:wght@500&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 72–96 px Cinzel 400, +22% harf aralığı
- Gövde: 30 px Libre Bodoni 400
- İtalik vurgu: 44–56 px Libre Bodoni italik, şeftali
- Etiket: 20 px Schibsted 500, +26%, büyük harf

**Tipografi kuralları:**

- Logodaki gibi ortalı: ikon (yarım güneş + dalga) → aralıklı büyük harf başlık → küçük alt satır.
- Vurgu kelimesi Libre Bodoni italik.
- Etiketler noktalı ayraçla: KAHVALTI · AKŞAM · ORGANİZASYON.

## Logo ve imza

- Logo ikonunu (güneş+dalga) yeniden çizmek yerine basit yarım daire + üç dalga çizgisi motifi kullan; tam logo varsa koyu zeminde ortada %26.
- İmza: 0530 132 10 17 · Anadolu Hamidiye Tabyası.

## Görsel dil ve kompozisyon

- Motif: şeftali yarım güneş + üç ince dalga çizgisi, kemer/tabya kavisi çerçeve.
- Fotoğraflar sabah denizi, kahvaltı sofrası, akşam mum ışığı; petrol gölge.
- Reels: güneş yükselir/batar; yumuşak geçişler.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Elegant restaurant by the sea inside a historic stone fortification in Canakkale, deep teal and soft peach tones, cream linens, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --tabya: #0A5250;
  --derin: #0B2F2E;
  --seftali: #F0C1A6;
  --krem: #F6F0E7;
  --bronz: #8A6633;
  --font-baslik: 'Cinzel', serif;
  --font-govde: 'Libre Bodoni', Georgia, serif;
  --font-vurgu: 'Schibsted Grotesk', sans-serif;
}
```

## Yapma

- Neon, sert kırmızı, kalın grotesk başlık kullanma.
- Logoyu birebir kopyalama; motif olarak sadeleştir.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
