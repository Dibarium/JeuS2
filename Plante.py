""":
Carte d'identitée de creature
type : plante/animal
regime : eau/plante/animal
comportement : 
"""
import random
def create(skin,carte):
    position = set_position(carte)
    return {"skin" : skin, 'position' : position}

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

def set_position(carte):
    goodplacement = False
    while goodplacement != True:
        x = random.randint(0, len(carte[0]))
        y = random.randint(0, len(carte))
        if carte[y][x] == "":
            goodplacement = True
            return (x,y)


def show(creature):
    pass

