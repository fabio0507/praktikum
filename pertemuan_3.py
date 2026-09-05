# Nilai yang diketahui (Variabel)
panjang = 12
lebar = 5
tinggi = 8

# Pertanyaan a: Hitunglah luas, volume dan keliling dari bangunan tersebut?
luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
volume = panjang * lebar * tinggi
keliling = 4 * (panjang + lebar + tinggi)

# Menampilkan hasil perhitungan ke layar
print("--- Hasil Perhitungan (pertanyaan a) ---")
print("Luas     : ",luas)
print("Volume   :",volume)
print("Keliling :",keliling)

# Pertanyaan B: Apakah luas bangunan tersebut lebih luas dari 50?
print("--- Jawaban Pertanyaan b ---")
if luas > 50:
    print("Apakah luas lebih dari 50? Jawaban : Ya, karena luasnya adalah",luas)
else:
    print("Apakah luas lebih dari 50? Jawaban : Tidak")

# Pertanyaan C: Apakah volume bernilai 480
print("--- Jawaban pertanyaan c ---")
if volume == 480:
    print("Apakah volume bernilai 480? Jawaban : Ya, tepat bernilai 480")
else:
    print("Apakah volume bernilai 480? Jawaban : Tidak, nilainya adalah",volume)