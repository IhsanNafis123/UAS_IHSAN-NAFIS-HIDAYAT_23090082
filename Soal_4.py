class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
        
    def setNama(self, nama):
        self.nama = nama
        
    def setWarna(self, warna):
        self.warna = warna
        
    def setRasa(self, rasa):
        self.rasa = rasa
        
    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin
        
    def setVitamin(self, vitamin):
        self.vitamin = vitamin
        
    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")

print(mangga.information())

mangga.setNama("Mangga Indramayu")
mangga.setWarna("Kuning")
mangga.setRasa("Manis Asam")
mangga.setVitamin("Vitamin A dan C")

print(mangga.information())
