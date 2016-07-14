import random

from tribble.monster import Monster

class Room:
    
    next_id = 0
    valid_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
    valid_features = ['stairs down', 'stairs up']
            
    @staticmethod      
    def reverse(direction):
        if direction == "NORTH":
            return "SOUTH"
        elif direction == "SOUTH": 
            return "NORTH"
        elif direction == "WEST":
            return "EAST"
        elif direction == "EAST":
            return "WEST"
        else:
            raise(Exception("Not sure how to reverse direction {0}".format(direction)))
    
    def __init__(self):
        self.id = Room.next_id
        Room.next_id += 1
        self.generate_monsters()
        # direction => target
        self.connections = {}
        self.features = []
        
    def connect_to(self, target):
        if target == self or target in self.connections.values():
            return # don't connect to yourself or if already connected
        else:
            # This room isn't already connected in that direction (eg. north) and the target room
            # isn't already connected int he opposite direction (eg. south)
            valid_directions = [d for d in Room.valid_directions if not d in self.connections.keys() and not Room.reverse(d) in target.connections.keys()]
            if len(valid_directions) > 0:
                direction = random.sample(valid_directions, 1)[0]
                self.connections[direction] = target
                target.connections[Room.reverse(direction)] = self
            
    def print_exits(self, print_function):
        for direction in self.connections.keys():
            print_function("    {0} to room {1}".format(direction, self.connections[direction].id))
        
    def print_features(self, print_function):
        for feature in self.features:
            print_function("You see {0} here.".format(feature))
        
     # private
    def generate_monsters(self):
        self.monsters = []
        has_monsters = random.randint(1, 100) <= 50
        
        if has_monsters == True:
            num_monsters = random.randint(1, 5)
            for i in range(0, num_monsters):
                m = Monster()
                self.monsters.append(m) 