class Fighter:
    #Combat-related properties and methods (monster, player, NPC, etc.)
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power