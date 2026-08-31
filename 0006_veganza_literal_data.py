# Nomor 1.Deklarasi variabel
nama = "Veganza Fabio Prasetya" #tipe data : string
umur = 17                       #tipe data : integer
berat = 68.5                    #tipe data : float/double

# Menampilkan Output
print("Nama  :",nama)          
print("Umur  :",umur,("Tahun"))
print("Berat :", berat,("Kg"))


# Nomor 2.ubah tipe data
# Data awal
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
konversi_1 = int(angka_string)
print("Hasil 1 :",konversi_1)

# 2. Konversi angka_float menjadi integer
konversi_2 = int(angka_float)
print("Hasil 2 :",konversi_2)

# 3. Konversi angka_integer menjadi float
konversi_3 = float(angka_integer)
print("Hasil 3 :",konversi_3)

# 4. Konversi angka_integer menjadi string
konversi_4 = str(angka_integer)
print("Hasil 4 :",konversi_4)

# Nomor 3. Membuat progam input data

# a. Meminta input usia (integer)
usia = int(input("Masukkan usia: "))

#b. Meminta input tinggi badan (float)
tinggi_badan = float(input("Masukkan tinggi badan: "))

#c. Meminta input nama (string)
nama = input("Masukkan nama: ")

# Menampilkan hasil
print ("Usia:",usia)
print("Tinggi badan:",tinggi_badan)
print("Nama:",nama)