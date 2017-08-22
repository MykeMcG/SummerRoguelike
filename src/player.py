import libtcodpy as libtcod
from entity import Entity
from entityList import EntityList
from fighter import Fighter
import consts
import utils

class Player(Entity):
    def __init__(self, x, y):
        fighter_component = Fighter(hp=consts.PLAYER_INITIAL_HP,
                             defense=consts.PLAYER_INITIAL_DEFENSE,
                             power=consts.PLAYER_INITIAL_POWER, exp=0)
        super(Player, self).__init__(x, y, 'the player', '@', libtcod.white,
                                     libtcod.BKGND_NONE, True,
                                     fighter=fighter_component)
        self.inventory = EntityList()
        self.level = 1

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

