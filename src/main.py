import random
import sys
from src import monster

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self):
        self.floor_number = 1
    
    def run(self):
        # Hash of input command + callback function
        self.commands = { 'quit': self.quit }
        
        self.print_instructions()
        self.generate_floor()
        self.input_loop()

    # private            
    def print_instructions(self):
        print "Welcome to Legendary Tribble!"
        print ""
        
        print "Instructions: type 'fight <name>' to fight a monster."
        print "Kill all the monsters, then, type 'descend' to go to the next floor"
        print "If you want to go back up one floor, type 'ascend'."
        print ""
        
        print "You are on floor B{0}.".format(self.floor_number)
        print ""
    
    # private 
    def input_loop(self):
        is_battling = True
        while is_battling:
            print "You see {0} monsters:".format(len(self.monsters))
            
            for m in self.monsters:
                print m
                
            input = raw_input("> ").lower()
            
            if input in self.commands:
                self.commands[input]()
            else:
                print "{0} isn't a valid command, try one of: {1}".format(input, self.commands.keys())
            
            
    # private
    def generate_floor(self):
        
        num_monsters = self.floor_number + int(random.uniform(3, 5))
        self.monsters = []
        for i in range(0, num_monsters):
            m = monster.Monster()
            self.monsters.append(m)
            
    # private
    def quit(self):
        print "Bye!"
        sys.exit()