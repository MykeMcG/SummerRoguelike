import libtcodpy as libtcod
import random
from entity import Entity
from fighter import Fighter
import death
import ai


class Skeleton(Entity):
    def __init__(self, x, y, background):
        fighter_component = Fighter(hp=10, defense=0, power=3, death_function=death.skeleton_death)
        ai_component      = ai.BasicMonster()
        super(Skeleton, self).__init__(x, y, 'skeleton', 's', libtcod.white, background, True, fighter_component, ai_component)


class Orc(Entity):
    def __init__(self, x, y, background):
        #CHARS = ['o', 'ò', 'ó', 'ô', 'õ', 'ö']
        #self.char = random.choice(CHARS)
        fighter_component = Fighter(hp=16, defense=1, power=4, death_function=death.generic_monster_death)
        ai_component      = ai.BasicMonster()
        super(Orc, self).__init__(x, y, 'orc', 'o', libtcod.desaturated_green, background, True, fighter_component, ai_component)


class Kobold(Entity):
    def __init__(self, x, y, background):
        fighter_component = Fighter(hp=7, defense=0, power=2, death_function=death.generic_monster_death)
        ai_component      = ai.CowardMonster()
        super(Kobold, self).__init__(x, y, 'kobold', 'k', libtcod.desaturated_yellow, background, True, fighter_component, ai_component)
