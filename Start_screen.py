import sys
import os
import time

def create():
    dossier = "Ecran_titre/"
    filenames = ["Ecran_titre.txt","Frame_2.txt", "Frame_3.txt", "Frame_4.txt"]
    frames = []
    for name in filenames:
        f = open(dossier+name).read().split("\n")
        frames.append([list(word) for word in f])
    return {"selected" : {"Play" : True, "Help": False, "Quitter" : False}, "all_frames" : frames, "frame_state" : (0,False)}

def get_current_selected(start):
    for i in start["selected"]:
        if start["selected"][i] == True:
            return i

def get_all_frames(start):
    return start["all_frames"]

def get_framestate(start):
    return start["frame_state"]

def set_frame_state(start, newvalue):
    start["frame_state"] = newvalue
    return start

def set_selected(start : dict, keyword : str, newstate : bool) -> dict:
    start["selected"][keyword] = newstate
    return start

def show(start, frame):
    #Couleur
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    #Background
    for y in range(len(frame)):
        for x in range(len(frame[y])):
            s="\033["+str(y)+";"+str(x)+"H"
            sys.stdout.write(s)
            sys.stdout.write(u"\u001b[1m\u001b[37 m" + frame[y][x] +"\u001b[0m")
            
    #Afficher play
    sys.stdout.write("\033["+str(25)+";"+str(49)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mPLAY\u001b[0m")

    #Afficher Help
    sys.stdout.write("\033["+str(26)+";"+str(49)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mHELP\u001b[0m")

    #Afficher quitter
    sys.stdout.write("\033["+str(27)+";"+str(49)+"H")
    sys.stdout.write(u"\u001b[1m\u001b[37mQUIT\u001b[0m")

    #Afficher le curseur
    count = 0
    for i in start["selected"]:
        if start["selected"][i] == True:
            sys.stdout.write("\033["+str(25+count)+";"+str(48)+"H")
            sys.stdout.write(u"\u001b[37m>\u001b[0m")
        count+=1

    sys.stdout.write("\033["+str(100)+";"+str(100)+"H")
    sys.stdout.flush()
    
def choose_image(start):
    listframes = get_all_frames(start)
    imagenumber,state = get_framestate(start)

    if imagenumber == len(listframes)-1 or imagenumber == 0:
        state = not(state)
    if state == True:
        imagenumber+=1
    else :
        imagenumber-=1
    start = set_frame_state(start, (imagenumber,state))
    return start

def select(start, direction):
    currentselect = get_current_selected(start)
    if direction == "s":
        for i in start["selected"]:
            if i == currentselect:
                if i == "Quitter":
                    start = set_selected(start, "Play", True)
                    start = set_selected(start, i, False)
                elif i == "Play":
                    start = set_selected(start, "Help", True)
                    start = set_selected(start, i, False)
                elif i == "Help":
                    start = set_selected(start, "Quitter", True)
                    start = set_selected(start, i, False)
    if direction == "z":
        for i in start["selected"]:
            if i == currentselect:
                if i == "Help":
                    start = set_selected(start, "Play", True)
                    start = set_selected(start, i, False)
                elif i == "Quitter":
                    start = set_selected(start, "Help", True)
                    start = set_selected(start, i, False)
                elif i == "Play":
                    start = set_selected(start, "Quitter", True)
                    start = set_selected(start, i, False)
    return start


if __name__ == "__main__":
    os.system('clear')
    start = create()
    while True:
        currentimage = start["frame_state"][0]
        show(start, start["all_frames"][currentimage])
        start = choose_image(start)
