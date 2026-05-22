# ==========================================================
# Implementasi Algoritma Dijkstra
# ==========================================================

# Mengimpor library heapq untuk membuat priority queue
# Priority queue digunakan agar node dengan jarak terkecil
# selalu diproses terlebih dahulu
import heapq

# Representasi weighted graph menggunakan dictionary bersarang
# Format:
# 'Node': {'Tetangga': bobot}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Fungsi algoritma Dijkstra
# Parameter:
# graph = graph berbobot
# start = node awal
def dijkstra(graph, start):

    # Membuat dictionary untuk menyimpan jarak minimum
    # Semua node awalnya bernilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue digunakan untuk menyimpan pasangan:
    # (jarak, node)
    # Node dengan jarak terkecil akan diproses lebih dulu
    pq = [(0, start)]

    # Perulangan berjalan selama priority queue masih berisi data
    while pq:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung total jarak baru
            # jarak sekarang + bobot edge
            distance = current_distance + weight

            # Jika ditemukan jalur yang lebih pendek
            if distance < distances[neighbor]:

                # Update jarak minimum node tetangga
                distances[neighbor] = distance

                # Masukkan node ke priority queue
                # agar diproses kembali
                heapq.heappush(pq, (distance, neighbor))

    # Mengembalikan hasil seluruh jarak minimum
    return distances

# Memanggil fungsi dijkstra dengan node awal 'A'
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak terpendek
print(hasil)

# ==========================================================
# Penjelasan Hasil
# ==========================================================
# A -> A = 0
# Karena node awal ke dirinya sendiri tidak memiliki biaya
#
# A -> B = 4
# Jalur langsung dari A ke B memiliki bobot 4
#
# A -> C = 2
# Jalur langsung dari A ke C memiliki bobot 2
#
# A -> D = 3
# Jalur terpendek diperoleh dari:
# A -> C -> D
# Total bobot = 2 + 1 = 3
#
# Jika melalui B:
# A -> B -> D = 4 + 5 = 9
# sehingga jalur tersebut tidak dipilih