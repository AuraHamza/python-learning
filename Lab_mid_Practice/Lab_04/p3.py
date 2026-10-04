class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def dls(self,graph, start, goal, depth_limit):
        visited = []
        stack = [(start, 0)]

        while stack:
            node, depth = stack.pop()

            if node not in visited:
                visited.append(node)
                print(node, end=" -> ")

                if node == goal:
                    return"Goal Found"
                

                if depth < depth_limit:
                    for neighbour in reversed(graph[node]):
                        if neighbour not in visited:
                            stack.append((neighbour, depth + 1))

        return"Goal Not Found"

    def act(self, percept, graph,limit):
        if percept == self.goal:
            return "Goal already reached!"
        return self.dls(graph, percept, self.goal,limit)


def run_agent(agent, environment, start_node,limit):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph,limit)
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
limit=5
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)
run_agent(agent, environment, start_node,limit)


def dls(tree,start,goal,depth_limit):
    visited=[]
    stack=[(start,0)]
    visited.append(start)

    while stack:
        node,limit=stack.pop()
        print(node, end="->")
        if node==goal:
            print("Goal Found")
            return
        if limit<depth_limit:
            for neighbour in reversed(tree[node]):
                 if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append((neighbour,limit+1))
        
    print("\nnot found")


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
start='A'
goal='I'
limit=5
dls(tree,start,goal,limit)