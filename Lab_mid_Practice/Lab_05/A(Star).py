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

maze = [
    ['S', '.', '.', '#'],
    ['.', '.', 'E', '.'],
    ['.', '.', '.', '#'],
    ['.', '#', '.', '.']
]

direction = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

graph = {}


def create_graph(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):

            if maze[i][j] != '#':

                neighbour = []

                for dx, dy in direction:
                    x = i + dx
                    y = j + dy

                    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
                        if maze[x][y] != '#':
                            neighbour.append((x, y))

                graph[(i, j)] = neighbour

    return graph


def heuristic(point, goal):
    x1, y1 = point
    x2, y2 = goal

    return abs(x1 - x2) + abs(y1 - y2)


def a_star(graph, start, goal):
    frontier = [(start, 0, [start])]
    g_cost = {start: 0}
    visited = set()

    while frontier:

        frontier.sort(key=lambda x: x[1])

        node, f, path = frontier.pop(0)

        if node in visited:
            continue

        visited.add(node)

        g = g_cost[node]
        h = heuristic(node, goal)

        print(node, "g =", g, "h =", h, "f =", f)

        if node == goal:
            print("Goal Found")
            print("Path:", path)
            print("Total Steps:", len(path) - 1)
            print("Total Cost:", g)
            return

        for neighbour in graph[node]:

            new_g = g + 1

            if neighbour not in g_cost or new_g < g_cost[neighbour]:

                g_cost[neighbour] = new_g

                new_f = new_g + heuristic(neighbour, goal)

                new_path = path + [neighbour]

                frontier.append((neighbour, new_f, new_path))

    print("Not Found")


def main():

    create_graph(maze)

    start = (0, 0)
    goal = (1, 2)

    a_star(graph, start, goal)


main()