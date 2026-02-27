#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
    # Fungsi ini digunakan untuk menjumlahkan seluruh isi list secara rekursif
    # Parameter index digunakan untuk menandai posisi elemen yang sedang diproses
    
    # Jika index sudah sama dengan panjang list
    # artinya semua elemen sudah dijumlahkan
    # fungsi mengembalikan 0 sebagai nilai akhir
    if index == len(data):
        return 0
    
    # Ambil nilai pada posisi sekarang
    # lalu tambahkan dengan hasil penjumlahan dari sisa elemen berikutnya
    # Fungsi akan terus memanggil dirinya sendiri sampai mencapai kondisi berhenti
    return data[index] + jumlah_list(data, index + 1)

# Memanggil fungsi dengan list berisi 2, 4, 6, 8
# Prosesnya adalah 2 + 4 + 6 + 8
# Hasil akhirnya adalah 20
print(jumlah_list([2, 4, 6, 8]))
