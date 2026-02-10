class Environment:
    def __init__(self):
        self.grid = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def has_fire(self, room):
        return self.grid[room] == 'fire'

    def extinguish(self, room):
        self.grid[room] = 'safe'

    def display(self):
        order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        for i in range(0, 9, 3):
            row = order[i:i+3]
            line = []
            for r in row:
                if self.grid[r] == 'fire':
                    line.append('@')
                else:
                    line.append(' ')
            print(line)
        print()

class FirefightingRobot:
    def __init__(self, path):
        self.path = path

    def run(self, environment):
        for room in self.path:
            print(f"Robot moved to room {room}")
            if environment.has_fire(room):
                print(f"Fire detected in room {room}. Extinguishing it")
                environment.extinguish(room)
            else:
                print(f"No fire in room {room}.")
            environment.display()

print("@ - Represents Fire\n\n")
environment = Environment()
robot = FirefightingRobot(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j'])
robot.run(environment)
print("Final Room Status:")
environment.display()
