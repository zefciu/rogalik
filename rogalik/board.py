class OutOfBounds(Exception):
    pass
    

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mobs = {}

    def add_mob(self, mob, x, y):
        self.mobs[(x, y)] = mob
        mob.board = self
        mob.position = (x, y)
        
#def move_to_player(self, pos_player):

    def render(self):
        result = []
        for row_number in range(self.height):
            row = []
            for col_number in range(self.width):
                mob = self.mobs.get((col_number, row_number))
                if mob is None:
                    row.append('.')
                else:
                    row.append(mob.render())
            result.append(''.join(row))
        return '\n'.join(result)

    def move(self, initial, vector):
        mob = self.mobs[initial]
        x, y = initial
        vx, vy = vector
        target_x, target_y = target = (x + vx), (y + vy)
        if (
            self.width <= target_x or
            target_x < 0 or
            self.height <= target_y or
            target_y < 0
        ):
            raise OutOfBounds()
        del self.mobs[initial]
        self.mobs[target] = mob
        mob.position = target
        
            
