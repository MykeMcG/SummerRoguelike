from tile import Tile
from rect import Rect

class MapGenerator:
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

    def generate(self, width, height):
        new_map = self._generate_empty_map(width, height)
        room1 = Rect(20, 15, 10, 15)
        room2 = Rect(50, 15, 10, 15)
        self._create_room(room1, new_map)
        self._create_room(room2, new_map)
        self._create_h_tunnel(25, 55, 23, new_map)
        return new_map

