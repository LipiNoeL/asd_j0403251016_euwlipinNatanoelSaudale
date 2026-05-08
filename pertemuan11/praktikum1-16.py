# jumlah node
n = 4

# bikin matrix 4x4 isi awalnya 0
matrix = [[0 for i in range(n)] for j in range(n)]

# daftar hubungan antar node
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]

# isi matrix berdasarkan hubungan
for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

# tampilkan matrix
print("Adjacency Matrix:\n")

for row in matrix:
    print(row)

# jelaskan isi tiap baris
print("\nPenjelasan setiap baris:")

for i in range(n):
    hubungan = []

    for j in range(n):
        if matrix[i][j] == 1:
            hubungan.append(str(j))

    print(f"Simpul {i} terhubung dengan simpul: {', '.join(hubungan)}")