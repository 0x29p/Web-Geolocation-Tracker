# 📍 Simple Web Geolocation Tracker (Termux Edition)

Sebuah proyek berbasis Python (Flask) dan HTML/JS untuk mendemonstrasikan pelacakan lokasi (*Client-Side Attack*) melalui *browser*. Tool ini dirancang untuk dieksekusi di Termux (Android) dengan memanfaatkan infrastruktur *tunneling* Cloudflare. Proyek ini sangat cocok sebagai referensi portofolio dalam eksplorasi keamanan siber, pemrograman Python, dan pemahaman integrasi *backend-frontend*.

⚠️ **DISCLAIMER:** *Tool ini dibuat murni untuk tujuan edukasi, pembelajaran Open-Source Intelligence (OSINT), dan demonstrasi kerentanan privasi. Pengembang tidak bertanggung jawab atas segala bentuk penyalahgunaan tool ini yang melanggar hukum. Gunakan dengan bijak (White-Hat Testing).*

---

## 🛠️ Persyaratan Sistem
- **Sistem Operasi:** Android (via Termux)
- **Koneksi:** Internet stabil untuk eksekusi tunnel
- **Paket Termux:** Python 3, Flask, Wget, CA-Certificates

---

## 🚀 Cara Instalasi

1. **Perbarui Termux & Instal Dependensi:**
   ```bash
   pkg update && pkg upgrade -y
   pkg install python git wget ca-certificates -y
   pip install Flask
   ```

2. **Kloning Repository:**
   ```bash
   git clone [https://github.com/UsernameKamu/NamaRepoKamu.git](https://github.com/UsernameKamu/NamaRepoKamu.git)
   cd NamaRepoKamu
   ```

3. **Unduh Cloudflared (Tunneling untuk ARM64):**
   ```bash
   wget -O cloudflared [https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64)
   chmod +x cloudflared
   ```

---

## 💻 Cara Penggunaan

Proyek ini membutuhkan 2 sesi Termux yang berjalan secara paralel.

### Sesi 1: Menjalankan Server (Backend)
Jalankan Flask server di layar pertama:
```bash
python app.py
```
*(Biarkan sesi ini tetap berjalan dan standby).*

### Sesi 2: Mengaktifkan Tunneling (Cloudflare)
Buka sesi Termux baru (*New Session*) dan jalankan perintah berikut untuk mengekspos *localhost* ke internet publik melalui HTTPS:
```bash
SSL_CERT_FILE=$PREFIX/etc/tls/cert.pem ./cloudflared tunnel --url http://localhost:5000
```

### 🎯 Eksekusi Pelacakan
1. Salin URL publik dari log Cloudflare pada Sesi 2 (contoh format: `https://[kata-acak].trycloudflare.com`).
2. Kirim URL tersebut ke perangkat target uji coba (URL dapat diperpendek menggunakan *URL Shortener* agar lebih rapi).
3. Saat target membuka tautan dan memberikan izin lokasi (*Allow*), koordinat GPS (Latitude/Longitude) beserta tautan Google Maps akan langsung tercetak secara *real-time* di log **Sesi 1**.

---

## 🧠 Arsitektur & Cara Kerja
- **Backend (app.py):** Server Flask beroperasi di `localhost:5000`, menangani *routing* web dan menerima pengiriman data kordinat melalui metode `POST`.
- **Frontend (HTML/JS):** Memanfaatkan trigger `window.onload` dan *HTML5 Geolocation API* untuk meminta akses GPS target secara asinkron tanpa memerlukan klik tambahan.
- **Tunneling (Cloudflare):** Mengamankan lalu lintas lokal menjadi protokol standar HTTPS. Hal ini wajib dilakukan agar *browser* modern mengizinkan eksekusi Geolocation API.

---
*Dibuat dengan ☕ dan Terminal.*
