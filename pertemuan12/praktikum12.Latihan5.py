# ==========================================================
# Nama  : Euwlipin Natanoel Saudale
# NIM   : J0403251016
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

# Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data sebelumnya,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga node
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Node yang memiliki jarak paling kecil dari
#    node awal adalah Depok dengan jarak 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Node yang memiliki jarak paling besar dari
#    node awal adalah Bandung dengan jarak 8.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Algoritma Dijkstra bekerja dengan memilih
#    node yang memiliki jarak terkecil terlebih dahulu,
#    kemudian memperbarui jarak ke node tetangganya.
#    Proses ini dilakukan terus sampai semua node
#    memperoleh jarak terpendek dari node awal.