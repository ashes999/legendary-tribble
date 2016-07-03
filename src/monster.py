import random

class Monster:
    """A fightable monster."""
    
    def __init__(self):
        
        self.difficulty = int(random.uniform(1, 10))
        
        if self.difficulty <= 3:
            self.name = "rat"
            self.current_health = self.total_health = 10
            self.strength = 3
            self.defense = 1
            self.agility = 5
        elif self.difficulty <= 7:
            self.name = "goblin"
            self.current_health = self.total_health = 20
            self.strength = 5
            self.defense = 1
            self.agility = 3
        else:
            self.name = "ogre"
            self.current_health = self.total_health = 40
            self.strength = 6
            self.defense = 6
            self.agility = 1
        
    def __str__(self):
        return "A {0}".format(self.name)