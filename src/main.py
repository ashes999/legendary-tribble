import random
from src import monster

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self):
        pass
    
    def run(self):
        print "Welcome to Legendary Tribble!"
        
        num_monsters = int(random.uniform(3, 5))
        monsters = []
        for i in range(0, num_monsters):
            m = monster.Monster()
            monsters.append(m)
            
        print "You see {0} monsters:".format(len(monsters))
        
        for m in monsters:
            print m