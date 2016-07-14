import sys
import time

from tribble.battle import Battle
from tribble.dungeon import Dungeon
from tribble.monster import Monster
from tribble.player import Player

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self, print_function = None, delay_function = time.sleep):
        self.player = Player()
        self.dungeon = Dungeon(self.write)
        # Hash of input command + callback function
        self.commands = { 'quit': self.quit, 'fight': self.fight, 'w': self.dungeon.move_west,
            'e': self.dungeon.move_east, 'n': self.dungeon.move_north,
            's': self.dungeon.move_south
        }
        self.print_function = print_function
        self.delay_function = delay_function
    
    def run(self):
        self.print_instructions()
        self.input_loop()

    # private            
    def print_instructions(self):
        self.write("Welcome to Legendary Tribble!")
        self.write("")
        
        self.write("Instructions: type 'fight <name>' to fight a monster.")
        self.write("Kill all the monsters, then, type 'descend' to go to the next floor")
        self.write("If you want to go back up one floor, type 'ascend'.")
        self.write("")
        
        self.write("You are on floor B{0}.".format(self.dungeon.floor_number))
        self.write("")
    
    # private 
    def input_loop(self):
        while True:
            self.write("You are in room {0}. You can go:".format(self.dungeon.current_room.id))
            self.dungeon.current_room.print_exits(self.write)
            self.dungeon.current_room.print_features(self.write)
            self.write("")
            
            self.write("You see {0} monsters:".format(len(self.dungeon.current_room.monsters)))
            self.write("Health: {0}/{1}".format(self.player.current_health, self.player.total_health))
            
            for m in self.dungeon.current_room.monsters:
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
            self.write("\"{0}\" isn't a valid command, try one of: {1}".format(command_name, self.commands.keys()))
                
    # private
    def quit(self, arguments):
        self.write("Bye!")
        sys.exit()
        
    # private
    def fight(self, arguments):
        target_name = arguments
        targets = [m for m in self.dungeon.current_room.monsters if m.name.lower().find(target_name) > -1]
        if len(targets) == 0:
            self.write("There doesn't seem to be any '{0}' here to fight".format(target_name))
            return
        else:
            target = targets[0] # fight the first such monster
            b = Battle(self.player, target, self.print_function, self.delay_function)
            is_victory = b.fight_it_out()
        
        if is_victory == True:
            self.write("Victory! You vanquished your foe!")
            self.dungeon.current_room.monsters.remove(target)
        else:
            self.write("You slink back, defeated.")
            
    # private
    def write(self, message):
        if self.print_function == None:
            print(message)
        else:
            self.print_function(message)