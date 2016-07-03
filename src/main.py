import random
from src import monster

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self):
        self.floor_number = 1
    
    def run(self):
        self.print_instructions()
        
        num_monsters = int(random.uniform(3, 5))
        monsters = []
        for i in range(0, num_monsters):
            m = monster.Monster()
            monsters.append(m)
            
        print "You see {0} monsters:".format(len(monsters))
        
        for m in monsters:
            print m
            
    def print_instructions(self):
        print "Welcome to Legendary Tribble!"
        print ""
        
        print "Instructions: type 'fight <name>' to fight a monster."
        print "Kill all the monsters, then, type 'descend' to go to the next floor"
        print "If you want to go back up one floor, type 'ascend'."
        print ""
        
        print "You are on floor B{0}.".format(self.floor_number)
        print ""
    