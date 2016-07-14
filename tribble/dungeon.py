import random
from tribble.room import Room

class Dungeon:
    def __init__(self, print_function):
        self.print_function = print_function
        self.floor_number = 1
        self.generate_floor()

    # private
    def generate_floor(self):
        Room.next_id = 1
        self.generate_rooms()
        self.connect_rooms()
        self.current_room = random.choice(self.rooms)
        self.generate_stairs()       
    
    # private
    def generate_rooms(self):
        self.rooms = []
        num_rooms = random.randint(5, 10)        
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
    
    def generate_stairs(self):
        all_rooms = random.sample(self.rooms, len(self.rooms))
        
        stairs_down = all_rooms[0]
        stairs_down.features.append("stairs down")
        
        if self.floor_number > 1:
            stairs_up = all_rooms[-1]
            stairs_up.features.append("stairs up")
            
            
    def move_west(self, arguments):
        self.move("WEST")
        
    def move_east(self, arguments):
        self.move("EAST")
        
    def move_north(self, arguments):
        self.move("NORTH")
        
    def move_south(self, arguments):
        self.move("SOUTH")
       
    def move(self, direction):
        if self.current_room.connections.has_key(direction):
            self.current_room = self.current_room.connections[direction]
            self.print_function("You move {0}".format(direction))
        else:
            self.print_function("There isn't any exit to the {0}.".format(direction)) 
           
            