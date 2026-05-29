# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah A.

# 2. Edge mana yang dipilih pertama kali?
#    Edge yang dipilih pertama kali adalah
#    ('A', 'C') dengan bobot 2.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menentukan edge berikutnya dengan
#    memilih edge berbobot paling kecil yang
#    terhubung ke node yang sudah dikunjungi
#    dan tidak membentuk cycle.

# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim membangun MST mulai dari satu node
#    dan memperluasnya sedikit demi sedikit,
#    sedangkan Kruskal memilih edge berbobot
#    terkecil dari seluruh graph secara global.