import libtcodpy as libtcod
from entity import Entity

class Player(Entity):
    def __init__(self, x, y):
        super(Player, self).__init__(x, y, 'player', '@', libtcod.white, libtcod.BKGND_NONE, True)


    def move_or_attack(self, delta_x, delta_y, map_tiles, map_objects):
        x = self.x + delta_x
        y = self.y + delta_y
        target = None
        for o in map_objects:
            if o.x == x and o.y == y:
                target = o
        if target != None:
            print('Attack ' + target.name)
        else:
            self.move(delta_x, delta_y, map_tiles, map_objects)