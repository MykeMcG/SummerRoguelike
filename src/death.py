import libtcodpy as libtcod


def player_death(player, message_panel):
    message_panel.append('You have fallen in battle...', libtcod.dark_red)
    player.char = '%'
    player.color = libtcod.dark_red


def skeleton_death(monster, object_list, message_panel):
    name = monster.name.capitalize()
    message_panel.append('{} collapses into a pile of bones!'.format(name),
                         libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    object_list.send_to_back(monster)


def generic_monster_death(monster, object_list, message_panel):
    name = monster.name.capitalize()
    message_panel.append('{} collapses into a mangled heap!'.format(name),
                         libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    object_list.send_to_back(monster)
