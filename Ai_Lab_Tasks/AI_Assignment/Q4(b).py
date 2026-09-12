maze=[
    ['S',0,1,0,0,0],
    [0,0,1,0,1,0],
    [0,1,0,0,1,0],
    [0,0,0,1,0,0],
    [1,1,0,0,0,'G']
]
ROWS=len(maze)
COLS=len(maze[0])

def find_cell(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c]==symbol:
                return (r,c)
    return None

START=find_cell('S')
GOAL=find_cell('G')

def get_neighbors(node):
    r,c=node
    moves=[(1,0),(0,1),(-1,0),(0,-1)]
    neighbors=[]
    for dr,dc in moves:
        nr=r+dr
        nc=c+dc
        if 0<=nr<ROWS and 0<=nc<COLS:
            if maze[nr][nc]!=1:
                neighbors.append((nr,nc))
    return neighbors

def reconstruct_path(parent,goal):
    path=[goal]
    while path[-1]!=START:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def bfs(start,goal):
    frontier=[start]
    visited={start}
    parent={}
    nodes_expanded=0
    while frontier:
        current=frontier.pop(0)
        if current==goal:
            path=reconstruct_path(parent,goal)
            return {
                "path":path,
                "path_length":len(path)-1,
                "nodes_expanded":nodes_expanded,
                "goal_found":True
            }
        nodes_expanded+=1
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=current
                frontier.append(neighbor)
    return {
        "path":None,
        "path_length":None,
        "nodes_expanded":nodes_expanded,
        "goal_found":False
    }

def dls(start,goal,limit):
    frontier=[(start,0,[start])]
    visited=set()
    nodes_expanded=0
    while frontier:
        current,depth,path=frontier.pop()
        if current==goal:
            return {
                "path":path,
                "path_length":len(path)-1,
                "nodes_expanded":nodes_expanded,
                "goal_found":True
            }
        if current in visited:
            continue
        visited.add(current)
        if depth<limit:
            nodes_expanded+=1
            neighbors=get_neighbors(current)

            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    frontier.append((neighbor,depth+1,path+[neighbor]))

    return {
        "path":None,
        "path_length":None,
        "nodes_expanded":nodes_expanded,
        "goal_found":False
    }

def ids(start,goal,max_limit=50):
    total_nodes_expanded=0
    iteration_log=[]
    for limit in range(max_limit+1):
        result=dls(start,goal,limit)
        iteration_log.append({
            "limit":limit,
            "goal_found":result["goal_found"],
            "path_length":result["path_length"],
            "nodes_expanded":result["nodes_expanded"]
        })
        total_nodes_expanded+=result["nodes_expanded"]

        if result["goal_found"]:
            return {
                "path":result["path"],
                "path_length":result["path_length"],
                "nodes_expanded":total_nodes_expanded,
                "goal_found":True,
                "iterations":iteration_log
            }

    return {
        "path":None,
        "path_length":None,
        "nodes_expanded":total_nodes_expanded,
        "goal_found":False,
        "iterations":iteration_log
    }

def print_result(name,result):
    print("---",name,"---")
    print("Goal found:",result["goal_found"])
    print("Path:",result["path"])
    print("Path length:",result["path_length"])
    print("Nodes expanded:",result["nodes_expanded"])

if __name__=="__main__":
    print("Start:",START,"Goal:",GOAL)
    bfs_result=bfs(START,GOAL)
    print_result("BFS",bfs_result)
    print("--- DLS at Different Depth Limits ---")
    for limit in [2,4,6,9]:
        result=dls(START,GOAL,limit)
        print("Limit=",limit,
              "| Goal found:",result["goal_found"],
              "| Path length:",result["path_length"],
              "| Nodes expanded:",result["nodes_expanded"],
              "| Path:",result["path"])

    ids_result=ids(START,GOAL)
    print_result("IDS",ids_result)
    print("--- IDS Iteration-by-Iteration Breakdown ---")
    for iteration in ids_result["iterations"]:
        print("Depth limit=",iteration["limit"],
              "| Goal found:",iteration["goal_found"],
              "| Path length:",iteration["path_length"],
              "| Nodes expanded:",iteration["nodes_expanded"])
