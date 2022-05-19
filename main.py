import Herbivore
import Plante
import Carnivore
import Gamedata
import Map
import Start_screen
import Joueur
import Parametrage
import Help_screen
import End_screen

import sys
import os
import time
import select
import tty 
import termios
import copy
import random


#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

def init():
    gamedata = Gamedata.create("Start")
    start = Start_screen.create()
    parametrage = Parametrage.create()
    joueur = Joueur.create((0,0))
    end = End_screen.create()
    return gamedata, start, parametrage, joueur, end
    
def creategame(gamedata, parametrage, state):
    gamedata = Gamedata.create(state)
    gamedata['carte'] = Map.create(100, 30)
    numberofherbivore = Parametrage.get_nbherbivore(parametrage)
    numberofplantes = Parametrage.get_nbplante(parametrage)
    numberofcarnivore = Parametrage.get_nbcarnivore(parametrage)
    for i in range(numberofherbivore):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addHerbivore(gamedata, validposition)
    for i in range(numberofplantes):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addPlante(gamedata, validposition)
    for i in range(numberofcarnivore):
        validposition = Gamedata.randomposition(gamedata)
        gamedata = Gamedata.addCarnivore(gamedata, validposition)
    joueur = Joueur.create(Gamedata.randomposition(gamedata))
    return gamedata, joueur

def tourjoueur(joueur, gamedata, generation, keypressed):
    allposition = Gamedata.get_allposition(gamedata)
    joueur = Joueur.move(joueur, gamedata, keypressed, allposition)
    if keypressed == " ":
        if Joueur.caneat(joueur, gamedata):
            gamedata = Joueur.eat(joueur, gamedata)
            joueur["score"] += 10
    return gamedata

def tourcarnivore(gamedata, generation):
    if generation%3 == 0:
        allposition = Gamedata.get_allposition(gamedata)
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
    return gamedata

def tourherbivore(gamedata, generation):
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
    return gamedata

def generationplantes(gamedata, generation):
    if generation%10 == 1:
        for i in range(random.randint(5,40)):
            plante = Gamedata.randomposition(gamedata)
            gamedata = Gamedata.addPlante(gamedata, plante)
    return gamedata

def interract(gamedata, start, parametrage, joueur, end, generation, Stop):
    currentstate = Gamedata.get_currentstate(gamedata)
    pressedkey = Joueur.get_key()

    if currentstate == "Start":
        if pressedkey == "\n":#Appuyer sur entré
            os.system('clear')
            current_selected = Start_screen.get_current_selected(start)
            if current_selected == "Play":
                Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Parametrage")
            elif current_selected == "Help":
                Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Help")
            elif current_selected == "Quit":
                Stop = True

        else:
            start = Start_screen.select(start, pressedkey)

    elif currentstate == "Help":
        if pressedkey == "\x1b":
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Start")

    elif currentstate == "Parametrage":
        if pressedkey == "\x1b":#Appuyer sur échap
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Start")
        elif pressedkey == "\n":#Appuyer sur entré
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Play")
            gamedata, joueur = creategame(gamedata, parametrage, "Play")
            
        else:
            parametrage = Parametrage.modify_value(parametrage, pressedkey)

    elif currentstate == "Play":
        if pressedkey == "\x1b":#Appuyer sur échap
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Start")
        elif Gamedata.is_game_ended(gamedata) == True:
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "End")

        else:
            gamedata = tourjoueur(joueur, gamedata, generation, pressedkey)
            gamedata = tourcarnivore(gamedata, generation)
            gamedata = tourherbivore(gamedata, generation)
            gamedata = generationplantes(gamedata, generation)

    elif currentstate == "End":
        if pressedkey == "\x1b":#Appuyer sur échap
            os.system('clear')
            Gamedata.change_currentstate(gamedata, Gamedata.get_currentstate(gamedata), "Start")
    return gamedata, start, parametrage, joueur, end, Stop, generation
        
def show(gamedata, start, parametrage, joueur, end, generation) -> None:
    currentstate = Gamedata.get_currentstate(gamedata)

    if currentstate == "Start":
        if generation%8==1:
            currentimage = start["frame_state"][0]
            Start_screen.show(start, start["all_frames"][currentimage])
            start = Start_screen.choose_image(start)
        Start_screen.showcursor(start)
        time.sleep(0.1)

    elif currentstate == "Help":
        Help_screen.show()

    elif currentstate == "Parametrage":
        Parametrage.showborder(parametrage)
        Parametrage.show(parametrage)

    elif currentstate == "Play":
        newcarte = copy.deepcopy(gamedata['carte'])
        for i in Gamedata.get_herbivore(gamedata):
            newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
        for i in Gamedata.get_plante(gamedata):
            newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
        for i in Gamedata.get_carnivore(gamedata):
            newcarte[i['position'][1]][i['position'][0]] = [i['skin'], i['color']]
        newcarte[joueur['position'][1]][joueur["position"][0]] = [joueur['skin'],joueur['color']]
        Map.show(newcarte)
        Joueur.show_score(joueur)
        #time.sleep(0.2)
    
    elif currentstate == "End":
        currentimage = end["frame_state"][0]
        End_screen.show(end, end["all_frames"][currentimage])
        end = End_screen.choose_image(end)
        time.sleep(0.2)
    

def run(gamedata, start, parametrage, joueur, end):
    os.system("clear")
    print("CHARGEMENT...")
    
    
    generation = 0
    Stop = False
    while Stop == False:

        gamedata, start, parametrage, joueur, end, Stop, generation = interract(gamedata, start, parametrage, joueur, end, generation, Stop)
        
        show(gamedata, start, parametrage, joueur, end, generation)
        generation += 1

def main():
    gamedata, start, parametrage, joueur, end = init()
    run(gamedata, start, parametrage, joueur, end)
    os.system('clear')
    print("MERCI D'AVOIR JOUE !")
    
if __name__ == "__main__":
    main()

