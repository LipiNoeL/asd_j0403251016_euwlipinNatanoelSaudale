# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 1: Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki lebih banyak edge dan dapat
#    memiliki cycle, sedangkan spanning tree hanya
#    mengambil edge yang diperlukan untuk menghubungkan
#    semua node tanpa cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena spanning tree harus membentuk struktur tree
#    yang sederhana dan efisien sehingga tidak boleh
#    terdapat jalur yang berputar kembali ke node awal.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya mengambil edge minimum
#    yang diperlukan untuk menghubungkan semua node.