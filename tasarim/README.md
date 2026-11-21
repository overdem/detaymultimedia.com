# Firma tasarım sistemleri

Her müşteri için tek bir tasarım dosyası: logosundan ve renklerinden çıkarılmış palet + font sistemi. Karusel, post, reels ve sunum sayfası bu dosyaya göre yapılır; yeni bir iş bu dosyadan devam eder.

## Kurallar

1. **Önce dosya, sonra tasarım.** Yeni bir firma için içerik üretmeden önce `tasarim/<firma-slug>.md` oluşturulur. Dosya varsa ona uyulur; değişiklik gerekiyorsa önce dosya güncellenir.
2. **Kaynak logodur.** Palet, firmanın kendi logosundan / tabelasından / web sitesinden alınır (Instagram profil logosu, Google Haritalar tabela fotoğrafı, web sitesi). Logo yoksa mekân fotoğrafından türetilir ve dosyada "öneri" diye belirtilir.
3. **Firmalar birbirinin kopyası olmaz ama sıfırdan icat da edilmez:** her firmanın kendi 4–6 renkli paleti ve 3 fontluk sistemi (başlık / gövde / vurgu) vardır. Yerleşim ilkeleri (1080×1350, güvenli kenar, imza köşesi) ortaktır.
4. **Fontlar:** Google Fonts, Türkçe karakterleri (ğ ş ı İ ç ö ü) içerdiği kontrol edilmiş olmalı. Aşağıdaki fontlar yasak (standart / aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans/Serif, Arial/Helvetica/system-ui.
5. **Bir font çifti iki firmada kullanılmaz.** Kullanılanlar aşağıdaki tabloda.
6. **Kontrast:** gövde yazısı en az 4.5:1; 3:1–4.5:1 arası çiftler yalnız büyük başlıkta.

## Dosyalar

| Firma | Dosya | Başlık / Gövde / Vurgu | Ana renkler |
|---|---|---|---|
| Şayka Restaurant | [sayka.md](sayka.md) | Young Serif / Hanken Grotesk / Courgette | lacivert, köpük, yelken sarısı |
| Şevket Steakhouse | [sevket.md](sevket.md) | Big Shoulders Display / Schibsted Grotesk / Gelasio italik | kömür, haki altın, kemik |
| Kuzey Çiçekçilik | [kuzey-cicekcilik.md](kuzey-cicekcilik.md) | Bricolage Grotesque / Albert Sans / Yeseva One | tabela sarısı, siyah, gül kırmızısı |
| Şahinler Simit Evi | [sahinler-simit-evi.md](sahinler-simit-evi.md) | Sedan / Onest / Sriracha | hamur kremi, kabuk kahve, susam |
| Beyzade Pide & Lahmacun | [beyzade-pide-lahmacun.md](beyzade-pide-lahmacun.md) | Gloock / Golos Text / Coustard | hardal altın, tarçın, is siyahı |
| Ayhan Çiçekçilik | [ayhan-cicekcilik.md](ayhan-cicekcilik.md) | Gilda Display / Red Hat Text / Italianno | zeytin, adaçayı, kirli beyaz |
| Rokka Kahvaltı | [rokka-kahvalti.md](rokka-kahvalti.md) | Shrikhand / Epilogue / Mynerve | roka yeşili, lavanta, krem |
| Liman Paşa Müdavim | [liman-pasa-mudavim.md](liman-pasa-mudavim.md) | Marcellus / Spectral / Pinyon Script | gece siyahı, paşa altını, fildişi |
| Çanakkale Esnaf Kahvaltısı | [canakkale-esnaf-kahvaltisi.md](canakkale-esnaf-kahvaltisi.md) | Bona Nova / Literata / Courier Prime | arduvaz, kâğıt, defne |
| Buegros Coffee Shop | [buegros-coffee-shop.md](buegros-coffee-shop.md) | Alfa Slab One / Rethink Sans / Tenor Sans | espresso siyahı, beyaz, kraft |
| Esenler Çıtır Pide | [esenler-citir-pide.md](esenler-citir-pide.md) | Rokkitt / Chivo / Abril Fatface | krem, çıtır turuncu, kahve |
| Lahmacun Time Ocakbaşı | [lahmacun-time-ocakbasi.md](lahmacun-time-ocakbasi.md) | Unbounded / Readex Pro / Kalam | gece, tabure pembesi, petrol |

## Yeni firma eklemek

1. Logoyu bul (Instagram profil resmi → web sitesi → Google Haritalar tabela fotoğrafı). Renkleri ölç (profil resmini 96×96 küçültüp en sık renkler).
2. `clients.json`'a firmayı ekle: palet (token, hex, rol), oranlar, kontrol edilecek yazı/zemin çiftleri, 3 font (yukarıdaki tabloda olmayan, Türkçe destekli, yasaklı olmayan), ölçek, kurallar, logo, kompozisyon, fotoğraf prompt eki, yapma listesi.
3. `python3 tasarim/gen.py` çalıştır: `.md` dosyası üretilir, kontrast oranları hesaplanır. "KULLANMA ✗" çıkan çift varsa paleti düzelt.
4. Bu README'deki tabloya satırı ekle.
