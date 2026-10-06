#imports
import random as ran
import time as time
from rooms import ranBool, ranRoom
#room generation
map = [
        [],
        [],
        [],
        [],
        [],
      ]

for k in range(len(map)): #collumn
    #make rooms
    for i in range(0,len(map)): #row
        coord = {"x": i, "y": k}
        map[k].append(ranRoom(map,coord))
        x = input(f"k:{k} | i:{i}")
    

print(map)