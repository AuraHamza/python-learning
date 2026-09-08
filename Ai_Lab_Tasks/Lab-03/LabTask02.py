import random

class Environment:
    def __init__(self):
        self.systems=["Web Server","Application Server","Database Server","File Server","Authentication Server","Backup Server"]
        self.status={}

        for system in self.systems:
            self.status[system]=random.choice(["Online","Offline","Under Maintenance"])

    def get_percept(self,system):
        return self.status[system]

    def change_status(self,system,status):
        self.status[system]=status

    def display_status(self):
        print("\nInitial Systems Status:")
        for system in self.systems:
            print(system,":",self.status[system])

    def get_final_report(self,agent):
        print("\nFinal System Check:")
        for system in self.systems:
            print("System:",system)
            print("Status:",self.status[system])

        print("\nFinal Internal Model:")
        for system in agent.model:
            print(system,":",agent.model[system])
            
        online=0
        offline=0
        maintenance=0
        for system in self.systems:
            if self.status[system]=="Online":
                online+=1
            elif self.status[system]=="Offline":
                offline+=1
            else:
                maintenance+=1
        print("\nTotal Online Systems:",online)
        print("Total Offline Systems:",offline)
        print("Total Under Maintenance:",maintenance)


class ModelBasedAgent:
    def __init__(self):
        self.model={}

    def update_model(self,system,percept):
        self.model[system]=percept

    def act(self,system,percept):
        previous=self.model.get(system)

        if previous=="Online" and percept=="Offline":
            action="System Failure Alert"
        elif percept=="Offline":
            action="Warning,System requires attention"
        elif percept=="Online":
            action="Success,System operating normally"
        else:
            action="System is under maintenance"
        self.update_model(system,percept)
        return action


def run_agent(agent,environment):
    print("\nSystem Monitoring")
    
    for system in environment.systems:
        percept=environment.get_percept(system)
        action=agent.act(system,percept)

        print("Checking System:",system)
        print("Percept:",percept)
        print("Action:",action)


environment = Environment()
agent = ModelBasedAgent()

environment.display_status()
run_agent(agent,environment)
print("\nSimulating Status Changes")
environment.change_status("Web Server","Offline")
environment.change_status("Database Server","Offline")

run_agent(agent,environment)
environment.get_final_report(agent)