#fungsi garis 
def garis():
    print("----------------------------------------------")

# SELAMAT DATANG DI JPHOTEL
garis()
print("--Selamat Datang di JPHOTEL--")
print("--No-----Tipe--------Harga--")
print("--01-----Suite----1.000.000")
print("--02-----Royal------500.000")
print("--03-----BPJS-------250.000")

# Sampai Resepsionis (input data)
garis()
cust = input("Masukan nama lengkap : ")
tipe = int(input("Tipe Kamar: "))
lama_inap = int(input("Masukan lama inap : "))

# tipe kamar
if tipe == 1:
    print ('Suite')
elif tipe == 2:
    print ("Royal")
elif tipe == 3:
    print ("BPJS")

# tipe kamar
if tipe == 1:
    tipe_kamar = ("Suite")
elif tipe == 2:
    tipe_kamar = ("Royal")
elif tipe == 3:
    tipe_kamar = ("BPJS")

#Kalkulasi Harga Total
if tipe == 1:
    total_harga = 1000000*lama_inap
elif tipe == 2:
    total_harga = 500000*lama_inap
elif tipe == 3:
    total_harga = 250000*lama_inap

# Struk JPHOTEL
garis()
print("Pelanggan atas nama : ", cust)
print("Tipe Kamar yang dipilih : ", tipe_kamar)
print("Lama menginap : ", lama_inap)
garis()
print("Total Harga : ", "Rp", total_harga , ",00")

