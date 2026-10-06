#┏━  ━┓          
#┃    ⠀          
#┗━  ━┛
from rooms import drawRoom, testDrawRoom

#functions
def nextFrame(n,e,s,w):
    print("\n RADAR\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃                          ┃\n┃                          ┃\n┃                          ┃")
    drawRoom(n, e, s, w,"          ","┃")
    print("┃                          ┃\n┃                          ┃\n┃                          ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

