import random

class Monster:
    """A fightable monster."""
    
    def __init__(self):
        self.difficulty = int(random.uniform(1, 10))
        
    def __str__(self):
        return "Monster with difficulty {0}".format(self.difficulty)