from queue import PriorityQueue
graph = {
    'S':[('B', 2),('C', 4)],
    'B':[('G', 2)],
    'C':[('D', 1)],
    'D':[('G', 1)],
    'G':[]
}

heuristic = {
    'S': 3,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0
}

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = PriorityQueue()
    visited = set()
    came_from = {start: None}

    priority_queue.put((heuristic[start], start))

    print("Traversal Path: ",end="")

    while not priority_queue.empty():
        current_h, current_node = priority_queue.get()

        if current_node in visited:
            continue

        visited.add(current_node)
        print(current_node,end=" ")

        if current_node == goal:
            path = []

            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()

            print("\nGoal reached successfully!")
            print("Path:", " -> ".join(path))
            return path

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                priority_queue.put(
                    (heuristic[neighbor], neighbor)
                )

    print("\nGoal is not reachable!")
    return None

print("Greedy Best-First Search:")
greedy_best_first_search( graph,'S','G', heuristic)