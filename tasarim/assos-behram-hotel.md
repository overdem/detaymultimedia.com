# Assos Behram Hotel · Tasarım sistemi

> Bu dosya Assos Behram Hotel için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Ayvacık / Behramkale, Assos Antik Liman
- **Sunum sayfası:** https://sunum.detaymultimedia.com/assos-behram-hotel-ornek/
- **Kaynak:** Instagram @assosbehramhotel profil logosu: beyaz zemin üstünde bronz-taba tapınak cephesi ve 'ASSOS' (96×96 ölçüm: #C09070 baskın). Web sitesi assosbehramhotel.com düğme rengi amber #FEB249. Ege laciverti ve taş paylaşımlardaki liman fotoğraflarından.
- **Son güncelleme:** 25.11.2026

## Marka gözlemi

Assos Antik Limanı'nda, denize sıfır taş otel; Antik Yunan tanrıları temalı, yetişkinlere özel (+12) 'special class' odalar; limanda balık restoranı, Aristo hikayesi ve yürüyüş parkurları; Instagram 22K. Google 4,1 (1.079) → itibar için düzenli, sıcak içerik.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `bronz` | `#B48461` | Logo bronzu: imza, motif (yazıda yalnız büyük) |
| `ege` | `#1D3A57` | Ege laciverti: koyu zemin, başlık |
| `tas` | `#EDE4D7` | Liman taşı: açık zemin |
| `amber` | `#F2A848` | Gün batımı amberi (web sitesi düğmesi): vurgu |
| `gece` | `#18212C` | Gece: en koyu zemin |

**Oranlar:** %40 taş, %35 Ege laciverti/gece, %15 bronz, %10 amber.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `ege` yazı / `tas` zemin → **9.3:1** (AA ✓) — gövde
- `tas` yazı / `ege` zemin → **9.3:1** (AA ✓) — koyu kare
- `amber` yazı / `gece` zemin → **8.1:1** (AA ✓) — koyu karede vurgu
- `bronz` yazı / `gece` zemin → **5.0:1** (AA ✓) — imza / büyük başlık
- `gece` yazı / `amber` zemin → **8.1:1** (AA ✓) — amber rozet yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Philosopher** | 400 / 700 | Antik/felsefe göndermesi, karakterli |
| Gövde | **Alegreya Sans** | 400 / 500 | Açıklama, iletişim |
| Vurgu | **Imperial Script** | 400 | Kısa not: 'antik limanda' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Alegreya+Sans:wght@400;500&family=Imperial+Script&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–150 px Philosopher 700
- Gövde: 30 px Alegreya Sans 400
- Vurgu: 90–120 px Imperial Script, amber ya da bronz

**Tipografi kuralları:**

- Başlık ortalı; tapınak alınlığı gibi üçgen/simetrik yerleşim.
- Imperial Script kare başına bir kez.
- Bronz yazı yalnız koyu zeminde ve büyük.

## Logo ve imza

- Logo: bronz tapınak cephesi + 'ASSOS BEHRAM HOTEL'. Dosya gelene kadar CSS ile sade alınlık (üçgen + 4 sütun çizgisi) + Philosopher yazı-imza; logo çizimi kopyalanmaz.

## Görsel dil ve kompozisyon

- Motif: tapınak alınlığı üçgeni ve sütun çizgileri, bronz ince çizgi.
- Gece/akşam kareleri Ege laciverti, gündüz taş.
- Reels: liman akşamı → balık sofrası → oda → gün batımı.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Assos ancient harbor, honey stone, Aegean deep blue and sunset amber tones, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --bronz: #B48461;
  --ege: #1D3A57;
  --tas: #EDE4D7;
  --amber: #F2A848;
  --gece: #18212C;
  --font-baslik: 'Philosopher', sans-serif;
  --font-govde: 'Alegreya Sans', sans-serif;
  --font-vurgu: 'Imperial Script', cursive;
}
```

## Yapma

- Rakı/şarap kadehi öne çıkaran kare (alkol tanıtım kısıtı).
- Logo yeniden çizmek.
- Neon turuncu.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
