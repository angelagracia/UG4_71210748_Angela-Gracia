import json
with open("karyawan.json","r" as datafile:
data = json.load(datafile)

hasilnya = dict()

karyawan = input(int("Masukkan jumlah karyawan baru : "))
for i in range(karyawan):
    nama = input("Masukkan nama : ")
    alamat = input("Masukkan alamat : ")
    kolega = []
    kolega1 = input(int("Masukkan nama kolega-1: "))
        for j in range (kolega):
            kolega2 = input(int("Masukkan nama kolega-2: ", str(j+1),":"))
            kolega2.append(kolega2)
        print("=== Data berhasil ditambahkan ===")
        print()

        hasilnya(nama) = [{"Alamat" : Alamat},{"Kolega" : Kolega}]
with open("karyawan.json","w" as datafile:
          
          
          

