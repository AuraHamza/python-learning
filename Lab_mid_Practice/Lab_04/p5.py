graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

def ucs(graph,start,goal):
    frontier=[(start,0)]
    visisted=set()

    while frontier:
        frontier.sort(key=lambda x:x[1])
        node,cost=frontier.pop(0)
        
        if node in visisted:
            continue

        visisted.add(node)
        print(node,end="-> ")

        if node==goal:
             print("\n Goal Found")
             print("Total Cost:",cost)
             return
        
        for neighbour in graph[node]:
            new_cost=cost+graph[node][neighbour]
            frontier.append((neighbour,new_cost))
            
    print("\nNot Found ")

ucs(graph, 'A', 'I')



class Environment:
    def __init__(self):
        self.graph = {
            'A': {'C': 3, 'B': 4},
            'B': {'A': 4, 'C': 2, 'D': 3, 'E': 6},
            'C': {'A': 3, 'B': 2, 'D': 1},
            'D': {'B': 3, 'C': 1, 'F': 3},
            'E': {'B': 6, 'I': 4},
            'F': {'D': 3, 'H': 2},
            'H': {'F': 2, 'I': 4},
            'I': {'H': 4, 'E': 4}
        }


class Agent:
    def __init__(self, environment, start, goal):
        self.environment = environment
        self.start = start
        self.goal = goal

    def ucs(self):
        graph = self.environment.graph
        start = self.start
        goal = self.goal

        frontier = [(start, 0)]
        visited = set()

        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, cost = frontier.pop(0)

            if node in visited:
                continue

            visited.add(node)

            print(node, end=" -> ")

            if node == goal:
                print("\nGoal Found")
                print("Total Cost:", cost)
                return

            for neighbour in graph[node]:
                new_cost = cost + graph[node][neighbour]
                frontier.append((neighbour, new_cost))

        print("\nNot Found")


def run_agent():
    environment = Environment()
    agent = Agent(environment, 'A', 'I')
    agent.ucs()


run_agent()