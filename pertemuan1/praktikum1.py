# =====================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1: Membaca Seluruh Isi File Data
# =====================================================================

# Mengambil data dan menyimpan semua data dalam satu variable
print("==== Membuka file dalam satu string ====")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()

print(isi_file)
print(f"Tipe Data : {type(isi_file)}")

# Membuka file per baris
print("==== Membuka file per baris ====")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip() # Menghilangkan karakter baris baru
        print(f"Baris ke-{jumlah_baris}")
        print(f"Isinya: {baris}") 


        
# =====================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 2: Parsing Data
# =====================================================================

# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghilankan karakter baris baru
        nim, nama, nilai = baris.split(",") # Pecah menjadi data satuan dan simpan ke variable
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}") # Menampilkan satuan data dalam satu kolom



# =====================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca Data dan Menyimpannya ke Struktur Data List
# =====================================================================

data_list = list() # Inisialisasi list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghilankan karakter baris baru
        nim, nama, nilai = baris.split(",") # Pecah menjadi data satuan dan simpan ke variable
        data_list.append([nim, nama, int(nilai)]) # Menyimpan data ke list

print("==== Menampilkan List ====")
print(data_list)
print(f"Contoh record ke-1 {data_list[0]}")
print(f"Contoh record ke-2 {data_list[1]}")



# =====================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca Data dan Menyimpannya ke Struktur Data Dictionary
# =====================================================================

data_dict = dict() # Inisialisasi dictionary

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghilankan karakter baris baru
        nim, nama, nilai = baris.split(",") # Pecah menjadi data satuan dan simpan ke variable
        # Simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }

print("==== Menampilkan Data Dictionary ====")
print(data_dict)