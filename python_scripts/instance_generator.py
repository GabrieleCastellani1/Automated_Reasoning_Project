import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from times_output_prettify import create_data

max_percentage = 10

n = 7


def generate_random_data(n):
    max_edges = int((n * (n - 1) / 2) * (max_percentage / 100))

    while True:
        # Generate the existing_bridges matrix with randomness
        existing_bridges = [[0 for _ in range(n)] for _ in range(n)]
        current_edges = 0

        for i in range(n):
            for j in range(i + 1, n):
                if current_edges < max_edges and random.random() < (max_percentage / 100):
                    existing_bridges[i][j] = 1
                    existing_bridges[j][i] = 1  # Ensure symmetry
                    current_edges += 1

        # Check if the graph is not fully connected
        if not is_connected(existing_bridges, n):
            break  # Exit the loop if the graph is not fully connected

    # Generate distances matrix
    max_distance = 100
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if existing_bridges[i][j] == 1 or i == j:
                distances[i][j] = 0
                distances[j][i] = 0
            else:
                distances[i][j] = random.randint(1, max_distance)
                distances[j][i] = distances[i][j]

    return existing_bridges, distances


def print_matrix(matrix, n):
    print("[| ", end="")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=", " if j < n - 1 else "")
        if i < n - 1:
            print(",\n| ", end="")
    print("|];")


def generate_clingo_format(existing_bridges, distances, n):
    # Print nodes
    print("\n% Nodes in the graph")
    for i in range(1, n + 1):
        print(f"node({i}).")

    print("\n% Edges with weights")

    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] > 0:
                print(f"edge({i + 1}, {j + 1}, {distances[i][j]}).")

    print("\n% Define fixed edges with zero cost")
    for i in range(n):
        for j in range(i + 1, n):
            if existing_bridges[i][j] == 1 and distances[i][j] == 0:
                print(f"fixed_edge({i + 1}, {j + 1}).")


def is_connected(bridges, n):
    """Check if the graph is connected using BFS."""
    visited = [False] * n
    queue = deque([0])
    visited[0] = True

    while queue:
        current = queue.popleft()
        for neighbor in range(n):
            if bridges[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return all(visited)


# Generates a random vector of dimension n with numbers in a given interval [lower_bound, upper_bound].
def generate_random_vector(n, lower_bound, upper_bound):
    random_vector = np.random.randint(lower_bound, upper_bound + 1, size=n)
    return random_vector


random_vector = generate_random_vector(n, 300, 500)

print(f"fixed_costs = [{', '.join(map(str, random_vector))}];\n")
# Translate the vector into Clingo facts

# Generate the data
existing_bridges, distances = generate_random_data(n)

# Print the generated matrices
print("n =", n, ";")
print("\nexisting_bridges = ", end="")
print_matrix(existing_bridges, n)
print("\ndistances = ", end="")
print_matrix(distances, n)
generate_clingo_format(existing_bridges, distances, n)


def print_vector_as_clingo_facts():
    for index, value in enumerate(random_vector, start=1):
        print(f"fixed_cost({index}, {value}).")


print("\n% Define fixed costs related to each single isle")
print_vector_as_clingo_facts()

# Input sizes
input_sizes = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Data converted to milliseconds
data = create_data()

# Check for length mismatches before plotting
for label, values in data.items():
    if len(values) != len(input_sizes):
        print(f"Length mismatch for {label}: input_sizes has {len(input_sizes)} elements, but values has {len(values)}")

# Plot the data
plt.figure(figsize=(14, 8))
for label, values in data.items():
    plt.plot(input_sizes, values, label=label.replace("_", " "), marker='o')

plt.title("Performance Comparison (Execution Time in msec)")
plt.xlabel("Input Size")
plt.ylabel("Time (msec)")
plt.yscale("log")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
