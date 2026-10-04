graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

def a_star(graph,start,goal,heuristic):
    forntier=[(start,0)]
    g_cost={start:0}
    visited=set()

    while forntier:
        forntier.sort(key=lambda x:x[1])
        node,f = forntier.pop(0)

        if node in visited:
            continue

        visited.add(node)

        g=g_cost[node]
        h=heuristic[node]
        print(node , "g=",g,"h=",h,"f=",f)

        if node==goal:
            print("Goal Found")
            print("Total cost:",g)
            return
        for neighnour , cost in graph[node].items():
            new_g=g+cost
            if neighnour not in g_cost or new_g<g_cost[neighnour]:
                g_cost[neighnour]=new_g
                new_f=new_g+heuristic[neighnour]
                forntier.append((neighnour,new_f))
    print("Not found")


a_star(graph, 'A', 'G', heuristic)