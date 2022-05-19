import sys
def show():
    f = open("Ecran_help.txt").read().split('\n')
    for i in range(len(f)):
        sys.stdout.write("\033["+str(0+i)+";"+str(0)+"H")
        sys.stdout.write(u"\u001b[1m\u001b[37m" + f[i] +"\u001b[0m")
        sys.stdout.write("\033["+str(100)+";"+str(100)+"H")
        sys.stdout.flush()

