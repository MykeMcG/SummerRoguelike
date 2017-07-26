import libtcodpy as libtcod
from entity import Entity


class Item:
    def pick_up(self, objects, inventory):
        if len(inventory) >= 26:
            output = "Your inventory is full. Unable to pick up {}."
        else:
            inventory.append(self.owner)
            objects.remove(self.owner)
            output = "You picked up a {}."
        # TODO: Fix bug where item name doesn't show
        output.format(self.owner.name)
        return output

class HealthPotion(Entity):
    def __init__(self, x, y):
        itemComponent = Item()
        super(HealthPotion, self).__init__(x, y, "health potion", 173, libtcod.red, libtcod.BKGND_NONE, item=itemComponent)