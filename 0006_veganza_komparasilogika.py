# Mengkategorikan usia menggunakan if-elif-else

# Versi pakai elif
usia = int(input("Masukkan usia :"))

if usia <= 12:
    print("Anak anak")
elif usia <= 17:
    print("Remaja")
elif usia <= 59:
    print("Dewasa")
else:
    print("Lansia")

# Versi tanpa pakai elif
usia = int(input("Masukkan usia :"))

if usia <= 12:
    print("anak anak")
else:
    if usia <= 17:
        print("Remaja")
    else:
        if usia <= 59:
            print("Dewasa")
        else:
            print("Lansia")
        
            
