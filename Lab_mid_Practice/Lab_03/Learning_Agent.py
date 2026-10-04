import random
class Environment:
    def __init__(self):
        self.state = "Dirty"

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = "Clean"
        return 10


class LearningAgent:
    def __init__(self):
        self.actions = ["Clean the room", "No action needed"]
        self.Q = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def act(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        return max(self.actions, key=lambda a: self.Q.get((state, a), 0))

    def learn(self, state, action, reward, next_state):
        old_Q = self.Q.get((state, action), 0)

        future_Q = max(self.Q.get((next_state, a), 0)
                       for a in self.actions)

        self.Q[(state, action)] = old_Q + self.alpha * (
            reward + self.gamma * future_Q - old_Q
        )


def run_agent(agent, environment, steps):
    for step in range(steps):
        state = environment.get_percept()
        action = agent.act(state)

        if state == "Dirty" and action == "Clean the room":
            reward = environment.clean_room()
        else:
            reward = 0

        next_state = environment.get_percept()
        agent.learn(state, action, reward, next_state)

        print("Step:", step + 1)
        print("State:", state)
        print("Action:", action)
        print("Reward:", reward)
        print()


agent = LearningAgent()
environment = Environment()

run_agent(agent, environment, 5)

print("--- Q-Table ---")
for key, value in agent.Q.items():
    print(key, ":", round(value, 2))




import random

class Environment:
    def __init__(self):
        self.start = (0, 0)
        self.goal = (2, 2)
        self.obstacles = [(1, 1)]
        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state

    def get_percept(self):
        return self.state

    def move(self, action):
        r, c = self.state

        if action == "Up":
            r -= 1
        elif action == "Down":
            r += 1
        elif action == "Left":
            c -= 1
        elif action == "Right":
            c += 1

        if r < 0 or r > 2 or c < 0 or c > 2:
            return self.state, -10

        new_state = (r, c)

        if new_state in self.obstacles:
            return self.state, -10

        self.state = new_state

        if self.state == self.goal:
            return self.state, 100

        return self.state, -1


class LearningAgent:
    def __init__(self):
        self.actions = ["Up", "Down", "Left", "Right"]
        self.Q = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_Q(self, state, action):
        return self.Q.get((state, action), 0)

    def act(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        return max(self.actions,
                   key=lambda a: self.get_Q(state, a))

    def learn(self, state, action, reward, next_state):
        old = self.get_Q(state, action)

        future = max(self.get_Q(next_state, a)
                     for a in self.actions)

        self.Q[(state, action)] = old + self.alpha * (
            reward + self.gamma * future - old
        )


def run_agent(agent, environment, episodes):
    for episode in range(episodes):
        state = environment.reset()
        total_reward = 0

        for step in range(20):
            action = agent.act(state)
            next_state, reward = environment.move(action)

            agent.learn(state, action, reward, next_state)

            state = next_state
            total_reward += reward

            if state == environment.goal:
                break

        if (episode + 1) % 10 == 0:
            print("Episode:", episode + 1,
                  "Reward:", total_reward)


environment = Environment()
agent = LearningAgent()

run_agent(agent, environment, 100)

print("\n--- Learned Q-Values ---")
for key, value in agent.Q.items():
    print(key, "=", round(value, 2))

print("\n--- Testing ---")
state = environment.reset()
path = [state]

agent.epsilon = 0

for step in range(20):
    action = agent.act(state)
    state, reward = environment.move(action)
    path.append(state)

    print("Action:", action, "| Position:", state)

    if state == environment.goal:
        break

print("Final Path:", path)
if state == environment.goal:
    print("UAV reached the destination")
else:
    print("UAV did not reach the destination")
