#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Latihan 4 Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Fungsi ini digunakan untuk membuat semua kemungkinan
    # kombinasi huruf A dan B sepanjang n karakter
    # hasil menyimpan susunan huruf yang sedang dibentuk

    # Base case
    # Jika panjang hasil sudah sama dengan n
    # berarti satu kombinasi sudah lengkap
    # lalu kombinasi tersebut ditampilkan dan proses pada cabang ini berhenti
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive call pertama
    # Menambahkan huruf A ke dalam hasil
    # Lalu fungsi dipanggil kembali untuk melanjutkan pembentukan huruf berikutnya
    kombinasi(n, hasil + "A")

    # Recursive call kedua
    # Menambahkan huruf B ke dalam hasil
    # Lalu fungsi dipanggil kembali untuk melanjutkan pembentukan huruf berikutnya
    kombinasi(n, hasil + "B")

# Pemanggilan fungsi dengan panjang kombinasi 2
kombinasi(2)