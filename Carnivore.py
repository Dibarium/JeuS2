import random
import Gamedata
import Map
def create(position : tuple) -> dict:
    assert type(position) is tuple
    skin = "▲"
    return {"skin" : skin, 'position' : position, 'manger' : False, "color" : '31', "last_eat" : 22, "max_last_eat" : 22}

def get_last_eat(creature : dict) -> int:
    assert type(creature) is dict
    return creature["last_eat"]

def get_max_last_eat(creature : dict) -> int:
    assert type(creature) is dict
    return creature["max_last_eat"]

def get_skin(creature : dict) -> str:
    assert type(creature) is dict
    return creature["skin"]

def get_position(creature : dict) -> bool:
    assert type(creature) is dict
    return creature["position"]

def get_manger(creature : dict) -> bool:
    assert type(creature) is dict
    return creature['manger']

def set_last_eat(creature, value):
    assert type(creature) is dict
    creature["last_eat"] = value
    return creature

def set_position(creature : dict, newposition : tuple) -> dict:
    """
    Return a dict with new position
    """
    assert type(creature) is dict
    assert type(newposition) is tuple
    creature['position'] = newposition
    return creature

def set_manger(creature : dict, etat : bool) -> dict :
    assert type(creature) is dict
    assert type(etat) is bool
    creature["manger"] = etat
    return creature 

def valid_move(gamedata: dict, allposition : list, newposition : tuple) -> dict:
    """
    Tells you if a move is possible or not
    """
    assert type(gamedata) is dict
    assert type(newposition) is tuple
    assert type(allposition) is list
    if newposition not in allposition and Map.isinmap(newposition, gamedata['carte']) :
        return True
    else:
        return False

def move(creature : dict, gamedata : dict, direction : str, allposition : list) -> dict:
    """Move character"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(direction) is str
    assert type(allposition) is list
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

def can_reproduce(creature : dict, gamedata : dict, allposition : list) -> bool:
    """return True if there's room"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
    if Gamedata.count_nearby_entities(gamedata, creature, allposition) == 8:
        return False
    return True

def reproduce(creature, gamedata, allposition) -> dict:
    """place another Carnivore around"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
    position = creature['position']
    nearbyposition = Gamedata.get_allposition_nearby(gamedata, position)
    for i in nearbyposition:
        if i not in allposition and Map.isinmap(i, gamedata['carte']):
            gamedata = Gamedata.addCarnivore(gamedata, i)
            return gamedata

def caneat(creature, gamedata) -> bool:
    """return True if herbivore nearby""" 
    assert type(creature) is dict
    assert type(gamedata) is dict
    herbivorepos = Gamedata.get_herbivore_position(gamedata)
    if Gamedata.count_nearby_entities(gamedata, creature, herbivorepos) >= 1:
        return True
    return False

def eat(creature, gamedata) -> dict:
    """found herbivore nearby and pop it"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    herbivores = Gamedata.get_herbivore(gamedata)
    for i in range(len(herbivores)):
        if Gamedata.distance(herbivores[i]['position'], creature['position']) == 1:
            gamedata = Gamedata.kill_herbivore(gamedata, i)
            return gamedata

def gotofood(creature, gamedata, allposition) -> tuple:
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
    herbivorepos = Gamedata.get_herbivore_position(gamedata)
    creaturepos = creature['position']
    closestherbivore = (Gamedata.distance(creaturepos, herbivorepos[0]), herbivorepos[0])
    for i in herbivorepos:
        distance = Gamedata.distance(creaturepos, i)
        if distance < closestherbivore[0]:
            closestherbivore = (distance,i)

    herbivorepos = closestherbivore[1]
    if creaturepos[0] != herbivorepos[0] and creaturepos[1] != herbivorepos[1]:
        i = random.randint(0,1)
        if i == 0:
            if herbivorepos[0] > creaturepos[0]:
                return move(creature, gamedata, "Right", allposition)
            else:
                return move(creature, gamedata, "Left", allposition)
        else :
            if herbivorepos[1] > creaturepos[1]:
                return move(creature, gamedata, "Down", allposition)
            else:
                return move(creature, gamedata, "Up", allposition)

    elif creaturepos[1] != herbivorepos[1]:
        if herbivorepos[1] > creaturepos[1]:
            return move(creature, gamedata, "Down", allposition)
        else:
            return move(creature, gamedata, "Up", allposition)

    elif creaturepos[0] != herbivorepos[0]:
        if herbivorepos[0] > creaturepos[0]:
            return move(creature, gamedata, "Right", allposition)
        else:
            return move(creature, gamedata, "Left", allposition)
    else:
        return creature

def isdead(creature : dict) -> bool:
    assert type(creature) is dict
    if get_last_eat(creature) <= 0:
        return True
    return False

def reset_time_eat(creature : dict) -> dict:
    assert type(creature) is dict
    creature = set_last_eat(creature, creature["max_last_eat"])
    return creature

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


