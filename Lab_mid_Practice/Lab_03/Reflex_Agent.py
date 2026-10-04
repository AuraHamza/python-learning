
# Basic Structure 
# class Environment:
#     def __init__(self,initial_state):
#         self.initial_state=initial_state

#     def get_percept(self):
#         pass

# class SimpleReflexAgent:
#     def __init__(self):
#         pass
#     def act(self,percept):
#         pass

# def run_agent(agent,environment):
#     action=agent.act(percept)
#     print("Percept:",percept,"Action",action)

# E1=Environment(initial_state=0)

#SimpleReflexAgent
# class Environment:
#     def __init__(self,initial_state):
#         self.initial_state=initial_state

#     def get_percept(self):
#         return self.initial_state

# class SimpleReflexAgent:
#     def __init__(self):
#         pass

#     def act(self,percept):
#         if percept == 0:
#             return "Move Right"
#         else:
#             return "Move Left"


# def run_agent(agent, environment):
#     percept=environment.get_percept()
#     action=agent.act(percept)
#     print("Percept:", percept, "Action:", action)


# E1=Environment(initial_state=0)
# A1=SimpleReflexAgent()
# run_agent(A1,E1)

class Environment:
    def __init__(self,initial_state="Dirty"):
        self.initial_state=initial_state

    def get_percept(self):
        return self.initial_state

    def clean_room(self):
        self.initial_state="Clean"

class ReflexAgent:
    def __init__(self):
        pass
    def act(self,percept):
        if percept =="Dirty":
            return "Clean the room!"
        else:
            return "Room is already cleaned."

def run_agent(agent,environmet,step):
    for step in range(1,step+1):

        percept=environmet.get_percept()
        action=agent.act(percept)

        print("Steps:",step)
        print("Percept:", percept)
        print("Action:", action)         
        if percept=="Dirty":
            environmet.clean_room()
        print("Room State After Action:",environmet.initial_state)
        print("--------------------------------------------------------------")
e1=Environment("Dirty")
a1=ReflexAgent()

run_agent(a1,e1,3)


# Using Random
import random
class Environment:
    def __init__(self,initial_state="Dirty"):
        self.initial_state=initial_state
    def get_percept(self):
        return self.initial_state

    def change_state(self):
        self.initial_state=random.choice(["Clean","Dirty"])


class ReflexAgent:
    def __init__(self):
        pass
    def act(self,percept):
        if percept=="Dirty":
            return("Clean the room!")
        else:
            return("Room is clean.")


def run_agent(agent,environment,step):

    for step in range(1,step+1):
        percept=environment.get_percept()
        action=agent.act(percept)
        print("Steps:",step)
        print("Percept:", percept)
        print("Action:", action)        
        environment.change_state()
        print("Room State After Action:",environment.initial_state)
        print("--------------------------------------------------------------")
e1=Environment("Dirty")
a1=ReflexAgent()

run_agent(a1,e1,5)


class Environment:
    def __init__(self):
        self.grid=[
            "Clean","Dirty","Clean",
            "Clean","Dirty","Dirty",
            "Clean","Dirty","Clean"
            ]
    def get_percept(self,position):
            return self.grid[position] 
    def clean_room(self,position):
            self.grid[position]="Clean"
    def display_grid(self,position):
            agent_grid=self.grid[:]
            agent_grid[position]="A"
            for i in range(0,9,3):
                print("|".join(agent_grid[i:i+3]))
            print()
class ReflexAgent:
    def __init__(self):
        self.position=0
    def act(self,percept,enviroment):
        if percept=="Dirty":
            return"Clean the room!"
            enviroment.clean_room(self.position)
        else:
            return"Room is cleaned"
    def move(self):
        if self.position<8:
            self.position+=1

def run_agent(agent,environment,steps):
    for step in range(1,steps+1):
        position=agent.position
        percept=environment.get_percept(position)
        action = agent.act(percept,environment)

        if step<steps:
            agent.move()
            
        print("=" * 50)
        print(f"Step {step}")
        print(f"Agent Position : {position}")
        print(f"Percept        : {percept}")
        print(f"Action         : {action}")

e1=Environment()
a1=ReflexAgent()
run_agent(a1,e1,9)



class Environment:
    def __init__(self):
        self.grid=[
            "Cool","Hot","Cool",
            "Hot","Cool","Hot",
            "Cool","Hot","Cool"
                   ]
    def get_percept(self,position):
        return self.grid[position]
    def Open_fan(self,position):
        self.grid[position]="Cool"
    def display_grid(self,position):
        agent_grid=self.grid[:]
        agent_grid[position]="A"
        for i in range(0,9,3):
            print("|".join(agent_grid[i:i+3]))
        print()

class ReflexAgent:
    def __init__(self):
        self.position=0
    def act(self,percept,environment):
        if percept=="Hot":
            environment.Open_fan(self.position)
            return"It Hot"
        else:
            return"IT COOL"
    def move(self):
        if self.position<8:
            self.position+=1

def agent_run(agent,enviromnet,steps):
    for step in range(1,steps+1):
        position=agent.position
        percept=enviromnet.get_percept(position)
        action=agent.act(percept,enviromnet)
        print("="*50)
        print("Step",step)
        print("Percept:",percept)
        print("Action:",action)

        enviromnet.display_grid(agent.position)

        if step<steps:
            agent.move()

e1=Environment()
a1=ReflexAgent()

agent_run(a1,e1,9)

import random

class Environment:
    def __init__(self):
        self.system=[ "Web Server", "Application Server", "Database Server", 
                     "File Server", "Authentication Server","Backup Server"]
        self.status={}
        for system in self.system:
            self.status[system]=random.choice(["Online","Offline","Under Maintenance"])
    def get_percept(self,system):
         return self.status[system]
    
    def display_status(self):
        print("\n-----Initial Status-----")
        for system in self.system:
             print("Sytem:",system ,"| Status:",self.status[system])
    def change_status(self,system):
        self.status[system]=random.choice(["Online","Offline","Under Maintenance"])
    
class ModelAgent:
    def __init__(self):
        self.model={}
    def update_model(self,precept,system):
        self.model[system]=precept
    def act(self,system,precept):
            current=precept
            previous_status=self.model.get(system)
            if previous_status=="Online" and current=="Offline":
                 action="System Failuer"
            elif previous_status=="Offline":
                 action="Warning"
            elif previous_status=="Online":
                 action="Success"
            else:
                action="Under Maintenance"

            self.update_model(current,system)
            return action
                            
            
def run_agent(agent,enviroment):
    for system in enviroment.system:
         percept=enviroment.get_percept(system)
         action=agent.act(system,percept)
         print("System:", system)
         print("Status:", percept)
         print("Action:", action)
         print()


e1=Environment()
m1=ModelAgent()
run_agent(m1,e1)

print("\n" + "=" * 60)
print("FINAL SYSTEM CHECK")
print("=" * 60)

e1.display_status()

print("\nFinal Internal Model:")
for system, status in m1.model.items():
    print("System:", system, "| Status:", status)

online = 0
offline = 0
maintenance = 0

for status in e1.status.values():
    if status == "Online":
        online += 1
    elif status == "Offline":
        offline += 1
    else:
        maintenance += 1

print("\nSystem Summary:")
print("Online:", online)
print("Offline:", offline)
print("Under Maintenance:", maintenance)
print("=" * 60)

