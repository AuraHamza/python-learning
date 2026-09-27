from queue import PriorityQueue
graph = {
    'S':[('A', 3),('B', 6),('C', 5)],
    'A':[('D', 9),('E', 8)],
    'B':[('F', 12),('G', 14)],
    'C':[('H', 7)],
    'H':[('I', 5),('J', 6)],
    'I':[('K', 1),('L', 10),('M', 2)],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[]
}

def best_first_search(graph, start, goals):
    priority_queue = PriorityQueue()
    visited = set()
    goals_reached = set()

    priority_queue.put((0, start, ()))
    print("Traversal Path: ",end="")
    while not priority_queue.empty():
        priority, current_node, path = priority_queue.get()
        state = (current_node, path)

        if state in visited:
            continue
        visited.add(state)
        current_path = path + (current_node,)

        if current_node in goals:
            goals_reached.add(current_node)
        print(current_node, end=" ")

        if goals_reached == set(goals):
            print("\nAll goals reached successfully!")
            print("Path:", " -> ".join(current_path))
            print("Total Cost:", priority)
            return True

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in current_path:
                new_cost = priority + edge_cost
                priority_queue.put(
                    (new_cost, neighbor, current_path)
                )

    print("\nAll goals are not reachable!")
    return False


goals = ['K', 'M']
print("Best-First Search with Multiple Goals:")
best_first_search(graph, 'S', goals)