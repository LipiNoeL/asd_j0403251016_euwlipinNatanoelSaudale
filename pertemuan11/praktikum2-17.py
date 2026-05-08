# bikin adjacency list pakai dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# tampilkan adjacency list
print("Adjacency List:\n")

for node in graph:
    print(node, "->", graph[node])