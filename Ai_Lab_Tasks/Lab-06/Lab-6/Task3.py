graph = {
    'S': {'A': 4, 'B': 3, 'C': 5},
    'A': {'S': 4, 'D': 4},
    'B': {'S': 3, 'D': 2, 'E': 4},
    'C': {'S': 5, 'E': 2},
    'D': {'A': 4, 'B': 2, 'G': 5},
    'E': {'B': 4, 'C': 2, 'G': 3},
    'G': {'D': 5, 'E': 3}
}
heuristic = {
    'S': 10,
    'A': 7,
    'B': 6,
    'C': 8,
    'D': 4,
    'E': 3,
    'G': 0
}
def hill_climbing(graph, heuristic, start, goal):
    current = start
    path = [current]
    cost = 0
    while current != goal:
        print("Current node:", current)
        neighbors = graph[current]
        best = current

        for neighbor in neighbors:
            if heuristic[neighbor] < heuristic[best]:
                best = neighbor
        if best == current:
            break
        cost += graph[current][best]
        current = best
        path.append(current)

    print("Path:", " -> ".join(path))
    print("Total flight cost:", cost)

    if current == goal:
        print("Goal reached")
    else:
        print("Goal not reached")
hill_climbing(graph, heuristic, 'S', 'G')
