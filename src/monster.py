import random

class Monster:
    """A fightable monster."""
    
    def __init__(self):
        self.difficulty = int(random.uniform(1, 10))
        if self.difficulty <= 3:
            self.name = "rat"
        elif self.difficulty <= 7:
            self.name = "goblin"
        else:
            self.name = "ogre"
        
    def __str__(self):
        return "A {0}".format(self.name)