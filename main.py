import Herbivore
import Plante
import Carnivore
import Gamedata
import time
# truc comme ça :
# gamedata = {'entities' : {'plante': [{'position' : (1,3)},{'position' : (3,4)}, {'position' : (1,0)}],'carnivores': [{'position' : (1,2)}],'herbivores': [{'position' : (5,2)}]}}


def init():
    gamedata = Gamedata.create(3,4,(10,10))
    return gamedata

def interract(gamedata, dt):
    #Herbivore turn
    allposition = Gamedata.get_allposition(gamedata)
    for i in Gamedata.get_herbivore(gamedata):

        if Herbivore.get_manger(i) == True:
            #Reproduction
            if Herbivore.canreproduce(i, gamedata, allposition):
                Herbivore.reproduce(i, gamedata, allposition)
                allposition = Gamedata.get_allposition(gamedata)
                i = Herbivore.setmanger(i, False)
        else:
            #Manger
            if Herbivore.caneat(i, gamedata) == True:
                Herbivore.eat(i, gamedata)
                allposition = Gamedata.get_allposition(gamedata)
                i = Herbivore.setmanger(i, True)

            else:
                #Chercher à manger et y aller
                if Herbivore.istherefood(i, gamedata):
                    Herbivore.gotofood(i,gamedata)




            



def show():
    pass

def run (gamedata):
    start_time = time_time()
    dt = time.time() - start_time
    while dt < 10:
        interract(gamedata, dt)
        show()

gamedata = init()

run(gamedata)
