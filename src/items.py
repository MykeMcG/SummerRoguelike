import libtcodpy as libtcod
from entity import Entity
import actions
import consts


class Item:
    def __init__(self, use_function=None):
        self.use_function = use_function

    def pick_up(self, objects, inventory):
        if len(inventory) >= 26:
            output = consts.MESSAGE_ITEM_PICKUP_FAIL
        else:
            inventory.append(self.owner)
            objects.remove(self.owner)
            output = consts.MESSAGE_ITEM_PICKUP_SUCCESS
        return output.format(self.owner.name)

    def use(self, inventory, message_panel, player=None, caster=None,
            entities=None, range=None, damage=None,):
        if self.use_function is None and self.owner.equipment is None:
            output = consts.MESSAGE_ITEM_USE_NOUSE
        elif self.owner.equipment:
            self.owner.equipment.toggle_equip(inventory, message_panel)
            return
        else:
            if self.use_function(player=player,
                                 message_panel=message_panel,
                                 caster=caster, entities = entities,
                                 range=range, damage=damage) != 'cancelled':
                inventory.remove(self.owner)
                output = consts.MESSAGE_ITEM_USE_SUCCESS
            else:
                output = consts.MESSAGE_ITEM_USE_FAIL
        message_panel.append(output.format(self.owner.name))

    def drop(self, player, object_list, inventory, message_panel):
        if self.owner.equipment:
            self.owner.equipment.dequip()

        # add to the map and remove from the player's inventory. also, place it at the player's coordinates
        object_list.append(self.owner)
        inventory.remove(self.owner)
        self.owner.x = player.x
        self.owner.y = player.y
        message = consts.MESSAGE_ITEM_DROP
        message = message.format(self.owner.name)
        message_panel.append(message, consts.COLOR_MESSAGE_NEUTRAL)

class HealthPotion(Entity):
    def __init__(self, x, y):
        item_component = Item(use_function=actions.player_cast_heal)
        super(HealthPotion, self).__init__(x, y, consts.ITEM_HEALTHPOTION_NAME,
                                           consts.ITEM_HEALTHPOTION_CHAR,
                                           libtcod.red, libtcod.BKGND_NONE,
                                           remain_visible=True,
                                           item=item_component,)


class ScrollLightning(Entity):
    def __init__(self, x, y):
        item_component = Item(use_function=actions.cast_lightning)
        super(ScrollLightning, self).__init__(x, y,
                                              consts.ITEM_SCROLLLIGHTNING_NAME,
                                              consts.ITEM_SCROLLLIGHTNING_CHAR,
                                              libtcod.light_yellow,
                                              libtcod.BKGND_NONE,
                                              remain_visible=True,
                                              item=item_component,)


class ScrollConfuse(Entity):
    def __init__(self, x, y):
        item_component = Item(use_function=actions.cast_confuse)
        super(ScrollConfuse, self).__init__(x, y,
                                            consts.ITEM_SCROLLCONFUSE_NAME,
                                            consts.ITEM_SCROLLCONFUSE_CHAR,
                                            libtcod.white,
                                            libtcod.BKGND_NONE,
                                            remain_visible=True,
                                            item=item_component)
