# Mut Coffee · Tasarım sistemi

> Bu dosya Mut Coffee için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahve dükkanı · Kemalpaşa / Eski Mahkeme Sk.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/mut-coffee-ornek/
- **Kaynak:** Instagram hesabı bulunamadı (23.11.2026). Kaynak: mekândaki duvar yazısı (Google Haritalar fotoğrafı): kum rengi kabartmalı sıva duvar üzerinde koyu kahve, yüksek kontrastlı kalın serif 'MUT'. Kum, kil ve hasır tonları iç mekândan (rattan, örgü sepetler) ölçülerek türetildi.
- **Son güncelleme:** 23.11.2026

## Marka gözlemi

Kum rengi, el yapımı kabartmalı duvarlar, rattan ve örgü sepetlerle bohem, sakin bir butik kafe; 1000'i aşkın yorumla 4,7; latte art ve salep öne çıkıyor; alt kat sohbet, üst kat çalışma. Ton: sıcak, dokulu, sakin, genç.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `mut` | `#3A261B` | Duvar yazısı 'MUT': başlık, gövde |
| `kum` | `#EADBC4` | Sıva duvar: ana açık zemin |
| `kil` | `#B07E52` | Toprak vurgu: büyük başlık, çizgi, rozet |
| `krem` | `#F7F0E5` | En açık: kart |
| `hasir` | `#9C7B52` | Rattan: ince ayrıntı (büyük boyutta) |

**Oranlar:** %55 kum/krem, %25 mut, %15 kil, %5 hasır.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `mut` yazı / `kum` zemin → **10.5:1** (AA ✓) — gövde
- `mut` yazı / `krem` zemin → **12.6:1** (AA ✓) — kart gövde
- `krem` yazı / `mut` zemin → **12.6:1** (AA ✓) — koyu kart
- `kil` yazı / `krem` zemin → **3.1:1** (yalnız büyük başlık ✓) — büyük başlık vurgu
- `krem` yazı / `kil` zemin → **3.1:1** (yalnız büyük başlık ✓) — rozet yazısı (büyük)

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Bodoni Moda** | 800 | Duvardaki kalın yüksek kontrastlı serif 'MUT' karşılığı |
| Gövde | **Commissioner** | 400 / 600 | Menü, açıklama |
| El yazısı | **Sacramento** | 400 | Kısa not: latte art, sıcak salep |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,700;6..96,800&family=Commissioner:wght@400;600&family=Sacramento&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 120–170 px Bodoni Moda 800, büyük harf, +6%
- Gövde: 30 px Commissioner 400
- El yazısı: 70–90 px Sacramento, kil rengi

**Tipografi kuralları:**

- 'MUT' gibi kısa, kalın, aralıklı büyük harf başlık.
- Sacramento kare başına bir kez.
- Bol boşluk; ortalı.

## Logo ve imza

- Logo dosyası yok → yazı-imza: 'MUT' Bodoni Moda 800, mut renginde; altında küçük 'COFFEE' Commissioner +40%. Sunumda kimlik önerisi olarak belirt.

## Görsel dil ve kompozisyon

- Motif: kemer (üstü yuvarlak) fotoğraf çerçevesi, sıva dokusu (çok hafif gren), örgü sepet daireleri.
- Fotoğraflar doğal gün ışığı, kum duvar önünde fincan, rattan.
- Reels: yavaş kaydırma, latte art dökülürken.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Boho chic coffee shop with sculpted sand-colored plaster walls, rattan and woven baskets, warm beige and clay tones, soft natural light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --mut: #3A261B;
  --kum: #EADBC4;
  --kil: #B07E52;
  --krem: #F7F0E5;
  --hasir: #9C7B52;
  --font-baslik: 'Bodoni Moda', serif;
  --font-govde: 'Commissioner', sans-serif;
  --font-vurgu: 'Sacramento', cursive;
}
```

## Yapma

- Soğuk gri/siyah zemin kullanma.
- Parlak renk ve neon kullanma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
