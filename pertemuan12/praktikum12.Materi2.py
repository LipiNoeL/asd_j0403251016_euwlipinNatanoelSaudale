# ==========================================================
# Implementasi Algoritma Bellman-Ford
# ==========================================================

# Fungsi Bellman-Ford digunakan untuk mencari
# jarak terpendek dari satu node ke seluruh node lain
# Algoritma ini dapat menangani bobot negatif

def bellman_ford(graph, start):

    # Membuat dictionary untuk menyimpan jarak minimum
    # Semua node awalnya bernilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # ==========================================================
    # Proses Relaksasi Edge
    # ==========================================================
    # Relaksasi dilakukan sebanyak jumlah node - 1
    # Tujuannya agar seluruh kemungkinan jalur
    # dapat diperiksa dan diperbarui
    for _ in range(len(graph) - 1):

        # Memeriksa setiap node pada graph
        for node in graph:

            # Memeriksa semua tetangga dan bobot edge
            for neighbor, weight in graph[node].items():

                # Mengecek apakah jalur baru lebih kecil
                # dibandingkan jarak sebelumnya
                if distances[node] + weight < distances[neighbor]:

                    # Jika lebih kecil, update jaraknya
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil seluruh jarak minimum
    return distances

# ==========================================================
# Penjelasan Algoritma
# ==========================================================
# Bellman-Ford bekerja dengan cara:
# 1. Memberikan jarak awal tak hingga ke semua node
# 2. Node awal diberi nilai 0
# 3. Melakukan relaksasi seluruh edge berulang kali
# 4. Jika ditemukan jalur yang lebih pendek,
#    maka jarak diperbarui
#
# Kelebihan Bellman-Ford:
# - Dapat menangani bobot negatif
#
# Kekurangan Bellman-Ford:
# - Lebih lambat dibanding Dijkstra
# karena harus memeriksa seluruh edge berulang kali