class Creature:
    def __init__(self, health, strength, defense, agility = 1):
        self.name = 'test creature'
        self.current_health = self.total_health = health
        self.strength = strength
        self.defense = defense
        self.agility = agility
        