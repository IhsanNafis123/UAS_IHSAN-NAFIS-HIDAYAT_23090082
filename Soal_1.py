def main():
    data_mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
    
        data_mahasiswa.append({'NIM': nim, 'Nama': nama})
      
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi != 'ya':
            break

    print("\nData Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

main()