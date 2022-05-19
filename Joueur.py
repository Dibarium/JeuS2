import random
import Gamedata
import Map

import sys
import os
import time
import select
import tty 
import termios

def create(position : tuple) -> dict:
    skin = "♥"
    return {"skin" : skin, 'position' : position, "color" : '33', "score" : 0}

def get_skin(joueur : dict) -> str:
    assert type(joueur) is dict
    return joueur["skin"]

def get_position(joueur : dict) -> bool:
    assert type(joueur) is dict
    return joueur["position"]

def set_position(joueur : dict, newposition) -> dict:
    """
    Return a dict with new position
    """
    assert type(joueur) is dict
    assert type(newposition) is tuple
    joueur['position'] = newposition
    return joueur

def valid_move(gamedata: dict, allposition : list, newposition : tuple) -> dict:
    """
    Tells you if a move is possible or not
    """
    assert type(gamedata) is dict
    assert type(newposition) is tuple
    assert type(allposition) is list
    if newposition not in allposition and Map.isinmap(newposition, gamedata['carte']) :
        return True
    else:
        return False

def move(joueur : dict, gamedata : dict, direction : str, allposition : list) -> dict:
    """Move character"""
    assert type(joueur) is dict
    assert type(gamedata) is dict
    assert type(allposition) is list

    actualposition = joueur['position']

    if direction == 's':
        newposition = (actualposition[0], actualposition[1]+1)
        if valid_move(gamedata, allposition, newposition):
            return set_position(joueur, newposition)
        else:
            return joueur

    if direction == 'z':
        newposition = (actualposition[0], actualposition[1]-1)
        if valid_move(gamedata, allposition, newposition):
            return set_position(joueur, newposition)
        else:
            return joueur

    if direction == "q":
        newposition = (actualposition[0]-1, actualposition[1])
        if valid_move(gamedata, allposition, newposition):
            return set_position(joueur, newposition)
        else:
            return joueur
    
    if direction == 'd':
        newposition = (actualposition[0]+1, actualposition[1])
        if valid_move(gamedata, allposition, newposition):
            return set_position(joueur, newposition)
        else:
            return joueur
    else :
        return joueur

def caneat(joueur, gamedata) -> bool:
    """return True if plante nearby""" 
    assert type(joueur) is dict
    assert type(gamedata) is dict
    pos = Gamedata.get_plante_position(gamedata)
    pos += Gamedata.get_carnivore_position(gamedata)
    pos += Gamedata.get_herbivore_position(gamedata)
    if Gamedata.count_nearby_entities(gamedata, joueur, pos) >= 1:
        return True
    return False

def eat(joueur, gamedata) -> dict:
    """found plante nearby and pop it"""
    assert type(joueur) is dict
    assert type(gamedata) is dict

    carnivores = Gamedata.get_carnivore(gamedata)
    for i in range(len(carnivores)):
        if Gamedata.distance(carnivores[i]['position'], joueur['position']) == 1:
            gamedata = Gamedata.kill_carnivore(gamedata, i)
            return gamedata
    
    herbivores = Gamedata.get_herbivore(gamedata)
    for i in range(len(herbivores)):
        if Gamedata.distance(herbivores[i]['position'], joueur['position']) == 1:
            gamedata = Gamedata.kill_herbivore(gamedata, i)
            return gamedata

    plantes = Gamedata.get_plante(gamedata)
    for i in range(len(plantes)):
        if Gamedata.distance(plantes[i]['position'], joueur['position']) == 1:
            gamedata = Gamedata.kill_plante(gamedata, i)
            return gamedata

def isData():
	#recuperation evenement clavier
	    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def get_key():
    if isData():
        c = sys.stdin.read(1)
        return c
        #return repr(c)

def show_score(joueur):
    sys.stdout.write("\033["+str(0)+";"+str(105)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mScore : "+str(joueur["score"])+"   \u001b[0m")

if __name__ == "__main__":
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    while True:
        key = get_key()
        if key != None:
            print(key)