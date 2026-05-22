# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi yang paling dekat dari Gerbang adalah
#    Kantin dengan waktu tempuh 2 menit.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendek dari Gerbang ke Aula
#    adalah 7 menit melalui jalur
#    Gerbang -> Kantin -> Lab -> Aula.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak. Jalur langsung tidak selalu menghasilkan
#    jarak paling kecil karena bisa saja terdapat
#    jalur lain dengan lebih banyak node tetapi
#    total bobotnya lebih kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Karena semua bobot pada graph bernilai positif
#    dan Dijkstra efektif digunakan untuk mencari
#    jalur tercepat atau terpendek pada graph
#    berbobot positif.