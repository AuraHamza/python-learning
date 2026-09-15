def dfs_recursive(graph, node, goal, visited, path):
    visited.append(node)
    path.append(node)
    print(node, end=" ")

    if node == goal:
        print("\nGoal found!")
        print("Path:", " -> ".join(path))
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs_recursive(graph, neighbour, goal, visited, path):
                return True
    path.pop()
    return False


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

visited = []
path = []

print("\nFollowing is the Recursive Depth-First Search (DFS):")
dfs_recursive(tree, start_node, goal_node, visited, path)