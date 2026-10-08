#imports
import random as ran
import time as time
from rooms import ranRoom
from ui import nextFrame, clearTerminal
#colors and symbols
reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'
grey = '\033[37m'
#room connect func
def connectRooms(roomMap):
    for row in roomMap:
        for room in row:
            room[:] = [False, False, False, False]

    width = len(roomMap[0])
    visited = [[False for room in row] for row in roomMap]
    visited[0][0] = True
    path = [0]

    while path:
        position = path[-1]
        x = position % width
        y = position // width
        neighbors = []

        if y > 0 and not visited[y - 1][x]:
            neighbors.append(0)
        if x + 1 < width and not visited[y][x + 1]:
            neighbors.append(1)
        if y + 1 < len(roomMap) and not visited[y + 1][x]:
            neighbors.append(2)
        if x > 0 and not visited[y][x - 1]:
            neighbors.append(3)

        if not neighbors:
            path.pop()
            continue

        direction = ran.choice(neighbors)
        nextX = x
        nextY = y
        door = direction
        oppositeDoor = (direction + 2) % 4

        if direction == 0:
            nextY -= 1
        elif direction == 1:
            nextX += 1
        elif direction == 2:
            nextY += 1
        else:
            nextX -= 1

        roomMap[y][x][door] = True
        roomMap[nextY][nextX][oppositeDoor] = True
        visited[nextY][nextX] = True
        path.append(nextY * width + nextX)

    for y, row in enumerate(roomMap):
        for x, room in enumerate(row):
            if x + 1 < len(row) and not room[1] and ran.random() < 0.25:
                room[1] = True
                row[x + 1][3] = True

            if y + 1 < len(roomMap) and not room[2] and ran.random() < 0.25:
                room[2] = True
                roomMap[y + 1][x][0] = True

#map choice (START)
clearTerminal()
print("{==============Game=Setup==============}")
sizeChoice = input(f"{bold}Select the game size:\n {blue}{bold}1) Minuscule\n {bold}{cyan}2) Tiny\n {bold}{green}3) Small\n {bold}{yellow}4) Large\n {bold}{red}5) Huge (DIFFICULT)\n{bold}{yellow}<Answer>> {reset}")
if sizeChoice == "2":
    size = 20
    print(f"{bold}Tiny {reset}selected")
elif sizeChoice == "3":
    size = 50
    print(f"{yellow}{bold}Small {reset}selected")
elif sizeChoice == "4":
    size = 80
    print(f"{yellow}{bold}Large {reset}selected")
elif sizeChoice == "5":
    size = 100
    print(f"{red}{bold}Huge {reset}selected")
else:
    size = 10
    print(f"Minuscule {bold}selected{reset}")
time.sleep(1)

#difficulty
print("----------------------------------------")
difficulty = input(f"{red}{bold}Choose your difficulty:\n {green}1) Peaceful{reset}\n {red}2) HOSTILE{reset}\n{yellow}{bold}<Answer>> {reset}")
if difficulty == "2":
    print(f"{red}{bold}HOSTILE {reset}selected")
    difficulty = "hostile"
else:
    print(f"{green}{bold}Peaceful {reset}selected")
    difficulty = "peaceful"
time.sleep(1)

#map setup
anomaly = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
map = []
for i in range(size):
    map.append([])
#map generation
for k in range(len(map)): #collumn
    mapGenComplete = False
    #make rooms
    while mapGenComplete == False:
        rowPreview = []
        for i in range(0,len(map)): #row
            coord = {"x": i, "y": k}
            rowPreview.append(ranRoom(map,coord,size, rowPreview))
            #x = input(f"k:{k} | i:{i}") #debugs
        
        #a down opening is required except on the bottom row.
        if k == size - 1:
            mapGenComplete = True
        else:
            for room in rowPreview:
                if room[2] == True:
                    mapGenComplete = True
                    break
    map[k] = rowPreview

connectRooms(map)
            
#intro
clearTerminal()
story = input(f"{red}{bold}Suddenly... {yellow}[ENTER to continue]{reset}")
story = input(f"you find yourself {bold}{red}falling{reset} through the ground you were standing on. {bold}{yellow}[ENTER to continue]{reset}")
story = input(f"When you land, you seem to be in a nearly {bold}{red}infinite maze of rooms{reset}, {bold}{yellow}[ENTER to continue]{reset}")
story = input(f"but you know exactly how to {bold}{red}escape{reset} from them. {bold}{yellow}[ENTER to continue]{reset}")
story = input(f"{bold}Obviously, you can use your {bold}{green}Anomaly Detection Radar{reset} to find a way back. {bold}{yellow}[ENTER to continue]{reset}")
story = input(f"{bold}{red}OBJECTIVE:{reset} Use your {bold}{green}ADR{reset} to find a way out {red}{bold}[ENTER to begin]{reset}")

#play game
player = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
while player != anomaly:
    clearTerminal()
    nextFrame(map[player["y"]][player["x"]][0],map[player["y"]][player["x"]][1],map[player["y"]][player["x"]][2],map[player["y"]][player["x"]][3],player,anomaly,size)
    #movement reception
    move = input(f"{yellow}{bold}<Move>> {reset}")
    try:
        move = move.lower()
    except:
        pass
    while not "w" in move and not "a" in move and not "s" in move and not "d" in move:
        print(f"{red}{bold}INVALID{reset}")
        time.sleep(0.2)
        clearTerminal()
        nextFrame(map[player["y"]][player["x"]][0],map[player["y"]][player["x"]][1],map[player["y"]][player["x"]][2],map[player["y"]][player["x"]][3],player,anomaly,size)
        move = input(f"{yellow}{bold}<Move>> {reset}")
    
    #moving the player
    move = move.lower()
    if "w" in move:
        move = "w"
    elif "d" in move:
        move = "d"
    elif "s" in move:
        move = "s"
    elif "a" in move:
        move = "a"

    if move == "w" and map[player["y"]][player["x"]][0] == True:
        player["y"] -= 1
    elif move == "d" and map[player["y"]][player["x"]][1] == True:
        player["x"] += 1
    elif move == "s" and map[player["y"]][player["x"]][2] == True:
        player["y"] += 1
    elif move == "a" and map[player["y"]][player["x"]][3] == True:
        player["x"] -= 1
clearTerminal()
print(f"{green}{bold}YOU SUCCESFULLY ESCAPED THE ROOMS{reset}")
    