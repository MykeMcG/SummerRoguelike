import libtcodpy as libtcod
import consts
import utils

def player_cast_heal(player, message_panel, **kwargs):
    if player.fighter.hp == player.fighter.max_hp:
        message_panel.append('You are already at full health!')
        return 'cancelled'

    message_panel.append(
        'Your wounds start to feel better!', consts.COLOR_MESSAGE_GOOD)
    heal_amount = 5
    player.fighter.heal(heal_amount)
    return None


def cast_lightning(caster, entities, message_panel, **kwargs):
    range = consts.LIGHTNING_RANGE
    damage = consts.LIGHTNING_DAMAGE
    target = utils.find_closest_target(caster, entities, range)
    if target is None:
        message_panel.append("Failed to cast lightning: No target in range.")
        return 'cancelled'
    # TODO: Revise this line
    message = "A lightning bolt strikes the {} with a loud thunder! "\
              + "The {} loses {} HP!"
    message = message.format(target.name, target.name, damage.__str__())
    message_panel.append(message, consts.COLOR_MESSAGE_DANGER)
    target.fighter.take_damage(damage, entities, message_panel)
