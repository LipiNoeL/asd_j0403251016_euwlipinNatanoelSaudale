# Euwlipin Natanoel Saudale / J0403251016 / TPL A1

# --- PROGRAM GRAPH PETA KOTA ---

# 1. Definisi Node
nodes = ["Jakarta", "Bogor", "Bandung", "Depok", "Bekasi"]

# 2. Representasi Adjacency List (Pakai Dictionary)
# Menunjukkan tiap kota nyambung ke mana saja
adj_list = {
    "Jakarta": ["Bogor", "Bekasi", "Depok"],
    "Bogor": ["Jakarta", "Bandung", "Depok"],
    "Bandung": ["Bogor", "Bekasi"],
    "Depok": ["Jakarta", "Bogor", "Bekasi"],
    "Bekasi": ["Jakarta", "Bandung", "Depok"]
}

# 3. Representasi Adjacency Matrix
# 0 = Tidak ada jalan, 1 = Ada jalan
# Urutan: Jakarta, Bogor, Bandung, Depok, Bekasi
adj_matrix = [
    [0, 1, 0, 1, 1], # Jakarta
    [1, 0, 1, 1, 0], # Bogor
    [0, 1, 0, 0, 1], # Bandung
    [1, 1, 0, 0, 1], # Depok
    [1, 0, 1, 1, 0]  # Bekasi
]

# --- OUTPUT PROGRAM ---
print("=== DAFTAR NODE (KOTA) ===")
for i, node in enumerate(nodes):
    print(f"{i}. {node}")

print("\n=== ADJACENCY LIST (HUBUNGAN LANGSUNG) ===")
for kota, tetangga in adj_list.items():
    print(f"{kota} terhubung ke: {', '.join(tetangga)}")

print("\n=== ADJACENCY MATRIX ===")
print("    JK  BG  BD  DP  BK") # Header singkat
for i, row in enumerate(adj_matrix):
    print(f"{nodes[i][:2]} {row}")
    
