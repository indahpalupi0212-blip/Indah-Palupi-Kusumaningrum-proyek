
from pathlib import Path


def tampilkan_hasil(data_siswa, statistik):
    print("\n===== HASIL ANALISIS NILAI SISWA =====")

    print("\nDaftar Nilai Siswa:")

    for siswa in data_siswa:
        print(
            f"{siswa['id']} - {siswa['nama']} - "
            f"{siswa['nilai']} - {siswa['status']}"
        )

    jumlah_tuntas = sum(
        1 for siswa in data_siswa
        if siswa["status"] == "Tuntas"
    )

    jumlah_belum_tuntas = len(data_siswa) - jumlah_tuntas

    print("\n===== RINGKASAN =====")
    print(f"Jumlah siswa       : {statistik['jumlah_siswa']}")
    print(f"Rata-rata nilai    : {statistik['rata_rata']:.2f}")
    print(f"Nilai tertinggi    : {statistik['nilai_maksimum']}")
    print(f"Nilai terendah     : {statistik['nilai_minimum']}")
    print(f"Siswa tuntas       : {jumlah_tuntas}")
    print(f"Siswa belum tuntas : {jumlah_belum_tuntas}")


def simpan_laporan(data_siswa, statistik, nama_file):
    jumlah_tuntas = sum(
        1 for siswa in data_siswa
        if siswa["status"] == "Tuntas"
    )

    jumlah_belum_tuntas = len(data_siswa) - jumlah_tuntas

    try:
        # Membuat folder output secara otomatis jika belum ada
        lokasi_file = Path(nama_file)
        lokasi_file.parent.mkdir(parents=True, exist_ok=True)

        # Menyimpan laporan ke file teks
        with open(lokasi_file, "w", encoding="utf-8") as file:
            file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
            file.write("=================================\n\n")

            file.write("DAFTAR NILAI SISWA\n")
            file.write("------------------\n")

            for siswa in data_siswa:
                file.write(
                    f"{siswa['id']} - {siswa['nama']} - "
                    f"{siswa['nilai']} - {siswa['status']}\n"
                )

            file.write("\nRINGKASAN HASIL\n")
            file.write("---------------\n")
            file.write(f"Jumlah siswa       : {statistik['jumlah_siswa']}\n")
            file.write(f"Rata-rata nilai    : {statistik['rata_rata']:.2f}\n")
            file.write(f"Nilai tertinggi    : {statistik['nilai_maksimum']}\n")
            file.write(f"Nilai terendah     : {statistik['nilai_minimum']}\n")
            file.write(f"Siswa tuntas       : {jumlah_tuntas}\n")
            file.write(f"Siswa belum tuntas : {jumlah_belum_tuntas}\n")

        print(f"\nLaporan berhasil disimpan di: {lokasi_file}")

    except OSError as error:
        print(f"\nGagal menyimpan laporan: {error}")
