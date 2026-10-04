# class Environment:
#     def __init__(self, graph):
#         self.graph = graph

#     def get_percept(self, node):
#         return node

# class GoalBasedAgent:
#     def __init__(self, goal):
#         self.goal = goal

#     def formulate_goal(self, percept):
#         if percept == self.goal:
#             return "Goal reached"
#         return "Searching"

#     def dls(self,tree, start, goal, depth_limit):
#         stack = [(start, 0)]

#         while stack:
#             node, depth = stack.pop()

#             print(node, end=" -> ")

#             if node == goal:
#                 return True

#             if depth < depth_limit:
#                 for neighbour in reversed(tree[node]):
#                     stack.append((neighbour, depth + 1))

#         return False


#     def ids(self,tree, start, goal, max_depth):
#         for depth in range(max_depth + 1):
#             print("\nDepth:", depth)

#             if self.dls(tree, start, goal, depth):
#                 print("\nGoal Found")
#                 return

#         print("\nGoal Not Found")

#     def act(self, percept, graph,limit):
#         if percept == self.goal:
#             return "Goal already reached!"
#         return self.ids(graph, percept, self.goal,limit)


# def run_agent(agent, environment, start_node,limit):
#     percept = environment.get_percept(start_node)
#     action = agent.act(percept, environment.graph,limit)
#     print(action)

# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': ['H'],
#     'E': [],
#     'F': ['I'],
#     'G': [],
#     'H': [],
#     'I': []
# }

# start_node = 'A'
# goal_node = 'I'
# limit=5
# agent = GoalBasedAgent(goal_node)
# environment = Environment(tree)
# run_agent(agent, environment, start_node,limit)


def dls(tree,start,goal,depth_limit):
    stack=[(start,0)]

    while stack:
        node ,limit=stack.pop()
        print(node , end="->")
        if node == goal:
            return True
        if limit<depth_limit:
            for n in reversed(tree[node]):
                stack.append((n,limit+1))
    return False

def ids ( tree , start , goal , depth_limit):
    for depth in range(depth_limit+1):
        print("\nDepth:",depth)
        if dls(tree,start,goal,depth):
            print("\nGoal found")
            return

    print("\nGoal Not Found.")


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
ids(tree, start_node,goal_node,limit)