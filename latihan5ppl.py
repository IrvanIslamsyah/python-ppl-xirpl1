# membuat variabel atau box bernama buah 
# buah = ["apel", "durian", "kiwi", "alpukat", "mangga"]
# sayur = ["pakcoy", "sledri", "kangkung", "bayem", "asem"]

# tampilkan data yang ada di variabel buah
# print(buah)

# # tampilkan data berurutan dari awal hingga akhir
# for gerobak in buah:
#     print(gerobak)

# tampilkan hanya beberapa data saja
# print(buah[0], buah[2])

# cara menambah nilai didalam list
# buah.append("anggur merah")
# print(buah)

# # cara menghapus yang ada di dalam buah 
# buah.remove("kiwi")
# print(buah)

# cara memotong nilai yang ada di box buah 
# print(buah[1:4])

# operasi aritmatika tipe data list 
# dagang_hari_ini = buah + sayur
# # print(dagang_hari_ini)

# for gerobak in dagang_hari_ini:
#     print(gerobak)

# kasir = input("Mau tambah apalagi? : ")
# buah.append(kasir) 
# print(buah)

siswa = []

data_siswa = input("Masukan nama Siswa : ")
siswa.append(data_siswa)

for nama_siswa in siswa:
    print(nama_siswa)