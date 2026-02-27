#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

# ==========================================================
# Latihan 3 Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    # Fungsi ini digunakan untuk mencari nilai terbesar dalam sebuah list
    # data adalah list angka
    # index menunjukkan posisi yang sedang diperiksa
    # secara default index dimulai dari 0

    # Base case
    # Jika index sudah berada di elemen terakhir
    # berarti tidak ada lagi yang perlu dibandingkan
    # sehingga langsung mengembalikan nilai pada posisi tersebut
    if index == len(data) - 1:
        return data[index]

    # Recursive call
    # Fungsi memanggil dirinya sendiri untuk mengecek sisa data
    # dimulai dari index berikutnya
    # Hasil maksimum dari sisa data disimpan dalam variabel maks_sisa
    maks_sisa = cari_maks(data, index + 1)

    # Setelah mendapatkan nilai maksimum dari sisa data
    # bandingkan dengan nilai pada index saat ini
    # Jika nilai sekarang lebih besar maka kembalikan nilai tersebut
    if data[index] > maks_sisa:
        return data[index]
    else:
        # Jika tidak lebih besar maka kembalikan nilai maksimum
        # yang sudah ditemukan dari sisa data
        return maks_sisa

# Membuat list angka
angka = [3, 7, 2, 9, 5]

# Memanggil fungsi untuk mencari nilai maksimum
print("Nilai maksimum:", cari_maks(angka))