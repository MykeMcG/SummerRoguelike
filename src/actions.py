import libtcodpy as libtcod
import consts
import ai
import utils

def player_cast_heal(player, message_panel, **kwargs):
    if player.fighter.hp == player.fighter.max_hp:
        message_panel.append(consts.MESSAGE_HEAL_FAIL)
        return 'cancelled'

    message_panel.append(consts.MESSAGE_HEAL_SUCCESS,
                         consts.COLOR_MESSAGE_GOOD)
    heal_amount = consts_HEAL_AMOUNT
    player.fighter.heal(heal_amount)
    return None


def cast_lightning(caster, entities, message_panel, **kwargs):
    range = consts.LIGHTNING_RANGE
    damage = consts.LIGHTNING_DAMAGE
    target = utils.find_closest_target(caster, entities, range)
    if target is None:
        message_panel.append(consts.MESSAGE_LIGHTNING_FAIL)
        return 'cancelled'
    # TODO: Revise this line
    message = consts.MESSAGE_LIGHTNING_SUCCESS
    message = message.format(target.name, damage.__str__())
    message_panel.append(message, consts.COLOR_MESSAGE_DANGER)
    target.fighter.take_damage(damage, entities, message_panel)

def cast_confuse(caster, entities, message_panel, **kwargs):
    target = utils.find_closest_target(caster, entities, consts.CONFUSE_RANGE)
    if target is None:
        message_panel.append(consts.MESSAGE_CONFUSE_FAIL)
        return 'cancelled'
    if target.ai is not None:
        old_ai = target.ai
        new_ai = ai.ConfusedMonster(old_ai)
        new_ai.owner = target
        target.ai = new_ai
        message = consts.MESSAGE_CONFUSE_SUCCESS.format(target.name)
        message_panel.append(message, consts.COLOR_MESSAGE_WARNING)
    # TODO: Implement player confusion
