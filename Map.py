import sys
import os
def create(sizex : int, sizey : int) -> list:
  assert type(sizex) is int           #Taille de la carte en x
  assert type(sizey) is int           #Taille de la carte en y

  carte = [[" " for i in range(sizex)] for i in range(sizey)]
  return carte

def get_size(carte):
  return (len(carte[0]),len(carte))

def get_carte(carte):
  return carte

def show(carte):
  #os.system("clear")
  sys.stdout.write("\033[40m")
  sys.stdout.write("\033[37m")
  mapsize = get_size(carte)
  for y in range(mapsize[1]+2):
      for x in range(mapsize[0]+2):
        #print(x," ",y)
        s="\033["+str(y+1)+";"+str(x+1)+"H"
        sys.stdout.write(s)
        if y == 0 or y == mapsize[1]+1:
          #print("upborder")
          sys.stdout.write("▓")
        elif x == 0 or x == mapsize[0]+1:
          #print("sideborder")
          sys.stdout.write("▓")
        else:
          #print("showmap")
          sys.stdout.write(carte[y-1][x-1])

def isinmap(newposition : tuple, carte : list) -> bool:
    """
    Tells you if the position is inside the map
    """
    assert type(newposition) is tuple
    assert type(carte) is list
    lenghtmap = (len(carte[0])-1, len(carte)-1)
    if newposition[0] >= 0 and newposition[0] <= lenghtmap[0] and newposition[1] >= 0 and newposition[1] <= lenghtmap[1] :
        return True
    else: 
        return False

if __name__ == "__main__":
  map = create(50, 50)
  show(map)