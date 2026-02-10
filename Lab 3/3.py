class GoalBasedAgent:
    def __init__(self):
        self.goal = 'Complete all subjects'
        self.subjects = ['AI', 'Math', 'Physics']
        self.completed = []

    def act(self):
        if len(self.completed) < len(self.subjects):
            subject = self.subjects[len(self.completed)]
            self.completed.append(subject)
            return f"Studying {subject}"
        else:
            return "Goal Achieved: All subjects completed"

class Environment:
    def __init__(self):
        self.done = False

def run_agent(agent, environment):
    while not environment.done:
        action = agent.act()
        print(action)
        if action == "Goal Achieved: All subjects completed":
            environment.done = True

agent = GoalBasedAgent()
environment = Environment()
run_agent(agent, environment)
