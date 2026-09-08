import random
class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}
        self.actions = actions
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def get_Q_value(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions,key=lambda action: self.get_Q_value(state, action))

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state, action)
        best_future_Q = max(
            self.get_Q_value(next_state, action)
            for action in self.actions
        )
        new_Q = old_Q + self.alpha * (
            reward + self.gamma * best_future_Q - old_Q
        )
        self.Q[(state, action)] = new_Q
    def act(self, state):
        return self.select_action(state)

class Environment:
    def __init__(self):
        self.grid=[
            ["S", ".", ".", "X", "."],
            [".", "X", ".", "X", "."],
            [".", ".", ".", ".", "."],
            ["X", ".", "X", ".", "."],
            [".", ".", ".", ".", "G"]
        ]
        self.start=(0, 0)
        self.goal=(4, 4)
        self.position=self.start
        self.obstacles=[
            (0, 3),
            (1, 1),
            (1, 3),
            (3, 0),
            (3, 2)
        ]
        self.dangerous=[
            (2, 1),
            (2, 3)
        ]
    def get_percept(self):
        return self.position
    def reset(self):
        self.position=self.start
    def step(self, action):

        row=self.position[0]
        col=self.position[1]
        if action=="Up":
            new_position=(row-1, col)
        elif action=="Down":
            new_position=(row+1, col)
        elif action=="Left":
            new_position=(row, col-1)
        else:
            new_position=(row, col+1)

        if new_position[0]<0 or new_position[0]>=5 or new_position[1]<0 or new_position[1]>=5:
            return self.position, -10, False

        if new_position in self.obstacles:
            return self.position, -20, False

        self.position=new_position

        if self.position==self.goal:
            return self.position, 100, True

        if self.position in self.dangerous:
            return self.position, -30, False

        return self.position, -1, False

    def display_grid(self):
        print("\nDisaster Area Grid:")
        for row in self.grid:
            print(" ".join(row))

def run_agent(agent, environment, episodes, max_steps):
    for episode in range(episodes):
        environment.reset()
        total_reward=0
        for step in range(max_steps):
            state=environment.get_percept()
            action=agent.act(state)
            next_state,reward,done=environment.step(action)
            agent.learn(
                state,
                action,
                reward,
                next_state
            )
            total_reward=total_reward+reward
            if done:
                break
        if episode==0 or episode==9 or episode==49 or episode==99:
            print(
                "Episode",
                episode+1,
                "Reward:",
                total_reward,
                "Steps:",
                step+1
            )

agent=LearningBasedAgent(
    ["Up","Down","Left","Right"]
)

environment=Environment()
environment.display_grid()
print("\nStarting Training...")
run_agent(agent, environment, 100, 50)

print("\n--- Learned Q-Values ---")
for (state, action), q_value in agent.Q.items():
    print(
        "State =",
        state,
        "Action =",
        action,
        "Q-value =",
        round(q_value, 2)
    )

print("\n--- Testing Trained Agent ---")
agent.epsilon=0
environment.reset()
current_state=environment.get_percept()
path=[current_state]
total_reward=0
steps=0

while current_state!=environment.goal and steps<50:
    action=agent.act(current_state)
    next_state,reward,done=environment.step(action)
    print("Step", steps + 1, "State:", current_state, "Action:", action, "Next State:", next_state, "Reward:", reward)
    path.append(next_state)

    total_reward=total_reward+reward
    steps=steps+1
    current_state=next_state
    if done:
        break

print("\n--- Final Result ---")
print("Learned Path:")
for position in path:
    print(position, end="")
    if position!=path[-1]:
        print(" -> ", end="")
print("Total Steps:", steps)
print("Total Reward:", total_reward)

if environment.position==environment.goal:
    print("Emergency Supplies Delivered Successfully!")
else:
    print("Delivery Failed")