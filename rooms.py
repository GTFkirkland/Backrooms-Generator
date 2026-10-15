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
grey = '\033[90m'
magenta = '\033[35m'
lightYellow = '\033[93m'
#functions
def drawRoom(map, player, spaces, border, roomSeen, anomaly, hostile, hunt, playerDead=False):
    y = player["y"]
    x = player["x"]
    for rowOffset in range(-1, 2):
        roomY = y + rowOffset
        topLine = ""
        middleLine = ""
        bottomLine = ""

        leftBorder = border
        rightBorder = border
        if hostile != None and hunt and not playerDead:
            if hostile["x"] == x - 2 and hostile["y"] == roomY:
                leftBorder = f"{red}{bold}■{reset}"
            elif hostile["x"] == x + 2 and hostile["y"] == roomY:
                rightBorder = f"{red}{bold}■{reset}"
        if anomaly["x"] == x - 2 and anomaly["y"] == roomY:
            leftBorder = f"{red}{bold}■{reset}"
        elif anomaly["x"] == x + 2 and anomaly["y"] == roomY:
            rightBorder = f"{red}{bold}■{reset}"

        for columnOffset in range(-1, 2):
            roomX = x + columnOffset

            roomInMap = roomY >= 0 and roomY < len(map) and roomX >= 0 and roomX < len(map[roomY])
            roomDiscovered = roomInMap and {"x": roomX, "y": roomY} in roomSeen

            if roomDiscovered:
                currentRoom = map[roomY][roomX]
                if currentRoom[0] == True:
                    topLine += "┏━  ━┓"
                else:
                    topLine += "┏━━━━┓"

                if currentRoom[3] == True:
                    leftSide = "⠀"
                else:
                    leftSide = "┃"
                if currentRoom[1] == True:
                    rightSide = "⠀"
                else:
                    rightSide = "┃"

                if currentRoom[2] == True:
                    bottomLine += "┗━  ━┛"
                else:
                    bottomLine += "┗━━━━┛"
            else:
                topLine += "      "
                bottomLine += "      "

            if roomInMap:
                markers = []
                if roomDiscovered and roomY == y and roomX == x and not playerDead:
                    markers.append(f"{green}{bold}■{reset}")
                if roomY == anomaly["y"] and roomX == anomaly["x"]:
                    markers.append(f"{red}{bold}■{reset}")
                if hostile != None and hunt and not playerDead and roomY == hostile["y"] and roomX == hostile["x"]:
                    markers.append(f"{red}{bold}■{reset}")

                markerSpaces = 4 - len(markers)
                leftSpaces = markerSpaces // 2
                rightSpaces = markerSpaces - leftSpaces
                if roomDiscovered:
                    middleLine += f"{leftSide}{' ' * leftSpaces}{''.join(markers)}{' ' * rightSpaces}{rightSide}"
                else:
                    middleLine += f" {' ' * leftSpaces}{''.join(markers)}{' ' * rightSpaces} "
            else:
                middleLine += "      "

        if rowOffset == -1:
            topFrame = _borderWithMarkers(x, y - 2, anomaly, hostile, hunt, playerDead)
            print(f"{grey}┏{topFrame}┓{reset}")

        print(f"{border}{spaces}{topLine}{spaces}{border}")
        print(f"{leftBorder}{spaces}{middleLine}{spaces}{rightBorder}")
        print(f"{border}{spaces}{bottomLine}{spaces}{border}")

        if rowOffset == 1:
            bottomFrame = _borderWithMarkers(x, y + 2, anomaly, hostile, hunt, playerDead)
            print(f"{grey}┗{bottomFrame}┛{reset}")


def _borderWithMarkers(playerX, markerY, anomaly, hostile, hunt, playerDead):
    line = ["━"] * 24
    markers = [anomaly]
    if hostile != None and hunt and not playerDead:
        markers.append(hostile)

    for marker in markers:
        offsetX = marker["x"] - playerX
        if marker["y"] == markerY and offsetX >= -2 and offsetX <= 2:
            markerIndex = round((offsetX + 2) * 23 / 4)
            line[markerIndex] = f"{red}{bold}■{reset}{grey}"

    return "".join(line)

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

#test
def testDrawRoom():
    sampleMap = [
        [[False, True, True, False], [False, True, True, True], [False, False, True, True]],
        [[True, True, True, False], [True, True, True, True], [True, False, True, True]],
        [[True, True, False, False], [True, True, False, True], [True, False, False, True]],
    ]
    drawRoom(sampleMap, {"x": 1, "y": 0}, "", "", [
        {"x": 0, "y": 0},
        {"x": 1, "y": 0},
        {"x": 2, "y": 0},
        {"x": 0, "y": 1},
        {"x": 1, "y": 1},
        {"x": 2, "y": 1},
        {"x": 0, "y": 2},
        {"x": 1, "y": 2},
        {"x": 2, "y": 2},
    ], {"x": 0, "y": 0}, {"x": 2, "y": 0}, True)

#random boolean generator
def ranBool():
    return ran.choice([True, False])

def ranRoom(map, coord, size, rowPreview):
    room = []
    roomAvail = []
    #up
    if coord["y"] > 0: #top row check
        if map[coord["y"]-1][coord["x"]][2] == True: #room above open downwards check
            room.append(True) #open upwards
            roomAvail.append(False)
        else:
            room.append(False) #close upwards
            roomAvail.append(False)
    else:
        room.append(False) #close upwards
        roomAvail.append(False)
        
    #right
    if coord["x"] < size-1: #far right check
        #if map[coord["y"]][coord["x"]+1][3] == True:
        room.append(ranBool()) #right won't be generated, so it's random
        if room[1] == True:
            roomAvail.append(False) #open
        else:
            roomAvail.append(True) #closed
    else:
        room.append(False) #close right
        roomAvail.append(False)
        
    #down
    if coord["y"] < size-1: #bottom row check
        #if map[coord["y"]-1][coord["x"]][0] == True:
        room.append(ranBool()) #down won't be generated, so it's random
        if room[2] == True:
            roomAvail.append(False) #open
        else:
            roomAvail.append(True) #closed
    else:
        room.append(False) #close bottom
        roomAvail.append(False)
        
    #left
    if coord["x"] > 0: #far left check
        if rowPreview[coord["x"]-1][1] == True: #room to the left rightwards check
            room.append(True) #open left
            roomAvail.append(False)
        else:
            room.append(False) #close left
            roomAvail.append(False)
    else:
        room.append(False) #close left
        roomAvail.append(False)    

    #room check
    if not True in room:
        if roomAvail == True and roomAvail[2] == True:
            room[ran.randint(1,2)] = True
        elif roomAvail[1] == True:
            room[1] = True
        elif roomAvail[2] == True:
            room[2] = True
        else:
            room.append("Closed")
    #finish
    return room
