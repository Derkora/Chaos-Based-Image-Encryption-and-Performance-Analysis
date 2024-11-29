# Chaos-Based Image Encryption and Performance Analysis

## Deskripsi Singkat
Proyek ini bertujuan untuk mengenkripsi gambar menggunakan dua algoritma berbasis chaos: Henon Map dan Rossler Attractor. Hasil enkripsi dianalisis berdasarkan kinerja waktu, distribusi kunci, dan performa algoritma. UI sederhana berbasis HTML menyediakan antarmuka untuk mengunggah gambar, mengirimkan data ke backend berbasis Flask, dan menampilkan hasil enkripsi beserta metrik kinerjanya.

## Fitur
- Dua Algoritma Berbasis Chaos:
    - Henon Map: Menggunakan peta chaos Henon untuk menghasilkan kunci pseudo-acak.
    - Rossler Attractor: Menggunakan atraktor Rossler untuk menghasilkan kunci chaos.
- Analisis Kinerja:
    - Evaluasi waktu proses enkripsi.
    - Analisis statistik kunci (nilai minimum, maksimum, rata-rata).
- Antarmuka Pengguna:
    - Upload gambar, proses dengan algoritma, dan tampilkan hasil.

## Persyaratan
1. Python: Pastikan Python 3.7+ terinstal.
2. Paket Python: Instal dependensi berikut:
```bash
pip install flask flask-cors pillow
```

## Cara Menjalankan
### Langkah 1: Jalankan Backend
1. Buka terminal dan arahkan ke direktori proyek.
2. Jalankan server Flask:
```bash
python app.py
```
Server akan berjalan di `http://127.0.0.1:5000`.

### Langkah 2: Jalankan Frontend
1. Jalankan server HTTP lokal untuk membuka file index.html:
``` bash
python -m http.server 8000
```
Akses UI di browser pada `http://127.0.0.1:8000`.

### Langkah 3: Gunakan Aplikasi
1. Pilih gambar yang ingin dienkripsi melalui UI.
2. Klik tombol Proses Gambar.
3. Hasil enkripsi dari algoritma Henon dan Rossler akan ditampilkan, beserta metrik kinerjanya.

## Hasil yang Diharapkan
- Dua gambar terenkripsi ditampilkan di UI:
    - Hasil Algoritma Henon Map.
    - Hasil Algoritma Rossler Attractor.
- Statistik kinerja algoritma (waktu proses, nilai kunci) tersedia untuk analisis lebih lanjut.

## Hasil
![hasil](/img/hasil.png)