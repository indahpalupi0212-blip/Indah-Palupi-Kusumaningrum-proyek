
KKM = 75


def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def hitung_statistik(data_siswa):
    if not data_siswa:
        return None

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    return {
        "jumlah_siswa": len(daftar_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "nilai_minimum": min(daftar_nilai),
        "nilai_maksimum": max(daftar_nilai)
    }


def tentukan_status(nilai):
    if nilai >= KKM:
        return "Tuntas"
    return "Belum Tuntas"


def analisis_data(data_siswa):
    data_valid = []

    for siswa in data_siswa:
        if validasi_nilai(siswa["nilai"]):
            siswa["status"] = tentukan_status(siswa["nilai"])
            data_valid.append(siswa)
        else:
            print(
                f"Nilai {siswa['nama']} tidak valid: "
                f"{siswa['nilai']}"
            )

    return data_valid
