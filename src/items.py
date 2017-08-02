import libtcodpy as libtcod
from entity import Entity
import actions


class Item:
    def __init__(self, use_function=None):
        self.use_function = use_function

    def pick_up(self, objects, inventory):
        if len(inventory) >= 26:
            output = 'Your inventory is full. Unable to pick up {}.'
        else:
            inventory.append(self.owner)
            objects.remove(self.owner)
            output = 'You picked up a {}.'
        return output.format(self.owner.name)

    def use(self, inventory, message_panel, player=None):
        if self.use_function is None:
            output = 'The {} cannot be used.'
        else:
            if self.use_function(player=player,
                                 message_panel=message_panel) != 'cancelled':
                inventory.remove(self.owner)
                output = 'Used the {}.'
            else:
                output = 'Unable to use the {}.'
        message_panel.append(output.format(self.owner.name))


class HealthPotion(Entity):
    def __init__(self, x, y):
        item_component = Item(use_function=actions.player_cast_heal)
        super(HealthPotion, self).__init__(
            x,
            y,
            "health potion",
            173,
            libtcod.red,
            libtcod.BKGND_NONE,
            item=item_component,
        )


class ScrollLightning(Entity):
    def __init__(self, x, y):
        item_component = Item(use_function=actions.cast_lightning)
        super(ScrollLightning, self).__init__(
            x,
            y,
            "scroll of lightning bolt",
            '#',
            libtcod.light_yellow,
            item=item_component,
        )
