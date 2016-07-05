import unittest

from tests.utils.creature import Creature
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
        
    def test_faster_agility_results_in_more_attacks(self):
        # Both the player and the monster do one damage per turn
        player = Creature(10, 2, 1, 4) # fast
        monster = Creature(10, 2, 1, 1) # slow

        b = self.create_battle(player, monster)
        b.fight_it_out()
        
        # It takes 8 turns for the player to kill the monster.
        # In that time, if agility is ignored, the monster will
        # also get eight turns (and the player should have 2 health left).
        # If the player has more than two health, it means the player
        # got extra turns over the monster. That's what we want.
        turns_to_kill = monster.total_health / (player.strength - monster.defense) 
        assert player.current_health >= 10 - turns_to_kill
        
    ### test helpers ###
        
    def create_battle(self, player, monster):
        # Don't print anything and don't call time.sleep
        return Battle(player, monster, self.do_nothing, self.do_nothing)
    
    # Has to have two arguments because print("{0}".format(...)) takes two arguments 
    def do_nothing(a1 = None, a2 = None):
        pass
    
