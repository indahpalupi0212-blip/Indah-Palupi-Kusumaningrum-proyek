
def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 3:
                    print(f"Format data baris {nomor_baris} tidak valid.")
                    continue

                try:
                    id_siswa = bagian[0].strip()
                    nama = bagian[1].strip()
                    nilai = float(bagian[2].strip())

                    data_siswa.append({
                        "id": id_siswa,
                        "nama": nama,
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} bukan angka.")

    except FileNotFoundError:
        print("File data tidak ditemukan.")
        return None

    return data_siswa
