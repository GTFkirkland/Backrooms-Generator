#imports
import random as ran
import time as time
from rooms import ranRoom
from ui import nextFrame, clearTerminal
#colors and symbals
reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'
#map generation
size = 500
map = []
for i in range(size):
    map.append([])
for k in range(len(map)): #collumn
    #make rooms
    for i in range(0,len(map)): #row
        coord = {"x": i, "y": k}
        map[k].append(ranRoom(map,coord))
        #x = input(f"k:{k} | i:{i}") #debugs

#play game
player = {"x":0, "y":0}
while True:
    nextFrame(map[player["y"]][player["x"]][0],map[player["y"]][player["x"]][1],map[player["y"]][player["x"]][2],map[player["y"]][player["x"]][3])
    #movement reception
    move = input(f"{yellow}{bold}<Move>> {reset}")
    availableMoves = ["w", "a", "s", "d", "W", "A", "S", "D"]
    while not move in availableMoves:
        print(f"{red}{bold}INVALID{reset}")
        time.sleep(0.2)
        clearTerminal()
        nextFrame(map[player["y"]][player["x"]][0],map[player["y"]][player["x"]][1],map[player["y"]][player["x"]][2],map[player["y"]][player["x"]][3])
        move = input(f"{yellow}{bold}<Move>> {reset}")
    #moving the player
    if move == "w" or "W":
        None
    elif move == "a" or "A":
        None
    elif move == "s" or "S":
        None
    elif move == "d" or "D":
        None