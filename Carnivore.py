import random
import Gamedata
def create(position : tuple) -> dict:
    skin = "?"
    return {"skin" : skin, 'position' : position, 'manger' : False}

def get_skin(creature : dict) -> str:
    assert type(creature) is dict
    return creature["skin"]

def get_position(creature : dict) -> bool:
    assert type(creature) is dict
    return creature["position"]

def get_manger(creature : dict) -> bool:
    assert type(creature) is dict
    return creature['manger']

def set_position(creature : dict, newposition) -> dict:
    """
    Return a dict with new position
    """
    creature['position'] = newposition
    return creature

def valid_move(gamedata: dict, allposition : list, newposition : tuple) -> dict:
    """
    Tells you if a move is possible or not
    """
    assert type(newposition) is tuple
    assert type(allposition) is list
    if newposition not in allposition and Map.isinmap(newposition, gamedata['carte']) :
        return True
    else:
        return False

def move(creature : dict, gamedata : dict, direction : str, allposition : list()) -> dict:
    """Move character"""
    actualposition = creature['position']

    if direction == 'Down':
        newposition = (actualposition[0], actualposition[1]+1)
        if valid_move(gamedata, allposition, newposition):
            return set_position(creature, newposition)
        else:
            return creature

    elif direction == 'Up':
        newposition = (actualposition[0], actualposition[1]-1)
        if valid_move(gamedata, allposition, newposition):
            return set_position(creature, newposition)
        else:
            return creature

    elif direction == "Left":
        newposition = (actualposition[0]-1, actualposition[1])
        if valid_move(gamedata, allposition, newposition):
            return set_position(creature, newposition)
        else:
            return creature
    
    elif direction == 'Right':
        newposition = (actualposition[0]+1, actualposition[1])
        if valid_move(gamedata, allposition, newposition):
            return set_position(creature, newposition)
        else:
            return creature
    else :
        print('error')
        assert 'pasdemove'

def can_reproduce(creature, gamedata, allposition) -> bool:
    """return True if there's room"""
    if Gamedata.count_nearby_entities(gamedata, creature, allposition) == 8:
        return False
    return True

def reproduce(creature, gamedata, allposition) -> dict:
    """place another herbivore around"""
    position = creature['position']
    nearbyposition = Gamedata.get_allposition_nearby(gamedata, position)
    for i in nearbyposition:
        if i not in allposition and Map.isinmap(i, gamedata['carte']):
            gamedata = Gamedata.addHerbivore(gamedata, i)
            return gamedata

def caneat(creature, gamedata) -> bool:
    """return True if plante nearby""" 
    plantepos = Gamedata.get_plante_position(gamedata)
    if Gamedata.count_nearby_entities(gamedata, creature, plantepos) >= 1:
        return True
    return False

def eat(creature, gamedata) -> dict:
    """found plante nearby and pop it"""
    plantes = Gamedata.get_plante(gamedata)
    for i in range(len(plantes)):
        if Gamedata.distance(plantes[i]['position'], creature['position']) == 1:
            gamedata = Gamedata.kill_plante(gamedata, i)
            return gamedata

def gotofood(creature, gamedata, allposition) -> tuple:
    plantepos = Gamedata.get_plante_position(gamedata)
    creaturepos = creature['position']
    closestplante = (Gamedata.distance(creaturepos, plantepos[0]), plantepos[0])
    for i in plantepos:
        distance = Gamedata.distance(creaturepos, i)
        if distance < closestplante[0]:
            closestplante = (distance,i)

    plantepos = closestplante[1]
    if creaturepos[0] != plantepos[0] and creaturepos[1] != plantepos[1]:
        i = random.randint(0,1)
        if i == 0:
            if plantepos[0] > creaturepos[0]:
                return move(creature, gamedata, "Right", allposition)
            else:
                return move(creature, gamedata, "Left", allposition)
        else :
            if plantepos[1] > creaturepos[1]:
                return move(creature, gamedata, "Down", allposition)
            else:
                return move(creature, gamedata, "Up", allposition)

    elif creaturepos[1] != plantepos[1]:
        if plantepos[1] > creaturepos[1]:
            return move(creature, gamedata, "Down", allposition)
        else:
            return move(creature, gamedata, "Up", allposition)

    elif creaturepos[0] != plantepos[0]:
        if plantepos[0] > creaturepos[0]:
            return move(creature, gamedata, "Right", allposition)
        else:
            return move(creature, gamedata, "Left", allposition)

if __name__ == "__main__":
    gamedata = {
    'carte' : [[[] for i in range(0,10)] for y in range(0,10)], 
    'entities' : {
        'plante': [{'position' : (3,0)},{'position' : (3,4)}],
        'carnivores': [{'position' : (1,2)}],
        'herbivores': [{'position' : (5,2)}]}}
    creature = create((0,0),"?", 10)
    print(creature)
    creature, asmoved = move(creature,'Right',gamedata)
    print(creature)
    print(asmoved)


