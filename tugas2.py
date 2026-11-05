# Nama : Muhammad Rafli Dzaki
# Kelompok : 8 Bastion
# Kode Peserta : BSN06
# Nim  : 2603176
# Kelas: 1A

print("============PILIH DATA=============")
print("1. Menghitung Jumlah Kata Dalam Kalimat")
print("2. Menampilkan Kalimat Dalam Huruf Kapital")
print("3. Membalikkan Urutan Kata Dalam Kalimat")
print("====================================")

opsi = int(input("Masukkan Pilihan Anda (1-3): "))
data = str(input("\nMasukkan Kalimat Yang Ingin Di Anu-kan: "))

print("====================================")

match(opsi):
    case 1:
        print("Jumlah Kata Dalam Kalimat Adalah : ",len(data.split()))
    case 2:
        print("Kalimat Dalam Huruf Kapital Adalah : ",data.upper())
    case 3:
        print("Urutan Kata Dalam Kalimat Adalah : ",data[::-1])
    case _:
        print("Pilihan Tidak Tersedia")