import libtcodpy as libtcod
from tile import Tile

class Entity:
    #A generic object [player, monster, item, stairs, etc.]
    #It is always represented by a character on screen.
    def __init__(self, x, y, char, color, background):
        self.x          = x
        self.y          = y
        self.char       = char
        self.color      = color
        self.background = background

    def move(self, delta_x, delta_y, map_tiles):
        if not map_tiles[self.x + delta_x][self.y + delta_y].blocked:
            self.x += delta_x
            self.y += delta_y

    def draw(self, console, fov_map):
        if libtcod.map_is_in_fov(fov_map, self.x, self.y):
            #set the color and draw the character representing the object
            libtcod.console_set_default_foreground(console, self.color)
            libtcod.console_put_char(console, self.x, self.y, self.char, self.background)

    def clear(self, console):
        #erase the character representing the object
        libtcod.console_put_char(console, self.x, self.y, ' ', libtcod.BKGND_NONE)
