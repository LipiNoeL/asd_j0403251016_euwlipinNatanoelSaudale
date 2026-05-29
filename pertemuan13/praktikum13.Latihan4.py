# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jaringan Kabel Antar Gedung
# ==========================================================

import heapq

graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
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

mst, total = prim(graph, 'GedungA')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Prim.

# 2. Edge mana saja yang dipilih?
#    Edge yang dipilih adalah:
#    ('GedungA', 'GedungC', 2)
#    ('GedungC', 'GedungD', 1)
#    ('GedungD', 'GedungB', 3)

# 3. Berapa total biaya minimum?
#    Total biaya minimum yang dihasilkan adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST dapat menghubungkan seluruh gedung
#    dengan total biaya pemasangan kabel paling minimum
#    tanpa membentuk cycle.