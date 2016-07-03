import math

class Battle:
    """A fight between the player and a monster."""
    
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        
    def fight_it_out(self):
        print "You attack the {0}!".format(self.monster.name)
        
        while self.player.current_health > 0 and self.monster.current_health > 0:
            print "Player: {0}/{1} {2}: {3}/{4}".format(self.player.current_health, self.player.total_health, self.monster.name, self.monster.current_health, self.monster.total_health)
            
            slowest = min(self.player.agility, self.monster.agility)
            num_player_attacks = int(math.floor(self.player.agility / slowest))
            num_monster_attacks = int(math.floor(self.monster.agility / slowest))
            
            if self.player.agility > self.monster.agility:
                self.attack(self.player, self.monster, num_player_attacks)
                if self.monster.current_health > 0:
                    self.attack(self.monster, self.player, num_monster_attacks)
            else:                
                self.attack(self.monster, self.player, num_monster_attacks)
                if self.player.current_health > 0:
                    self.attack(self.player, self.monster, num_player_attacks)
                    
        if self.player.current_health <= 0:
            return False
        else:
            return True
            
    # private
    def attack(self, attacker, target, times):
        for i in range(times):
            damage = attacker.strength - target.defense        
            target.current_health -= damage
            print "{0} attacks {1} for {2} damage!".format(attacker.name, target.name, damage)