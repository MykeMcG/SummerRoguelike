import libtcodpy as libtcod
import math
import consts
from tile import Tile


class Entity:
    # A generic object [player, monster, item, stairs, etc.]
    # It is always represented by a character on screen.
    def __init__(self, x, y, name, char, color, background, blocks=False,
                 remain_visible=False, fighter=None, ai=None, item=None, equipment=None):
        self.x = x
        self.y = y
        self.name = name
        self.char = char
        self.color = color
        self.background = background
        self.blocks = blocks
        self.remain_visible = remain_visible
        self.fighter = fighter
        if self.fighter:
            self.fighter.owner = self
            self.inventory = []
        self.ai = ai
        if self.ai:
            self.ai.owner = self
        self.item = item
        if self.item:
            self.item.owner = self
        self.equipment = equipment
        if self.equipment:
            self.item.owner = self
            self.equipment.owner = self

    def move(self, delta_x, delta_y, map_tiles, objects):
        if not self.is_blocked(self.x + delta_x, self.y + delta_y, map_tiles,
                               objects):
            self.x += delta_x
            self.y += delta_y

    def move_towards(self, target_x, target_y, map_tiles, objects):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy, map_tiles, objects)

    def move_away(self, target_x, target_y, map_tiles, objects):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance)) * -1
        dy = int(round(dy / distance)) * -1
        self.move(dx, dy, map_tiles, objects)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def draw(self, console, map_tiles, fov_map, show_whole_map):
        if libtcod.map_is_in_fov(fov_map, self.x, self.y) or show_whole_map\
            or (self.remain_visible and map_tiles[self.x][self.y].explored):
            # set the color and draw the character representing the object
            libtcod.console_set_default_foreground(console, self.color)
            libtcod.console_put_char(console, self.x, self.y, self.char,
                                     self.background)

    def clear(self, console):
        # erase the character representing the object
        libtcod.console_put_char(console, self.x, self.y, ' ',
                                 libtcod.BKGND_NONE)

    def is_blocked(self, x, y, terrain_map, objects):
        if terrain_map[x][y].blocked:
            return True
        if objects is None:
            return False
        for o in objects:
            if o.blocks and o.x == x and o.y == y:
                return True
        return False

class StairsUp(Entity):
    def __init__(self, x, y):
        super(StairsUp, self).__init__(x, y, consts.ENTITY_STAIRSUP_NAME,
                                        consts.ENTITY_STAIRSUP_CHAR,
                                        libtcod.white,
                                        libtcod.BKGND_NONE,
                                        remain_visible=True)
