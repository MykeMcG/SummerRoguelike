import libtcodpy as libtcod

def player_death(player, messagePanel):
    messagePanel.append('You have fallen in battle...', libtcod.dark_red)
    player.char = '%'
    player.color = libtcod.dark_red

def skeleton_death(monster, objectList, messagePanel):
    messagePanel.append('{} collapses into a pile of bones!'.format(monster.name.capitalize()), libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    objectList.send_to_back(monster)

def generic_monster_death(monster, objectList, messagePanel):
    messagePanel.append('{} collapses into a mangled heap!'.format(monster.name.capitalize()), libtcod.orange)
    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    objectList.send_to_back(monster)