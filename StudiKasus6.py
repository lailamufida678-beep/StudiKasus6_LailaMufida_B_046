import json

with open("barang.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

def tambah_data (nama, jumlah):
    data.append({
        "nama_barang" : nama,
        "jumlah" : jumlah,
    })
    simpan_file()
    return "Data ditambah"

def simpan_file():
    with open("barang.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)
        return "tersimpan barang ke barang.json"

print("===== Data Awal =====")
print (data)

while True:
    print("\n======Menu Inventaris======")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        print("===== Data Barang =====")
        print(data)
    elif pilihan == "2":
        nama_barang = input("Masukkan nama barang: ")
        jumlah = input("Masukkan jumlah: ")
        print(tambah_data(nama_barang, jumlah))
        simpan_file()
    elif pilihan == "3":
        print("Keluar dari program.")
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")