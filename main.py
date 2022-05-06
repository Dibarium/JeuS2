import Herbivore
import Plante
import Carnivore
import Gamedata
import Map
import os
import time
import copy
import random
# truc comme ça :
# gamedata = {'entities' : {'plante': [{'position' : (1,3)},{'position' : (3,4)}, {'position' : (1,0)}],'carnivores': [{'position' : (1,2)}],'herbivores': [{'position' : (5,2)}]}}

def init():
    gamedata = Gamedata.create()
    gamedata['carte'] = Map.create(100, 30)
    numberofherbivore = 6
    numberofplantes = 200
    numberofcarnivore = 5
    for i in range(numberofherbivore):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addHerbivore(gamedata, validposition)
    for i in range(numberofplantes):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addPlante(gamedata, validposition)
    for i in range(numberofcarnivore):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addCarnivore(gamedata, validposition)

    return gamedata

def interract(gamedata, generation):
    #print("ooooooooooooo")
    if generation%3 == 0:
        allposition = Gamedata.get_allposition(gamedata)
        #Carnivore turn
        countcarnivore = 0
        for i in Gamedata.get_carnivore(gamedata):
            #print("-------------------")
            #print(i)
            Carnivore.set_last_eat(i, Carnivore.get_last_eat(i)-1)
            if Carnivore.isdead(i):
                Gamedata.kill_carnivore(gamedata, countcarnivore)
                allposition = Gamedata.get_allposition(gamedata)
            else:
                if Carnivore.get_manger(i) == True:
                    #reproduction
                    if Carnivore.can_reproduce(i, gamedata, allposition):
                        #print("se reproduit")
                        Carnivore.reproduce(i, gamedata, allposition)
                        allposition = Gamedata.get_allposition(gamedata)
                        i = Carnivore.set_manger(i, False)
                        #print(i)
                else:
                    #Manger
                    if Gamedata.get_herbivore(gamedata) != []:
                        if Carnivore.caneat(i, gamedata) == True:
                            #print("peut manger")
                            Carnivore.eat(i, gamedata)
                            i = Carnivore.reset_time_eat(i)
                            allposition = Gamedata.get_allposition(gamedata)
                            i = Carnivore.set_manger(i, True)
                            
                        else:
                            #Chercher à manger et y aller
                            #print("se dirige vers le manger")
                            i = Carnivore.gotofood(i,gamedata, allposition)
                gamedata['entities']['Carnivore'][countcarnivore] = i
            countcarnivore +=1
        #print(i)
    


    #Herbivore turn
    if generation%3 == 0:
        allposition = Gamedata.get_allposition(gamedata)
        countherbivore = 0
        for i in Gamedata.get_herbivore(gamedata):
            Herbivore.set_last_eat(i, Herbivore.get_last_eat(i)-1)
            if Herbivore.isdead(i):
                Gamedata.kill_herbivore(gamedata, countherbivore)
                allposition = Gamedata.get_allposition(gamedata)
            else:
                if Herbivore.get_manger(i) == True:
                    #reproduction
                    if Herbivore.can_reproduce(i, gamedata, allposition):
                        Herbivore.reproduce(i, gamedata, allposition)
                        allposition = Gamedata.get_allposition(gamedata)
                        i = Herbivore.set_manger(i, False)
                else:
                    #Manger
                    if Gamedata.get_plante(gamedata) != []:
                        if Herbivore.caneat(i, gamedata) == True:
                            #print("peut manger")
                            i = Herbivore.set_last_eat(i, i["max_last_eat"])
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

        #Nouvelles plantes
    if generation%10 == 1:
        for i in range(random.randint(5,40)):
            plante = Gamedata.randomposition(gamedata)
            gamedata = Gamedata.addPlante(gamedata, plante)

    return gamedata
        
def show(gamedata) -> None:
    newcarte = copy.deepcopy(gamedata['carte'])
    for i in Gamedata.get_herbivore(gamedata):
        newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
    for i in Gamedata.get_plante(gamedata):
        newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
    for i in Gamedata.get_carnivore(gamedata):
        newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
    Map.show(newcarte)
    #time.sleep(0.2)
        
    

def run(gamedata):
    os.system("clear")
    print("CHARGEMENT...")
    
    
    generation = 0
    while generation < 10000:
        gamedata = interract(gamedata, generation)
        show(gamedata)
        generation += 1

def main():
    gamedata = init()
    run(gamedata)
    
if __name__ == "__main__":
    main()
