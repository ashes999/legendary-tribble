import random
import sys

from tribble.battle import Battle
from tribble.monster import Monster
from tribble.player import Player

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self):
        self.player = Player()
        self.floor_number = 1
    
    def run(self):
        # Hash of input command + callback function
        self.commands = { 'quit': self.quit, 'fight': self.fight }
        
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
            print "Health: {0}/{1}".format(self.player.current_health, self.player.total_health)
            
            for m in self.monsters:
                print m
                
            input = raw_input("> ").lower()
            
            space = input.find(' ')
            if (space == -1):
                space = len(input)
            command_name = input[0:space]
            arguments = input[space:].strip()
            
            if command_name in self.commands:
                self.commands[command_name](arguments)
            else:
                print "{0} isn't a valid command, try one of: {1}".format(input, self.commands.keys())
            
            
    # private
    def generate_floor(self):
        
        num_monsters = self.floor_number + int(random.uniform(3, 5))
        self.monsters = []
        for i in range(0, num_monsters):
            m = Monster()
            self.monsters.append(m)
            
    # private
    def quit(self, arguments):
        print "Bye!"
        sys.exit()
        
    # private
    def fight(self, arguments):
        target_name = arguments
        targets = [m for m in self.monsters if m.name.lower() == target_name]
        if len(targets) == 0:
            print "There doesn't seem to be any '{0}' here to fight".format(target_name)
            return
        else:
            target = targets[0] # fight the first such monster
            is_victory = Battle(self.player, target).fight_it_out()
        
        if is_victory == True:
            print "Victory! You vanquished your foe!"
            self.monsters.remove(target)
        else:
            print "You slink back, defeated."