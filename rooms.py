#imports
import random as ran

#functions
def drawRoom(topOpen, rightOpen, downOpen, leftOpen, spaces, border):
    room = ("""""")
    if topOpen == True:
        room += f"{border}{spaces}┏━  ━┓{spaces}{border}"
    else:
        room += f"{border}{spaces}┏━━━━┓{spaces}{border}"
    
    if leftOpen == True:
        room += f"\n{border}{spaces}⠀  "
    else:
        room += f"\n{border}{spaces}┃  "
    
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
    return ran.choice([True, False])

def ranRoom(map, coord):
    room = []
    #up
    if coord["y"] > 0: #top row check
        if map[coord["y"]-1][coord["x"]][2] == True: #room above open downwards check
            room.append(True) #open upwards
        else:
            room.append(False) #close upwards
    else:
        room.append(False) #close upwards
    
    #right
    if coord["x"] < 4: #far right check
        #if map[coord["y"]][coord["x"]+1][3] == True:
        room.append(ranBool()) #right won't be generated, so it's random
    else:
        room.append(False) #close right
    
    #down
    if coord["y"] < 4: #bottom row check
        #if map[coord["y"]-1][coord["x"]][0] == True:
        room.append(ranBool()) #down won't be generated, so it's random
    else:
        room.append(False) #close bottom
    
    #left
    if coord["x"] > 0: #far left check
        if map[coord["y"]][coord["x"]-1][1] == True: #room to the left rightwards check
            room.append(True) #open left
        else:
            room.append(False) #close left
    else:
        room.append(False) #close left

    #finish
    return room
