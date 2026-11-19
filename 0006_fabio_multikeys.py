# untidar = {
#     "Teknik":{
#         "Informasi":{
#             "nama":"Ucup",
#             "npm":100
#         },
#         "Sipil":{
#             "nama":"siti",
#             "npm":70
#         }
#     }
# }

# print(untidar["Teknik"]["Sipil"]["nama"])
# print(untidar["Teknik"]["Sipil"]["npm"])


# import datetime

# mahasiswa1 = {
#     "nama": "Ucup Surucup", 
#     "sks_lulus": 130, 
#     "lahir": datetime.datetime(2001, 4, 10)
# }
# mahasiswa2 = {"nama": "Azan Magrib", "sks_lulus": 140, "lahir": datetime.datetime(2002, 10, 10)}
# mahasiswa3 = {"nama": "Slamet Dunia Akhirat", "sks_lulus": 100, "lahir": datetime.datetime(1977, 5, 10)}

# data_mahasiswa = {
#     "MAH001": mahasiswa1,
#     "MAH002": mahasiswa2,
#     "MAH003": mahasiswa3,
# }
# # print(data_mahasiswa["MAH003"]["nama"]) #manggil variabel
# for key, mhs in data_mahasiswa.items():
#         format_lahir = mhs["lahir"].strftime("tanggal %d bulan %m tahun %Y")
#         print(f"{key}: {mhs["nama"]} sudah lulus {mhs["sks_lulus"]} SKS dan lahir pada {format_lahir}.")




# import datetime

# mahasiswa1 = {
#     'nama': 'Ucup Surucup',
#     'nim': '19022001',
#     'sks_lulus': 130,
#     'beasiswa': False,
#     'lahir': datetime.datetime(2001, 4, 10)  # tahun, bulan, tanggal
# }

# mahasiswa2 = {
#     'nama': 'Azan Magrib',
#     'nim': '19022002',
#     'sks_lulus': 140,
#     'beasiswa': True,
#     'lahir': datetime.datetime(2002, 10, 10)
# }

# mahasiswa3 = {
#     'nama': 'Slamet Dunia Akhirat',
#     'nim': '19022003',
#     'sks_lulus': 100,
#     'beasiswa': True,
#     'lahir': datetime.datetime(1977, 5, 10)
# }

# data_mahasiswa = {
#     'MAH001': mahasiswa1,
#     'MAH002': mahasiswa2,
#     'MAH003': mahasiswa3,
# }

# print(f"{'KEY':<6} {'Nama':<6} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
# print("-" * 50)

# for mahasiswa in data_mahasiswa:
#     KEY = mahasiswa

#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM = data_mahasiswa[KEY]['nim']
#     SKS = data_mahasiswa[KEY]['sks_lulus']
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#     print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")



# import datetime

# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }

# data_mahasiswa = {}

# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-" * 20)

# mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# print(mahasiswa)

# mahasiswa['nama'] = input("Nama Mahasiswa: ")
# mahasiswa['nim'] = input("NIM Mahasiswa: ")
# mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
# TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
# BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
# mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

# print(mahasiswa)




# import datetime
# import os
# import string
# import random

# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }

# data_mahasiswa = {}

# while True:
#     # os.system("cls")  # untuk Windows
#     os.system("clear")  # untuk Linux/Mac
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print("-" * 20)

#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())

#     mahasiswa['nama'] = input("Nama Mahasiswa: ")
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")
#     mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
#     TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
#     mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

#     KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
#     data_mahasiswa.update({KEY: mahasiswa})

#     print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
#     print('-' * 60)

#     for mahasiswa in data_mahasiswa:
#         KEY = mahasiswa
#         NAMA = data_mahasiswa[KEY]['nama']
#         NIM = data_mahasiswa[KEY]['nim']
#         SKS = data_mahasiswa[KEY]['sks_lulus']
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
#         print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

#     print("\n")
#     is_done = input("Mau tambah lagi bro (y/n)? ")
#     if is_done == "n":
#         break

# print("\nAkhir dari program, terima kasih")


import datetime
import os
import string
import random

buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0,
    'terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_buku = {}

while True:
    # os.system("cls")  # untuk Windows
    os.system("clear")  # untuk Linux/Mac
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'PERPUSTAKAAN MINI':^30}")
    print("-" * 30)

    buku = dict.fromkeys(buku_template.keys())

    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit (YYYY): "))

    TAHUN_PINJAM = int(input("Tahun terakhir dipinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan terakhir dipinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal terakhir dipinjam (1-31): "))
    buku['terakhir_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)

    tersedia = input("Apakah buku tersedia (y/n)? ")
    if tersedia == "y":
        buku['status'] = "TERSEDIA"
    else:
        buku['status'] = "TIDAK TERSEDIA"

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_buku.update({KEY: buku})

    print(f"\n{'KEY':<6} | {'Judul Buku':<20} | {'Penulis':<22} | {'Terbit':<6} | {'Terakhir Pinjam':<15} | {'Status':<14}")
    print("-" * 100)

    for KEY in data_buku:
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TERBIT = data_buku[KEY]['tahun_terbit']
        PINJAM = data_buku[KEY]['terakhir_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[KEY]['status']
        print(f"{KEY:<6} | {JUDUL:<20} | {PENULIS:<22} | {TERBIT:<6} | {PINJAM:<15} | {STATUS:<14}")

    print("\n")
    lagi = input("Mau tambah buku lagi (y/n)? ")
    if lagi == "n":
        break

print("\nAkhir dari program, terima kasih")