import libtcodpy as libtcod


class Fighter:
    # Combat-related properties and methods (monster, player, NPC, etc.)
    def __init__(self, hp, defense, power, death_function=None):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.death_function = death_function

    def take_damage(self, damage, object_list, message_panel):
        # apply damage if possible
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            func = self.death_function
            if func is None:
                func(self.owner, object_list, message_panel)

    def attack(self, target, object_list, message_panel):
        damage = self.power - target.fighter.defense
        name = self.owner.name.capitalize()
        if damage > 0:
            message = '{} attacks {} for {} damage!'
            message = message.format(name, target.name, damage.__str__())
            message_panel.append(message, libtcod.red)
            target.fighter.take_damage(damage, object_list, message_panel)
        else:
            message = '{} attacks {}, but fails to deal any damage.'
            message = message.format(name)
            message_panel.append(message)

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp