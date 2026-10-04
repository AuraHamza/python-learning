from queue import PriorityQueue
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 6), ('E', 5)],
    'C': [('F', 3), ('G', 7)],
    'D': [],
    'E': [('I', 2)],
    'F': [('I', 4)],
    'G': [],
    'I': []
}
def best_first_search(graph,start,goal):
    queue=PriorityQueue()
    visited = set()
    queue.put((0,start))
    while not queue.empty():
        h,node=queue.get()

        if node in visited:
            continue
        visited.add(node)
        print(node,end="->")

        if node==goal:
            print("\nGoal Found")
            return
        for neighbour ,herustic in graph[node]:
            if neighbour not in visited:
                queue.put((herustic,neighbour))
    print("\nNot Found")

best_first_search(graph, 'A', 'I')


from queue import PriorityQueue


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start=(0,0)
goal=(4,4)

def heuristic(position,goal):
    return abs(position[0]-goal[0])+abs(position[1]-goal[1])

def Best_first_search(maze,start,goal):
    row=len(maze)
    col=len(maze[0])
    visited=set()
    queue=PriorityQueue()

    queue.put((heuristic( start,goal),start))
    visited.add(start)

    direction=[(1,0),(-1,0),(0,1),(0,-1)]

    while not queue.empty():
        h,node=queue.get()
        print(node,end="->")

        if node==goal:
            print("\nGOal Found:")
            return
        for dx,dy in direction:
            new_position=(node[0]+dx, node[1]+dy)

            if( 0<=new_position[0]<row
                and 0<=new_position[1]<col 
                and maze[new_position[0]][new_position[1]]==0
                and new_position not in visited):
                    new__h=heuristic(new_position,goal)
                    queue.put((new__h,new_position))
                    visited.add(new_position)

    print("\nGoal Not Found")
Best_first_search(maze, start, goal)