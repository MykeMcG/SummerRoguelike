import libtcodpy as libtcod
from player import Player
from entityList import EntityList
from bspmapgenerator import BspMapGenerator

# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = 80
MAP_HEIGHT = 45
ROOM_MIN_SIZE = 6
MAX_ROOMS = 50
FOV_ALGORITHM = 1
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

# Debug Flags
DEBUG = True
DebugShowWholeMap = False

# Colors
COLOR_DARK_WALL = libtcod.Color(50, 50, 150)
COLOR_DARK_GROUND = libtcod.Color(0, 0, 100)
COLOR_LIGHT_WALL = libtcod.Color(204, 204, 204)
COLOR_LIGHT_GROUND = libtcod.Color(33, 33, 33)

# Map Options
BSP_RECURSION_DEPTH = 30
BSP_FULL_ROOMS = False

# Game Variables
PlayerX = None
PlayerY = None
Objects = EntityList()
MAX_ROOM_MONSTERS = 2
MapTiles = None
FovRecompute = True
GameState = 'playing'
PlayerAction = None

def handle_keys(player):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full-screen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return 'exit'  # exit game
    elif key.vk == libtcod.KEY_F1 and DEBUG:
        global DebugShowWholeMap
        DebugShowWholeMap = not DebugShowWholeMap  # Toggle DebugShowWholeMap
    if GameState == 'playing':
        # movement keys
        global FovRecompute
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            player.move_or_attack(0, -1, MapTiles, Objects)
            FovRecompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            player.move_or_attack(0, 1, MapTiles, Objects)
            FovRecompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            player.move_or_attack(-1, 0, MapTiles, Objects)
            FovRecompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            player.move_or_attack(1, 0, MapTiles, Objects)
            FovRecompute = True
        else:
            return 'didnt-take-turn'

def render_wall(con, x, y, color):
    #TODO: Think of a better way to do this
    #TODO: Improve outside walls
    if y + 1 >= MAP_HEIGHT:
        north = False
    else:
        north = MapTiles[x][y + 1].blocked
    if y - 1 < 0:
        south = False
    else:
        south = MapTiles[x][y - 1].blocked
    if x + 1 >= MAP_WIDTH:
        west = False
    else:
        west  = MapTiles[x + 1][y].blocked
    if x - 1 < 0:
        east = False
    else:
        east = MapTiles[x - 1][y].blocked
    if north and south and east and west:
        wall_char = libtcod.CHAR_DCROSS
    elif north and not south and east and west:
        wall_char = libtcod.CHAR_DTEES
    elif not north and south and east and west:
        wall_char = libtcod.CHAR_DTEEN
    elif north and south and east and not west:
        wall_char = libtcod.CHAR_DTEEW
    elif north and south and not east and west:
        wall_char = libtcod.CHAR_DTEEE
    elif north and not south and east and not west:
        wall_char = libtcod.CHAR_DNE
    elif     north and not south and not east and west:
        wall_char = libtcod.CHAR_DNW
    elif not north and south and  east and not west:
        wall_char = libtcod.CHAR_DSE
    elif not north and south and not east and west:
        wall_char = libtcod.CHAR_DSW
    elif north and south:
        wall_char = libtcod.CHAR_DVLINE
    elif east and west:
        wall_char = libtcod.CHAR_DHLINE
    else:
        wall_char = libtcod.CHAR_DCROSS
    libtcod.console_set_char_foreground(con, x, y, color)
    libtcod.console_set_char(con, x, y, wall_char)

def render_all(con, fov_map):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if DebugShowWholeMap:
                visible = True
            else:
                visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = MapTiles[x][y].block_sight
            if not visible:
                if MapTiles[x][y].explored or DebugShowWholeMap:
                    if wall:
                        render_wall(con, x, y, COLOR_DARK_WALL)
                    else:
                        libtcod.console_set_char_background(con, x, y, COLOR_DARK_GROUND, libtcod.BKGND_SET)
            else:
                if wall:
                    render_wall(con, x, y, COLOR_LIGHT_WALL)
                else:
                    libtcod.console_set_char_background(con, x, y, COLOR_LIGHT_GROUND, libtcod.BKGND_SET)
                MapTiles[x][y].explored = True
    for object in Objects:

        object.draw(con, fov_map, DebugShowWholeMap)

def generate_fov_map(width, height):
    fov_map = libtcod.map_new(width, height)
    for y in range(height):
        for x in range(width):
            libtcod.map_set_properties(fov_map, x, y, not MapTiles[x][y].block_sight, not MapTiles[x][y].blocked)
    return fov_map

def main():
    global Objects, MapTiles, FovRecompute, PlayerAction
    libtcod.console_set_custom_font('tiles.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Wrath of Exuleb', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Player(PlayerX, PlayerY)
    Objects.append(player)
    map_gen = BspMapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOM_MIN_SIZE, BSP_RECURSION_DEPTH, BSP_FULL_ROOMS, MAX_ROOM_MONSTERS, player)
    MapTiles = map_gen.generate_map()
    for obj in map_gen.objects:
        Objects.append(obj)
    fov_map = generate_fov_map(MAP_WIDTH, MAP_HEIGHT)
    while not libtcod.console_is_window_closed():
        if FovRecompute:
            FovRecompute = False
            libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGORITHM)
        render_all(con, fov_map)
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()
        for obj in Objects:
            obj.clear(con)
        libtcod.console_set_default_foreground(con, libtcod.white)
        PlayerAction = handle_keys(player)
        if PlayerAction == 'exit':
            break
        if GameState == 'playing' and PlayerAction != 'didnt-take-turn':
            for obj in Objects:
                if obj.ai != None:
                    obj.ai.take_turn(fov_map, MapTiles, Objects, player)

if __name__ == '__main__':
    main()
