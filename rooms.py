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
def drawRoom(topOpen, rightOpen, downOpen, leftOpen, spaces, border):
    room = ("""""")
    if topOpen == True:
        room += f"{border}{spaces}┏━  ━┓{spaces}{border}"
    else:
        room += f"{border}{spaces}┏━━━━┓{spaces}{border}"
    
    if leftOpen == True:
        room += f"\n{border}{spaces}⠀ {bold}{green}▢{reset}"
    else:
        room += f"\n{border}{spaces}┃ {bold}{green}▢{reset}"
    
    if rightOpen == True:
        room += f"  ⠀{spaces}{border}"
    else:
        room += f"  ┃{spaces}{border}"

    if downOpen == True:
        room += f"\n{border}{spaces}┗━  ━┛{spaces}{border}"
    else:
        room += f"\n{border}{spaces}┗━━━━┛{spaces}{border}"
    print(room)

#test
def testDrawRoom():
    drawRoom(True, True, True, True,"","")
    drawRoom(False, False, False, False,"","")
    drawRoom(True, False, False, False,"","")
    drawRoom(False, True, False, False,"","")
    drawRoom(False, False, True, False,"","")
    drawRoom(False, False, False, True,"","")

#random boolean generator
def ranBool():
    return ran.choice([True, True, True, False, False])

def ranRoom(map, coord):
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
    if coord["x"] < 4: #far right check
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
    if coord["y"] < 4: #bottom row check
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
        if map[coord["y"]][coord["x"]-1][1] == True: #room to the left rightwards check
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
