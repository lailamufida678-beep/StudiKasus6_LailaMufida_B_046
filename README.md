# StudiKasus6_LailaMufida_B_046

Nama: Laila Mufida
NIM: 2609116046
Kelas: B 2026

Berikut merupakan program python untuk menambah dan melihat ketersediaan stok barang di sebuah toko kelontong:
<img width="866" height="539" alt="Screenshot 2026-10-08 210219" src="https://github.com/user-attachments/assets/55d78367-c39a-44a8-bcac-7a0946416549" />
<img width="959" height="539" alt="Screenshot 2026-10-08 210234" src="https://github.com/user-attachments/assets/097f0aef-cc45-4274-9591-f5bcbc19b48a" />

Penjelasan singkat mnegenai kode-kode yang digunakan dalam program diatas:
1. import json: memanggil modul untuk membaca dan menulis file JSON.
2. with open("barang.json", "r", ...) dan json.load(f): membuka barang.json untuk dibaca, lalu mengubah isinya jadi list Python yang disimpan di variabel data. Dengan begitu, data lama langsung terbawa saat program dijalankan.
3. def tambah_data(nama, jumlah): menambahkan satu barang (dictionary berisi nama_barang dan jumlah) ke list data dengan append. Setelah itu memanggil simpan_file() supaya barang baru langsung masuk ke file.
4. def simpan_file(): membuka barang.json dengan mode "w" (tulis), lalu json.dump(data, f, indent = 4) menulis seluruh isi data ke file dengan format rapi (indentasi 4 spasi). Karena itu data tidak hilang saat program ditutup.

Berikut adalah hasil keluaran (output) yang dihasilkan dari program diatas: 
<img width="747" height="527" alt="Screenshot 2026-10-08 210337" src="https://github.com/user-attachments/assets/aefb69bf-6987-40bf-9861-567a685abe03" />

Berikut merupakan bukti jika file.py ketambah di file.json:
<img width="776" height="539" alt="Screenshot 2026-10-08 210359" src="https://github.com/user-attachments/assets/0fb47020-2cbb-4258-aacf-82ec31d38670" />

Berikut merupakan bukti bahwa data baru tetap tersimpan setelah program dijalankan kembali:
<img width="827" height="539" alt="Screenshot 2026-10-08 211147" src="https://github.com/user-attachments/assets/313aa06f-969b-4844-90f8-f9f64fb6c49a" />




