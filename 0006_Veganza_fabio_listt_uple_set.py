#LATIHAN 1
 #a. Membuat tuple mahasiswa
mahasiswa = ("Veganza Fabio Prasetya", "2605060006", "Teknologi Informasi")

# b. Menampilkan NIM (index 1) dan Prodi (index 2)
print("NIM   :", mahasiswa[1])
print("Prodi :", mahasiswa[2])

# c. Mencoba mengubah isi tuple (akan error)
mahasiswa[2] = "Teknologi Informasi"

# d. Membuat set dari barisan angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

# LATIHAN 2
# a. Membuat dictionary
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

# b. Mengubah prodi sekaligus menambah key angkatan
data_mahasiswa.update({"prodi": "Sastra Mesin", "angkatan": 2026})

# c. Menghapus key nim, lalu tampilkan hasil akhir
del data_mahasiswa["nim"]
print(data_mahasiswa)


#LATIHAN 3
# a. Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Menampilkan setiap barang dan harganya
total = 0
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total += harga

# c. Menampilkan total belanja
print(f"Total belanja: Rp {total}")