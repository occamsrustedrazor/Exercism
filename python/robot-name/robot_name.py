import random
from string import ascii_uppercase

class Robot:
    def __init__(self):
        self.name = self.generate()
    def reset(self):
        self.name = self.generate()
    def generate(self):
        name = ""
        for _ in range(0,2):
            name += random.choice(ascii_uppercase)
        for _ in range(0,3):
            name += str(random.randint(0,9))
        return name