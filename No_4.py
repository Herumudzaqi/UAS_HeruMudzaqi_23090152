class Buah:
    def __init__(self, nama, rasa, warna):
        self.nama = nama
        self.rasa = rasa
        self.warna = warna

    def setNama(self, nama):
        self.nama = nama

    def setRasa(self, rasa):
        self.rasa = rasa

    def setWarna(self, warna):
        self.warna = warna

    def information(self):
        return f"Nama: {self.nama}, Rasa: {self.rasa}, Warna: {self.warna}"

class Mangga(Buah):
    def __init__(self, nama, rasa, warna, vitamin):
        super().__init__(nama, rasa, warna)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        return f"Nama: {self.nama}, Rasa: {self.rasa}, Warna: {self.warna}, Vitamin: {self.vitamin}"

# Membuat instance objek dari kelas child (Mangga)
mangga1 = Mangga("Mangga Belum Matang", "Kecut", "Hijau", "Vitamin C")

# Memanggil atribut dan metode dari instance objek mangga1
print(mangga1.information())

mangga1.setNama("Mangga Sudah Matang")
mangga1.setRasa("Manis")
mangga1.setWarna("Orange")
mangga1.setVitamin("Vitamin A")

print(mangga1.information())
