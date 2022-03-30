import random
def create(position, skin, r_action):
    skin = "?"
    return {"skin" : skin, 'position' : position, 'r_action' : r_action, 'manger' : False}

def get_skin(creature : dict) -> str:
    assert type(creature) is dict

    return creature["skin"]

def get_r_action(creature : dict) -> int:
    assert type(creature) is dict

    return creature["r_action"]

def get_position(creature : dict) -> bool:
    assert type(creature) is dict

    return creature["position"]

def get_manger(creature : dict) -> bool:
    assert type(creature) is dict

    return creature['manger']

def get_allposition(gamedata : dict) -> list:
    assert type(gamedata) is dict

    #gamedata = {'entities' : {'plante': [{'position' : (1,3)},{'position' : (3,4)}, {'position' : (1,0)}],'carnivores': [{'position' : (1,2)}],'herbivores': [{'position' : (5,2)}]}}
    position = []
    for i in gamedata['entities']:
        for y in gamedata['entities'][i]:
            position.append(y['position'])
    return position



def set_skin(creature : dict, newskin : str) -> dict:
    assert type(creature) is dict
    assert type(newskin) is str

    creature['skin'] = newskin
    return creature

def set_position(creature : dict, newposition):
    creature['position'] = newposition
    return creature

def isinmap(newposition : tuple, carte : list) -> bool:
    assert type(newposition) is tuple
    assert type(carte) is list

    lengthmap = (len(carte[0]), len(carte))
    if newposition[0] >= 0 and newposition[0] <= lengthmap[0] and newposition[1] >= 0 and newposition[1] <= lenghtmap[1] :
        return True
    else: 
        return False 

def valid_move(creature : dict, allposition : list, newposition : tuple) -> dict:
    assert type(newposition) is tuple
    assert type(allposition) is list
    assert type(creature) is dict

    if newposition not in allposition and isinmap(newposition, gamedata['carte']) :
        return set_position(creature, newposition)
    else:
        return creature

def move(creature : dict, direction : str, gamedata : dict) -> dict:
    actualposition = creature['position']
    allposition = get_allposition(gamedata)

    if direction == 'Down':
        newposition = (actualposition[0], actualposition[1]+1)
        return valid_move(creature, allposition, newposition)

    elif direction == 'Up':
        newposition = (actualposition[0], actualposition[1]-1)
        return valid_move(creature, allposition, newposition)

    elif direction == "Left":
        newposition = (actualposition[0]-1, actualposition[1])
        return valid_move(creature, allposition, newposition)
    
    elif direction == 'Right':
        newposition = (actualposition[0]+1, actualposition[1])
        return valid_move(creature, allposition, newposition)
    else :
        print('error')
        assert 'pasdemove'

def show(creature):
    pass

