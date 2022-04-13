import random
import Gamedata
import Map
import sys
def create(position : tuple) -> dict():
    return {"skin" : "♣", 'position' : position}

def get_skin(creature : dict) -> str:
    assert type(creature) is dict

    return creature["skin"]

def get_position(creature : dict) -> tuple:
    assert type(creature) is dict

    return creature["position"]
    
def set_skin(creature : dict, newskin : str) -> dict:
    assert type(creature) is dict
    assert type(newskin) is str

    creature['skin'] = newskin
    return creature

def randomposition(gamedata : dict) -> tuple:
    assert type(gamedata) is dict
    allposition = Gamedata.get_allposition(gamedata)
    mapsize = Map.get_size(gamedata['carte'])

    goodposition = False
    while goodposition != True:
        newposition = (random.randint(0, mapsize[0]-1), random.randint(0, mapsize[1]-1))
        if valid_move(gamedata, allposition, newposition):
            goodposition = True
            return newposition

def isinmap(newposition : tuple, carte : list) -> bool:
    """
    Tells you if the position is inside the map
    """
    assert type(newposition) is tuple
    assert type(carte) is list
    lenghtmap = (len(carte[0])-1, len(carte)-1)
    if newposition[0] >= 0 and newposition[0] <= lenghtmap[0] and newposition[1] >= 0 and newposition[1] <= lenghtmap[1] :
        return True
    else: 
        return False 

def valid_move(gamedata: dict, allposition : list, newposition : tuple) -> dict:
    """
    Tells you if a move is possible or not
    """
    assert type(newposition) is tuple
    assert type(allposition) is list
    if newposition not in allposition and isinmap(newposition, gamedata['carte']) :
        return True
    else:
        return False

def show(creature):
    pass

if __name__ == "__main__":
    gamedata = {
    'carte' : [[] for i in range(0,10)], 
    'entities' : {
        'plante': [{'position' : (1,3)},{'position' : (3,4)}],
        'carnivores': [{'position' : (1,2)}],
        'herbivores': [{'position' : (5,2)}]}}
    plante = create("?", 10, gamedata)
    print(plante)
