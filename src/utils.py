def find_closest_target(caster, entities, range):
    closest_target = None
    closest_dist = range + 1

    for obj in entities:
        if obj.fighter and obj != caster:
            dist = caster.distance_to(obj)
            if dist < closest_dist:
                closest_target = obj
                closest_dist = dist
    return closest_target