# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Identitas Proyek

- **Nama Proyek:** Program Rekap dan Analisis Nilai Matematika Kelas

- **Nama Pengembang:** Indah Palupi Kusumaningrum

- **NIM:** 2225250212

- **Mata Kuliah:** Algoritma dan Pemrograman

- **Jenis Proyek:** Individu

- **Bahasa Pemrograman:** Python

## 2. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan aplikasi sederhana berbasis Python yang digunakan untuk membantu guru mengolah dan menganalisis nilai siswa secara otomatis.

Program ini dapat membaca data siswa dari file teks, memvalidasi nilai, menghitung statistik nilai, menentukan ketuntasan berdasarkan KKM, serta menyimpan hasil analisis ke dalam file laporan.

## 3. Tujuan Program

1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai dalam rentang 0 sampai 100.
3. Menghitung rata-rata nilai siswa.
4. Menentukan nilai tertinggi dan terendah.
5. Menghitung jumlah siswa yang tuntas dan belum tuntas.
6. Menyimpan hasil analisis dalam file laporan.

## 4. Teknologi yang Digunakan

- Python
- Visual Studio Code
- Git
- GitHub

## 5. Ketentuan Program

- Nilai siswa harus berada pada rentang 0–100.
- Kriteria Ketuntasan Minimal (KKM) adalah 75.
- Siswa dinyatakan tuntas jika nilai lebih besar atau sama dengan KKM.
- Data siswa disimpan dalam file teks.
- Laporan hasil analisis disimpan dalam folder output.

## 6. Struktur Folder

```text
Indah-Palupi-Kusumaningrum-proyek/
├── data/
│   └── contoh_data.txt
├── docs/
│   └── screenshot/
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── output.py
│   └── proses.py
├── tests/
│   └── test_case.md
├── .gitignore
├── main.py
└── README.md
```

## 7. Cara Menjalankan Program

1. Buka folder proyek menggunakan Visual Studio Code.
2. Pastikan Python sudah terpasang.
3. Buka terminal VS Code.
4. Jalankan perintah berikut:

```bash
python main.py
```

## 8. Format Data

Data siswa disimpan di dalam file `data/contoh_data.txt`.

Format setiap baris:

```text
ID_Siswa,Nama_Siswa,Nilai
```

Contoh:

```text
A001,Ayu,85
A002,Budi,70
A003,Citra,90
```

## 9. Hasil Program

Program menampilkan:
- Daftar nilai siswa.
- Status ketuntasan setiap siswa.
- Jumlah seluruh siswa.
- Rata-rata nilai.
- Nilai tertinggi dan terendah.
- Jumlah siswa tuntas dan belum tuntas.

Hasil analisis juga disimpan dalam file laporan teks.

## 10. Pengujian

Pengujian dilakukan menggunakan beberapa test case, meliputi:
- Data nilai normal.
- Nilai batas minimum 0.
- Nilai batas maksimum 100.
- Nilai tidak valid.
- File data tidak ditemukan.
- Seluruh siswa dinyatakan tuntas.

Detail test case dan hasil pengujian terdapat pada folder `tests`.

## 11. Repository GitHub

Repository proyek:

https://github.com/indahpalupi0212-blip/proyek-akhir-indah-palupi

## 12. Status Proyek

Tahap implementasi, pengujian, debugging, dan dokumentasi proyek.