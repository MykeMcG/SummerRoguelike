import libtcodpy as libtcod
import consts

class BasicMonster:
    #AI for a basic monster
    def take_turn(self, fov_map, map_tiles, objects, message_panel, player):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y, map_tiles, objects)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player, objects, message_panel)


class CowardMonster:
    #AI for a cowardly monster that runs from the player
    def take_turn(self, fov_map, map_tiles, objects, message_panel, player):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_away(player.x, player.y, map_tiles, objects)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player, objects, message_panel)


class ConfusedMonster:
    # AI for a confused monster that just kind of bumbles around
    def __init__(self, old_ai, num_turns=consts.CONFUSE_NUM_TURNS):
        self.old_ai = old_ai
        self.num_turns = num_turns

    def take_turn(self, fov_map, map_tiles, objects, message_panel, player):
        if self.num_turns > 0: # Still confused
            delta_x = libtcod.random_get_int(0, -1, 1)
            delta_y = libtcod.random_get_int(0, -1, 1)
            self.owner.move(delta_x, delta_y, map_tiles, objects)
            self.num_turns -= 1
        else:
            self.owner.ai = self.old_ai
            message = consts.MESSAGE_CONFUSE_END.format(self.owner.name)
            message_panel.append(message, consts.COLOR_MESSAGE_WARNING)
