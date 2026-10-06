#imports
import random as ran
import time as time
from rooms import ranBool, ranRoom
from ui import nextFrame
#map generation
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
        #x = input(f"k:{k} | i:{i}") #debug

#play game
player = {"x":0, "y":0}
nextFrame(map[player["y"]][player["x"]][0],map[player["y"]][player["x"]][1],map[player["y"]][player["x"]][2],map[player["y"]][player["x"]][3])