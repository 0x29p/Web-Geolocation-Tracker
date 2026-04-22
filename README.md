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
