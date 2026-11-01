# HASIL PENGUJIAN PROGRAM

## Program Rekap dan Analisis Nilai Matematika Kelas

KKM yang digunakan: 75.

| No. | Test Case | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Data normal | 80, 70, 90 | Rata-rata 80 | Jumlah siswa 3, rata-rata 80.00, nilai tertinggi 90, nilai terendah 70, siswa tuntas 2, siswa belum tuntas 1 | LULUS |
| TC02 | Nilai minimum | 0 | Nilai diterima | Nilai 0 diterima, siswa belum tuntas | LULUS |
| TC03 | Nilai maksimum | 100 | Nilai diterima | Nilai 100 diterima, siswa tuntas | LULUS |
| TC04 | Nilai tidak valid | 105 | Nilai ditolak | Nilai 105 ditolak dan tidak masuk analisis | LULUS |
| TC05 | File tidak ditemukan | File data tidak tersedia | Program menampilkan pesan kesalahan | Muncul pesan "File data tidak ditemukan." | LULUS |
| TC06 | Semua siswa tuntas | 80, 85, 90 | Semua siswa tuntas | Jumlah siswa 3, rata-rata 85.00, nilai tertinggi 90, nilai terendah 80, siswa tuntas 3, siswa belum tuntas 0 | LULUS |

## Catatan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data siswa, memvalidasi nilai, menghitung statistik, menentukan status ketuntasan siswa, dan menangani kondisi kesalahan.

### Hasil Pengujian

- **TC01:** Program berhasil mengolah data normal dan menghitung rata-rata nilai dengan benar.
- **TC02:** Program berhasil menerima nilai minimum, yaitu 0.
- **TC03:** Program berhasil menerima nilai maksimum, yaitu 100.
- **TC04:** Program berhasil menolak nilai di luar rentang 0–100.
- **TC05:** Program menampilkan pesan kesalahan ketika file data tidak ditemukan.
- **TC06:** Program berhasil menentukan bahwa seluruh siswa telah mencapai KKM.

### Keterangan Status

- **LULUS:** Hasil aktual sesuai dengan hasil yang diharapkan.
- **GAGAL:** Hasil aktual tidak sesuai dengan hasil yang diharapkan.

Berdasarkan hasil pengujian, seluruh test case dinyatakan LULUS.