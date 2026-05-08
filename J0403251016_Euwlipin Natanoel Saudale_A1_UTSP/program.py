# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Euwlipin Natanoel Saudale
# NIM     : J0403251016
# Kelas   : TPL A1
# ==============================================================================

import os

# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca file buku.txt lalu menyimpannya
    ke dalam Dictionary.

    Format file:
    kode_buku,judul,harga

    Return:
    Dictionary dengan kode_buku sebagai key
    dan value berupa dictionary berisi judul dan harga.
    """
    database_buku = {}

    try:
        file = open(nama_file, "r")

        for baris in file:
            baris = baris.strip()
            kode_buku, judul, harga = baris.split(",")

            database_buku[kode_buku] = {
                "judul": judul,
                "harga": int(harga)
            }

        file.close()

    except FileNotFoundError:
        print("Error: file buku.txt tidak ditemukan!")

    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    """
    Node pada Linked List.
    Setiap node menyimpan judul buku dan pointer ke node berikutnya.
    """
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class LinkedListPromosi:    
    """
    Linked List untuk menyimpan daftar buku yang sedang promosi.
    """
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """
        Menambahkan buku ke akhir linked list promosi.
        """
        node_baru = Node(judul)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

        print("Buku berhasil ditambahkan ke daftar promosi.")

    def tampilkan_promosi(self):
        """
        Menampilkan seluruh isi linked list promosi.
        """
        if self.head is None:
            print("Daftar promosi kosong.")
            return

        current = self.head
        print("\nDaftar Buku Promosi:")

        while current:
            print("-", current.judul)
            current = current.next


# 3. QUEUE - ANTREAN KASIR
class AntreanKasir:
    """
    Struktur data Queue menggunakan list Python
    dengan prinsip FIFO (First In First Out).
    """
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """
        Menambahkan pelanggan ke antrean (enqueue).
        """
        self.antrean.append(nama_pelanggan)
        print(nama_pelanggan, "masuk ke antrean.")

    def layani_pelanggan(self):
        """
        Melayani pelanggan pertama dalam antrean (dequeue).
        """
        if len(self.antrean) == 0:
            print("Tidak ada pelanggan dalam antrean.")
        else:
            pelanggan = self.antrean.pop(0)
            print("Melayani pelanggan:", pelanggan)


# 4. SORTING - LAPORAN TRANSAKSI
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga menggunakan algoritma
    Insertion Sort dari kecil ke besar.
    """
    for i in range(1, len(list_harga)):

        key = list_harga[i]
        j = i - 1

        # Geser elemen yang lebih besar dari key
        while j >= 0 and list_harga[j] > key:
            list_harga[j + 1] = list_harga[j]
            j -= 1

        list_harga[j + 1] = key

    return list_harga


# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():

    direktori_script = os.path.dirname(os.path.abspath(__file__))
    file_db = os.path.join(direktori_script, "buku.txt")
    
    data_buku = muat_data_buku(file_db)

    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()

    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi")
        print("3. Kelola Antrean Kasir")
        print("4. Lihat Laporan Penjualan Terurut")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        # ========================
        # MENU 1 - KATALOG BUKU
        # ========================
        if pilihan == '1':
            while True:
                print("\n--- KATALOG BUKU ---")
                for kode, info in data_buku.items():
                    print(kode, "-", info["judul"], "- Rp", info["harga"])

                print("\n0. Kembali")
                back = input("Pilih: ")

                if back == '0':
                    break

        # ========================
        # MENU 2 - PROMOSI
        # ========================
        elif pilihan == '2':
            while True:
                print("\n--- KELOLA PROMOSI ---")
                print("1. Tambah Buku Promosi")
                print("2. Lihat Daftar Promosi")
                print("0. Kembali")

                opsi = input("Pilih: ")

                if opsi == '1':
                    judul_baru = input("Masukkan judul buku: ")
                    list_promosi.tambah_buku_promosi(judul_baru)

                elif opsi == '2':
                    list_promosi.tampilkan_promosi()

                elif opsi == '0':
                    break

                else:
                    print("Pilihan tidak valid!")

        # ========================
        # MENU 3 - ANTREAN
        # ========================
        elif pilihan == '3':
            while True:
                print("\n--- ANTREAN KASIR ---")
                print("1. Tambah Antrean")
                print("2. Layani Pelanggan")
                print("3. Lihat Antrean")
                print("0. Kembali")

                opsi = input("Pilih: ")

                if opsi == '1':
                    nama = input("Nama Pelanggan: ")
                    antrean_toko.tambah_antrean(nama)

                elif opsi == '2':
                    antrean_toko.layani_pelanggan()

                elif opsi == '3':
                    print("Antrean saat ini:", antrean_toko.antrean)

                elif opsi == '0':
                    break

                else:
                    print("Pilihan tidak valid!")

        # ========================
        # MENU 4 - SORTING
        # ========================
        elif pilihan == '4':
            while True:
                print("\n--- LAPORAN TRANSAKSI ---")
                print("1. Lihat dan Urutkan Transaksi")
                print("0. Kembali")

                opsi = input("Pilih: ")

                if opsi == '1':
                    print("Harga Sebelum Urut:", riwayat_transaksi)
                    hasil_sort = urutkan_transaksi(riwayat_transaksi.copy())
                    print("Harga Sesudah Urut:", hasil_sort)

                elif opsi == '0':
                    break

                else:
                    print("Pilihan tidak valid!")

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()