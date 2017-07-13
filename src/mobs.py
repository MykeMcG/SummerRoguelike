import libtcodpy as libtcod
import random
from entity import Entity

class Skeleton(Entity):
    def __init__(self, x, y, background):
        super(Skeleton, self).__init__(x, y, 'skeleton', 's', libtcod.white, background, True)


class Orc(Entity):
    def __init__(self, x, y, background):
        #CHARS = ['o', 'ò', 'ó', 'ô', 'õ', 'ö']
        #self.char = random.choice(CHARS)
        super(Orc, self).__init__(x, y, 'orc', 'o', libtcod.desaturated_green, background, True)


class Kobold(Entity):
    def __init__(self, x, y, background):
        super(Kobold, self).__init__(x, y, 'kobold', 'k', libtcod.desaturated_yellow, background, True)
