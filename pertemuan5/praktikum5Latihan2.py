#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Latihan 2 Tracing Rekursi
# ==========================================================

def countdown(n):
    # Fungsi ini akan menampilkan proses masuk dan keluar
    # dari sebuah pemanggilan rekursif

    # Base case
    # Jika n sama dengan 0 maka proses berhenti
    # Program mencetak Selesai lalu kembali ke pemanggil sebelumnya
    if n == 0:
        print("Selesai")
        return

    # Bagian ini dijalankan sebelum masuk ke pemanggilan berikutnya
    # Karena itu tulisan Masuk akan tampil dari angka terbesar ke terkecil
    print("Masuk:", n)

    # Recursive call
    # Fungsi memanggil dirinya sendiri dengan nilai n dikurangi 1
    # Program akan terus masuk lebih dalam sampai n menjadi 0
    countdown(n - 1)

    # Baris ini dijalankan setelah pemanggilan rekursif selesai
    # Artinya program sedang kembali ke atas satu per satu
    # Karena kembali dari pemanggilan terakhir, maka angka yang dicetak
    # akan muncul dari yang paling kecil menuju yang paling besar
    print("Keluar:", n)

# Pemanggilan fungsi dengan nilai awal 3
countdown(3)