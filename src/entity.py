import libtcodpy as libtcod
from tile import Tile

class Entity:
    #A generic object [player, monster, item, stairs, etc.]
    #It is always represented by a character on screen.
    def __init__(self, x, y, char, color, background, blocks):
        self.x          = x
        self.y          = y
        self.char       = char
        self.color      = color
        self.background = background
        self.blocks     = blocks


    def move(self, delta_x, delta_y, map_tiles, objects):
        if not self.is_blocked(self.x + delta_x, self.y + delta_y, map_tiles, objects):
            self.x += delta_x
            self.y += delta_y


    def draw(self, console, fov_map, show_whole_map):
        if libtcod.map_is_in_fov(fov_map, self.x, self.y) or show_whole_map:
            #set the color and draw the character representing the object
            libtcod.console_set_default_foreground(console, self.color)
            libtcod.console_put_char(console, self.x, self.y, self.char, self.background)


    def clear(self, console):
        #erase the character representing the object
        libtcod.console_put_char(console, self.x, self.y, ' ', libtcod.BKGND_NONE)


    def is_blocked(self, x, y, terrain_map, objects):
        if terrain_map[x][y].blocked:
            return True
        if objects == None:
            return False
        for o in objects:
            if o.blocks and o.x == x and o.y == y:
                return True
        return False
