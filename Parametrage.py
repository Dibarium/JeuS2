import sys
import os


def create():
    parametrage = {"nbherbivore" : 5, "nbcarnivore" : 5, "nbplante" : 170}
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

def showborder(parametrage):
    f = open("carre.txt").read().split('\n')
    for i in range(len(f)):
        sys.stdout.write("\033["+str(5+i)+";"+str(5)+"H")
        sys.stdout.write(u"\u001b[1m\u001b[37m" + f[i] +"\u001b[0m")

        sys.stdout.write("\033["+str(5+i)+";"+str(53)+"H")
        sys.stdout.write(u"\u001b[1m\u001b[37m" + f[i] +"\u001b[0m")

        sys.stdout.write("\033["+str(5+i)+";"+str(100)+"H")
        sys.stdout.write(u"\u001b[1m\u001b[37m" + f[i] +"\u001b[0m")

def show(parametrage):
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    #herbivores
    sys.stdout.write("\033["+str(7)+";"+str(16)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m■ Grubbies ■\u001b[0m")
    sys.stdout.write("\033["+str(9)+";"+str(21)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m"+str(get_nbherbivore(parametrage))+"   \u001b[0m")
    sys.stdout.write("\033["+str(11)+";"+str(18)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m-Q   A+\u001b[0m")
    #carnivores
    sys.stdout.write("\033["+str(7)+";"+str(65)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m▲ Stabbers ▲\u001b[0m")
    sys.stdout.write("\033["+str(9)+";"+str(70)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m"+str(get_nbcarnivore(parametrage))+"   \u001b[0m")
    sys.stdout.write("\033["+str(11)+";"+str(67)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m-S   Z+\u001b[0m")
    #plantes
    sys.stdout.write("\033["+str(7)+";"+str(106)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m♣ Matières Organiques ♣\u001b[0m")
    sys.stdout.write("\033["+str(9)+";"+str(116)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m"+str(get_nbplante(parametrage))+"   \u001b[0m")
    sys.stdout.write("\033["+str(11)+";"+str(114)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37m-D   E+\u001b[0m")

    sys.stdout.write("\033["+str(100)+";"+str(100)+"H")
    sys.stdout.flush()

if __name__ == "__main__":
    parametrage = create()
    show(parametrage)