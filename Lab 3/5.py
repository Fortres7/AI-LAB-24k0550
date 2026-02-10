import random

class Environment:
    def get_reward(self, action):
        if action == 'Play':
            return 5
        else:
            return 1

class LearningBasedAgent:
    def __init__(self, actions, alpha=0.5):
        self.actions = actions
        self.alpha = alpha
        self.q_table = {action: 0 for action in actions}

    def act(self):
        return random.choice(self.actions)

    def learn(self, action, reward):
        old_q = self.q_table[action]
        new_q = old_q + self.alpha * (reward - old_q)
        self.q_table[action] = new_q
        return old_q, new_q

def run_agent(agent, environment, steps):
    for step in range(steps):
        action = agent.act()
        reward = environment.get_reward(action)
        old_q, new_q = agent.learn(action, reward)
        print(f"Step {step + 1}: Action {action} Reward {reward}")
        print(f"Q-value Old = {old_q}, New = {new_q}")

agent = LearningBasedAgent(['Play', 'Rest'])
environment = Environment()
run_agent(agent, environment, 10)
