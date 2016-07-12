import random
from tribble.room import Room

class Dungeon:
    def __init__(self):
        self.floor_number = 1
        self.generate_floor()

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