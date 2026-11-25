# Kinzi House · Tasarım sistemi

> Bu dosya Kinzi House için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama (apart) · Çanakkale Merkez / Kemalpaşa, Dibek Sk.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/kinzi-house-ornek/
- **Kaynak:** Logo, web sitesi ve Instagram hesabı bulunamadı. Palet Google Haritalar giriş fotoğrafından (koyu ceviz doğramalar, kireç beyazı cephe, saksı yeşilleri) türetildi + Boğaz mavisi — öneri.
- **Son güncelleme:** 25.11.2026

## Marka gözlemi

Saat Kulesi'ne bir dakika, Dibek Sokak'ta; mutfaklı aile daireleri; Google 4,8 (266), trivago 9,5. Misafirler merkezi konumu, ilgili ev sahibini ve temizliği övüyor. Ton: sıcak, şehir içinde ev.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `ceviz` | `#4A2F20` | Ceviz doğrama: başlık, koyu zemin |
| `kirec` | `#F5F0E6` | Kireç cephe: açık zemin |
| `tas` | `#D6CCBD` | Arnavut kaldırımı taşı: ara zemin |
| `yaprak` | `#4F6B3A` | Saksı yeşili: küçük ayrıntı |
| `bogaz` | `#2B5A70` | Boğaz mavisi: vurgu |

**Oranlar:** %50 kireç/taş, %30 ceviz, %10 Boğaz mavisi, %10 yaprak.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `ceviz` yazı / `kirec` zemin → **10.8:1** (AA ✓) — gövde
- `ceviz` yazı / `tas` zemin → **7.7:1** (AA ✓) — gövde
- `kirec` yazı / `ceviz` zemin → **10.8:1** (AA ✓) — koyu kare
- `bogaz` yazı / `kirec` zemin → **6.6:1** (AA ✓) — vurgu
- `kirec` yazı / `bogaz` zemin → **6.6:1** (AA ✓) — Boğaz bandı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Sora** | 600 / 700 | Yalın, modern başlık |
| Gövde | **Asap** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Yellowtail** | 400 | Kısa not: 'evinizdesiniz' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Asap:wght@400;600&family=Yellowtail&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–150 px Sora 700
- Gövde: 30 px Asap 400
- Vurgu: 70–90 px Yellowtail, Boğaz mavisi

**Tipografi kuralları:**

- Başlık sola dayalı, sıkı satır.
- Yellowtail kare başına bir kez.
- Rakamlar (1 dk, 4,8) Sora 700 iri.

## Logo ve imza

- Logo yok → yazı-imza 'KINZI HOUSE' Sora 700 +12% aralık + altta 'Kemalpaşa · Çanakkale' Asap. Sunumda öneri diye belirt.

## Görsel dil ve kompozisyon

- Motif: kapı doğraması gibi ince ceviz çerçeve + köşede küçük anahtar dairesi.
- Fotoğraf + alt bilgi şeridi (kireç).
- Reels: sokak girişi → daire → kordon akşamı → iletişim.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Canakkale old town, warm walnut wood, lime-washed walls and leafy green tones, natural daylight, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --ceviz: #4A2F20;
  --kirec: #F5F0E6;
  --tas: #D6CCBD;
  --yaprak: #4F6B3A;
  --bogaz: #2B5A70;
  --font-baslik: 'Sora', sans-serif;
  --font-govde: 'Asap', sans-serif;
  --font-vurgu: 'Yellowtail', cursive;
}
```

## Yapma

- Lüks otel/havuz imajı verme; apart ve aile odaklı kal.
- Logo uydurma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
