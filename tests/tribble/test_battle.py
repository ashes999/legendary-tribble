import unittest

from tribble.battle import Battle

class TestBattle:
    def test_attack_decreases_targets_health(self):
        defender_health = 7
        attacker = Creature(10, 5, 3)
        defender = Creature(defender_health, 3, 1)
        
        expected_damage = attacker.strength - defender.defense
        b = self.create_battle(attacker, defender)
        b.attack(attacker, defender)
        
        assert defender.current_health == defender_health - expected_damage
                
    def test_fight_it_out_terminates_when_player_dies(self):
        player = Creature(3, 3, 3)
        monster = Creature(10, 10, 10)
        b = self.create_battle(player, monster)
        b.fight_it_out()
        
        assert player.current_health <= 0
        
    def test_fight_it_out_terminates_when_monster_dies(self):
        player = Creature(3, 3, 3)
        monster = Creature(100, 1, 1)
        b = self.create_battle(player, monster)
        b.fight_it_out()
        
        assert monster.current_health <=  0 
        
    ### test helpers ###
        
    def create_battle(self, player, monster):
        # Don't print anything and don't call time.sleep
        return Battle(player, monster, self.do_nothing, self.do_nothing)
    
    # Has to have two arguments because print("{0}".format(...)) takes two arguments 
    def do_nothing(a1 = None, a2 = None):
        pass
    
class Creature:
    def __init__(self, health, strength, defense, agility = 1):
        self.name = 'test creature'
        self.current_health = self.total_health = health
        self.strength = strength
        self.defense = defense
        self.agility = agility
        