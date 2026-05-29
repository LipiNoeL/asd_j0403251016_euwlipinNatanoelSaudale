# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 5: Tugas Mandiri Minimum Spanning Tree
# ==========================================================

edges = [
    (1, 'RouterC', 'RouterD'),
    (2, 'RouterA', 'RouterC'),
    (3, 'RouterA', 'RouterB'),
    (4, 'RouterB', 'RouterC'),
    (5, 'RouterB', 'RouterD')
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

print("Total bobot minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Kasus apa yang dipilih?
#    Kasus yang dipilih adalah Jaringan Komputer.

# 2. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Kruskal.

# 3. Edge mana saja yang dipilih dalam MST?
#    Edge yang dipilih dalam MST adalah:
#    ('RouterC', 'RouterD', 1)
#    ('RouterA', 'RouterC', 2)
#    ('RouterA', 'RouterB', 3)

# 4. Berapa total bobot MST?
#    Total bobot MST adalah 6.

# 5. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut dapat membentuk cycle
#    atau memiliki bobot lebih besar dibanding
#    edge lain yang sudah dipilih.