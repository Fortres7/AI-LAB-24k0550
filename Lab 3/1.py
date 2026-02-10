class Environment:
    def __init__(self, traffic_level='Light'):
        self.traffic_level = traffic_level

    def get_percept(self):
        return self.traffic_level

class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Heavy Traffic':
            return 'Extend Green Time'
        else:
            return 'Normal Green'

def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} --> Action: {action}")

agent = SimpleReflexAgent()
environment = Environment(traffic_level='Heavy Traffic')
run_agent(agent, environment)

environment = Environment(traffic_level='Light Traffic')
run_agent(agent, environment)
