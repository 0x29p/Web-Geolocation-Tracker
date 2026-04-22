# 📍 Simple Web Geolocation Tracker (Termux Edition)

Sebuah tool sederhana berbasis Python (Flask) dan HTML5 Geolocation API untuk mendemonstrasikan bagaimana pelacakan lokasi (*Client-Side Attack*) bekerja melalui web browser. Tool ini dirancang khusus untuk dijalankan di lingkungan Termux (Android) dengan bantuan *tunneling* Cloudflare.

⚠️ **DISCLAIMER:** *Tool ini dibuat murni untuk tujuan edukasi, pembelajaran *Open-Source Intelligence* (OSINT), dan demonstrasi kerentanan privasi. Pengembang tidak bertanggung jawab atas segala bentuk penyalahgunaan tool ini yang melanggar hukum atau merugikan pihak lain. Gunakan dengan bijak dan hanya pada target yang telah memberikan izin (White-Hat Testing).*

---

## 🛠️ Persyaratan Sistem (Prerequisites)
Sebelum menjalankan tool ini, pastikan kamu menggunakan aplikasi **Termux** di Android dan memiliki koneksi internet yang stabil.

Paket yang dibutuhkan:
- Python 3
- Flask
- Wget
- CA-Certificates (untuk SSL Cloudflare)

---

## 🚀 Cara Instalasi

1. **Buka Termux** dan perbarui sistem paket:
   ```bash
   pkg update && pkg upgrade -y

2. **Instal bahasa pemrograman dan tool pendukung:**
   ```bash
   pkg install python git wget ca-certificates -y

3. **Instal framework Flask**
   ```bash
   pip install Flask

4. **Kloning repository ini:**
   ```bash

5. **Unduh Cloudflared (Tunneling):**
   Karena kita menggunakan Android (ARM64), unduh Cloudflare versi Linux ARM64 ke dalam folder yang sama
   ```bash
   wget -O cloudflared [https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64] (https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64)
   chmod +x cloudflared


  ## Cara Penggunaan​
  Tool ini membutuhkan dua sesi (session) Termux yang berjalan bersamaan.
  ## Sesi 1: Menjalankan Server Python**
    ​Di layar Termux pertama, 
    jalankan file Python untuk menghidupkan server Flask:
    ```bash
    python app.py
    
  (Biarkan sesi ini tetap berjalan dan standby. Jangan tekan CTRL+C).

  ## Sesi 2: Mengaktifkan Cloudflare Tunnel
   Catatan: Variabel SSL_CERT_FILE
   digunakan agar Termux dapat memverifikasi sertifikat HTTPS dari Cloudflare.
  
​   Geser layar Termux dari tepi kiri ke tengah, pilih New Session untuk membuka layar baru.
   Kemudian jalankan perintah ini:
   ```bash
   SSL_CERT_FILE=$PREFIX/etc/tls/cert.pem ./cloudflared tunnel --url http://localhost:5000

