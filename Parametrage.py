import sys
import os


def create():
    parametrage = {"nbherbivore" : 0, "nbcarnivore" : 0, "nbplante" : 0}
    return parametrage

def get_nbherbivore(parametrage):
    return parametrage["nbherbivore"]

def get_nbcarnivore(parametrage):
    return parametrage["nbcarnivore"]

def get_nbplante(parametrage):
    return parametrage["nbplante"]

def set_nbherbivore(parametrage, value):
    parametrage["nbherbivore"] += value
    return parametrage

def set_nbcarnivore(parametrage, value):
    parametrage["nbcarnivore"] += value
    return parametrage

def set_nbplante(parametrage, value):
    parametrage["nbplante"] += value
    return parametrage

def modify_value(parametrage, keypressed):
    #changer nombre herbivore
    if keypressed == "a":
        parametreage = set_nbherbivore(parametrage, 1)
    elif keypressed == "q":
        parametreage = set_nbherbivore(parametrage, -1)
    #changer nombre carnivore
    elif keypressed == "z":
        parametreage = set_nbcarnivore(parametrage, 1)
    elif keypressed == "s":
        parametreage = set_nbcarnivore(parametrage, -1)
    #changer nombre plantes
    elif keypressed == "e":
        parametreage = set_nbplante(parametrage, 1)
    elif keypressed == "d":
        parametreage = set_nbplante(parametrage, -1)

    for i in parametrage:
        if parametrage[i] < 0:
            parametrage[i] = 0
            
    return parametrage

def show(parametrage):
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    #herbivores
    sys.stdout.write("\033["+str(5)+";"+str(10)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mHerbivores\u001b[0m")
    sys.stdout.write("\033["+str(6)+";"+str(14)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m"+str(get_nbherbivore(parametrage))+"   \u001b[0m")
    sys.stdout.write("\033["+str(9)+";"+str(11)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m-Q   A+\u001b[0m")
    #carnivores
    sys.stdout.write("\033["+str(5)+";"+str(55)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mNombre Carnivores (z = +, s = -) : "+ str(get_nbcarnivore(parametrage)) +"   \u001b[0m")
    #plantes
    sys.stdout.write("\033["+str(5)+";"+str(100)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mNombre Plantes (e = +, d = -) : "+ str(get_nbplante(parametrage)) +"   \u001b[0m")
    sys.stdout.flush()

if __name__ == "__main__":
    parametrage = create()
    show(parametrage)