# Pertemuan 05 Perulangan Python

Nama: Ahadin Ilman
NIM: 2225250220
Kelas: 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Membaca input nilai suku pertama (a) dan beda (d) sebagai float.
2. Membaca input banyak suku (n) sebagai integer dan melakukan pengulangan validasi dengan while hingga n > 0.
3. Inisialisasi variabel total dengan nilai 0.
4. Melakukan perulangan for sebanyak n kali dari i = 0 hingga n - 1.
5. Menghitung nilai suku ke-i menggunakan rumus suku = a + i * d.
6. Menambahkan nilai suku ke variabel akumulator total dan mencetak suku.
7. Menampilkan jumlah keseluruhan suku setelah loop selesai.

## Hasil Pengujian
- Input: a = 2, d = 3, n = 5
  - Ekspektasi: Suku 2, 5, 8, 11, 14 | Jumlah: 40.00
  - Aktual: Suku 2, 5, 8, 11, 14 | Jumlah: 40.00
  - Status: Sesuai
- Input: a = 10, d = -2, n = 4
  - Ekspektasi: Suku 10, 8, 6, 4 | Jumlah: 28.00
  - Aktual: Suku 10, 8, 6, 4 | Jumlah: 28.00
  - Status: Sesuai
- Input: a = 1.5, d = 0.5, n = 3
  - Ekspektasi: Suku 1.5, 2.0, 2.5 | Jumlah: 6.00
  - Aktual: Suku 1.5, 2.0, 2.5 | Jumlah: 6.00
  - Status: Sesuai

## Refleksi
Kesalahan perulangan yang ditemukan adalah kelupaan melakukan *update* variabel kontrol saat menggunakan `while` loop yang mengakibatkan *infinite loop*. Cara memperbaikinya adalah memastikan variabel kondisi diperbarui di dalam badan loop.