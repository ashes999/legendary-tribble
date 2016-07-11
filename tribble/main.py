import random
import sys
import time

from tribble.battle import Battle
from tribble.monster import Monster
from tribble.player import Player
from tribble.room import Room

class Main:
    """The main game loop logic. TODO: refactor into better classes"""
    
    def __init__(self, print_function = None, delay_function = time.sleep):
        self.player = Player()
        self.floor_number = 1        
        # Hash of input command + callback function
        self.commands = { 'quit': self.quit, 'fight': self.fight }
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
            self.write("You are in room {0}".format(self.current_room.id + 1))
            self.write("You see {0} monsters:".format(len(self.current_room.monsters)))
            self.write("Health: {0}/{1}".format(self.player.current_health, self.player.total_health))
            
            for m in self.current_room.monsters:
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
    def generate_floor(self):
        Room.next_id = 1
        self.generate_rooms()
        self.connect_rooms()
        self.current_room = random.choice(self.rooms)
    
    # private
    def generate_rooms(self):
        self.rooms = []
        num_rooms = random.randint(8, 16)        
        for i in range(0, num_rooms):
            r = Room()
            self.rooms.append(r)
            
    def connect_rooms(self):
        # Connect each room to one other room, in random order
        connect_me = random.sample(self.rooms, len(self.rooms))
        random.shuffle(connect_me)
        for i in range(0, len(connect_me) - 1):
            room = connect_me[i]
            connect_to = connect_me[i + 1]
            room.connect_to(connect_to)
            
        # For each room, connect to 1-2 other rooms.
        for room in self.rooms:
            num_targets = random.randint(1, 2)
            for i in range(num_targets):
                target = random.sample(self.rooms, 1)[0]
                room.connect_to(target)
            
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