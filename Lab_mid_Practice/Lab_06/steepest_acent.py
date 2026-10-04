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

def steepest_ascent_hill_climbing(start):
    current=start
    path=[start]

    best=current

    for neighbour in graph[current]:
        print("Checking neighbour:",neighbour,"value:",value[neighbour])

        if value[neighbour]>value[current]:
            best=neighbour

        if best==current:
            print("No better Found")
            path.append(current)
    return path,value[best]


path, final_value = steepest_ascent_hill_climbing('A')

print("\nFINAL RESULT")
print("Path:", " -> ".join(path))
print("Final State:", path[-1])
print("Final Value:", final_value)