n = 9  # Number of islands

# Fixed costs for each island (node)
fixed_costs = [474, 368, 327, 485, 374, 391, 419, 408, 356]

# distances matrix (original edge weights)
distances = [
    [0, 76, 0, 54, 53, 96, 99, 31, 49],
    [76, 0, 61, 71, 20, 31, 19, 0, 58],
    [0, 61, 0, 16, 0, 91, 89, 18, 34],
    [54, 71, 16, 0, 31, 8, 98, 96, 38],
    [53, 20, 0, 31, 0, 6, 41, 29, 53],
    [96, 31, 91, 8, 6, 0, 31, 14, 60],
    [99, 19, 89, 98, 41, 31, 0, 37, 37],
    [31, 0, 18, 96, 29, 14, 37, 0, 78],
    [49, 58, 34, 38, 53, 60, 37, 78, 0]
]

# List of edges (u, v, weight)
edges = []

# Build the list of edges from the distances matrix, adjusting the weights
for i in range(n):
    for j in range(i + 1, n):
        if distances[i][j] > 0:
            adjusted_weight = distances[i][j]*10 + fixed_costs[i] + fixed_costs[j]
            edges.append((i, j, adjusted_weight))
        else:
            edges.append((i,j, 0))

# Sort edges by the adjusted weight
edges.sort(key=lambda x: x[2])

# Kruskal's algorithm to find MST with adjusted weights
parent = list(range(n))
rank = [0] * n


# Find function for union-find
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]


# Union function for union-find
def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


# Kruskal's algorithm to construct MST
mst = []
mst_cost = 0
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u + 1, v + 1, weight))
        mst_cost += weight

# Print the resulting MST and its total cost
print("Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with adjusted weight: {weight}")

print(f"Total cost of MST: {mst_cost}")
