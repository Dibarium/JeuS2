import os
filenames = ["Ecran_titre.txt","Frame_2.txt", "Frame_3.txt", "Frame_4.txt", "Frame_3.txt", "Frame_2.txt", "Ecran_titre.txt"]
frames = []
import os,time

os.system('cls')


for name in filenames:
    with open(name, "r", encoding="utf8") as f :
        frames.append(f.readlines())

for i in range(10):
    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)
        