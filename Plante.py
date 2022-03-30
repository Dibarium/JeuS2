import random
def create(skin : str, r_action : int, gamedata : dict) -> dict():
    assert type(gamedata) is dict
    assert type(skin) is str
    assert type(r_action) is int
    
    position = move(gamedata)
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


def move(gamedata : dict) -> tuple:
    assert type(gamedata) is dict

    maplength = (len(gamedata['carte'][0]), len(gamedata['carte']))
    allpos = get_allposition(gamedata)
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
    creature = create("?", 10, gamedata)
    print(creature)
