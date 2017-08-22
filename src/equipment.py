import libtcodpy as libtcod
import consts
from items import Item
from entity import Entity
import utils

class Equipment:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0):
        self.slot = slot
        self.is_equipped = False
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus

    def toggle_equip(self, inventory, message_panel):
        if self.is_equipped:
            self.dequip(message_panel)
        else:
            self.equip(inventory, message_panel)

    def equip(self, inventory, message_panel):
        old_equipment = utils.get_equipped_in_slot(inventory, self.slot)
        if old_equipment is not None:
            old_equipment.dequip(message_panel)
        self.is_equipped = True
        message = consts.MESSAGE_EQUIP
        message = message.format(item=self.owner.name,
                                 slot=self.slot)
        message_panel.append(message, consts.COLOR_MESSAGE_GOOD)

    def dequip(self, message_panel):
        self.is_equipped = True
        message = consts.MESSAGE_DEQUIP
        message = message.format(item=self.owner.name,
                                 slot=self.slot)
        message_panel.append(message, consts.COLOR_MESSAGE_NEUTRAL)

class SwordCopper(Entity):
    def __init__(self, x, y):
        equipment_component = Equipment(consts.SLOT_RIGHTHAND, power_bonus=2)
        item_component = Item()
        super(SwordCopper, self).__init__(x, y, consts.ITEM_SWORDCOPPER_NAME,
                                    consts.ITEM_SWORDCOPPER_CHAR,
                                    libtcod.copper,
                                    libtcod.BKGND_NONE,
                                    remain_visible=True,
                                    equipment=equipment_component,
                                    item=item_component)

class BucklerCopper(Entity):
    def __init__(self, x, y):
        equipment_component = Equipment(consts.SLOT_LEFTHAND, defense_bonus=1)
        item_component = Item()
        super(BucklerCopper, self).__init__(x, y, consts.ITEM_BUCKLERCOPPER_NAME,
                                            consts.ITEM_BUCKLERCOPPER_CHAR,
                                            libtcod.copper,
                                            libtcod.BKGND_NONE,
                                            remain_visible=True,
                                            equipment=equipment_component,
                                            item=item_component)