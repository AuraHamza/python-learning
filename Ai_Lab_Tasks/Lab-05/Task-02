from queue import PriorityQueue

graph = {
    'S':[('A', 2),('B', 4),('C', 3)],
    'A':[('D', 6)],
    'B':[('E', 2)],
    'C':[('E', 2)],
    'D':[('G', 0)],
    'E':[('F', 1)],
    'F':[('G', 0)],
    'G':[]
}

def best_first_search(graph, start, goal):
    priority_queue = PriorityQueue()
    visited = set()

    priority_queue.put((0, start))

    print("Traversal Path: ",end="")

    while not priority_queue.empty():
        priority, current_node = priority_queue.get()

        if current_node in visited:
            continue

        visited.add(current_node)
        print(current_node,end=" ")

        if current_node == goal:
            print("\nGoal reached successfully!")
            return True

        for neighbor, evaluation_value in graph[current_node]:
            if neighbor not in visited:
                priority_queue.put((evaluation_value, neighbor))

    print("\nGoal is not reachable!")
    return False


print("Best-First Search:")
best_first_search(graph, 'S', 'G')