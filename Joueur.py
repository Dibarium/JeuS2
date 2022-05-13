import sys
import os
import time
import select
import tty 
import termios

def isData():
	#recuperation evenement clavier
	    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def get_key():
    if isData():
        c = sys.stdin.read(1)
        return c
        #return repr(c)

if __name__ == "__main__":
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    while True:
        key = get_key()
        if key != None:
            print(key)