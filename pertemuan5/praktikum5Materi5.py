#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi ini digunakan untuk membentuk semua kemungkinan bilangan biner sepanjang n
    # dengan syarat jumlah angka 1 tidak boleh lebih dari nilai batas
    
    # Jika jumlah angka 1 sudah melebihi batas yang ditentukan
    # proses dihentikan agar tidak melanjutkan percabangan yang tidak valid
    if jumlah_1 > batas:
        return
    
    # Jika panjang string hasil sudah sama dengan n
    # artinya kita sudah membentuk satu kombinasi lengkap
    # kombinasi tersebut langsung ditampilkan
    if len(hasil) == n:
        print(hasil)
        return
    
    # Menambahkan angka 0 ke posisi berikutnya
    # jumlah angka 1 tidak berubah karena yang ditambahkan adalah 0
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Menambahkan angka 1 ke posisi berikutnya
    # jumlah angka 1 bertambah satu karena kita menambahkan 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Memanggil fungsi untuk membuat bilangan biner sepanjang 4 digit
# dengan jumlah maksimal angka 1 sebanyak 2
biner_batas(4, 2)