import random

class Environment:
    def __init__(self):
        self.servers=["S1","S2","S3","S4","S5","S6","S7","S8"]
        self.status={}
        self.action={}

        for server in self.servers:
            self.status[server]=random.choice(["Healthy","OverLoaded"])

    def get_percept(self,server):
        return self.status[server]

    def display_status(self):
        print("\nInitial Servers Status:")
        for server in self.servers:
            print(server,":",self.status[server])

    def get_final_report(self):
        print("\nFinal report: ")
        for server in self.servers:
            print("Server:",server)
            print("Percept:",self.status[server])
            print("Action:",self.action[server])
        healthy=0
        overloaded=0
        for server in self.servers:
            if self.status[server]=="Healthy":
                healthy+=1
            else:
                overloaded+=1
        print("\nTotal Healthy Servers:",healthy)
        print("Total Overloaded Servers:",overloaded)

class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == "Healthy":
            return "Success - Server operating normally"
        else:
            return "Alert - Recommend Load Reduction"

def run_agent(agent,environment):
    print("\nMonitoring")
    for server in environment.servers:
        percept=environment.get_percept(server)
        action=agent.act(percept)
        environment.action[server]=action
        
        print("Checking Server:", server)
        print("Percept:", percept)
        print("Action:", action)


environment = Environment()
agent = SimpleReflexAgent()

environment.display_status()

run_agent(agent, environment)

environment.get_final_report()