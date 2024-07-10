class RestaurantQueue:
    def init(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' Telah Ditambahkan Kedalam Pesanan.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order '{order}' Telah Dihilangkan Dari Pesanan.")
            return order
        else:
            print("Pesanan Anda Kosong, Tidak Ada Pesanan Untuk Dihapus.")
            return None

    def displayqueue(self):
        if len(self.queue) > 0:
            print("Pesanan Anda Sekarang:")
            for i, order in enumerate(self.queue, 1):
                print(f"{i}. {order}")
        else:
            print("Pesanan Anda Kosong.")

def main():
    restaurantqueue = RestaurantQueue()

    while True:
        print("\nMenu:")
        print("1. Tambahkan Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Pesanan Saat Ini")
        print("4. Keluar")

        choice = input("Masukan Pilihan (1-4): ")

        if choice == '1':
            order = input("Masukan Pesanan Untuk Ditambahkan: ")
            restaurantqueue.enqueue(order)
        elif choice == '2':
            restaurantqueue.dequeue()
        elif choice == '3':
            restaurantqueue.display_queue()
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan anda salah, Tolong pilih antara 1 sampai 4.")

if __name__ == "__main":
    main()