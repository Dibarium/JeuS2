import random
import Gamedata
def create(skin : str, r_action : int, gamedata : dict) -> dict():
    assert type(gamedata) is dict
    assert type(skin) is str
    assert type(r_action) is int
    
    position = placement(gamedata)
    return {"skin" : skin, 'position' : position, 'r_action' : r_action}

def get_skin(creature : dict) -> str:
    assert type(creature) is dict

    return creature["skin"]

def get_r_action(creature : dict) -> int:
    assert type(creature) is dict

    return creature['r_action']

def get_position(creature : dict) -> tuple:
    assert type(creature) is dict

    return creature["position"]
    



def set_skin(creature : dict, newskin : str) -> dict:
    assert type(creature) is dict
    assert type(newskin) is str

    creature['skin'] = newskin
    return creature

def isdead(creature : dict, gamedata : dict):
    pass

def placement(gamedata : dict) -> tuple:
    assert type(gamedata) is dict

    maplength = (len(gamedata['carte'][0]), len(gamedata['carte']))
    allpos = Gamedata.get_allposition(gamedata)
    goodposition = False
    while goodposition != True:
        newposition = (random.randint(0, maplength[0]), random.randint(0, maplength[1]))
        if newposition not in allpos:
            goodposition = True
            return newposition
    

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
