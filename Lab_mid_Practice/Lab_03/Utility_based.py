class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state
    
    def clean_room(self):
        self.state = 'Clean'


class UtilityBasedAgent:
    def __init__(self):
        self.dirty_utility=-10
        self.clean_utility=10

    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'No action needed'
    def calculate_utility(self, percept):
        if percept == 'Dirty':
            return self.dirty_utility
        else:
            return self.clean_utility


def run_agent(agent, environment, steps):
    total_utility = 0
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        utility = agent.calculate_utility(percept)
        print("Step:", step)
        print("Percept:", percept)
        print("Action:", action)
        print("Utility:", utility)
        print()

        total_utility += utility
        if percept == 'Dirty':
            environment.clean_room()
    print("Total Utility:", total_utility)


agent = UtilityBasedAgent()
environment = Environment()
run_agent(agent, environment, 5)



class Environment:
    def __init__(self, movies):
        self.movies = movies
    def get_percept(self):
        return self.movies
# Utility-Based Agent Class
class UtilityBasedAgent:
    def __init__(self, mood_factor):
        self.mood_factor = mood_factor
    def utility(self, review):
        return review * self.mood_factor
    def act(self, percept):
        best_movie = None
        highest_utility = float('-inf')

        for movie, review in percept.items():
            current_utility = self.utility(review)
            print(
                f"{movie}: Review = {review}, "
                f"Utility = {current_utility:.2f}"
            )
            highest_utility=max(current_utility,highest_utility)
            best_movie = movie
        return best_movie, highest_utility
    
# Simulation Function
def run_agent(agent, environment):
    percept = environment.get_percept()
    selected_movie, utility_value = agent.act(percept)
    print("\n--- Agent Decision ---")
    print("Selected Movie:", selected_movie)
    print("Highest Utility:", f"{utility_value:.2f}")



environment = Environment({
    "Movie A": 7,
    "Movie B": 9,
    "Movie C": 5
})
agent = UtilityBasedAgent(mood_factor=0.8)
run_agent(agent, environment)

class Environment:
    def __init__(self,resturants):
        self.resturants=resturants
    def get_percept(self):
        return self.resturants
class UtilityAgent:
    def __init__(self,budget_factor):
        self.budget_factor=budget_factor
    def utility(self,rating):
        return  rating*self.budget_factor
    
    def act(self,percept):
        selected_resturant=None
        highest_utility=0
        for name,rating in percept.items():
            current_utility=self.utility(rating)
            print("Name:",name)
            print("Rating:",rating) 
            print("Utility:",current_utility)
            if current_utility > highest_utility:
                highest_utility = current_utility
                selected_resturant = name
        return highest_utility,selected_resturant
    
def run_agen(agent,environment):
    percept=environment.get_percept()
    highest_utility,selected_name=agent.act(percept)
    print("\n--- Agent Decision ---")
    print("Selected Movie:", selected_name)
    print("Highest Utility:", highest_utility)

environment = Environment({
    "Restaurant A": 8,
    "Restaurant B": 6,
    "Restaurant C": 9
})

agent = UtilityAgent(0.8)

run_agen(agent, environment)

class Environment:
    def __init__(self,option):
        self.option=option
    def get_percept(self):
        return self.option

class UtilityAgent:
    def __init__(self,performance_factor):
        self.performance_factor=performance_factor
    def utility(self,rating):
        return self.performance_factor*rating

    def act(self,percept):
        selected_option=None
        highest_rating=0
        for name,rating in percept.items():
            current=self.utility(rating)
            print("Name:",name)
            print("Rating:",rating)
            if(highest_rating<current):
                highest_rating=current
                selected_option=name
        return highest_rating,selected_option
def run_agent(agent,environment):
    percept=environment.get_percept()
    h,s=agent.act(percept)
    print("Selected Option:",s)
    print("Highest Rating:",h)

e1=Environment({"Laptop A": 8,
"Laptop B":  6,
"Laptop C" : 9,
"Laptop D ": 7})
a1=UtilityAgent(0.9)
run_agent(a1,e1)