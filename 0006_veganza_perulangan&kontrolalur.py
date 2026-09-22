print("--- Bilangan Ganjil dan Genap (1 - 50) ---")

for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} adalah bilangan GENAP")
    else:
        print(f"{i} adalah bilangan GANJIL")


print("--- Bilangan Prima antara 1 sampai 100 ---")

for angka in range(1, 101):
    if angka > 1:
        # Cek apakah angka memiliki pembagi lain selain 1 dan dirinya sendiri
        is_prima = True
        for i in range(2, angka):
            if (angka % i) == 0:
                is_prima = False
                break  # Keluar dari perulangan jika ditemukan pembagi

        # Jika tidak ada pembagi lain, maka itu bilangan prima
        if is_prima:
            print(angka, end=" ")
print()  # Membuat baris baru di akhir