# Bizim Yaka Restaurant · Tasarım sistemi

> Bu dosya Bizim Yaka Restaurant için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Et & balık restoranı · Kıyı AVM, Barbaros sahil
- **Sunum sayfası:** https://sunum.detaymultimedia.com/bizim-yaka-restaurant-ornek/
- **Kaynak:** Web sitesi bizimyakarestaurant.com logosu (23.11.2026): beyaz imza tarzı el yazısı 'Bizim Yaka' + geometrik büyük olmayan 'Restaurant'. Sitenin renkleri ölçüldü: arduvaz mavi #495A77 (yazı), zeytin yeşili #4F772D, kum altını #CEB077, köpük #F3F7F8.
- **Son güncelleme:** 23.11.2026

## Marka gözlemi

İmza logosu kişisel ve sıcak ('bizim'), site sakin deniz mavisi ve zeytin yeşili. Kıyıda gün batımı, meze çeşitliliği, ızgara ahtapot, et ve balık. Ton: rahat, deniz kenarı akşamı, cömert sofra.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `gece` | `#1F2A40` | Ana koyu zemin (beyaz logonun zemini) |
| `kiyi` | `#495A77` | Site ana rengi: başlık (açık zeminde), ikincil kart |
| `kopuk` | `#F3F7F8` | Açık zemin, koyu zeminde yazı |
| `zeytin` | `#4F772D` | Site vurgu yeşili: buton, etiket |
| `kum` | `#CEB077` | Gün batımı/kum: imza yazısı, ince çizgi (koyu zeminde) |

**Oranlar:** %45 gece/kıyı, %35 köpük, %10 kum, %10 zeytin.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `kopuk` yazı / `gece` zemin → **13.3:1** (AA ✓) — gövde
- `kum` yazı / `gece` zemin → **6.9:1** (AA ✓) — imza/vurgu
- `kiyi` yazı / `kopuk` zemin → **6.5:1** (AA ✓) — açık kartta başlık
- `gece` yazı / `kopuk` zemin → **13.3:1** (AA ✓) — açık kartta gövde
- `kopuk` yazı / `zeytin` zemin → **4.9:1** (AA ✓) — buton/etiket
- `kopuk` yazı / `kiyi` zemin → **6.5:1** (AA ✓) — kart yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Urbanist** | 700 / 500 | Logodaki geometrik 'Restaurant' yazısının karşılığı; geniş harf aralıklı başlık |
| Gövde | **Figtree** | 400 / 600 | Menü, açıklama, rezervasyon |
| İmza | **Allura** | 400 | Logodaki el yazısı 'Bizim Yaka' havası; tek kelime/kısa ifade |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Urbanist:wght@500;700&family=Figtree:wght@400;600&family=Allura&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 72–96 px Urbanist 700, +8% harf aralığı
- İmza: 120–150 px Allura, kum rengi
- Gövde: 30 px Figtree 400
- Etiket: 20 px Urbanist 700, +24%, büyük harf

**Tipografi kuralları:**

- Logodaki gibi: büyük el yazısı kelime + altında küçük geometrik satır.
- Allura kare başına bir kez.
- Başlıklar sola yaslı, ufuk çizgisi hizasında.

## Logo ve imza

- Beyaz imza logosu koyu zeminde sağ alt köşede (%22). Dosya: web sitesindeki PNG; içerikte logo yerine yazıyla 'Bizim Yaka' kullanıldıysa Allura ile.

## Görsel dil ve kompozisyon

- Motif: ince ufuk çizgisi (kum rengi yatay çizgi, karenin 2/3 hizasında), yarım güneş dairesi.
- Fotoğraflar gün batımı, deniz kenarı masa, meze yukarıdan.
- Reels: güneş batarken ufuk çizgisi soldan sağa çizilir.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Seaside restaurant on the Canakkale waterfront, slate blue sea, olive green herbs, sand-gold accents, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --gece: #1F2A40;
  --kiyi: #495A77;
  --kopuk: #F3F7F8;
  --zeytin: #4F772D;
  --kum: #CEB077;
  --font-baslik: 'Urbanist', sans-serif;
  --font-govde: 'Figtree', sans-serif;
  --font-vurgu: 'Allura', cursive;
}
```

## Yapma

- Parlak turkuaz/tropik renk kullanma.
- Logoyu yeniden çizme; yoksa yazı imza kullan.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
