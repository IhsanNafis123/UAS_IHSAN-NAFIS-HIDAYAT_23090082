from Soal_3 import Queue

def main():
    order_queue = Queue()

    while True:
        print("\n=== Sistem Antrian Pesanan ===")
        print("1. Tambah Pesanan")
        print("2. Proses Pesanan")
        print("3. Lihat Pesanan Berikutnya")
        print("4. Lihat Semua Pesanan")
        print("5. Hapus Pesanan dari Index Tertentu")
        print("6. Keluar")

        choice = input("Pilih operasi yang ingin dilakukan: ")

        if choice == "1":
            item = input("Masukkan pesanan baru: ")
            order_queue.enqueue(item)
            print(f"Pesanan '{item}' ditambahkan ke antrian.")

        elif choice == "2":
            processed_item = order_queue.dequeue()
            if processed_item:
                print(f"Pesanan '{processed_item}' telah diproses dan dihapus dari antrian.")
            else:
                print("Antrian kosong, tidak ada pesanan untuk diproses.")

        elif choice == "3":
            next_item = order_queue.head()
            if next_item:
                print(f"Pesanan berikutnya yang akan diproses adalah: '{next_item}'")
            else:
                print("Antrian kosong, tidak ada pesanan berikutnya.")

        elif choice == "4":
            order_queue.display()

        elif choice == "5":
            index = int(input("Masukkan index pesanan yang ingin dihapus: "))
            removed_item = order_queue.remove_at(index)
            if removed_item:
                print(f"Pesanan '{removed_item}' dihapus dari antrian.")
            else:
                print("Index tidak valid atau antrian kosong.")

        elif choice == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih operasi yang tersedia (1-6).")

if __name__ == "_main_":
    main()