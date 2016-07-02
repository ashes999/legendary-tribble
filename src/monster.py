import random

class Monster:
    """A fightable monster."""
    
    def __init__(self):
        difficulty = int(random.uniform(1, 10))
        print "Created a monster d={0}".format(difficulty)