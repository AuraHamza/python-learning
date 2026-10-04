class Environment:
    def __init__(self,initial_state="Dirty"):
        self.initial_state=initial_state
    def get_percept(self):
        return self.initial_state
    def clean_room(self):
        self.initial_state="Clean"

class ModelAgent:
    def __init__(self):
        self.model={"current":"Unknown",
                    "previous":"Unknown"}
    def update_model(self,percept):
        self.model["previous"]=self.model["current"]
        self.model["current"]=percept
        print("Internal Model:",self.model)
    def act(self,percept,environment):
         self.update_model(percept)
         if self.model["current"]=="Dirty":
             environment.clean_room()
             return"Clean the Room"
         else:
             return"Room is clean"

def run_agent(agent,environment,steps):
    for step in range(1,steps+1):
        percept=environment.get_percept()
        action=agent.act(percept,environment)
        
        print("Step:",step)
        print("percept:",percept)
        print("Action:",action)
        print("_"*10)

e1=Environment()
m1=ModelAgent()
run_agent(m1,e1,5)

class Environment:
    def __init__(self,is_raining="yes",window_open="yes"):
        self.is_raining=is_raining
        self.window_open=window_open
    def get_percept(self):
        return {"is_raining":self.is_raining,
                "window_open":self.window_open}
    def close_window(self):
        self.window_open="no"

class ModelAgent():
    def __init__(self):
        self.model={"current":"Unknown",
                    "previous":"Unknown"}
    def update_model(self,percept):
        self.model["previous"]=self.model["current"]
        self.model["current"]=percept
    def act(self,percept,environment):
        self.update_model(percept)
        if (self.model["current"]["is_raining"]=="yes" and self.model["current"]["window_open"]=="yes"):
            environment.close_window()
            return "Close the window"
        else:
            return "No action needed"
def run_agent(agent,environment,steps):
    for step in range(1,steps+1):
        percept=environment.get_percept()
        action=agent.act(percept,environment)
        print("\n" + "=" * 50)
        print(f"Step: {step}")
        print(f"Percept: {percept}")
        print(f"Action: {action}")
        print(f"Internal Model: {agent.model}")
        print("=" * 50)

e1=Environment()
a1=ModelAgent()
run_agent(a1,e1,5)