# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge dengan format:
# (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan edge yang masuk ke Minimum Spanning Tree
mst = []

# Menyimpan total bobot Minimum Spanning Tree
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Memeriksa setiap edge yang sudah diurutkan
for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai node sebagai sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)