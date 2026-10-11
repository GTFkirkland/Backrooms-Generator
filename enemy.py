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
def moveHostile(hostile, player, map, size, previousRoom):
    if hostile == player:
        return hostile

    room = map[hostile["y"]][hostile["x"]]
    openDirections = []
    if room[0] == True:
        openDirections.append(0)
    if room[1] == True:
        openDirections.append(1)
    if room[2] == True:
        openDirections.append(2)
    if room[3] == True:
        openDirections.append(3)

    otherDirections = []
    for direction in openDirections:
        nextX = hostile["x"]
        nextY = hostile["y"]
        if direction == 0:
            nextY -= 1
        elif direction == 1:
            nextX += 1
        elif direction == 2:
            nextY += 1
        else:
            nextX -= 1

        if previousRoom == None or nextX != previousRoom["x"] or nextY != previousRoom["y"]:
            otherDirections.append(direction)

    if otherDirections:
        openDirections = otherDirections

    preferredDirections = []
    currentDistance = abs(player["x"] - hostile["x"]) + abs(player["y"] - hostile["y"])
    for direction in openDirections:
        nextX = hostile["x"]
        nextY = hostile["y"]
        if direction == 0:
            nextY -= 1
        elif direction == 1:
            nextX += 1
        elif direction == 2:
            nextY += 1
        else:
            nextX -= 1

        nextDistance = abs(player["x"] - nextX) + abs(player["y"] - nextY)
        if nextDistance < currentDistance:
            preferredDirections.append(direction)

    if preferredDirections:
        direction = ran.choice(preferredDirections)
    elif openDirections:
        direction = ran.choice(openDirections)
    else:
        return hostile

    if direction == 0:
        hostile["y"] -= 1
    elif direction == 1:
        hostile["x"] += 1
    elif direction == 2:
        hostile["y"] += 1
    else:
        hostile["x"] -= 1

    return hostile