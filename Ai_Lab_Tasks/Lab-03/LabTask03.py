class GoalBasedAgent:
    def __init__(self,goal):
        self.goal=goal

    def act(self,percept):
        current=percept["current"]
        available=percept["available"]

        if current==self.goal:
            return "Deliver Emergency Supplies"

        if self.goal in available:
            return self.goal

        return available[0]


class Environment:
    def __init__(self):
        self.locations=[
            "Base Station",
            "Medical Camp",
            "Supply Station",
            "Hospital",
            "Warehouse",
            "Command Center",
            "Emergency Center",
            "Relief Center"
        ]

        self.map={
            "Base Station":["Medical Camp","Supply Station"],
            "Medical Camp":["Base Station","Hospital","Relief Center"],
            "Supply Station":["Base Station","Warehouse"],
            "Hospital":["Medical Camp","Command Center"],
            "Warehouse":["Supply Station","Emergency Center"],
            "Command Center":["Hospital","Relief Center"],
            "Emergency Center":["Warehouse","Relief Center"],
            "Relief Center":["Medical Camp","Command Center","Emergency Center"]
        }

        self.unavailable_paths=[
            ("Base Station","Supply Station"),
            ("Supply Station","Base Station"),
            ("Hospital","Command Center"),
            ("Command Center","Hospital")
        ]

        self.current_location="Base Station"
        self.goal="Relief Center"
        self.route=["Base Station"]

    def get_percept(self):
        available=[]

        for location in self.map[self.current_location]:
            if (self.current_location,location) not in self.unavailable_paths:
                available.append(location)

        return {
            "current":self.current_location,
            "available":available
        }

    def move(self,location):
        self.current_location=location
        self.route.append(location)

    def display_map(self):
        print("\nInitial UAV Setup:")
        print("Starting Location:",self.current_location)
        print("Destination:",self.goal)
        print("Unavailable Flight Paths:")

        for path in self.unavailable_paths:
            print(path[0],"->",path[1])


def run_agent(agent,environment):
    print("\nUAV Monitoring and Navigation")

    while environment.current_location!=environment.goal:

        percept=environment.get_percept()

        print("\nCurrent Location:",percept["current"])
        print("Available Flight Paths:",percept["available"])

        action=agent.act(percept)

        print("Action:",action)

        environment.move(action)

    print("\nCurrent Location:",environment.current_location)
    print("Action: Deliver Emergency Supplies")
    print("Success - Emergency supplies delivered successfully!")

    print("\nFinal Result:")
    print("Complete Route:")

    for location in environment.route:
        print(location,end="")

        if location!=environment.route[-1]:
            print(" -> ",end="")

    print("\nTotal Locations Visited:",len(environment.route))
    print("Emergency Supplies Delivered: Yes")


agent=GoalBasedAgent("Relief Center")

environment=Environment()

environment.display_map()

run_agent(agent,environment)