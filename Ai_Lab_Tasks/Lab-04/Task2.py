graph = {
    'Central Command': {'Shelter A': 4, 'Shelter B': 2},
    'Shelter A': {'Street 1': 5, 'Street 2': 3},
    'Shelter B': {'Street 2': 2},
    'Street 1': {'Hospital Zone': 7},
    'Street 2': {'Hospital Zone': 4, 'Street 3': 6},
    'Street 3': {'Hospital Zone': 2},
    'Hospital Zone': {}
}

def ucs(graph, start, goal):
    frontier = [(start, 0)]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}
    expansion_order = []

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)
        if current_node in visited:
            continue
        visited.add(current_node)
        expansion_order.append(current_node)
        print(current_node, end=" ")

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print("\nGoal found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", current_cost)
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("\nGoal not found")


start_node = 'Central Command'
goal_node = 'Hospital Zone'

print("Following is the Uniform Cost Search (UCS):")
ucs(graph, start_node, goal_node)