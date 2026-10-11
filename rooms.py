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
def drawRoom(map, player, spaces, border, roomSeen, anomaly, hostile, hunt):
    y = player["y"]
    x = player["x"]
    playerDead = hunt and hostile == player
    for rowOffset in range(-1, 2):
        roomY = y + rowOffset
        topLine = ""
        middleLine = ""
        bottomLine = ""

        for columnOffset in range(-1, 2):
            roomX = x + columnOffset

            if roomY >= 0 and roomY < len(map) and roomX >= 0 and roomX < len(map[roomY]):
                roomDiscovered = {"x": roomX, "y": roomY} in roomSeen
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
                topLine += "      "
                middleLine += "      "
                bottomLine += "      "

        print(f"{border}{spaces}{topLine}{spaces}{border}")
        print(f"{border}{spaces}{middleLine}{spaces}{border}")
        print(f"{border}{spaces}{bottomLine}{spaces}{border}")

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
