import libtcodpy as libtcod
import items
import consts
from player import Player
from entityList import EntityList
from bspmapgenerator import BspMapGenerator
from messagePanel import MessagePanel

DebugShowWholeMap = False

# Game Variables
PlayerX = None
PlayerY = None
MapTiles = None
FovRecompute = True
GameState = 'playing'
PlayerAction = None


def handle_keys(console, key, player, objects, message_panel):
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full-screen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return 'exit'  # exit game
    elif key.vk == libtcod.KEY_F1 and consts.DEBUG:
        global DebugShowWholeMap
        DebugShowWholeMap = not DebugShowWholeMap  # Toggle DebugShowWholeMap
    if GameState == 'playing':
        # movement keys
        global FovRecompute
        if key.vk == libtcod.KEY_UP:
            player.move_or_attack(0, -1, MapTiles, objects, message_panel)
            FovRecompute = True
        elif key.vk == libtcod.KEY_DOWN:
            player.move_or_attack(0, 1, MapTiles, objects, message_panel)
            FovRecompute = True
        elif key.vk == libtcod.KEY_LEFT:
            player.move_or_attack(-1, 0, MapTiles, objects, message_panel)
            FovRecompute = True
        elif key.vk == libtcod.KEY_RIGHT:
            player.move_or_attack(1, 0, MapTiles, objects, message_panel)
            FovRecompute = True
        else:
            key_char = chr(key.c)
            if key_char == 'g':
                for obj in objects:
                    if obj.x == player.x and obj.y == player.y and obj.item:
                        msg = obj.item.pick_up(objects, player.inventory)
                        message_panel.append(msg, consts.COLOR_MESSAGE_GOOD)
                        break
            elif key_char == 'i':
                chosen_item = show_inventory_menu(console,
                                                  consts.MESSAGE_INVENTORY_OPEN,
                                                  player.inventory)
                if chosen_item is not None:
                    chosen_item.use(player.inventory,
                                    message_panel=message_panel,
                                    player=player, caster=player,
                                    entities=objects)
            return 'didnt-take-turn'


def get_names_under_mouse(mouse, fov_map, objects):
    (x, y) = (mouse.cx, mouse.cy)
    # Create a list with the names of all
    # objects at the mouse's coordinates if they're in FOV
    names = [obj.name for obj in objects
             if obj.x == x and obj.y == y 
             and libtcod.map_is_in_fov(fov_map, obj.x, obj.y)]
    names = ', '.join(names)
    return names.capitalize()


def render_wall(con, x, y, color):
    # TODO: Think of a better way to do this
    # TODO: Improve outside walls
    if y + 1 >= consts.MAP_HEIGHT:
        north = False
    else:
        north = MapTiles[x][y + 1].blocked
    if y - 1 < 0:
        south = False
    else:
        south = MapTiles[x][y - 1].blocked
    if x + 1 >= consts.MAP_WIDTH:
        west = False
    else:
        west = MapTiles[x + 1][y].blocked
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
    elif north and not south and not east and west:
        wall_char = libtcod.CHAR_DNW
    elif not north and south and east and not west:
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


def render_all(con, stats_panel, message_panel, mouse, fov_map, player, 
               objects):
    for y in range(consts.MAP_HEIGHT):
        for x in range(consts.MAP_WIDTH):
            if DebugShowWholeMap:
                visible = True
            else:
                visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = MapTiles[x][y].block_sight
            if not visible:
                if MapTiles[x][y].explored or DebugShowWholeMap:
                    if wall:
                        render_wall(con, x, y, consts.COLOR_DARK_WALL)
                    else:
                        libtcod.console_set_char_background(con, x, y,
                                                            consts.COLOR_DARK_GROUND,
                                                            libtcod.BKGND_SET)
            else:
                if wall:
                    render_wall(con, x, y, consts.COLOR_LIGHT_WALL)
                else:
                    libtcod.console_set_char_background(con, x, y, 
                                                        consts.COLOR_LIGHT_GROUND,
                                                        libtcod.BKGND_SET)
                MapTiles[x][y].explored = True
    for obj in objects:
        obj.draw(con, fov_map, DebugShowWholeMap)
    libtcod.console_blit(con, 0, 0, consts.MAP_WIDTH, consts.MAP_HEIGHT, 0, 0, 0)

    # Prepare to render the GUI stats_panel
    libtcod.console_set_default_background(stats_panel, libtcod.black)
    libtcod.console_clear(stats_panel)

    # Render the player stats
    render_bar(stats_panel, 1, 1, consts.BAR_WIDTH, 'HP', player.fighter.hp,
               player.fighter.max_hp, libtcod.red, libtcod.darker_red)

    # Render a list of what's under the mouse cursor
    libtcod.console_set_default_foreground(stats_panel, libtcod.light_gray)
    libtcod.console_print_ex(stats_panel, 1, 0, libtcod.BKGND_NONE, 
                             libtcod.LEFT, 
                             get_names_under_mouse(mouse, fov_map, objects))

    libtcod.console_blit(stats_panel, 0, 0, consts.SCREEN_WIDTH,
                         consts.PANEL_HEIGHT, 0, 0, consts.PANEL_Y)

    # Render the message log
    libtcod.console_blit(message_panel.render(), 0, 0, message_panel.width,
                         message_panel.height, 0, consts.MSG_X, consts.PANEL_Y)


