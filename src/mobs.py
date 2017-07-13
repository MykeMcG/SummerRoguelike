import libtcodpy as libtcod
import random
from entity import Entity

class Skeleton(Entity):
    def __init__(self, x, y, background):
        self.char = 's'
        self.x = x
        self.y = y
        self.color = libtcod.white
        self.background = background
        self.blocks = True

class Orc(Entity):
    def __init__(self, x, y, background):
        #CHARS = ['o', 'ò', 'ó', 'ô', 'õ', 'ö']
        #self.char = random.choice(CHARS)
        self.char = 'o'
        self.x = x
        self.y = y
        self.color = libtcod.desaturated_green
        self.background = background
        self.blocks = True
