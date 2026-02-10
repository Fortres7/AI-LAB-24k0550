class Environment:
    def __init__(self, restaurants=None):
        if restaurants is None:
            restaurants = {
                'A': {'distance': 3, 'rating': 7},
                'B': {'distance': 5, 'rating': 9}
            }
        self.restaurants = restaurants

    def get_percept(self):
        return self.restaurants

class UtilityBasedAgent:
    def utility(self, rating, distance):
        return rating - distance

    def act(self, percept):
        best_restaurant = None
        best_utility = -float('inf')

        for name, data in percept.items():
            u = self.utility(data['rating'], data['distance'])
            print(f"Restaurant {name} Utility = {u}")
            if u > best_utility:
                best_utility = u
                best_restaurant = name

        return best_restaurant

def run_agent(agent, environment):
    percept = environment.get_percept()
    selected = agent.act(percept)
    print()
    print(f"Selected Restaurant: {selected}")

agent = UtilityBasedAgent()
environment = Environment({
    'A': {'distance': 3, 'rating': 7},
    'B': {'distance': 5, 'rating': 9}
})
run_agent(agent, environment)
