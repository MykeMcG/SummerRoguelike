import libtcodpy as libtcod
from entity import Entity
from bspmapgenerator import BspMapGenerator

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50
playerx =25 
playery = 23
objects = None
MAP_WIDTH = 80
MAP_HEIGHT = 45
ROOM_MIN_SIZE = 6
MAX_ROOMS = 50
terrain_map = None;

color_dark_wall    = libtcod.Color(  0,   0, 100)
color_light_wall   = libtcod.Color(130, 110,  50)
color_dark_ground  = libtcod.Color( 50,  50, 150)
color_light_ground = libtcod.Color(200, 180,  50)

FOV_ALGORITHM = 1
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

DEBUG_DISABLE_FOW = False

fov_recompute = True

def handle_keys(player):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    #movement keys
    global fov_recompute
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move( 0, -1, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move( 0,  1, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,  0, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move( 1,  0, terrain_map)
        fov_recompute = True

def render_all(con, terrain_map, fov_map, objects):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = terrain_map[x][y].block_sight
            if not visible:
                if terrain_map[x][y].explored or DEBUG_DISABLE_FOW:
                    if wall:
                        libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)
            else:
                if wall:
                    libtcod.console_set_char_background(con, x, y, color_light_wall, libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(con, x, y, color_light_ground, libtcod.BKGND_SET)
                terrain_map[x][y].explored = True
    for object in objects:
        object.draw(con, fov_map)

def generate_fov_map(width, height, terrain_map):
    fov_map = libtcod.map_new(width, height)
    for y in range(height):
        for x in range(width):
            libtcod.map_set_properties(fov_map, x, y, not terrain_map[x][y].block_sight, not terrain_map[x][y].blocked)
    return fov_map

def main():
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Wrath of Exuleb', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Entity(playerx, playery, '@', libtcod.white, libtcod.BKGND_NONE)
    objects = [player]
    map_gen = BspMapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOM_MIN_SIZE, 5, False, player)
    global terrain_map
    terrain_map = map_gen.generate_map()
    fov_map = generate_fov_map(MAP_WIDTH, MAP_HEIGHT, terrain_map)
    while not libtcod.console_is_window_closed():
        global fov_recompute
        if fov_recompute:
            fov_recompute = False
            libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGORITHM)
        render_all(con, terrain_map, fov_map, objects)
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()
        for object in objects:
            object.clear(con)
        libtcod.console_set_default_foreground(con, libtcod.white)
        exit = handle_keys(player)
        if exit:
            break

if __name__ == '__main__':
    main()
