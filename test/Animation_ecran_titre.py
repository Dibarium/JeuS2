filenames = ["Ecran_titre.txt","Frame_2.txt"]
frames = []
import os,time

os.system('clear')


for name in filenames:
    with open(name, "r") as f :
        frames.append(f.readlines())

for i in range(10):
    for frame in frames:
        print("".join(frame))
        time.sleep(2)
        os.system('clear')