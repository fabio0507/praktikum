# # Fungsinya
# def sapa_dunia():
#     print("Hello wrold")

# # manggilnya
# sapa_dunia()

# Fungsinya
# def sapa_orang(siapa = "Pak iwan", pesan = "Mie ayam"):
#     print(f"Hello {siapa}! Aku mau titip {pesan}")

# # manggilnya
# sapa_orang(pesan = "Bakso")

# def tambah(x, y):
#     hasil = x + y
#     return hasil

# akhir = tambah(3, 7)
# print(akhir)

# def luasPersegiPanjang(panjang, lebar):
#     luas = panjang * lebar
#     # print(f"luas persegi panjang{luas})
#     return luas

# p = 7
# l = 3
# luas = luasPersegiPanjang(p, l)

# luasKaliDua = luas * 2
# print(luasKaliDua)


# LATIHAN FUNGSI
# --- Fungsi-fungsi perhitungan ---

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_lingkaran(jari_jari, pi=3.14):
    return pi * jari_jari ** 2

def volume_bola(jari_jari, pi=3.14):
    return 4 / 3 * pi * jari_jari ** 3


# --- Program utama ---

while True:
    print(f"\n{'KALKULATOR BANGUN':^30}")
    print("-" * 30)
    print("1. Luas persegi panjang")
    print("2. Volume persegi panjang")
    print("3. Luas lingkaran")
    print("4. Volume bola")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        hasil = luas_persegi_panjang(p, l)
        print(f"Luas persegi panjang = {hasil:.2f}")

    elif pilihan == "2":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        hasil = volume_persegi_panjang(p, l, t)
        print(f"Volume persegi panjang = {hasil:.2f}")

    elif pilihan == "3":
        r = float(input("Jari-jari: "))
        hasil = luas_lingkaran(r)
        print(f"Luas lingkaran = {hasil:.2f}")

    elif pilihan == "4":
        r = float(input("Jari-jari: "))
        hasil = volume_bola(r)
        print(f"Volume bola = {hasil:.2f}")

    elif pilihan == "5":
        break

    else:
        print("Menu tidak tersedia, coba lagi ya!")

print("\nAkhir dari program, terima kasih")