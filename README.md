# 📍 Simple Web Geolocation Tracker (Termux Edition)

Sebuah proyek berbasis Python (Flask) dan HTML/JS untuk mendemonstrasikan pelacakan lokasi (*Client-Side Attack*) melalui *browser*. Proyek ini dioptimalkan khusus untuk lingkungan **Termux (Android)** dengan memanfaatkan infrastruktur *tunneling* Cloudflare yang stabil dan tahan banting.

⚠️ **DISCLAIMER:** *Tool ini dibuat murni untuk tujuan edukasi, pembelajaran Open-Source Intelligence (OSINT), dan demonstrasi kerentanan privasi. Pengembang tidak bertanggung jawab atas segala bentuk penyalahgunaan tool ini yang melanggar hukum. Gunakan dengan bijak (White-Hat Testing).*

---

## 🛠️ Persyaratan Sistem
- **Perangkat:** Android dengan aplikasi Termux terbaru.
- **Koneksi:** Internet stabil (Data Seluler/WiFi).
- **Paket Wajib:** Python 3, Flask, Wget, CA-Certificates, PRoot.

---

## 🚀 Cara Instalasi

1. **Perbarui Termux & Instal Dependensi:**
   ```bash
   pkg update && pkg upgrade -y
   pkg install python git wget ca-certificates proot resolv-conf -y
   pip install Flask
   ```

2. **Kloning Repository:**
   ```bash
   git clone https://github.com/0x29p/Web-Geolocation-Tracker.git
   cd eb-Geolocation-Tracker
   ```

3. **Unduh & Siapkan Cloudflared:**
   ```bash
   wget -O cloudflared [https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64
   ```
   ```bash
   chmod +x cloudflared
   ```

---

## 💻 Cara Penggunaan

Proyek ini membutuhkan 2 sesi Termux yang berjalan secara bersamaan.

### Sesi 1: Menjalankan Server (Backend)
Jalankan Flask server di layar pertama:
```bash
python app.py
```
*(Biarkan sesi ini tetap berjalan dan jangan ditutup).*

### Sesi 2: Mengaktifkan Tunneling (Cloudflare)
Buka sesi Termux baru (*New Session*). Karena keterbatasan DNS di Android, jalankan perintah dalam mode **chroot** agar koneksi stabil:

1. **Masuk ke mode simulasi Linux:**
   ```bash
   termux-chroot
   ```
2. **Jalankan Tunnel:**
   ```bash
   SSL_CERT_FILE=$PREFIX/etc/tls/cert.pem ./cloudflared tunnel --url http://localhost:5000
   ```

### 🎯 Eksekusi Pelacakan
1. Cari URL publik di log Sesi 2 (contoh: `https://...trycloudflare.com`).
2. Kirim URL tersebut ke target (disarankan menggunakan URL Shortener agar lebih meyakinkan).
3. Saat target menekan **"Allow/Izinkan"** akses lokasi, koordinat GPS (Latitude/Longitude) dan link Google Maps akan muncul di log **Sesi 1** secara otomatis.

---

## 🧠 Solusi Masalah (Troubleshooting)
Jika kamu menemui error `connection refused` atau `x509 certificate`, pastikan kamu telah melakukan:
- Menjalankan `termux-chroot` sebelum memanggil `cloudflared`.
- Menggunakan variabel `SSL_CERT_FILE` untuk menunjuk lokasi sertifikat Termux.
- Mematikan VPN atau DNS Pribadi di pengaturan HP Android.

---
*Dibuat dengan ☕ dan Terminal.*
