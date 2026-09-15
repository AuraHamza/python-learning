graph = {
    "Entrance": [("Room A", 2), ("Room B", 3)],
    "Room A": [("Room C", 2), ("Room D", 5)],
    "Room B": [("Room D", 2)],
    "Room C": [("Treasure Room 1", 4)],
    "Room D": [("Treasure Room 2", 3), ("Trap Room", 1)],
    "Trap Room": [("Treasure Room 3", 2)]
}

treasure_values = {
    "Treasure Room 1": 10,
    "Treasure Room 2": 8,
    "Treasure Room 3": 15
}

def utility_based_agent(graph, start, treasure_values):
    frontier = [(start, 0)]
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}
    expansion_order = []

    best_treasure = None
    best_path = []
    best_cost = 0
    best_utility = float("-inf")

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)
        expansion_order.append(current_node)

        if current_node in treasure_values:
            utility = treasure_values[current_node] - current_cost

            if utility > best_utility:
                best_utility = utility
                best_treasure = current_node
                best_cost = current_cost

                path = []
                node = current_node

                while node is not None:
                    path.append(node)
                    node = came_from[node]

                path.reverse()
                best_path = path

        for neighbor, cost in graph.get(current_node, []):
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Node expansion order:", ", ".join(expansion_order))
    print("Path to goal:", " -> ".join(best_path))
    print("Total utility:", treasure_values[best_treasure], "-", best_cost, "=", best_utility)


start_node = "Entrance"

print("Following is the Utility-Based Agent:")
utility_based_agent(graph, start_node, treasure_values)