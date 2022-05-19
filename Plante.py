import sys

def create(position : tuple) -> dict():
    return {"skin" : "♣", 'position' : position, "color" : '32'}

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

def valid_move(gamedata: dict, allposition : list, newposition : tuple) -> bool:
    """
    Tells you if a move is possible or not
    """
    assert type(gamedata) is dict
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
