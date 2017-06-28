import libtcodpy as libtcod
from entity import entity

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50
playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2
objects = None

def handle_keys(player):
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move( 0,  1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move( 0, -1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,  0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move( 1,  0)

def main():
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Wrath of Exuleb', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = entity(playerx, playery, '@', libtcod.white, libtcod.BKGND_NONE)
    npc = entity(playerx, playery + 5, '@', libtcod.green, libtcod.BKGND_NONE)
    objects = [player, npc]
    while not libtcod.console_is_window_closed():
        for object in objects:
            object.clear(con)
        for object in objects:
            object.draw(con)
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()
        libtcod.console_set_default_foreground(con, libtcod.white)
        exit = handle_keys(player)
        if exit:
            break

if __name__ == '__main__':
    main()
