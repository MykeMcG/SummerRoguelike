import libtcodpy as libtcod
from entity import Entity
from fighter import Fighter
import death
import ai
import consts


class Skeleton(Entity):
    def __init__(self, x, y, background):
        fighter_component = Fighter(hp=10, defense=0, power=3, exp=35,
                                    death_function=death.skeleton_death)
        ai_component = ai.BasicMonster()
        super(Skeleton, self).__init__(x, y, consts.MOB_SKELETON_NAME,
                                       consts.MOB_SKELETON_CHAR,
                                       libtcod.white, background, True,
                                       False, fighter_component,
                                       ai_component)


class Orc(Entity):
    def __init__(self, x, y, background):
        # CHARS = ['o', 'ò', 'ó', 'ô', 'õ', 'ö']
        # self.char = random.choice(CHARS)
        fighter_component = Fighter(hp=16, defense=1, power=4, exp=100,
                                    death_function=death.generic_monster_death)
        ai_component = ai.BasicMonster()
        super(Orc, self).__init__(x, y, consts.MOB_ORC_NAME,
                                  consts.MOB_ORC_CHAR,
                                  libtcod.desaturated_green, background,
                                  True, False, fighter_component,
                                  ai_component)


class Kobold(Entity):
    def __init__(self, x, y, background):
        fighter_component = Fighter(hp=7, defense=0, power=2, exp=10,
                                    death_function=death.generic_monster_death)
        ai_component = ai.CowardMonster()
        super(Kobold, self).__init__(x, y, consts.MOB_KOBOLD_NAME,
                                     consts.MOB_KOBOLD_CHAR,
                                     libtcod.desaturated_yellow, background,
                                     True, False, fighter_component,
                                     ai_component)
