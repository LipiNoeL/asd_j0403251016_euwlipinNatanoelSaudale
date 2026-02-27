#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    # Jika panjang string hasil sudah sama dengan panjang yang diminta,
    # artinya kombinasi PIN sudah lengkap dan siap ditampilkan
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Melakukan perulangan untuk setiap pilihan angka yang tersedia
    for angka in ["0", "1", "2"]:
        
        # Rekursi dipanggil kembali dengan menambahkan angka yang dipilih
        # ke dalam string hasil sampai panjang yang diinginkan tercapai
        buat_pin(panjang, hasil + angka)

# Memanggil fungsi untuk membuat PIN dengan panjang 3 digit
buat_pin(3)