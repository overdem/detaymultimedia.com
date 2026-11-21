# Şahinler Simit Evi · Tasarım sistemi

> Bu dosya Şahinler Simit Evi için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Fırın / simit · Barbaros
- **Sunum sayfası:** https://sunum.detaymultimedia.com/sahinler-simit-evi-ornek/
- **Kaynak:** Instagram @simitevisahinler profil logosu (21.11.2026): krem yuvarlak rozet, kahverengi el yazısı 'Şahinler', üstte kavisli 'ÇANAKKALE', altta 'SİMİT EVİ', ince çizgi çerçeve; öne çıkanlarda aynı rozet içinde çizim ikonlar.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Krem + tek kahverengi, damga/rozet kimliği, vintage fırın havası. Öne çıkan ikonları tutarlı çizilmiş. Ton: sıcak, sabah, mahalle fırını; nostaljik ama temiz.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `hamur` | `#F3EEDB` | Ana zemin (logo zemini) |
| `kabuk` | `#6E4632` | Logo rengi: başlık, çizgiler, ikonlar |
| `susam` | `#C99A5B` | Vurgu: susam/kızarık ton, ayraçlar |
| `pekmez` | `#3B2418` | Koyu zemin, gövde yazısı |
| `cay` | `#B5402A` | Çok sınırlı: çay bardağı kırmızısı, kampanya noktası |

**Oranlar:** %60 hamur, %25 kabuk/pekmez, %10 susam, %5 cay.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `kabuk` yazı / `hamur` zemin → **7.0:1** (AA ✓) — başlık
- `pekmez` yazı / `hamur` zemin → **12.4:1** (AA ✓) — gövde
- `hamur` yazı / `pekmez` zemin → **12.4:1** (AA ✓) — koyu kare yazısı
- `hamur` yazı / `kabuk` zemin → **7.0:1** (AA ✓) — rozet içi
- `hamur` yazı / `cay` zemin → **4.8:1** (AA ✓) — kampanya noktası

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Sedan** | 400 | Ürün adları, kapak; klasik fırın serifi |
| Gövde | **Onest** | 400 / 600 | Açıklama, saat, adres |
| El yazısı | **Sriracha** | 400 | Logodaki 'Şahinler' el yazısına yakın; tek kelime vurgu ('sıcacık', 'taze') |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Sedan&family=Onest:wght@400;600&family=Sriracha&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 100–120 px Sedan
- El yazısı: 72–96 px Sriracha, −3° eğik
- Gövde: 30 px Onest 400
- Rozet yazısı: 22 px Onest 600, büyük harf, +14%
- Saat/fiyat: 56 px Sedan

**Tipografi kuralları:**

- Her karede bir rozet/damga öğesi (daire çerçeve, kavisli yazı) bulunur.
- Sriracha yalnız tek kelime; uzun cümle yok.
- Saatler '06:30'dan itibaren' gibi Sedan ile büyük.

## Logo ve imza

- Krem rozet logo karelerde sağ üstte, genişliğin %16'sı; koyu karede krem üstüne kabuk çizgili versiyon.
- Öne çıkan ikonların çizim dili (ince kahverengi çizgi) karusel ikonlarında da kullanılır.

## Görsel dil ve kompozisyon

- Motif: kavisli yazılı daire rozet, ince çift çizgi çerçeve, susam noktacıkları doku olarak (%8 opaklık).
- Fotoğraflar hafif sıcak, sabah ışığı; bazı karelerde fotoğraf yuvarlak rozet içinde.
- Reels: buharın yükselişi, tepsiden çıkış; geçişlerde rozet dönerek gelir.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Fresh Turkish simit with sesame on a wooden bakery tray, warm early morning light, steam, tea glass in background, cozy neighborhood bakery, cream and brown tones, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --hamur: #F3EEDB;
  --kabuk: #6E4632;
  --susam: #C99A5B;
  --pekmez: #3B2418;
  --cay: #B5402A;
  --font-baslik: 'Sedan', Georgia, serif;
  --font-govde: 'Onest', sans-serif;
  --font-vurgu: 'Sriracha', cursive;
}
```

## Yapma

- Siyah zemin veya neon/canlı renk kullanma.
- Kalın modern sans ile kapak yapma; marka vintage fırın.
- Rozeti bozacak kadar çok öğe ekleme.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
