# adjacency matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# dictionary buat adjacency list
adj_list = {}

# ubah matrix jadi adjacency list
for i in range(len(matrix)):
    adj_list[i] = []

    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

# tampilkan hasil
print("Adjacency List:\n")

for node in adj_list:
    print(node, "->", adj_list[node])