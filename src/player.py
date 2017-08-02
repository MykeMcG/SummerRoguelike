import libtcodpy as libtcod
from entity import Entity
from entityList import EntityList
from fighter import Fighter

class Player(Entity):
    def __init__(self, x, y):
        fighter_component = Fighter(hp=30, defense=2, power=5)
        super(Player, self).__init__(x, y, 'player', '@', libtcod.white,
                                     libtcod.BKGND_NONE, True,
                                     fighter_component)
        self.inventory = EntityList()

    # TODO: Figure out a way to change the game state when the player dies
    def move_or_attack(self, delta_x, delta_y, map_tiles, map_objects,
                       message_panel):
        x = self.x + delta_x
        y = self.y + delta_y
        target = None
        for obj in map_objects:
            if obj.fighter is not None and obj.x == x and obj.y == y:
                target = obj
        if target != None:
            self.fighter.attack(target, map_objects, message_panel)
        else:
            self.move(delta_x, delta_y, map_tiles, map_objects)