import Herbivore
import Plante
import Carnivore
import Gamedata
import Map
import os
import time
import copy
# truc comme ça :
# gamedata = {'entities' : {'plante': [{'position' : (1,3)},{'position' : (3,4)}, {'position' : (1,0)}],'carnivores': [{'position' : (1,2)}],'herbivores': [{'position' : (5,2)}]}}

def init():
    gamedata = Gamedata.create()
    gamedata['carte'] = Map.create(100, 30)
    for i in range(1):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addHerbivore(gamedata, validposition)
    for i in range(100):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addPlante(gamedata, validposition)
    return gamedata

def interract(gamedata, dt):
    #Herbivore turn
    allposition = Gamedata.get_allposition(gamedata)
    countherbivore = 0
    for i in Gamedata.get_herbivore(gamedata):
        #print("---------------------")
        #print(countherbivore)
        #print(i)
        if Herbivore.get_manger(i) == True:
            #Reproduction
            #print("reproduction")
            if Herbivore.can_reproduce(i, gamedata, allposition):
                Herbivore.reproduce(i, gamedata, allposition)
                allposition = Gamedata.get_allposition(gamedata)
                i = Herbivore.set_manger(i, False)
        else:
            #Manger
            if Gamedata.get_plante(gamedata) != []:
                if Herbivore.caneat(i, gamedata) == True:
                    #print("peut manger")
                    gamedata = Herbivore.eat(i, gamedata)
                    allposition = Gamedata.get_allposition(gamedata)
                    i = Herbivore.set_manger(i, True)

                else:
                    #Chercher à manger et y aller
                    #print("aller vers manger")
                    i = Herbivore.gotofood(i,gamedata, allposition)
        #print(i)
        gamedata['entities']['Herbivore'][countherbivore] = i
        countherbivore +=1
    return gamedata
        
def show(gamedata) -> None:
    newcarte = copy.deepcopy(gamedata['carte'])
    for i in Gamedata.get_herbivore(gamedata):
        newcarte[i['position'][1]][i['position'][0]] = i['skin']
    for i in Gamedata.get_plante(gamedata):
        newcarte[i['position'][1]][i['position'][0]] = i['skin']
    Map.show(newcarte)
    time.sleep(0.5)
        
    

def run ():
    os.system("clear")
    print("CHARGEMENT...")
    
    gamedata = init()
    start_time = time.time()
    dt = time.time() - start_time
    while dt < 100:
        gamedata = interract(gamedata, dt)
        show(gamedata)
        dt = time.time() - start_time

if __name__ == "__main__":
    run()
