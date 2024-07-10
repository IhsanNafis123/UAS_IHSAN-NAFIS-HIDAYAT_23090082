data = [
    ["Nama", "Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    ["Algoritma dan Struktur Data 2", 90, 50, 65],
    ["Matematika Numerik", 80, 60, 70]
]

def rata_rata_matakuliah(data):
    rata_rata = {}
    for i in range(1, len(data)):
        matakuliah = data[i][0]
        nilai = data[i][1:]
        rata_rata[matakuliah] = sum(nilai) / len(nilai)
    return rata_rata


def rata_rata_mahasiswa(data):
    rata_rata = {}
    for m in range(1, len(data[0])):
        nama_mahasiswa = data[0][m]
        nilai_mahasiswa = [data[i][m] for i in range(1, len(data))]
        rata_rata[nama_mahasiswa] = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
    return rata_rata


rata_rata_matkul = rata_rata_matakuliah(data)
print("==============================================")
print("1. Rata-rata nilai untuk setiap mata kuliah:")
print("==============================================")
for matakuliah, rata2 in rata_rata_matkul.items():
    print(f"{matakuliah}: {rata2}")


rata_rata_mhs = rata_rata_mahasiswa(data)
print("\n==============================================")
print("2. Rata-rata nilai untuk setiap mahasiswa:")
print("==============================================")
for mahasiswa, rata2 in rata_rata_mhs.items():
    print(f"{mahasiswa}: {rata2}")