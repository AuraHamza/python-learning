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

def dfs(tree,start_node,goal):
    visited=[]
    stack=[]

    visited.append(start_node)
    stack.append(start_node)

    while stack:
        node=stack.pop()
        print(node,end="->")
        if node==goal:
            print("\nGoal found")
            return
        for neghbour in reversed(tree[node]):
            if neghbour not in visited:
                 visited.append(neghbour)
                 stack.append(neghbour)
    print("\n Goal not found")


start_node = 'A'
goal_node = 'I'

print("DFS:")
dfs(tree, start_node, goal_node)


#GOAL BASE

class Environment:
    def __init__(self,graph):
        self.graph=graph
    def get_p(self,node):
        return node

class GoalAgent:
    def __init__(self,goal):
        self.goal=goal
    def formulate_goal(self,p):
        if p==self.goal:
            return "Goal Found"
        else:
            return "Searching"
    def dfs(self,tree,start_node,goal):
        visited=[]
        stack=[]
        visited.append(start_node)
        stack.append(start_node)

        while stack:
            node=stack.pop()
            print(node, end=" -> ")
            if node == goal:
                return "Goal Found"
            for neighbour in reversed(tree[node]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
        return "Not Found!"
    def act(self,p,tree):
        status_goal=self.formulate_goal(p)
        if status_goal=="Goal Found":
            return "Goal Reached"
        else:
            return self.dfs(tree,p,self.goal)
    
def run_agent(agent,environment,start_node):
    p=environment.get_p(start_node)
    action=agent.act(p,environment.graph)
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
agent = GoalAgent(goal_node)
environment = Environment(tree)
run_agent(agent, environment, start_node)