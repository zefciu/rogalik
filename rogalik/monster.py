from rogalik.mob import Mob
from math import copysign

def sign(x):
    if x == 0:
        return 0
    return x // abs(x)

class Monster(Mob):
        
    def move_to_player(self, pos_player):
        my_x, my_y = self.position
        player_x, player_y = pos_player
        return (
            sign(player_x - my_x),
            sign(player_y - my_y),
        )
        
        


class Orc(Monster):
    symbol = 'o'
