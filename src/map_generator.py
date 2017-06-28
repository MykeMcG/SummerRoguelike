from tile import tile

class map_generator:
    def __init__(self):
        return

    def _generate_empty_map(self, width, height):
        empty_map = [[ tile(False)
            for y in range(height)]
                for x in range(width)]
        return empty_map

    def generate(self, width, height):
        new_map = self._generate_empty_map(width, height)
        new_map[30][22].blocked = True
        new_map[30][22].block_sight = True
        new_map[50][22].blocked = True
        new_map[50][22].block_sight = True
        return new_map

