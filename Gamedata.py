import Carnivore
import Herbivore
import Plante
import Map
import random

def create(nbcarnivore : int, nbherbivore : int, mapsize : tuple) -> dict:
    gamedata = dict()
    gamedata['carte'] = Map.create(mapsize[0],mapsize[1])
    entities = {'Plante' : [], 'Carnivore' : [], 'Herbivore' : []}
    gamedata['entities'] = entities
    for i in range(1, random.randint(1,nbcarnivore)):
        gamedata = addCarnivore(gamedata, Carnivore.placement(gamedata), "?", 10)
    for i in range(1, random.randint(1,nbherbivore)):
        gamedata = addHerbivore(gamedata, Herbivore.placement(gamedata), "?", 10)
    for i in range(1, random.randint(1,10)):
        gamedata = addPlante(gamedata, "?", 10)

    print(gamedata['entities'])
    
def addPlante(gamedata : dict, skin : str, r_action : int):
    gamedata['entities']['Plante'].append(Plante.create(skin, r_action, gamedata))
    return gamedata

def addCarnivore(gamedata : dict, position : tuple, skin : str, r_action : int) -> dict: 
    gamedata['entities']['Carnivore'].append(Carnivore.create(position, skin, r_action))
    return gamedata

def addHerbivore(gamedata : dict, position : tuple, skin : str, r_action : int) -> dict:
    gamedata['entities']['Herbivore'].append(Herbivore.create(position, skin, r_action))
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
    herbivore = []
    for i in gamedata['entities']['Herbivore']:
        herbivore.append(i)
    return herbivore

def get_carnivore(gamedata : dict):
    carnivore = []
    for i in gamedata['entities']['Carnivore']:
        carnivore.append(i)
    return carnivore

def get_plante(gamedata : dict):
    plante = []
    for i in gamedata['entities']['Plante']:
        plante.append(i)
    return plante
    
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

def distance(position1, position2):
    return sqrt((position2[0]-position1[0])**2 +(position2[1]-position1[1])**2)
if __name__ == '__main__':
    game = create(1, 1, (10,10))
