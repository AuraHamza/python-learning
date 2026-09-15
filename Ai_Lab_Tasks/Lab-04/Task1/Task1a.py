def bfs(graph, start, goal):
    visited = []
    queue = []
    parent = {}

    visited.append(start)
    queue.append(start)
    parent[start] = None

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Path:", " -> ".join(path))
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                parent[neighbour] = node

tree = {
    'Control Room': ['Storage A', 'Storage B'],
    'Storage A': ['Lab 1', 'Lab 2'],
    'Storage B': ['Server Room'],
    'Lab 1': ['Debris 1'],
    'Lab 2': ['Debris 2'],
    'Debris 1': ['Maintenance Corridor'],
    'Debris 2': ['Maintenance Corridor'],
    'Server Room': ['Charging Bay'],
    'Charging Bay': ['Maintenance Corridor'],
    'Maintenance Corridor': ['Survivor Room'],
    'Survivor Room': []
}

start_node = 'Control Room'
goal_node = 'Survivor Room'

print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)