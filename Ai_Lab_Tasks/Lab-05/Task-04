from queue import PriorityQueue
graph = {
    'S':[('A', 3),('B', 2),('C', 4)],
    'A':[('D', 4)],
    'B':[('E', 3)],
    'C':[('E', 2),('F', 5)],
    'D':[('G', 5)],
    'E':[('F', 2)],
    'F':[('G', 3)],
    'G':[]
}

heuristic = {
    'S': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 5,
    'E': 5,
    'F': 3,
    'G': 0
}

def a_star(graph, start, goal, heuristic):
    priority_queue = PriorityQueue()
    g_cost = {start: 0}
    came_from = {start: None}
    visited = set()

    priority_queue.put((heuristic[start], start))
    print("Nodes Explored:")

    while not priority_queue.empty():
        current_f, current_node = priority_queue.get()

        if current_node in visited:
            continue
        visited.add(current_node)
        current_g = g_cost[current_node]
        current_h = heuristic[current_node]

        print(current_node, "g =", current_g, "h =", current_h, "f =", current_f)

        if current_node == goal:
            path = []

            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()

            print("\nGoal reached successfully!")
            print("UAV Route:", " -> ".join(path))
            print("Total Route Cost:", g_cost[goal])

            return path, g_cost[goal]

        for neighbor, edge_cost in graph[current_node]:
            new_g = current_g + edge_cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                came_from[neighbor] = current_node
                f_cost = new_g + heuristic[neighbor]

                priority_queue.put(
                    (f_cost, neighbor)
                )

    print("\nGoal is not reachable!")
    return None, None


print("A* Search for UAV Navigation:")
a_star(graph, 'S', 'G', heuristic)