# detaymultimedia.com

Stack: Astro + Vercel Functions + Demo Panel
Durum: Vercel'e deploy hazır ✅

## ✅ Tamamlanan Özellikler

### 1. Backend API (Vercel Functions)
- Astro API Routes → Vercel Serverless Functions
- JWT authentication
- In-memory data storage (demo için yeterli)
- Auth: `/api/auth/login`, `/api/auth/register`
- Demos: `/api/demos`, `/api/demos/[id]`
- Feedback: `/api/feedback` (POST), `/api/feedback?demoId=X` (GET)

### 2. Frontend - Müşteri Paneli
- **Login**: `/musteri/login` - Email/password ile giriş
- **Register**: `/musteri/register` - Yeni hesap oluşturma
- **Dashboard**: `/musteri/dashboard` - Tüm demolar listesi
- **Project Detail**: `/musteri/project/:id` - Demo gösterim + feedback formu

### 3. Database
- 21 demo projesi (Campus Maya + 20 kategori)
- User authentication
- Feedback sistemi (rating + comment)

### 4. Images
- 21 placeholder SVG görseli (color-coded)
- `/public/placeholder-demo-1.svg` ... `placeholder-demo-21.svg`

### 5. Navbar Güncelleme
- "DEMO AL →" butonu eklendi
- `/musteri/login` adresine link
- Responsive (mobile-friendly)

## 🚀 Local Development

```bash
npm run dev
# Astro dev server: http://localhost:4321
```

API routes otomatik olarak `/api/*` endpoints'e konur.

## 🌍 Production Deployment

```bash
vercel --prod
```

Vercel otomatik olarak:
- Astro'yu build eder
- API routes'u serverless functions'a dönüştürür
- SSL/TLS ve custom domain'i kurarak deploy eder

## 🔑 Test Credentials

### Demo User:
- **Email**: `demo@detay.com`
- **Şifre**: `demo123`

### Yeni Hesap Oluştur:
- `/musteri/register` sayfasından herhangi email/şifre ile kayıt ol
- (In-memory storage, session'da kalır)

## 📝 Feedback Sistemi

- 5 yıldız rating sistemi
- Başlık + mesaj yazabilme
- Tüm feedbackler kaydediliyor (session'da)
- Demo sayfasında feedback listesi görüntüleniyor

## ⚙️ Environment Variables

### JWT_SECRET (İsteğe bağlı)
```bash
JWT_SECRET=your-secret-key-change-this
```

Vercel'de ayarlamak:
```bash
vercel env add JWT_SECRET
```

Default değer (test): `demo-secret-key-change-in-production`

## 📌 Notlar

- **Data Storage**: In-memory (session'da kalır, deploy sonrası reset olur)
- **Production için**: Supabase PostgreSQL'e migrate et
- **Özellikler**: Demo paneli, feedback, JWT auth, 21 demo projesi
