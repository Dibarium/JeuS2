import Carnivore
import Herbivore
import Plante
import Map
import random
import math

def create() -> dict:
    gamedata = dict()
    gamedata['carte'] = None
    entities = {'Plante' : [], 'Carnivore' : [], 'Herbivore' : []}
    gamedata['entities'] = entities
    gamedata["currentstate"] = {"Start" : True, "Parametrage" : False, "Help" : False, "Play" : False}
    gamedata["since_last_generation"] = 0
    return gamedata

def get_since_last_generation(gamedata):
    return gamedata["since_last_generation"]

def set_since_last_generation(gamedata : dict, newvalue : int):
    gamedata["since_last_generation"] = newvalue
    return gamedata

def set_currentstate(gamedata : dict, newstate : str, newvalue : bool)-> dict:
    gamedata["currentstate"][newstate] = newvalue
    return gamedata

def change_currentstate(gamedata : dict,currentstate: str , newstate : str):
    gamedata = set_currentstate(gamedata, newstate, True)
    gamedata = set_currentstate(gamedata, currentstate, False)
    return gamedata

def get_allposition(gamedata : dict) -> list:
    assert type(gamedata) is dict
    #gamedata = {'entities' : {'plante': [{'position' : (1,3)},{'position' : (3,4)}, {'position' : (1,0)}],'carnivores': [{'position' : (1,2)}],'herbivores': [{'position' : (5,2)}]}}
    position = []
    for i in gamedata['entities']:
        for y in gamedata['entities'][i]:
            position.append(y['position'])
    return position

def get_allposition_nearby(gamedata : dict, position : tuple) -> list:
    assert type(gamedata) is dict
    assert type(position) is tuple
    allpos = []
    for y in range(-1,2):
        for x in range(-1,2):
            allpos.append((position[0]+x,position[1]+y))
    return allpos

def get_herbivore(gamedata : dict):
    assert type(gamedata) is dict
    return gamedata['entities']['Herbivore']

def get_carnivore(gamedata : dict):
    assert type(gamedata) is dict
    return gamedata['entities']['Carnivore']
  
def get_plante(gamedata : dict):
    assert type(gamedata) is dict
    return gamedata['entities']['Plante']
        
def get_herbivore_position(gamedata : dict) -> list:
    assert type(gamedata) is dict
    position = []
    for i in gamedata['entities']['Herbivore']:
        position.append(i['position'])
    return position

def get_carnivore_position(gamedata : dict) -> list:
    assert type(gamedata) is dict
    position = []
    for i in gamedata['entities']['Carnivore']:
        position.append(i['position'])
    return position

def get_plante_position(gamedata : dict) -> list:
    assert type(gamedata) is dict
    position = []
    for i in gamedata['entities']['Plante']:
        position.append(i['position'])
    return position

def get_currentstate(gamedata : dict) -> dict:
    for i in gamedata["currentstate"]:
        if gamedata["currentstate"][i] == True:
            return i
    

def addPlante(gamedata : dict, position : tuple):
    assert type(gamedata) is dict
    assert type(position) is tuple
    gamedata['entities']['Plante'].append(Plante.create(position))
    return gamedata

def addCarnivore(gamedata : dict, position : tuple) -> dict: 
    assert type(gamedata) is dict
    assert type(position) is tuple
    carnivore = Carnivore.create(position)
    gamedata['entities']['Carnivore'].append(carnivore)
    return gamedata

def addHerbivore(gamedata : dict, position : tuple) -> dict:
    assert type(gamedata) is dict
    assert type(position) is tuple
    herbivore = Herbivore.create(position)
    gamedata['entities']['Herbivore'].append(herbivore)
    return gamedata

def kill_plante(gamedata : dict, plantetokill : int):
    assert type(gamedata) is dict
    assert type(plantetokill) is int
    gamedata['entities']['Plante'].pop(plantetokill)
    return gamedata

def kill_carnivore(gamedata : dict, carnivoretokill : int):
    assert type(carnivoretokill) is int
    gamedata['entities']['Carnivore'].pop(carnivoretokill)
    return gamedata

def kill_herbivore(gamedata : dict, herbivoretokill : int):
    assert type(herbivoretokill) is int
    gamedata['entities']['Herbivore'].pop(herbivoretokill)
    return gamedata

def distance(position1, position2):
    assert type(position1) is tuple
    assert type(position2) is tuple
    return math.sqrt((position2[0]-position1[0])**2 +(position2[1]-position1[1])**2)
if __name__ == '__main__':
    game = create(1, 1, (10,10))

def count_nearby_entities(gamedata, creature, thingtocount):
    assert type(gamedata) is dict
    assert type(creature) is dict
    c = 0
    if type(thingtocount[0]) is tuple:
        for i in thingtocount:
            if distance(creature['position'], i) == 1:
                c += 1
    return c

def randomposition(gamedata : dict) -> tuple:
    assert type(gamedata) is dict
    allposition = get_allposition(gamedata)
    mapsize = Map.get_size(gamedata['carte'])

    goodposition = False
    while goodposition != True:
        newposition = (random.randint(0, mapsize[0]-1), random.randint(0, mapsize[1]-1))
        if Herbivore.valid_move(gamedata, allposition, newposition):
            goodposition = True
            return newposition