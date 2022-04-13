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
    return gamedata
    
def addPlante(gamedata : dict, position : tuple):
    gamedata['entities']['Plante'].append(Plante.create(position))
    return gamedata

def addCarnivore(gamedata : dict, position : tuple) -> dict: 
    gamedata['entities']['Carnivore'].append(Carnivore.create(position))
    return gamedata

def addHerbivore(gamedata : dict, position : tuple) -> dict:
    herbivore = Herbivore.create(position)
    gamedata['entities']['Herbivore'].append(herbivore)
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
    allpos = []
    allpos.append((position[0]+1,position[1]))
    allpos.append((position[0]-1,position[1]))
    allpos.append((position[0],position[1]+1))
    allpos.append((position[0],position[1]-1))
    return allpos

def get_herbivore(gamedata : dict):
    return gamedata['entities']['Herbivore']

def get_carnivore(gamedata : dict):
    return gamedata['entities']['Carnivore']
  

def get_plante(gamedata : dict):
    return gamedata['entities']['Plante']
        
    
def get_herbivore_position(gamedata : dict) -> list:
    position = []
    for i in gamedata['entities']['Herbivore']:
        position.append(i['position'])
    return position

def get_carnivore_position(gamedata : dict) -> list:
    position = []
    for i in gamedata['entities']['Carnivore']:
        position.append(i['position'])
    return position

def get_plante_position(gamedata : dict) -> list:
    position = []
    for i in gamedata['entities']['Plante']:
        position.append(i['position'])
    return position

def kill_plante(gamedata : dict, plantetokill : int):
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
    return math.sqrt((position2[0]-position1[0])**2 +(position2[1]-position1[1])**2)
if __name__ == '__main__':
    game = create(1, 1, (10,10))

def count_nearby_entities(gamedata, creature, thingtocount):
    c = 0
    if type(thingtocount[0]) is tuple:
        for i in thingtocount:
            if distance(creature['position'], i) == 1:
                c += 1
    elif type(thingtocount[0]) is dict:
        for i in thingtocount:
            if distance(creature['position'], i['position']) == 1:
                c += 1
    else:
        print('error')
        assert 'error'
    return c