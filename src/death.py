import libtcodpy as libtcod
import consts


def player_death(player, message_panel):
    message_panel.append(consts.MESSAGE_PLAYER_DEATH, libtcod.dark_red)
    player.char = consts.ITEM_CORPSE_CHAR
    player.color = libtcod.dark_red


def skeleton_death(monster, object_list, message_panel):
    name = monster.name.capitalize()
    message_panel.append(consts.MESSAGE_SKELETON_DEATH.format(name),
                         libtcod.orange)
    monster.char = consts.ITEM_CORPSE_CHAR
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = consts.ITEM_CORPSE_NAME.format(monster.name)
    object_list.send_to_back(monster)


def generic_monster_death(monster, object_list, message_panel):
    name = monster.name.capitalize()
    message_panel.append(consts.MESSAGE_GENERIC_DEATH.format(name),
                         libtcod.orange)
    monster.char = consts.ITEM_CORPSE_CHAR
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = consts.ITEM_CORPSE_NAME.format(monster.name)
    object_list.send_to_back(monster)
