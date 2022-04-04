def create(sizex : int, sizey : int) -> list:
  assert type(sizex) is int           #Taille de la carte en x
  assert type(sizey) is int           #Taille de la carte en y

  carte = [["" for i in range(sizex)] for i in range(sizey)]
  return carte


def get_carte(carte):
  return carte