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
color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 4
MAX_ROOMS = 50
game_map = None;

def handle_keys(player):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move( 0, -1, game_map)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move( 0,  1, game_map)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,  0, game_map)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move( 1,  0, game_map)

def render_all(con, game_map, objects):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = game_map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)
    for object in objects:
        object.draw(con)

def main():
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Wrath of Exuleb', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Entity(playerx, playery, '@', libtcod.white, libtcod.BKGND_NONE)
    objects = [player]
    map_gen = BspMapGenerator(MAP_WIDTH, MAP_HEIGHT, ROOM_MIN_SIZE, 10, False, player)
    global game_map
    game_map = map_gen.generate_map()
    while not libtcod.console_is_window_closed():
        render_all(con, game_map, objects)
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
