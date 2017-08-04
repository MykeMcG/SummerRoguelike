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
INTRO_MESSAGE = 'Welcome, mortal, to the Tomb of Exlueb!'

# Map Options
BSP_RECURSION_DEPTH = 30
BSP_FULL_ROOMS = False
MAP_WIDTH = 80
MAP_HEIGHT = 43
ROOM_MIN_SIZE = 6
MAX_ROOMS = 50
MAX_ROOM_MONSTERS = 2
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

# UI Options
BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MSG_X = BAR_WIDTH + 2
MSG_WIDTH = (SCREEN_WIDTH - BAR_WIDTH - 2) - 1
MSG_HEIGHT = PANEL_HEIGHT - 1
INVENTORY_WIDTH = 50
INVENTORY_MESSAGE = 'Press the key next to an item to use it. ' \
                  + 'Press any other key to cancel\n'

# Spell Options
LIGHTNING_DAMAGE = 20
LIGHTNING_RANGE = 5