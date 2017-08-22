import libtcodpy as libtcod

# Game Options
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FOV_ALGORITHM = 1
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10
FPS_LIMIT = 15
TILESET = 'tiles.png'
GAME_TITLE = 'Wrath of Exuleb'
TITLE_CREDITS = 'By Mike McGivern.\n'\
    + 'Many thanks to the /r/roguelikedev and RogueBasin communities.'
TITLE_IMAGE = 'menu_background.png'
STARTING_FLOOR = -15
LEVELUP_BASE = 30
LEVELUP_FACTOR = 5
LEVELUP_AMOUNT_HP = 10
LEVELUP_AMOUNT_STRENGTH = 1
LEVELUP_AMOUNT_AGILITY = 1

# Player Stats
PLAYER_INITIAL_HP = 100
PLAYER_INITIAL_DEFENSE = 1
PLAYER_INITIAL_POWER = 4


# Save Configuration
SAVE_LOCATION = 'save/savegame'
SAVE_HEADER_MAP = 'map'
SAVE_HEADER_OBJECTS = 'objects'
SAVE_HEADER_PLAYERINDEX = 'player_index'
SAVE_HEADER_INVENTORY = 'inventory'
SAVE_HEADER_MESSAGELOG = 'msg_log'
SAVE_HEADER_STATE = 'game_state'
SAVE_HEADER_STAIRINDEX = 'stairs_index'
SAVE_HEADER_DUNGEONLEVEL = 'dungeon_level'


# Map Options
BSP_RECURSION_DEPTH = 30
BSP_FULL_ROOMS = False
MAP_WIDTH = 80
MAP_HEIGHT = 43
ROOM_MIN_SIZE = 6
MAX_ROOMS = 50
MAX_ROOM_ITEMS = 1


# Debug Flags
DEBUG = True


# Colors
COLOR_DARK_WALL = libtcod.Color(50, 50, 150)
COLOR_DARK_GROUND = libtcod.Color(0, 0, 100)
COLOR_LIGHT_WALL = libtcod.Color(204, 204, 204)
COLOR_LIGHT_GROUND = libtcod.Color(33, 33, 33)
COLOR_MESSAGE_DANGER = libtcod.dark_red
COLOR_MESSAGE_WARNING = libtcod.orange
COLOR_MESSAGE_GOOD = libtcod.dark_green
COLOR_MESSAGE_NEUTRAL = libtcod.white
COLOR_MESSAGE_CHEAT = libtcod.purple
COLOR_UI_HEALTH_FRONT = libtcod.red
COLOR_UI_HEALTH_BACK = libtcod.dark_red


# UI Options
BAR_WIDTH = 20
BAR_TEXT_TEMPLATE = '{name}: {value}/{max}'
BAR_HEALTH_GODMODE = "GOD MODE"
UI_FLOORINDICATOR_PREFIX_NEGATIVE = 'B'
UI_FLOORINDICATOR_PREFIX_POSITIVE = ''
UI_FLOORINDICATOR_SUFFIX = 'F'
UI_FLOORINDICATOR_TEMPLATE = 'Dungeon Level: {prefix}{level}{suffix}'
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MSG_X = BAR_WIDTH + 2
MSG_WIDTH = (SCREEN_WIDTH - BAR_WIDTH - 2) - 1
MSG_HEIGHT = PANEL_HEIGHT - 1
INVENTORY_WIDTH = 50
LEVEL_SCREEN_WIDTH = 64


# Spell Options
HEAL_AMOUNT = 40
LIGHTNING_DAMAGE = 40
LIGHTNING_RANGE = 5
CONFUSE_NUM_TURNS = 10
CONFUSE_RANGE = 8


# Items
ITEM_HEALTHPOTION_NAME = 'health potion'
ITEM_HEALTHPOTION_CHAR = 173
ITEM_HEALTHPOTION_SPAWNRATE = 35
ITEM_SCROLLLIGHTNING_NAME = 'scroll of lightning bolt'
ITEM_SCROLLLIGHTNING_CHAR = '#'
ITEM_SCROLLLIGHTNING_SPAWNRATE = [[25, STARTING_FLOOR + 3]]
ITEM_SCROLLCONFUSE_NAME = 'scroll of confusion'
ITEM_SCROLLCONFUSE_CHAR = '#'
ITEM_SCROLLCONFUSE_SPAWNRATE = [[10, STARTING_FLOOR + 1]]
ITEM_CORPSE_NAME = '{} remains'
ITEM_CORPSE_CHAR = '%'
ITEM_SWORDCOPPER_NAME = 'copper sword'
ITEM_SWORDCOPPER_CHAR = '/'
ITEM_SWORDCOPPER_SPAWNRATE = [[5, 4]]
ITEM_BUCKLERCOPPER_NAME = 'copper buckler'
ITEM_BUCKLERCOPPER_CHAR = '['
ITEM_BUCKLERCOPPER_SPAWNRATE = [[15, 8]]


