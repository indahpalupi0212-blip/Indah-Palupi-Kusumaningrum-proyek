
from pathlib import Path

from src.input_data import baca_data
from src.proses import analisis_data, hitung_statistik
from src.output import tampilkan_hasil, simpan_laporan


FOLDER_PROYEK = Path(__file__).resolve().parent
FILE_DATA = FOLDER_PROYEK / "data" / "contoh_data.txt"
FILE_LAPORAN = FOLDER_PROYEK / "output" / "laporan_nilai.txt"


def main():
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("==========================================")

    data_siswa = baca_data(FILE_DATA)

    if data_siswa is None:
        return

    data_valid = analisis_data(data_siswa)

    if not data_valid:
        print("Tidak ada data siswa yang valid.")
        return

    statistik = hitung_statistik(data_valid)

    tampilkan_hasil(data_valid, statistik)

    simpan_laporan(data_valid, statistik, FILE_LAPORAN)


if __name__ == "__main__":
    main()
