import random
import Gamedata
import Map
import sys
import os

def create(position : tuple) -> dict:
    skin = "■"
    return {"skin" : skin, 'position' : position, 'manger' : False, "color" : '34'}

def get_skin(creature : dict) -> str:
    assert type(creature) is dict
    return creature["skin"]

def get_position(creature : dict) -> bool:
    assert type(creature) is dict
    return creature["position"]

def get_manger(creature : dict) -> bool:
    assert type(creature) is dict
    return creature['manger']

def set_skin(creature : dict, newskin : str) -> dict:
    assert type(creature) is dict
    assert type(newskin) is str
    creature['skin'] = newskin
    return creature

def set_position(creature : dict, newposition) -> dict:
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



def can_reproduce(creature, gamedata, allposition) -> bool:
    """return True if there's room"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
    if Gamedata.count_nearby_entities(gamedata, creature, allposition) == 8:
        return False
    return True

def reproduce(creature, gamedata, allposition) -> dict:
    """place another herbivore around"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
    position = creature['position']
    nearbyposition = Gamedata.get_allposition_nearby(gamedata, position)
    for i in nearbyposition:
        if i not in allposition and Map.isinmap(i, gamedata['carte']):
            gamedata = Gamedata.addHerbivore(gamedata, i)
            return gamedata

def caneat(creature, gamedata) -> bool:
    """return True if plante nearby""" 
    assert type(creature) is dict
    assert type(gamedata) is dict
    plantepos = Gamedata.get_plante_position(gamedata)
    if Gamedata.count_nearby_entities(gamedata, creature, plantepos) >= 1:
        return True
    return False

def eat(creature, gamedata) -> dict:
    """found plante nearby and pop it"""
    assert type(creature) is dict
    assert type(gamedata) is dict
    plantes = Gamedata.get_plante(gamedata)
    for i in range(len(plantes)):
        if Gamedata.distance(plantes[i]['position'], creature['position']) == 1:
            gamedata = Gamedata.kill_plante(gamedata, i)
            return gamedata

def gotofood(creature, gamedata, allposition) -> tuple:
    assert type(creature) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list
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
    
        
        

def show(creature):
    creaturepo = (creature["position"][0],creature["position"][1])
    sys.stdout.write("\033["+str(creaturepo[1]+1)+";"+str(creaturepo[1]+1)+"H")
    sys.stdout.write(creature["skin"])

if __name__ == "__main__":
    gamedata = Gamedata.create(2, 2, (10,10))
    allpos = Gamedata.get_allposition(gamedata)
    gamedata = Gamedata.addHerbivore(gamedata, (0,0))
    creature = create((0,0))
    