# tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
def bfs(graph,start,goal):
    visited=[]
    queue=[]
    queue.append(start)
    visited.append(start)

    while queue:
        node=queue.pop(0)
        print(node, end=" ")
        if node==goal:
            print("\n Goal Found!")
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start_node ="A"
goal_node = "H"

print("\nFollowing is the Breath-First Search(BFS):")
bfs(tree,start_node,goal_node)


class Environment:
    def __init__(self,graph):
        self.graph=graph
    def get_percept(self,node):
        return node

class ModelAgent:
    def __init__(self,goal):
        self.goal=goal
    def formulate_goal(self,percept):
        if percept==self.goal:
            return "Goal reached"
        else:
            return"Searching"
    def bfs(self,graph,start,goal):
        visited=[]
        queue=[]

        visited.append(start)
        queue.append(start)
        while queue:
            node=queue.pop(0)
            print("Visiting:",node)

            if node==goal:
                return "Goal",goal,"Found"
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return "Goal not Found!"

    def act(self,graph,percept):
        goal_status=self.formulate_goal(percept)
        if goal_status=="Goal reached":
            return "Goal ", self.goal,"Found"
        else:
            return self.bfs(graph,percept,self.goal)

def run_agent(agent,environment,start_node):
    percept=environment.get_percept(start_node)
    action=agent.act(environment.graph,percept)
    print(action)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
start_node = 'A'
goal_node = 'I'

e1=Environment(tree)
a1=ModelAgent(goal_node)
run_agent(a1,e1,start_node)

maze= [ 
    [1,1,0],
    [0,1,0],
    [0,1,1]
]
direction=[(0,1),(1,0)]
graph={}
def create_graph(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==1:
                neighbour=[]
                for dx ,dy in direction:
                    x=dx+i
                    y=dy+j
                    if x<len(maze) and y<len(maze[0]) and maze[x][y]==1:
                        neighbour.append((x,y))
                graph[(i,j)]=neighbour 
    return graph                 

def bfs(graph,start,goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)
    while queue:
        node=queue.pop(0)
        if node==goal:
            print("Goal Found:",node)
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print("Goal not Found!")
    return

graph=create_graph(maze)
print("\nAdjency List:")
for node in graph:
    print(node,":",graph[node])

start=(0,0)
goal=(2,2)

print("\nBFS:")
bfs(graph,start,goal)

maze = [["A","0","0","#","#"],
        ["#","F","0","#","P"],
        ["0","0","0","F","0"],
        ["0","#","F","#","0"],
        ["0","0","0","0","0"],]

direction= [[0,1],[1,0],[0,-1],[-1,0]]

def graph_creation(maze):
    graph={}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
           if maze[i][j] in ["A", "0", "P"]:
                neighbour=[]
                for dx, dy in direction:
                    x=dx+i
                    y=dy+j
                    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] in ["0", "P"]:
                         neighbour.append((x,y))
                graph[(i,j)]=neighbour
    return graph

class Environment:
    def __init__(self,graph):
        self.graph=graph
    def get_percept(self,node):
        return node

class GoalAgent:
    def __init__(self,goal):
        self.goal=goal
    def formulate_goal(self,percept):
        if self.goal==percept:
            return "Goal Found"
        else:
            return "Searching"
    def bfs(self,graph,start,goal):
        visited=[]
        queue=[]

        visited.append(start)
        queue.append(start)

        while queue:
            node=queue.pop(0)
            if node==goal:
                return "Goal ", self.goal,"Found"
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return "Goal not found!"

    def act(self,percept,graph):
        goal_status=self.formulate_goal(percept)
        if goal_status=="Goal Found":
            return "Goal ", self.goal,"Found"
        else:
            return self.bfs(graph,percept,self.goal)
def act_agent(agent,environment,start_node):
    percept=environment.get_percept(start_node)
    action=agent.act(percept,environment.graph)
    print(action)

graph=graph_creation(maze)
e1=Environment(graph)
start_node=(0,0)
goal_node=(1,4)
a1=GoalAgent(goal_node)


act_agent(a1,e1,start_node)