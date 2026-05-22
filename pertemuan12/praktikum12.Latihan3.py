# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):

        for node in graph:
            for neighbor, weight in graph[node].items():

                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung dari A ke B adalah 5.

# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobot jalur A -> C -> B adalah
#    4 + (-2) = 2.

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B menghasilkan jarak
#    lebih kecil menuju B karena total bobotnya 2,
#    sedangkan jalur langsung A -> B memiliki bobot 5.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford melakukan relaksasi
#    seluruh edge secara berulang sehingga tetap
#    dapat menemukan jarak terpendek meskipun
#    terdapat bobot negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah proses memeriksa
#    apakah suatu jalur baru memiliki jarak
#    lebih kecil dibanding jarak sebelumnya,
#    lalu memperbarui nilai jaraknya.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Bellman-Ford dapat menangani bobot negatif,
#    sedangkan Dijkstra tidak dapat digunakan
#    dengan benar pada graph berbobot negatif.