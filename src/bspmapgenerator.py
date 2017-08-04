import libtcodpy as libtcod
import random
from tile import Tile
import mobs
import items
from entityList import EntityList


class BspMapGenerator:
    def __init__(self, map_width, map_height, min_room_size,
                 generation_depth, full_rooms, max_room_monsters,
                 max_room_items, player, message_panel):
        self.map_width = map_width
        self.map_height = map_height
        self.min_room_size = min_room_size
        self.generation_depth = generation_depth
        self.full_rooms = full_rooms
        self.max_room_monsters = max_room_monsters
        self.max_room_items = max_room_items
        self.player = player
        self.objects = EntityList()
        self._map = []
        self._rooms = []
        self.message_panel = message_panel

    def _vline(self, x, y1, y2):
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False

    def _vline_up(self, x, y):
        while y >= 0 and self._map[x][y].blocked is True:
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False
            y -= 1

    def _vline_down(self, x, y):
        while y < self.map_height and self._map[x][y].blocked is True:
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False
            y += 1

    def _hline(self, x1, y, x2):
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False

    def _hline_left(self, x, y):
        while x >= 0 and self._map[x][y].blocked is True:
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False
            x -= 1

    def _hline_right(self, x, y):
        while x < self.map_width and self._map[x][y].blocked is True:
            self._map[x][y].blocked = False
            self._map[x][y].block_sight = False
            x += 1

    def _traverse_node(self, node, dat):
        # Create room
        if libtcod.bsp_is_leaf(node):
            minx = node.x + 1
            maxx = node.x + node.w - 1
            miny = node.y + 1
            maxy = node.y + node.h - 1
            if maxx == self.map_width - 1:
                maxx -= 1
            if maxy == self.map_height - 1:
                maxy -= 1

            if self.full_rooms is False:
                minx = libtcod.random_get_int(None, minx,
                                              maxx - self.min_room_size + 1)
                miny = libtcod.random_get_int(None, miny,
                                              maxy - self.min_room_size + 1)
                maxx = libtcod.random_get_int(None,
                                              minx + self.min_room_size - 2,
                                              maxx)
                maxy = libtcod.random_get_int(None,
                                              miny + self.min_room_size - 2,
                                              maxy)

            node.x = minx
            node.y = miny
            node.w = maxx - minx + 1
            node.h = maxy - miny + 1

            # Dig room
            for x in range(minx, maxx + 1):
                for y in range(miny, maxy + 1):
                    self._map[x][y].blocked = False
                    self._map[x][y].block_sight = False
            self._rooms.append(((minx + maxx) // 2, (miny + maxy) // 2))
            self._place_objects(minx, miny, maxx, maxy)
        # Create corridor
        else:
            left = libtcod.bsp_left(node)
            right = libtcod.bsp_right(node)
            node.x = min(left.x, right.x)
            node.y = min(left.y, right.y)
            node.w = max(left.x + left.w, right.x + right.w) - node.x
            node.h = max(left.y + left.h, right.y + right.h) - node.y
            if node.horizontal:
                if left.x + left.w - 1 < right.x \
                        or right.x + right.w - 1 < left.x:
                    x1 = libtcod.random_get_int(None, left.x,
                                                left.x + left.w - 1)
                    x2 = libtcod.random_get_int(None, right.x,
                                                right.x + right.w - 1)
                    y = libtcod.random_get_int(None, left.y + left.h, right.y)
                    self._vline_up(x1, y - 1)
                    self._hline(x1, y, x2)
                    self._vline_down(x2, y + 1)
                else:
                    minx = max(left.x, right.x)
                    maxx = min(left.x + left.w - 1, right.x + right.w - 1)
                    x = libtcod.random_get_int(None, minx, maxx)
                    self._vline_down(x, right.y)
                    self._vline_up(x, right.y - 1)
            else:
                if left.y + left.h - 1 < right.y \
                        or right.y + right.h - 1 < left.y:
                    y1 = libtcod.random_get_int(None, left.y,
                                                left.y + left.h - 1)
                    y2 = libtcod.random_get_int(None, right.y,
                                                right.y + right.h - 1)
                    x = libtcod.random_get_int(None, left.x + left.w, right.x)
                    self._hline_left(x - 1, y1)
                    self._vline(x, y1, y2)
                    self._hline_right(x + 1, y2)
                else:
                    miny = max(left.y, right.y)
                    maxy = max(left.y + left.h - 1, right.y + right.h - 1)
                    y = libtcod.random_get_int(None, miny, maxy)
                    self._hline_left(right.x - 1, y)
                    self._hline_right(right.x, y)
        return True

    def _generate_empty_map(self):
        self._map = [
            [Tile(True) for y in range(self.map_height)]
            for x in range(self.map_width)
        ]
        return self._map

    def _place_objects(self, x1, y1, x2, y2):
        num_monsters = libtcod.random_get_int(0, 0, self.max_room_monsters)
        for i in range(num_monsters):
            x = libtcod.random_get_int(0, x1 + 1, x2 - 1)
            y = libtcod.random_get_int(0, y1 + 1, y2 - 1)
            if libtcod.random_get_int(0, 0, 100) < 80:
                monster = mobs.Skeleton(x, y, libtcod.BKGND_NONE)
            else:
                monster = mobs.Kobold(x, y, libtcod.BKGND_NONE)
            if not monster.is_blocked(x, y, self._map, self.objects):
                self.objects.append(monster)

        num_items = libtcod.random_get_int(0, 0, self.max_room_items)
        for i in range(num_items):
            x = libtcod.random_get_int(0, x1 + 1, x2 - 1)
            y = libtcod.random_get_int(0, y1 + 1, y2 - 1)
            dice = libtcod.random_get_int(0, 0, 100)
            if dice < 70:
                item = items.HealthPotion(x, y)
            elif dice < 70 + 15:
                item = items.ScrollLightning(x, y)
            else:
                item = items.ScrollConfuse(x, y)
            self.objects.append(item)
            self.objects.send_to_back(item)

    def generate_map(self):
        self._map = self._generate_empty_map()
        bsp = libtcod.bsp_new_with_size(0, 0, self.map_width, self.map_height)
        libtcod.bsp_split_recursive(bsp, 0, self.generation_depth,
                                    self.min_room_size + 1,
                                    self.min_room_size + 1, 1.5, 1.5)
        libtcod.bsp_traverse_inverted_level_order(bsp, self._traverse_node)

        # TODO: Generate stairs

        player_room = random.choice(self._rooms)
        self._rooms.remove(player_room)
        self.player.x = player_room[0]
        self.player.y = player_room[1]

        return self._map
