#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Latihan 1 Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Fungsi ini digunakan untuk menghitung a pangkat n
    # a adalah bilangan yang akan dipangkatkan
    # n adalah jumlah pangkatnya

    # Base case
    # Jika n bernilai 0 maka hasilnya selalu 1
    # Ini adalah kondisi berhenti agar rekursi tidak berjalan terus menerus
    if n == 0:
        return 1

    # Recursive case
    # Jika n tidak sama dengan 0 maka fungsi akan memanggil dirinya sendiri
    # Nilai n dikurangi 1 setiap pemanggilan sampai akhirnya mencapai 0
    # Setiap pemanggilan akan mengalikan a dengan hasil dari pemanggilan berikutnya
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi
# Menghitung 2 pangkat 4 yang berarti 2 x 2 x 2 x 2
print(pangkat(2, 4))  # Output yang dihasilkan adalah 16