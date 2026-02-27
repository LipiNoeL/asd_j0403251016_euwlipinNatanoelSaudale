#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):
    # Fungsi ini digunakan untuk membentuk semua kemungkinan
    # kombinasi bilangan biner dengan panjang n
    
    # Jika panjang string sudah sama dengan n
    # artinya satu kombinasi lengkap sudah terbentuk
    # kombinasi tersebut langsung ditampilkan
    if len(hasil) == n:
        print(hasil)
        return
    
    # Tambahkan angka 0 ke bagian akhir string
    # lalu lanjutkan proses untuk membentuk digit berikutnya
    biner(n, hasil + "0")
    
    # Tambahkan angka 1 ke bagian akhir string
    # lalu lanjutkan proses untuk membentuk digit berikutnya
    biner(n, hasil + "1")

# Memanggil fungsi untuk membuat semua kombinasi
# bilangan biner sepanjang 3 digit
biner(3)