#┏━  ━┓          
#┃    ⠀          
#┗━  ━┛
#imports
from rooms import drawRoom, testDrawRoom
#colors and symbals
reset = '\033[0m'
red = '\033[31m' 
green = '\033[32m' 
yellow = '\033[33m' 
blue = '\033[34m' 
cyan = '\033[36m' 
bold = '\033[1m'
#functions
def nextFrame(n,e,s,w):
    print(f"\n {bold}RADAR {green}ONLINE{reset}\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃                          ┃\n┃                          ┃\n┃                          ┃")
    drawRoom(n, e, s, w,"          ","┃")
    print("┃                          ┃\n┃                          ┃\n┃                          ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def clearTerminal():
    for i in range(50):
        print("")