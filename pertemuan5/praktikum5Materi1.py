#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Contoh Rekursi 1: Faktorial
# ==========================================================

def faktorial(n):
    # Kondisi berhenti ketika nilai n sudah mencapai 0
    # Pada matematika 0 faktorial bernilai 1 sehingga fungsi langsung mengembalikan 1
    if n == 0:
        return 1
    
    # Jika n belum 0 maka fungsi akan memanggil dirinya sendiri
    # Nilai n dikalikan dengan hasil faktorial dari n dikurangi 1
    # Proses ini terus berulang sampai mencapai kondisi berhenti di atas
    return n * faktorial(n - 1)

# Memanggil fungsi faktorial dengan nilai 5
# Artinya kita menghitung 5 × 4 × 3 × 2 × 1
print(faktorial(5))  # Hasil yang ditampilkan adalah 120