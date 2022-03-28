""":
Carte d'identitée de creature
type : plante/animal
regime : eau/plante/animal
comportement : 
"""
import random
def create():
    creature = 'plante'
    regime = random.choice(['eau','plante','animal'])
    comportement = 'manger'
    skin = "?"
    color = random.randint(0,1000)
    position = (random.randint(0,10),random.randint(0, 10))
    return {'type' : creature , 'regime' : regime, 'comportement' : comportement, "skin" : skin, "color" : color, 'position' : position}

def get_type(creature : dict):
    assert type(creature) is dict
    return creature["type"]

def get_regime(creature : dict):
    assert type(creature) is dict
    return creature["regime"]

def get_skin(creature : dict):
    assert type(creature) is dict
    return creature["skin"]

def get_color(creature : dict):
    assert type(creature) is dict
    return creature["color"]

def get_position(creature : dict):
    assert type(creature) is dict
    return creature["position"]

def set_skin(creature : dict, newskin : str):
    assert type(creature) is dict
    assert type(newskin) is str
    creature['skin'] = newskin
    return creature

def set_position(creature : dict, newposition):
    creature['position'] = newposition
    return creature

def show(creature):
    pass