def generate_fov_map(width, height):
    fov_map = libtcod.map_new(width, height)
    for y in range(height):
        for x in range(width):
            libtcod.map_set_properties(fov_map, x, y, 
                                       not MapTiles[x][y].block_sight,
                                       not MapTiles[x][y].blocked)
    return fov_map


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color,
               back_color, fore_color=libtcod.white):
    bar_width = int(float(value) / maximum * total_width)

    # Render the background
    libtcod.console_set_default_background(panel, back_color)
    libtcod.console_rect(panel, x, y, total_width, 1, False,
                         libtcod.BKGND_SCREEN)

    # Render the filled section of the bar
    libtcod.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        libtcod.console_rect(panel, x, y, bar_width, 1, False,
                             libtcod.BKGND_SCREEN)

    # Render centered text containing the actual value
    libtcod.console_set_default_foreground(panel, fore_color)
    label = consts.BAR_TEXT_TEMPLATE.format(name=name,
                                            value=value.__str__(),
                                            max=maximum.__str__())
    bar_center = x + total_width // 2
    libtcod.console_print_ex(panel, bar_center, y, libtcod.BKGND_NONE,
                             libtcod.CENTER, label)


def menu(console, header, options, width):
    if len(options) > 26:
        # TODO: Add pagination
        raise ValueError('Cannot have a menu with more than 26 options.')

    # Calculate total height for the header and one line per option
    header_height = libtcod.console_get_height_rect(console, 0, 0,
                                                    width, consts.SCREEN_HEIGHT,
                                                    header)
    height = len(options) + header_height

    window = libtcod.console_new(width, height)
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height,
                                  libtcod.BKGND_NONE, libtcod.LEFT, header)
    y = header_height
    letter_index = ord('a')
    for opt_txt in options:
        text = '(' + chr(letter_index) + ') ' + opt_txt
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE,
                                 libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # Blit the contents of "window" to the root console
    x = consts.SCREEN_WIDTH//2 - width//2
    y = consts.SCREEN_HEIGHT//2 - height//2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
    index = key.c - ord('a')
    if index >= 0 and index < len(options):
        return index
    return None


def show_inventory_menu(console, header, inventory):
    if len(inventory) == 0:
        options = [consts.MESSAGE_INVENTORY_EMPTY]
    else:
        options = [item.name for item in inventory]
    index = menu(console, header, options, consts.INVENTORY_WIDTH)
    if index is None or len(inventory) == 0:
        return None
    return inventory[index].item


def main():
    global MapTiles, FovRecompute, PlayerAction
    libtcod.sys_set_fps(consts.FPS_LIMIT)
    libtcod.console_set_custom_font(consts.TILESET, libtcod.FONT_TYPE_GREYSCALE
                                    | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT,
                              consts.GAME_TITLE,
                              False)
    con = libtcod.console_new(consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT)

    stat_panel = libtcod.console_new(consts.SCREEN_WIDTH, consts.PANEL_HEIGHT)
    message_panel = MessagePanel(consts.MSG_WIDTH, consts.MSG_HEIGHT)
    message_panel.append(consts.MESSAGE_GAME_START)
    objects = EntityList()
    player = Player(PlayerX, PlayerY)
    objects.append(player)
    map_gen = BspMapGenerator(consts.MAP_WIDTH, consts.MAP_HEIGHT,
                              consts.ROOM_MIN_SIZE, consts.BSP_RECURSION_DEPTH,
                              consts.BSP_FULL_ROOMS, consts.MAX_ROOM_MONSTERS,
                              consts.MAX_ROOM_ITEMS, player, message_panel)
    MapTiles = map_gen.generate_map()
    for obj in map_gen.objects:
        objects.append(obj)
    fov_map = generate_fov_map(consts.MAP_WIDTH, consts.MAP_HEIGHT)

    mouse = libtcod.Mouse()
    key = libtcod.Key()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS
                                    | libtcod.EVENT_MOUSE, key, mouse)
        if FovRecompute:
            FovRecompute = False
            libtcod.map_compute_fov(fov_map, player.x, player.y,
                                    consts.TORCH_RADIUS,
                                    consts.FOV_LIGHT_WALLS,
                                    consts.FOV_ALGORITHM)
        render_all(con, stat_panel, message_panel, mouse, fov_map, player,
                   objects)
        libtcod.console_flush()
        for obj in objects:
            obj.clear(con)
        libtcod.console_set_default_foreground(con, libtcod.white)
        PlayerAction = handle_keys(con, key, player, objects, message_panel)
        if PlayerAction == 'exit':
            break
        if GameState == 'playing' and PlayerAction != 'didnt-take-turn':
            for obj in objects:
                if obj.ai is not None:
                    obj.ai.take_turn(fov_map, MapTiles, objects, message_panel,
                                     player)


if __name__ == '__main__':
    main()