ENTITY_STAIRSUP_NAME = 'stairs'
ENTITY_STAIRSUP_CHAR = '>'

# Equipment Slots
SLOT_RIGHTHAND = 'right hand'
SLOT_LEFTHAND = 'left hand'

# Mobs
MOB_KOBOLD_NAME = 'kobold'
MOB_KOBOLD_CHAR = 'k'
MOB_KOBOLD_SPAWNRATE = 20
MOB_SKELETON_NAME = 'skeleton'
MOB_SKELETON_CHAR = 's'
MOB_SKELETON_SPAWNRATE = 80
MOB_ORC_NAME = 'orc'
MOB_ORC_CHAR = 'o'
MOB_ORC_SPAWNRATE = [[15, STARTING_FLOOR + 2],
                     [30, STARTING_FLOOR + 4], 
                     [60, STARTING_FLOOR + 6]]


# Tables
TABLE_MAX_ROOM_MOBS = [
    [2, STARTING_FLOOR],
    [3, STARTING_FLOOR + 3],
    [5, STARTING_FLOOR + 5],
]

TABLE_MAX_ROOM_ITEMS = [
    [1, STARTING_FLOOR],
    [2, STARTING_FLOOR + 3],
]

# Messages
MESSAGE_GAME_START = 'Welcome, mortal, to the Tomb of Exlueb!'
MESSAGE_PLAYER_DEATH = 'You have fallen in battle...'
MESSAGE_NO_SAVE = 'Either there is no saved game to load, '\
    + 'or the save file has become corrupt.'

MESSAGE_CHEAT_XRAY = 'CHEAT ACTIVATED: X-Ray Vision'
MESSAGE_CHEAT_GODMODE = 'CHEAT ACTIVATED: God Mode'

MESSAGE_EQUIP = 'Equipped {item} on {slot}.'
MESSAGE_DEQUIP = 'Dequipped {item} from {slot}.'

MESSAGE_LEVELUP = 'Your battle skills grow stronger! You reached level {}!'
MESSAGE_LEVELUP_MENU = 'Level up!\nChoose a stat to raise:\n'
MESSAGE_LEVELUP_CONSTITUTION = 'Constitution (+{increase}HP, from {current}, '\
    + 'fully restore HP)'
MESSAGE_LEVELUP_STRENGTH = 'Strength (+{increase} attack, from {current})'
MESSAGE_LEVELUP_AGILITY = 'Agility (+{increase} defense, from {current})'
MESSAGE_NEXT_FLOOR = 'You take a moment to rest, and recover your strength.\n'\
    + 'After a rare moment of peace, you ascend to the next floor of the tomb.'

MESSAGE_INVENTORY_OPEN = 'Press the key next to an item to use it.'\
    + 'Press any other key to cancel.\n'
MESSAGE_INVENTORY_DROP = 'Press the key next to an item to drop it.' \
    + 'Press any other key to cancel.\n'
MESSAGE_INVENTORY_EMPTY = 'Inventory is empty.'
MESSAGE_INVENTORY_EQUIPPED = ' (on {})'

MESSAGE_ITEM_PICKUP_FAIL = 'Your inventory is full. Unable to pick up {}.'
MESSAGE_ITEM_PICKUP_SUCCESS = 'You picked up a {}.'
MESSAGE_ITEM_DROP = 'You drop the {}.'
MESSAGE_ITEM_USE_NOUSE = 'The {} cannot be used.'
MESSAGE_ITEM_USE_FAIL = 'Unable to use the {}.'
MESSAGE_ITEM_USE_SUCCESS = 'Used the {}.'

MESSAGE_HEAL_FAIL = 'You are already at full health!'
MESSAGE_HEAL_SUCCESS = 'Your wounds start to feel better!'
MESSAGE_LIGHTNING_FAIL = 'Failed to cast lightning: No target in range.'
MESSAGE_LIGHTNING_SUCCESS = 'A lightning bolt strikes the {0} with '\
    + 'a loud thunder! The {0} loses {1} HP!'
MESSAGE_CONFUSE_FAIL = 'Failed to cast confuse: No target in range.'
MESSAGE_CONFUSE_SUCCESS = 'The eyes of the {} look vacant, '\
    + 'as it starts to stumble around!'
MESSAGE_CONFUSE_END = 'The {} is no longer confused!'

MESSAGE_GENERIC_DEATH = '{} collapses into a mangled heap!'
MESSAGE_SKELETON_DEATH = '{} collapses into a pile of bones!'
