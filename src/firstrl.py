import libtcodpy as libtcod
from player import player

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50
playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2

def handle_keys(plr):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    global playerx, playery
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        plr.pos_y -= 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        plr.pos_y += 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        plr.pos_x -= 1
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        plr.pos_x += 1

def main():
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Wrath of Exuleb', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    plr = player(playerx, playery, libtcod.BKGND_NONE)
    #draw the initial screen
    plr.draw(con)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    while not libtcod.console_is_window_closed():
        libtcod.console_set_default_foreground(con, libtcod.white)
        exit = handle_keys(plr)
        plr.draw(con)
        if exit:
            break
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()

if __name__ == '__main__':
    main()
