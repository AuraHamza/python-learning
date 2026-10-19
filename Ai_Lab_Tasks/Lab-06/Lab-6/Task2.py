graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'S': 3, 'D': 4},
    'B': {'S': 2, 'C': 2},
    'C': {'B': 2, 'D': 2, 'G': 5},
    'D': {'A': 4, 'C': 2, 'G': 3},
    'G': {'C': 5, 'D': 3}
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'G': 0
}

def beam_search(graph, heuristic, start, goal, k):
    beam = [([start], 0)]
    while beam:
        print("Beam:", [path[-1] for path, cost in beam])

        for path, cost in beam:
            if path[-1] == goal:
                return path, cost

        candidates = []

        for path, cost in beam:
            current = path[-1]

            for neighbor, edge_cost in graph[current].items():
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_cost = cost + edge_cost
                    candidates.append((new_path, new_cost))

        if not candidates:
            break
        candidates.sort(key=lambda x: heuristic[x[0][-1]])
        beam = candidates[:k]
    return None, 0

path, cost = beam_search(graph, heuristic, 'S', 'G', 2)
if path:
    print("Final Path:", " -> ".join(path))
    print("Total Path Cost:", cost)
else:
    print("No path found")
