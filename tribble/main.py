import random
import sys
import time

from tribble.battle import Battle
from tribble.monster import Monster
from tribble.player import Player

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self, print_function = None, delay_function = time.sleep):
        self.player = Player()
        self.floor_number = 1        
        # Hash of input command + callback function
        self.commands = { 'quit': self.quit, 'fight': self.fight }
        self.monsters = []
        self.print_function = print_function
        self.delay_function = delay_function
    
    def run(self):
        self.print_instructions()
        self.generate_floor()
        self.input_loop()

    # private            
    def print_instructions(self):
        self.write("Welcome to Legendary Tribble!")
        self.write("")
        
        self.write("Instructions: type 'fight <name>' to fight a monster.")
        self.write("Kill all the monsters, then, type 'descend' to go to the next floor")
        self.write("If you want to go back up one floor, type 'ascend'.")
        self.write("")
        
        self.write("You are on floor B{0}.".format(self.floor_number))
        self.write("")
    
    # private 
    def input_loop(self):
        while True:            
            self.write("You see {0} monsters:".format(len(self.monsters)))
            self.write("Health: {0}/{1}".format(self.player.current_health, self.player.total_health))
            
            for m in self.monsters:
                self.write(m)
                
            input = raw_input("> ").lower()
            
            space = input.find(' ')
            if (space == -1):
                space = len(input)
            command_name = input[0:space]
            arguments = input[space:].strip()
            
            self.process_command(command_name, arguments)
            
    # private
    def process_command(self, command_name, arguments):
        if command_name in self.commands:
            self.commands[command_name](arguments)
        else:
            self.write("{0} isn't a valid command, try one of: {1}".format(input, self.commands.keys()))
            
    # private
    def generate_floor(self):
        self.monsters = []
        num_monsters = self.floor_number + int(random.uniform(3, 5))
        for i in range(0, num_monsters):
            m = Monster()
            self.monsters.append(m)
            
    # private
    def quit(self, arguments):
        self.write("Bye!")
        sys.exit()
        
    # private
    def fight(self, arguments):
        target_name = arguments
        targets = [m for m in self.monsters if m.name.lower().find(target_name) > -1]
        if len(targets) == 0:
            self.write("There doesn't seem to be any '{0}' here to fight".format(target_name))
            return
        else:
            target = targets[0] # fight the first such monster
            b = Battle(self.player, target, self.print_function, self.delay_function)
            is_victory = b.fight_it_out()
        
        if is_victory == True:
            self.write("Victory! You vanquished your foe!")
            self.monsters.remove(target)
        else:
            self.write("You slink back, defeated.")
            
    # private
    def write(self, message):
        if self.print_function == None:
            print(message)
        else:
            self.print_function(message)