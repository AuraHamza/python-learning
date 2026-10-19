graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'S': 4, 'C': 3},
    'B': {'S': 2, 'C': 2},
    'C': {'A': 3, 'B': 2, 'G': 2},
    'G': {'C': 2}
}
heuristic = {
    'S': 8,
    'A': 6,
    'B': 5,
    'C': 3,
    'G': 0
}

def hill_climbing(graph, heuristic, start, goal):
    current = start
    path = [current]
    cost = 0
    while current != goal:
        found = False
        for neighbor, edge_cost in graph[current].items():
            if heuristic[neighbor] < heuristic[current]:
                cost += edge_cost
                current = neighbor
                path.append(current)
                found = True
                break

        if not found:
            break

    print("Route:", " -> ".join(path))
    print("Heuristic values:", [heuristic[node] for node in path])
    print("Total travel cost:", cost)

    if current == goal:
        print("Hospital reached")
    else:
        print("Hospital not reached")

hill_climbing(graph, heuristic, 'S', 'G')