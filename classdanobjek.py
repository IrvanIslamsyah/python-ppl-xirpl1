class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def tambah(self):
        return self.a + self.b
    def kurang(self):
        return self.a - self.b
a = int(input('Silahkan masukan angka pertama'))
b = int(input('Silahkan masukan angka kedua'))
obj = cal(a,b)

while True:
    def menu():
        x = ('1. Tambah \n2. Kurang')
        print(x)
    menu()
    pilihan = int(input('Silahkan dipilih'))
    if pilihan == 1:
        print("Hasilnya : ", obj.tambah())
        break
    elif pilihan == 2:
        print("Hasilnya : ", obj.kurang())
        break