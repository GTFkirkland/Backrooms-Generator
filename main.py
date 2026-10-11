#imports
import random as ran
import time as time
from rooms import ranRoom
from ui import nextFrame, clearTerminal
from enemy import moveHostile
#colors and symbols
reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'
grey = '\033[37m'
magenta = '\033[35m'
lightYellow = '\033[93m'
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
sizeChoice = input(f"{bold}Select the game size:\n {bold}1){reset}{blue} Minuscule{reset}\n {bold}2){reset}{cyan} Tiny{reset}\n {bold}3){reset}{green} Small{reset}\n {bold}4){reset}{lightYellow} Large{reset}\n {bold}5){reset}{red} Huge {reset}\n {bold}6){reset}{magenta} Massive {reset}\n{bold}{yellow}<Answer>> {reset}")
if sizeChoice == "2":
    size = 50
    print(f"{cyan}Tiny {reset}selected")
elif sizeChoice == "3":
    size = 80
    print(f"{green}Small {reset}selected")
elif sizeChoice == "4":
    size = 120
    print(f"{lightYellow}Large {reset}selected")
elif sizeChoice == "5":
    size = 180
    print(f"{red}Huge {reset}selected")
elif sizeChoice == "6":
    size = 270
    print(f"{magenta}Massive {reset}selected")
else:
    size = 20
    print(f"{blue}Minuscule {reset}selected")
time.sleep(1)

#difficulty
print("----------------------------------------")
difficulty = input(f"Choose the {bold}{red}Rooms'{reset} difficulty:\n {bold}1){reset} {green}Peaceful{reset}\n {bold}2){reset} {cyan}Easy{reset}\n {bold}3){reset} {blue}Normal{reset}\n {bold}4){reset} {red}Hard{reset}\n {bold}5){reset} {magenta}Insane{reset}\n {bold}6){reset} {magenta}N̴̫̈́̍Ỉ̸̪͒G̷̛̺̈H̴̺̙̏T̸̞͇̿M̷̮͘A̸̤͌͗R̷̼̹̾É̷̲̫{reset}\n{yellow}{bold}<Answer>> {reset}")
if difficulty == "2":
    print(f"{cyan}{bold}Easy {reset}selected")
    difficulty = "hostile"
    subDifficulty = "easy"
elif difficulty == "3":
    print(f"{blue}{bold}Normal {reset}selected")
    difficulty = "hostile"
    subDifficulty = "normal"
elif difficulty == "4":
    print(f"{red}{bold}Hard {reset}selected")
    difficulty = "hostile"
    subDifficulty = "hard"
elif difficulty == "5":
    print(f"{magenta}{bold}Insane {reset}selected")
    difficulty = "hostile"
    subDifficulty = "insane"
elif difficulty == "6":
    print(f"{magenta}{bold}N̴̫̈́̍Ỉ̸̪͒G̷̛̺̈H̴̺̙̏T̸̞͇̿M̷̮͘A̸̤͌͗R̷̼̹̾É̷̲̫{reset}selected")
    difficulty = "hostile"
    subDifficulty = "nightmare"
else:
    print(f"{green}{bold}Peaceful {reset}selected")
    difficulty = "peaceful"
time.sleep(1)

#exit, enemy placement, and player placement
player = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
anomaly = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
hostileSpawnRange = min(10, size - 1)
if difficulty == "hostile":
    hostile = {
        "x": ran.randint(max(0, player["x"] - hostileSpawnRange), min(size - 1, player["x"] + hostileSpawnRange)),
        "y": ran.randint(max(0, player["y"] - hostileSpawnRange), min(size - 1, player["y"] + hostileSpawnRange))
    }
else:
    hostile = None

while player == anomaly or player == hostile or anomaly == hostile:
    player = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
    anomaly = {"x":ran.randint(0,size-1), "y":ran.randint(0,size-1)}
    if difficulty == "hostile":
        hostile = {
            "x": ran.randint(max(0, player["x"] - hostileSpawnRange), min(size - 1, player["x"] + hostileSpawnRange)),
            "y": ran.randint(max(0, player["y"] - hostileSpawnRange), min(size - 1, player["y"] + hostileSpawnRange))
        }
    else:
        hostile = None
#map setup
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
if difficulty == "hostile":
    story = input(f"{bold}{red}<!WARNING!>{reset}")
    story = input(f"{bold}{red}<!HOSTILE-PRESENSE-DETECTED!>{reset}")
    story = input(f"<Your {bold}{green}ADR {reset}isn't able to differentiate between {bold}{red}ANOMALIES{reset}>")
    story = input(f"<Ensure the {bold}{red}ANOMALY{reset} you approach is... {bold}{green}CORRECT{reset}>")
#hostile setup
if difficulty == "hostile":
    #hunt chance based on difficulty
    if subDifficulty == "easy":
        huntChance = [True] + [False] * 31 #3.125% 1/32
        huntLength = 18
        grace = 25
    if subDifficulty == "normal":
        huntChance = [True] + [False] * 15 #6.25% 1/16
        huntLength = 26
        grace = 20
    if subDifficulty == "hard":
        huntChance = [True] + [False] * 7 #12.5% 1/8
        huntLength = 34
        grace = 15
    if subDifficulty == "insane":
        huntChance = [True, False, False, False] #25% 1/4
        huntLength = 42
        grace = 10
    if subDifficulty == "nightmare":
        huntChance = [True, False] #50% 1/2
        huntLength = 50
        grace = 5
    #hunt timer setup
    hunt = False
    huntTurnsRemaining = huntLength
#play game
hostilePreviousRoom = None
roomSeen = [player.copy()]
while player != anomaly:
    
    if difficulty == "hostile" and hunt == False:
        if grace > 0:
            grace -= 1
        else:
            hunt = ran.choice(huntChance)

    clearTerminal()
    nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt if difficulty == "hostile" else False)
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
        nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt if difficulty == "hostile" else False)
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

    #room rememberance
    if player not in roomSeen:
        roomSeen.append(player.copy())

    if difficulty == "hostile" and player == hostile:
        break

    #hostile movement
    if difficulty == "hostile" and hunt:
        oldHostileRoom = hostile.copy()
        hostile = moveHostile(hostile, player, map, size, hostilePreviousRoom)
        hostilePreviousRoom = oldHostileRoom
        if player == hostile:
            break

        huntTurnsRemaining -= 1 
        if huntTurnsRemaining == 0:
            hunt = False
            huntTurnsRemaining = huntLength
            hostile = {
                "x": ran.randint(max(0, player["x"] - round(size / 10)), min(size - 1, player["x"] + round(size / 10))),
                "y": ran.randint(max(0, player["y"] - round(size / 10)), min(size - 1, player["y"] + round(size / 10)))}
            while hostile == player:
                hostile = {
                    "x": ran.randint(max(0, player["x"] - round(size / 10)), min(size - 1, player["x"] + round(size / 10))),
                    "y": ran.randint(max(0, player["y"] - round(size / 10)), min(size - 1, player["y"] + round(size / 10)))}
            hostilePreviousRoom = None
        

            


#end
if difficulty == "hostile" and player == hostile: #death
    clearTerminal()
    nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt,True)
elif player == anomaly: #escape
    clearTerminal()
    print(f"{green}{bold}YOU SUCCESFULLY ESCAPED THE ROOMS{reset}")