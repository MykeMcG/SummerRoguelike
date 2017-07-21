import libtcodpy as libtcod

def player_death(player):
    print('You have fallen in battle...')
    player.char = '%'
    player.color = libtcod.dark_red

def skeleton_death(monster, objectList):
    print('{} collapses into a pile of bones!'.format(monster.name.capitalize()))
    monster.char = '%'
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    objectList.send_to_back(monster)

def generic_monster_death(monster, objectList):
    print('{} collapses into a mangled heap!'.format(monster.name.capitalize()))
    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = '{} remains'.format(monster.name)
    objectList.send_to_back(monster)