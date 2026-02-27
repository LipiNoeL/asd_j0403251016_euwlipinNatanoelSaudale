#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):
    # Fungsi ini menunjukkan bagaimana rekursi bekerja
    # Kita bisa melihat urutan masuk sebelum pemanggilan ulang
    # dan urutan keluar setelah proses rekursi selesai
    
    # Kondisi berhenti ketika n sudah bernilai 0
    # Saat titik ini tercapai proses tidak dilanjutkan lagi
    if n == 0:
        print("Selesai")
        return
    
    # Bagian ini dijalankan sebelum fungsi memanggil dirinya sendiri
    # Bisa dibayangkan seperti proses yang sedang ditumpuk
    print("Masuk:", n)
    
    # Fungsi memanggil dirinya sendiri dengan nilai n yang lebih kecil
    # Nilai terus berkurang sampai mencapai kondisi berhenti
    hitung(n - 1)
    
    # Bagian ini dijalankan setelah pemanggilan rekursif selesai
    # Bisa dibayangkan seperti proses yang kembali satu per satu
    print("Keluar:", n)

# Memanggil fungsi dengan nilai awal 3
# Kita bisa melihat urutan masuk dan keluar yang menunjukkan alur rekursi
hitung(3)
