class UtilityBasedAgent:
    def __init__(self):
        self.distance_weight=0.25
        self.time_weight=0.20
        self.battery_weight=0.20
        self.weather_weight=0.15
        self.safety_weight=0.20

    def calculate_utility(self,route):
        if route["weather"]=="Good":
            weather_score=10
        elif route["weather"]=="Moderate":
            weather_score=5
        else:
            weather_score=1

        if route["safety"]=="High":
            safety_score=10
        elif route["safety"]=="Medium":
            safety_score=5
        else:
            safety_score=1

        distance_score=10/route["distance"]
        time_score=10/route["time"]
        battery_score=10/route["battery"]

        utility=(
            distance_score*self.distance_weight+
            time_score*self.time_weight+
            battery_score*self.battery_weight+
            weather_score*self.weather_weight+
            safety_score*self.safety_weight
        )

        return utility

    def act(self,routes):
        best_route=None
        highest_utility=-1

        print("\nRoute Utility Calculation:")

        for route in routes:
            utility=self.calculate_utility(route)
            route["utility"]=utility
            print(route["name"],":",round(utility,2))

            if utility>highest_utility:
                highest_utility=utility
                best_route=route

        return best_route


class Environment:
    def __init__(self):
        self.routes=[
            {
                "name":"Route 1",
                "locations":["Distribution Center","Checkpoint A","Customer Location"],
                "distance":10,
                "time":15,
                "battery":20,
                "weather":"Good",
                "safety":"High"
            },
            {
                "name":"Route 2",
                "locations":["Distribution Center","Checkpoint B","Checkpoint C","Customer Location"],
                "distance":8,
                "time":12,
                "battery":30,
                "weather":"Moderate",
                "safety":"Medium"
            },
            {
                "name":"Route 3",
                "locations":["Distribution Center","Checkpoint D","Checkpoint E","Customer Location"],
                "distance":12,
                "time":18,
                "battery":18,
                "weather":"Good",
                "safety":"High"
            },
            {
                "name":"Route 4",
                "locations":["Distribution Center","Checkpoint F","Customer Location"],
                "distance":7,
                "time":10,
                "battery":35,
                "weather":"Poor",
                "safety":"Low"
            }
        ]
        self.start="Distribution Center"
        self.destination="Customer Location"

    def get_percept(self):
        return self.routes

    def display_routes(self):
        print("\nAvailable Flight Routes:")

        for route in self.routes:
            print("\nRoute:",route["name"])
            print("Distance:",route["distance"],"km")
            print("Estimated Flight Time:",route["time"],"minutes")
            print("Battery Consumption:",route["battery"],"%")
            print("Weather:",route["weather"])
            print("Safety Level:",route["safety"])


def run_agent(agent,environment):
    percept=environment.get_percept()
    selected_route=agent.act(percept)
    print("\nSelected Route:",selected_route["name"])
    print("\nUAV Delivery:")
    for location in selected_route["locations"]:
        print("UAV visited:",location)
    print("\nPackage delivered successfully!")
    print("\nFinal Report:")
    for route in environment.routes:
        print(
            route["name"],
            "-> Utility:",
            round(route["utility"],2)
        )
    print("\nSelected Route:",selected_route["name"])
    print("Total Distance:",selected_route["distance"],"km")
    print("Estimated Flight Time:",selected_route["time"],"minutes")
    print("Delivery Status: Successfully Delivered")


agent=UtilityBasedAgent()
environment=Environment()
environment.display_routes()
run_agent(agent,environment)