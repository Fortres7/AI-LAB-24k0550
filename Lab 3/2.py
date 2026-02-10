import random

class Environment:
    def __init__(self, students_present='No', light_status='OFF'):
        self.students_present = students_present
        self.light_status = light_status

    def get_percept(self):
        return {
            'students_present': self.students_present,
            'light_status': self.light_status
        }
    
    def turn_light_on(self):
        if self.light_status == 'OFF':
            self.light_status = 'ON'

    def turn_light_off(self):
        if self.light_status == 'ON':
            self.light_status = 'OFF'

    def random_update_students(self):
        self.students_present = random.choice(['Yes', 'No'])

class ModelBasedAgent:
    def __init__(self):
        self.model = {
            'students_present': 'No',
            'light_status': 'OFF'
        }

    def act(self, percept):
        self.model.update(percept)

        if self.model['students_present'] == 'Yes' and self.model['light_status'] == 'OFF':
            return 'Turn lights ON'
        elif self.model['students_present'] == 'No' and self.model['light_status'] == 'ON':
            return 'Turn lights OFF'
        else:
            return 'No action'

def run_agent(agent, environment, steps):
    for step in range(steps):
        environment.random_update_students()
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        if action == 'Turn lights ON':
            environment.turn_light_on()
        elif action == 'Turn lights OFF':
            environment.turn_light_off()

agent = ModelBasedAgent()
environment = Environment(students_present='No', light_status='OFF')
run_agent(agent, environment, 8)
