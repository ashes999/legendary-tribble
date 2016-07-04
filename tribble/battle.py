import math
import time

class Battle:
    """A fight between the player and a monster."""
    
    def __init__(self, player, monster, print_function = None, delay_function = time.sleep):
        self.player = player
        self.monster = monster
        self.print_function = print_function
        self.delay_function = delay_function
        
    def fight_it_out(self):
        self.write("You attack the {0}!".format(self.monster.name))
        
        while self.player.current_health > 0 and self.monster.current_health > 0:
            self.write("Player: {0}/{1} {2}: {3}/{4}".format(self.player.current_health, self.player.total_health, self.monster.name, self.monster.current_health, self.monster.total_health))
            
            slowest = min(self.player.agility, self.monster.agility)
            
            # TODO: care about the remainder and accumulate it towards next round
            # eg. with agilities 2 and 3, attacks should be: 3, 2, 3, 3, 2
            num_player_attacks = self.player.agility // slowest
            num_monster_attacks = self.monster.agility // slowest
            
            # TODO: extract this logic into a separate method so we can test it
            if self.player.agility > self.monster.agility:
                self.attack(self.player, self.monster, num_player_attacks)
                if self.monster.current_health > 0:
                    self.attack(self.monster, self.player, num_monster_attacks)
            else:                
                self.attack(self.monster, self.player, num_monster_attacks)
                if self.player.current_health > 0:
                    self.attack(self.player, self.monster, num_player_attacks)
              
            self.delay_function(1)
                  
        if self.player.current_health <= 0:
            return False
        else:
            return True
            
    # private
    def attack(self, attacker, target, times):
        for i in range(times):
            damage = attacker.strength - target.defense        
            target.current_health -= damage
            self.write("{0} attacks {1} for {2} damage!".format(attacker.name, target.name, damage))
            
    def write(self, message):
        if self.print_function == None:
            print(message)
        else:
            self.print_function(message)
    