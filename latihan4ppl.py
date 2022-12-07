class kal():
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def tambah(self):
        return self.a + self.b

a = int(input("Masukan angka pertama : "))
b = int(input("Masukan angka kedua: "))
obj = kal(a,b)
while True:
    ask = ('1. Pertambahan')
    print(ask)

    menu()
    pilihan = int(input('Silahkan pilih : '))
    if pilihan == 1:
        print('Hasilnya adalah', obj.tambah())
        break
