#imports
import random as ran
#colors and symbals
reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'

#functions
def moveHostile(hostile, player, map, size):
    #move hostile towards player if possible
    if player["x"] > hostile["x"] and map[hostile["y"]][hostile["x"]][1] == True:
        hostile["x"] += 1
    elif player["x"] < hostile["x"] and map[hostile["y"]][hostile["x"]][3] == True:
        hostile["x"] -= 1
    elif player["y"] > hostile["y"] and map[hostile["y"]][hostile["x"]][2] == True:
        hostile["y"] += 1
    elif player["y"] < hostile["y"] and map[hostile["y"]][hostile["x"]][0] == True:
        hostile["y"] -= 1
    else:
        #wall in way, move random
        direction = [0,1,2,3]
        if hostile["x"] == 0:
            direction.remove(3)
        if hostile["x"] == size-1:
            direction.remove(1)
        if hostile["y"] == 0:
            direction.remove(0)
        if hostile["y"] == size-1:
            direction.remove(2)
        direction = ran.choice(direction)

        if direction == 0: #up
            hostile["y"] -= 1
        elif direction == 1: #right
            hostile["x"] += 1
        elif direction == 2: #down
            hostile["y"] += 1
        elif direction == 3: #left
            hostile["x"] -= 1
    return hostile