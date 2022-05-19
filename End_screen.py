import sys

import sys
import os
import time

def create():
    dossier = "Ecran_fin/"
    filenames = ["Ecran_fin.txt","Frame_1_fin.txt", "Frame_2_fin.txt"]
    frames = []
    for name in filenames:
        f = open(dossier+name).read().split("\n")
        frames.append([list(word) for word in f])
    return {"all_frames" : frames, "frame_state" : (0,False)}

def get_all_frames(end):
    return end["all_frames"]

def get_framestate(end):
    return end["frame_state"]

def set_frame_state(end, newvalue):
    end["frame_state"] = newvalue
    return end

def show(end, frame):
    #Couleur
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    #Background
    for y in range(len(frame)):
        for x in range(len(frame[y])):
            s="\033["+str(y)+";"+str(x)+"H"
            sys.stdout.write(s)
            sys.stdout.write(u"\u001b[1m\u001b[37 m" + frame[y][x] +"\u001b[0m")

    sys.stdout.write("\033["+str(100)+";"+str(100)+"H")
    sys.stdout.flush()

def choose_image(end):
    listframes = get_all_frames(end)
    imagenumber,state = get_framestate(end)

    if imagenumber == len(listframes)-1 or imagenumber == 0:
        state = not(state)
    if state == True:
        imagenumber+=1
    else :
        imagenumber-=1
    end = set_frame_state(end, (imagenumber,state))
    return end

if __name__ == "__main__":
    os.system('clear')
    end = create()
    while True:
        currentimage = end["frame_state"][0]
        show(end, end["all_frames"][currentimage])
        end = choose_image(end)
        time.sleep(0.1)
