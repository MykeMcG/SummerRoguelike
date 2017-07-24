import libtcodpy as libtcod

class Fighter:
    # Combat-related properties and methods (monster, player, NPC, etc.)
    def __init__(self, hp, defense, power, death_function=None):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.death_function = death_function

    def take_damage(self, damage, objectList, messagePanel):
        # apply damage if possible
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            function = self.death_function
            if function != None:
                function(self.owner, objectList, messagePanel)

    def attack(self, target, objectList, messagePanel):
        damage = self.power - target.fighter.defense
        if damage > 0:
            message = '{} attacks {} for {} damage!'
            messagePanel.append(message.format(self.owner.name.capitalize(), target.name, damage.__str__()), libtcod.red)
            target.fighter.take_damage(damage, objectList, messagePanel)
        else:
            message = '{} attacks {}, but fails to deal any damage.'
            print(message.format( self.owner.name.capitalize(), target.name))