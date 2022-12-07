#Latihan Atribut

#Class Siswa 
class siswa:
    nama = None
    mantan = None

    def perkenalan(self):
        print(f'Perkenalkan saya {self.nama} dan nama mantan saya adalah {self.mantan}')

dhea = siswa()
dhea.nama = "Dhea Aisya Andhini"
dhea.mantan = "Firgi"

dhea.perkenalan()