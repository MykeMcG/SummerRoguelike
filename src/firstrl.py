import libtcodpy as libtcod
from entity import Entity
from bspmapgenerator import BspMapGenerator

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
playerx = 25
playery = 23
objects = None
MAP_WIDTH = 80
MAP_HEIGHT = 45
ROOM_MIN_SIZE = 6
MAX_ROOMS = 50
terrain_map = None

color_dark_wall    = libtcod.Color(  0,   0, 100)
color_light_wall   = libtcod.Color(130, 110,  50)
color_dark_ground  = libtcod.Color( 50,  50, 150)
color_light_ground = libtcod.Color(200, 180,  50)

FOV_ALGORITHM = 1
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

DEBUG = True
debug_show_whole_map = False

fov_recompute = True


def handle_keys(player):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  # exit game
    elif key.vk == libtcod.KEY_F1 and DEBUG:
        global debug_show_whole_map
        debug_show_whole_map = not debug_show_whole_map #Toggle debug_show_whole_map
    # movement keys
    global fov_recompute
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0, terrain_map)
        fov_recompute = True
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0, terrain_map)
        fov_recompute = True


def render_wall(con, terrain_map, x, y, color, background):
    #TODO: Think of a better way to do this
    #TODO: Improve outside walls
    if y + 1 >= MAP_HEIGHT:
        north = False
    else:
        north = terrain_map[x][y + 1].blocked
    if y - 1 < 0:
        south = False
    else:
        south = terrain_map[x][y - 1].blocked
    if x + 1 >= MAP_WIDTH:
        west = False
    else:
        west  = terrain_map[x + 1][y].blocked
    if x - 1 < 0:
        east = False
    else:
        east = terrain_map[x - 1][y].blocked
    if       north and     south and     east and     west:
        wall_char = libtcod.CHAR_DCROSS
    elif     north and not south and     east and     west:
        wall_char = libtcod.CHAR_DTEES
    elif not north and     south and     east and     west:
        wall_char = libtcod.CHAR_DTEEN
    elif     north and     south and     east and not west:
        wall_char = libtcod.CHAR_DTEEW
    elif     north and     south and not east and     west:
        wall_char = libtcod.CHAR_DTEEE
    elif     north and not south and     east and not west:
        wall_char = libtcod.CHAR_DNE
    elif     north and not south and not east and     west:
        wall_char = libtcod.CHAR_DNW
    elif not north and     south and     east and not west:
        wall_char = libtcod.CHAR_DSE
    elif not north and     south and not east and     west:
        wall_char = libtcod.CHAR_DSW
    elif north and south:
        wall_char = libtcod.CHAR_DVLINE
    elif east and west:
        wall_char = libtcod.CHAR_DHLINE
    else:
        wall_char = libtcod.CHAR_DCROSS
    libtcod.console_set_char_foreground(con, x, y, color)
    libtcod.console_set_char(con, x, y, wall_char)



def render_all(con, terrain_map, fov_map, objects):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if debug_show_whole_map:
                visible = True
            else:
                visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = terrain_map[x][y].block_sight
            if not visible:
                if terrain_map[x][y].explored or debug_show_whole_map:
                    if wall:
                        render_wall(con, terrain_map, x, y, color_dark_wall, libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)
            else:
                if wall:
                    render_wall(con, terrain_map, x, y, color_light_wall, libtcod.BKGND_SET)
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
    libtcod.console_set_custom_font('tiles.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
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
