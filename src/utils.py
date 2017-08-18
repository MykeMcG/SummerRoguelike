import libtcodpy as libtcod
import consts


def find_closest_target(caster, entities, range):
    closest_target = None
    closest_dist = range + 1

    for obj in entities:
        if obj.fighter and obj != caster:
            dist = caster.distance_to(obj)
            if dist < closest_dist:
                closest_target = obj
                closest_dist = dist
    return closest_target


def random_choice(chances):
    dice = libtcod.random_get_int(0, 1, sum(chances))
    running_sum = 0
    choice = 0
    for c in chances:
        running_sum += c
        if dice <= running_sum:
            return choice
        choice += 1


def random_choice_dict(chances_dict):
    chances = list(chances_dict.values())
    strings = list(chances_dict.keys())
    return strings[random_choice(chances)]


def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value
    return 0


def build_leveled_item_list(level):
    item_chances = {}
    item_chances[consts.ITEM_HEALTHPOTION_NAME] = consts.ITEM_HEALTHPOTION_SPAWNRATE
    item_chances[consts.ITEM_SCROLLLIGHTNING_NAME] = from_dungeon_level(consts.ITEM_SCROLLLIGHTNING_SPAWNRATE, level)
    item_chances[consts.ITEM_SCROLLCONFUSE_NAME] = from_dungeon_level(consts.ITEM_SCROLLCONFUSE_SPAWNRATE, level)
    return item_chances

def build_leveled_mob_list(level):
    mob_chances = {}
    mob_chances[consts.MOB_KOBOLD_NAME] = consts.MOB_KOBOLD_SPAWNRATE
    mob_chances[consts.MOB_SKELETON_NAME] = consts.MOB_SKELETON_SPAWNRATE
    mob_chances[consts.MOB_ORC_NAME] = from_dungeon_level(consts.MOB_ORC_SPAWNRATE, level)
    return mob_chances
