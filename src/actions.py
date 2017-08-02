import libtcodpy as libtcod

def player_cast_heal(player, message_panel):
    if player.fighter.hp == player.fighter.max_hp:
        # TODO: Figure out why this gets called every frame
        message_panel.append('You are already at full health!')
        return 'cancelled'

    message_panel.append(
        'Your wounds start to feel better!',
        libtcod.light_violet,
    )
    heal_amount = 5
    player.fighter.heal(heal_amount)
    return None

#def cast_lightning()