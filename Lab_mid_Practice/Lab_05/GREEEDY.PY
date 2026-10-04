graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0
}

def greedy_best_first_search(graph, start, goal, heuristic):
    frontier=[(start,heuristic[start])]
    visisted=set()

    while frontier:
        frontier.sort(key=lambda x:x[1])
        node,h=frontier.pop(0)
        if node in visisted:
            continue
        print(node,"h",h)

        if node == goal:
            print("Goal Found")
            return
        visisted.add(node)
        for neighbour in graph[node]:
            if neighbour not in visisted:
                frontier.append((neighbour,heuristic[neighbour]))
    return("\n Goal not found")

greedy_best_first_search(graph, 'A', 'I', heuristic)