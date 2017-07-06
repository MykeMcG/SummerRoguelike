import libtcodpy as libtcod
from tile import Tile
from rect import Rect
from entity import Entity

class BasicMapGenerator:
    def __init__(self):
        return

    def _generate_empty_map(self, width, height):
        empty_map = [[Tile(True)
            for y in range(height)]
                for x in range(width)]
        return empty_map

    def _create_room(self, room, out_map):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                out_map[x][y].blocked = False
                out_map[x][y].block_sight = False

    def _create_h_tunnel(self, x1, x2, y, out_map):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            out_map[x][y].blocked = False
            out_map[x][y].block_sight = False

    def _create_v_tunnel(self, x, y1, y2, out_map):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            out_map[x][y].blocked = False
            out_map[x][y].block_sight = False

    def generate_map(self, width, height, room_min_size, room_max_size, max_rooms, player):
        new_map = self._generate_empty_map(width, height)
        rooms = []
        num_rooms = 0
        for r in range(max_rooms):
            w = libtcod.random_get_int(0, room_min_size, room_max_size)
            h = libtcod.random_get_int(0, room_min_size, room_max_size)
            x = libtcod.random_get_int(0, 0, width - w - 1)
            y = libtcod.random_get_int(0, 0, height - h - 1)
            new_room = Rect(x, y, w, h)

            failed = False
            for old_room in rooms:
                if new_room.intersect(old_room):
                    failed = True
                    break
            if not failed:
                self._create_room(new_room, new_map)
                (new_x, new_y) = new_room.center()
                if num_rooms == 0:
                    player.x = new_x
                    player.y = new_y
                else:
                    #Dig the tunnels
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    #Flip a coin to see if we go horizontally then vertically, or vice-versa
                    if libtcod.random_get_int(0, 0, 1) == 1:
                        self._create_h_tunnel(prev_x, new_x, prev_y, new_map)
                        self._create_v_tunnel(new_x, prev_y, new_y, new_map)
                    else:
                        self._create_v_tunnel(prev_x, prev_y, new_y, new_map)
                        self._create_h_tunnel(prev_x, new_x, new_y, new_map)
                rooms.append(new_room)
                num_rooms += 1
        return new_map

