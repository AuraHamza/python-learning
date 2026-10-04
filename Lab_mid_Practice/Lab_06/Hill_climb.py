graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

value = {
    'A': 4,
    'B': 6,
    'C': 5,
    'D': 8,
    'E': 7
}

def hill_climbing(start):
    current=start
    path=[current]
    while True:
        print("\nCurrent State:",current)
        print("Current value:",value[current])

        moved=False

        for neighbour in graph[current]:
            print("Checking neighbour:",neighbour,"value:",value[neighbour])

            if value[neighbour]>value[current]:
                current=neighbour
                path.append(current)
                moved=True
                break
        if not moved:
            print("No better neighbour found;")
            break
    return path,value[current]

path, final_value = hill_climbing('A')

print("\nFINAL RESULT")
print("Path:", " -> ".join(path))
print("Final State:", path[-1])
print("Final Value:", final_value)