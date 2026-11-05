# Nama : Muhammad Rafli Dzaki
# Kelompok : 8 Bastion
# Kode Peserta : BSN06
# Nim  : 2603176
# Kelas: 1A

nama = nim = kelas = prodi = umur = telp = ""

while True:
    print("============PILIH DATA============")
    print("1. Nama Lengkap")
    print("2. Nim")
    print("3. Kelas")
    print("4. Program Studi")
    print("5. Umur")
    print("6. No Telepon")
    print("===================================")
    data = int(input("Masukkan Data Yang Ingin Di Input : "))
    print("===================================\n")

    # menyesuaikan data yang ingin di input
    match(data):
        case 1:
            nama = input("Masukkan Nama Lengkap Anda : ")
        case 2:
            nim = input("Masukkan Nim Anda : ")
        case 3:
            kelas = input("Masukkan Kelas Anda : ")
        case 4:
            prodi = input("Masukkan Program Studi Anda : ")
        case 5:
            umur = input("Masukkan Umur Anda : ")
        case 6:
            telp = input("Masukkan No Telepon Anda : ")
        case _:
            print("Pilihan Tidak Tersedia")

    # menampilkan biodata
    print("\n============BIODATA ANDA============")
    print("Nama Lengkap Anda Adalah : ", nama)
    print("Nim Anda Adalah : ", nim)
    print("Kelas Anda Adalah : ", kelas)
    print("Program Studi Anda Adalah : ", prodi)
    print("Umur Anda Adalah : ", umur)
    print("No Telepon Anda Adalah : ", telp)
    print("===================================\n")

    edit = input("Apakah Ingin Melanjutkan Edit (y/n) : ")

    if edit == "y":
        continue
    else:
        print("-------------Program Selesai-------------")
        break