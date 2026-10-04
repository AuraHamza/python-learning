# Goal-Based Agent Class
class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'

class GoalBasedAgent:
    def __init__(self):
        self.goal = 'No action needed'

    def formulate_goal(self, percept):
        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        self.formulate_goal(percept)
        if self.goal == 'Clean':
            return 'Clean the room'
        else:
            return 'Room is clean'
# Simulation Function
def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}")
        print("Percept :", percept)
        print("Goal    :", agent.goal)
        print("Action  :", action)
        if action == 'Clean the room':
            environment.clean_room()

        print("Room State :", environment.state)
        print("-" * 50)


# Main Program
agent = GoalBasedAgent()
environment = Environment()
run_agent(agent, environment, 5)

class Environment:
    def __init__(self,level):
        self.level=level
    def get_percept(self):
        return self.level
    def fill_tank(self):
         self.level="Normal"
         return self.level
    def drain_tank(self):
        self.level="Normal"
        return self.level

class GoalAgent:
    def __init__(self):
        self.goal="No action"
    def update_goal(self,percept):
        if percept=="Low":
            self.goal="Fill the tank"
        elif percept=="Full":
            self.goal="drain the tank"
        else:
            self.goal="No action"
        return self.goal
    
    def act(self,percept,environment):
        self.update_goal(percept)
        if self.goal=="Fill the tank":
            action=environment.fill_tank()
        elif self.goal=="drain the tank":
           action=environment.drain_tank()
        else:
             action="No action"
        return action
    
def run_agent(agent,environment,steps):
    for step in range(1,steps+1):
        percept=environment.get_percept()
        action=agent.act(percept,environment)
        print("="*50)
        print("Step",step)
        print("Percept:",percept)
        print("Tank State:", environment.level)
        print("Action:",action)

agent = GoalAgent()
environment = Environment('Low')
run_agent(agent, environment, 5)