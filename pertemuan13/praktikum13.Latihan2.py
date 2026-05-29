# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Algoritma Kruskal
# ==========================================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:

    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Edge mana yang dipilih pertama kali?
#    Edge yang dipilih pertama kali adalah
#    ('C', 'D') dengan bobot 1.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal bertujuan
#    membentuk Minimum Spanning Tree dengan
#    total bobot sekecil mungkin.

# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut dapat membentuk
#    cycle atau tidak diperlukan lagi
#    untuk menghubungkan semua node.