# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 1: Membuat Fungsi Load Data dari File
# =====================================================================

# Variable menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = dict() # Inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # Ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") # Ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} # Masukkan dalam dictionary
    return data_dict

buka_data = baca_data(nama_file)
print(f"Jumlah data terbaca {len(buka_data)}")

# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 2: Membuat Fungsi Menampilkan Data
# =====================================================================

def tampilkan_data(data_dict):
    # Membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' :<10} | {'Nama' :<12} | {'Nilai' :>5}")
    ''' 
    Untuk tampilan yang rapi, atur lebar kolom
    {'NIM' :<10} artinya NIM rata kiri dengan lebar kolom 10 karakter
    {'Nama' :<12} artinya Nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' :>5} artinya Nilai rata kanan dengan lebar kolom 5 karakter
    '''

    print("-" * 32) # Membuat garis

    # Menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim :<10} | {nama :<12} | {nilai:>5}")

# tampilkan_data(buka_data) # Memanggil fungsi untuk menampilkan data

# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 3: Membuat Fungsi Mencari Data
# =====================================================================

# Membuat fungsi pencarian data

def cari_data(data_dict):
    # Pencarian data berdasarkan NIM sebagai Key Dictionary
    # Membuat input NIM Mahasiswa yang akan dicari

    nim_cari = input("Masukkan NIM Mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama     : {nama}")
        print(f"Nilai     : {nilai}")
    
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

# Memanggil Fungsi untuk mencari data
# cari_data(buka_data)

# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 4: Membuat Fungsi Update Data
# =====================================================================

# Membuat Fungsi update data
def ubah_data(data_dict):
    # Awali dulu dengan mencari NIM/Data Mahasiswa yang ingin diupdate

    nim = input("Masukkan NIM Mahasiswa yang ingin biubah datanya: ")

    if nim not in data_dict:
        print("NIM tidak ditemukan!")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

# ubah_data(buka_data) # Memanggil fungsi update data

# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 5: Membuat Fungsi Menyimpan Data
# =====================================================================

# Membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

# Memanggil fungsi simpan data
# simpan_data(nama_file, buka_data)
print(f"\nData berhasil disimpan ke file: {nama_file}")

# =====================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 6: Membuat Menu Interaktif
# =====================================================================

def main():
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()