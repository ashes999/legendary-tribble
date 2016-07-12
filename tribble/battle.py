import math
import time

class Battle:
    """A fight between the player and a monster."""
    
    def __init__(self, player, monster, print_function = None, delay_function = time.sleep):
        self.player = player
        self.monster = monster
        self.print_function = print_function
        self.delay_function = delay_function
        
        self.agility_points = { "player": 0, "monster": 0 }
        
    def fight_it_out(self):
        self.write("You attack the {0}!".format(self.monster.name))
        ap_per_turn = max(self.player.agility, self.monster.agility)
        
        while self.player.current_health > 0 and self.monster.current_health > 0:

            # Increment points until someone gets a turn                                    
            if self.agility_points["player"] < ap_per_turn and self.agility_points["monster"] < ap_per_turn:
                player_iterations = (ap_per_turn - self.agility_points["player"]) / self.player.agility
                monster_iterations = (ap_per_turn - self.agility_points["monster"]) / self.monster.agility
                iterations = min(player_iterations, monster_iterations)
                
                # Rounding error. If you don't like this, use ceil(...) instead of just dividing by agility.
                if (iterations == 0):
                    iterations = 1
                                
                self.agility_points["player"] += (self.player.agility * iterations)
                self.agility_points["monster"] += (self.monster.agility * iterations)
            
            # Just give the player priority. It's simpler than checking for ties and awarding
            # a turn to the faster unit.
            if self.agility_points["player"] >= ap_per_turn:
                attacker = self.player
                target = self.monster                
                self.attack(attacker, target)
                self.agility_points["player"] -= ap_per_turn
            
            if self.agility_points["monster"] >= ap_per_turn:
                attacker = self.monster
                target = self.player
                self.attack(attacker, target)
                self.agility_points["monster"] -= ap_per_turn
                self.write("Player: {0}/{1} {2}: {3}/{4}".format(self.player.current_health, self.player.total_health, self.monster.name, self.monster.current_health, self.monster.total_health))                                    
                
            self.delay_function(0.25)
                  
        if self.player.current_health <= 0:
            return False
        else:
            return True
    
    # private
    def attack(self, attacker, target):
        damage = attacker.strength - target.defense        
        target.current_health -= damage
        self.write("{0} attacks {1} for {2} damage!".format(attacker.name, target.name, damage))
            
    def write(self, message):
        if self.print_function == None:
            print(message)
        else:
            self.print_function(message)
    