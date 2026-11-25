# Talay Bağları Konukevi · Tasarım sistemi

> Bu dosya Talay Bağları Konukevi için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Bozcaada / Sulubahçe Bağ Yolu
- **Sunum sayfası:** https://sunum.detaymultimedia.com/talay-baglari-konukevi-ornek/
- **Kaynak:** Web sitesi talaybaglari.com logosu (mavi serif 'BOZCAADA TALAY BAĞLARI KONUK EVİ', 96×96 ölçüm: #2070A0/#1060A0 baskın) + Instagram @talaybaglarikonukevi profil logosu (krem zemin üstünde koyu kahve yazı). Bağ yeşili ve üzüm moru bağ fotoğraflarından tamamlandı.
- **Son güncelleme:** 25.11.2026

## Marka gözlemi

Talay ailesinin dört kardeşi aileye ait eski bağevini restore edip konukevine çevirmiş; yalnız 4 oda, bağların arasında deniz ve bağ manzaralı teras; Google 4,9 (60), yorumlarda Serpil Hanım'ın ilgisi ve kahvaltı. Ton: sakin, aile hikayesi, bağ ve deniz. Alkol tanıtımı yok: bağ/deneyim odaklı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `murekkep` | `#1D5A86` | Logo mavisi: başlık, koyu zemin |
| `bag` | `#4B6633` | Bağ yaprağı: ikinci koyu zemin, küçük ayrıntı |
| `uzum` | `#5A2A46` | Üzüm moru: vurgu yazısı (küçük dozda) |
| `kirec` | `#F7F4EC` | Kireç beyazı: açık zemin |
| `toprak` | `#6B5646` | Instagram logosu kahvesi: ince çizgi, etiket |

**Oranlar:** %50 kireç, %25 mürekkep mavisi, %15 bağ yeşili, %10 üzüm/toprak.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `murekkep` yazı / `kirec` zemin → **6.7:1** (AA ✓) — gövde
- `kirec` yazı / `murekkep` zemin → **6.7:1** (AA ✓) — koyu kare yazısı
- `kirec` yazı / `bag` zemin → **5.9:1** (AA ✓) — bağ karesi yazısı
- `uzum` yazı / `kirec` zemin → **10.3:1** (AA ✓) — vurgu
- `toprak` yazı / `kirec` zemin → **6.3:1** (AA ✓) — etiket

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Cardo** | 400 / 700 | Logodaki klasik serif büyük harf havası |
| Gövde | **Hind** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Ms Madi** | 400 | El yazısı not: 'bağların arasında' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Cardo:wght@400;700&family=Hind:wght@400;600&family=Ms+Madi&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 120–170 px Cardo 700
- Etiket: 20–24 px Hind 600, +30% aralık, büyük harf
- Gövde: 30 px Hind 400
- Vurgu: 80–100 px Ms Madi, üzüm moru

**Tipografi kuralları:**

- Başlık logodaki gibi ortalı ve sakin; büyük harf yalnız etiketlerde.
- Ms Madi kare başına bir kez, en az 80 px.
- Koyu karede yazı yalnız kireç beyazı.

## Logo ve imza

- Yazı-imza: 'TALAY BAĞLARI' Cardo 700 büyük harf + üstte küçük 'BOZCAADA', altta 'konuk evi' Ms Madi; mürekkep mavisi. Firmanın gerçek logo dosyası gelince o kullanılır.

## Görsel dil ve kompozisyon

- Motif: asma dalı gibi ince yatay çizgi + üç küçük üzüm tanesi (daire) imza köşesinde.
- Fotoğraflar yumuşak köşeli dikey pencerede; altta kireç beyazı bant.
- Reels: bağ → teras kahvaltısı → oda → iletişim.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Bozcaada vineyard, soft Aegean light, deep vineyard green, whitewashed stone and calm sea blue tones, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --murekkep: #1D5A86;
  --bag: #4B6633;
  --uzum: #5A2A46;
  --kirec: #F7F4EC;
  --toprak: #6B5646;
  --font-baslik: 'Cardo', serif;
  --font-govde: 'Hind', sans-serif;
  --font-vurgu: 'Ms Madi', cursive;
}
```

## Yapma

- Şarap kadehi, şişe ya da içki öne çıkaran kare kullanma (alkol tanıtım kısıtı).
- Logo uydurma; yalnız yazı-imza.
- Neon/turkuaz kartpostal mavisi.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
