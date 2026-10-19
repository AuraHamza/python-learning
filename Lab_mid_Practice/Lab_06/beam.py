graph = {
    'S': [('A', 2), ('B', 4), ('C', 3), ('D', 5), ('E', 1)],
    'A': [('F', 4), ('H', 6)],
    'B': [('I', 2), ('J', 3)],
    'C': [('K', 4)],
    'D': [('L', 3), ('M', 2)],
    'E': [('N', 5)],
    'F': [('G', 3)],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'G': []
}

heuristic = {
    'S': 8,
    'A': 6,
    'B': 5,
    'C': 7,
    'D': 8,
    'E': 9,
    'F': 2,
    'H': 10,
    'I': 10,
    'J': 10,
    'K': 10,
    'L': 10,
    'M': 10,
    'N': 10,
    'G': 0
}

def beam_search(start,goal,beam_width):
    beam=[(start,0,[start])]
    while beam:
        for node , cost , path in beam:
            if node == goal:
                return path , cost
        canditate=[]

        for node , cost , path in beam:
            for neighbour ,edge_cost in graph[node]:
                new_cost=cost+edge_cost
                new_path=path+[neighbour]
                h=heuristic[neighbour]

                canditate.append((neighbour,new_cost,new_path,h))
                
        if not canditate:
            break

        canditate.sort(key=lambda x:x[3])

        beam=[]

        for node,cost,path,h in canditate[:beam_width]:
            beam.append((node,cost,path))

        print("current Beam")

        for node ,cost ,path in beam:
            print(path, "h =", heuristic[node], "cost =", cost)
            
        print()
    return path, cost





path, cost = beam_search('S', 'G', 2)

if path:
    print("Goal Found")
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Goal Not Found")