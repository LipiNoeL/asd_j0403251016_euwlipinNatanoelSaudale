# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot jalur A -> B -> D adalah 9.

# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot jalur A -> C -> D adalah 3.

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur yang dipilih sebagai jalur terpendek adalah
#    A -> C -> D karena memiliki total bobot lebih kecil.

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge
#    yang paling sedikit?
#    Karena algoritma shortest path berfokus pada total bobot
#    terkecil, bukan jumlah edge atau jumlah langkah perjalanan.