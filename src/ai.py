import libtcodpy as libtcod

class BasicMonster:
    #AI for a basic monster
    def take_turn(self, fov_map, map_tiles, objects, player):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y, map_tiles, objects)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player, objects)


class CowardMonster:
    #AI for a cowardly monster that runs from the player
    def take_turn(self, fov_map, map_tiles, objects, player):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_away(player.x, player.y, map_tiles, objects)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player, objects)
