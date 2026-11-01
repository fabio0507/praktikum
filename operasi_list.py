
# Latihan 1
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. tambah 'truk' di akhir
kendaraan.append('truk')
print(f"a. {kendaraan}")

# b. sisipkan 'becak' di index ke-1
kendaraan.insert(1, 'becak')
print(f"b. {kendaraan}")

# c. hapus data paling belakang
kendaraan.pop()
print(f"c. {kendaraan}")

# d. ubah 'sepeda' menjadi 'skuter'
kendaraan[kendaraan.index('sepeda')] = 'skuter'
print(f"d. {kendaraan}")

# e. jumlah total data
print(f"e. jumlah data = {len(kendaraan)}")

#Latihan 2
angka = [75, 80, 90, 75, 85, 100, 65]

# a. indeks skor 100
print(f"a. skor 100 ada di indeks ke-{angka.index(100)}")

# b. jumlah siswa dengan skor 75
print(f"b. siswa dengan skor 75 = {angka.count(75)}")

# c. urutkan dari terkecil ke terbesar
angka.sort()
print(f"c. {angka}")

# d. balikkan urutan
angka.reverse()
print(f"d. {angka}")

# #Latihan 3
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"menu gabungan = {menu_utama}")

#Latihan 4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. harga Pensil -> baris ke-1, kolom ke-1
print(data_barang[1][1])

# b. tampilkan semua data dengan perulangan
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")