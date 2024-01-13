class Mahasiswa:
    def __init__(self, nama, nilai_indonesia, nilai_inggris):
        self.nama = nama
        self.nilai_indonesia = nilai_indonesia
        self.nilai_inggris = nilai_inggris

def input_data():
    nama = input("Masukkan nama mahasiswa: ")
    nilai_indonesia = int(input("Masukkan nilai bahasa Indonesia: "))
    nilai_inggris = int(input("Masukkan nilai bahasa Inggris: "))
    mahasiswa = Mahasiswa(nama, nilai_indonesia, nilai_inggris)
    return mahasiswa

def hapus_data(mahasiswa_list, nama):
    mahasiswa_list = [mahasiswa for mahasiswa in mahasiswa_list if mahasiswa.nama != nama]
    return mahasiswa_list

def hitung_nilai_rata(mahasiswa_list):
    total_nilai_indonesia = 0
    total_nilai_inggris = 0

    for mahasiswa in mahasiswa_list:
        total_nilai_indonesia += mahasiswa.nilai_indonesia
        total_nilai_inggris += mahasiswa.nilai_inggris

    rata_nilai_indonesia = total_nilai_indonesia / len(mahasiswa_list)
    rata_nilai_inggris = total_nilai_inggris / len(mahasiswa_list)

    return rata_nilai_indonesia, rata_nilai_inggris

mahasiswa_list = []

while True:
    print("Menu:")
    print("1. Input Data")
    print("2. Hapus Data")
    print("3. Hitung Nilai Rata-Rata")
    print("4. Keluar")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        mahasiswa = input_data()
        mahasiswa_list.append(mahasiswa)
    elif pilihan == 2:
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        mahasiswa_list = hapus_data(mahasiswa_list, nama)
    elif pilihan == 3:
        rata_nilai_indonesia, rata_nilai_inggris = hitung_nilai_rata(mahasiswa_list)
        print("Nilai rata-rata bahasa Indonesia:", rata_nilai_indonesia)
        print("Nilai rata-rata bahasa Inggris:", rata_nilai_inggris)
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid")