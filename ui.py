#┏━  ━┓          
#┃    ⠀          
#┗━  ━┛
#imports
from rooms import drawRoom, testDrawRoom
import os
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
def nextFrame(n,e,s,w, player, anomaly, size):
    print(f'\n {bold}{grey}ADR {green}ONLINE{reset} {grey}┃ {bold}{grey}x: {green}{player["x"]}{reset} {bold}{grey}y: {green}{size - player["y"]}{reset}{grey}\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃                          ┃\n┃                          ┃\n┃                          ┃{reset}')
    drawRoom(n, e, s, w,"          ",f"{grey}┃{reset}")
    print(f"{grey}┃                          ┃\n┃                          ┃\n┃                          ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛{reset}")
    #anomaly
    distance = abs(player["x"] - anomaly["x"]) + abs(player["y"] - anomaly["y"])
    anomalyPrint = ""
    if distance <= 2:
        anomalyPrint = f"{green}{bold}!▪▪▪▪▪▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 5:
        anomalyPrint = f"{green}{bold}10▪▪▪▪▪▪▪▪▪▪{grey}▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 10:
        anomalyPrint = f"{green}{bold}9▪▪▪▪▪▪▪▪▪{grey}▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 15:
        anomalyPrint = f"{green}{bold}8▪▪▪▪▪▪▪▪{grey}▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 20:
        anomalyPrint = f"{green}{bold}7▪▪▪▪▪▪▪{grey}▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 25:
        anomalyPrint = f"{green}{bold}6▪▪▪▪▪▪{grey}▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 30:
        anomalyPrint = f"{green}{bold}5▪▪▪▪▪{grey}▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 35:
        anomalyPrint = f"{green}{bold}4▪▪▪▪{grey}▪▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 40:
        anomalyPrint = f"{green}{bold}3▪▪▪{grey}▪▪▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 45:
        anomalyPrint = f"{green}{bold}2▪▪{grey}▪▪▪▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    elif distance <= 50:
        anomalyPrint = f"{green}{bold}1▪{grey}▪▪▪▪▪▪▪▪▪▪{reset}"
        print(f"{bold}{grey}ANOMALY-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
    else:
        if player["y"] < anomaly["y"]:
            cardinalPrint = "South"
        elif player["y"] > anomaly["y"]:
            cardinalPrint = "North"
        else:
            cardinalPrint = ""
        
        if player["x"] < anomaly["x"]:
            cardinalPrint += "east"
        elif player["x"] > anomaly["x"]:
            cardinalPrint += "west"
        else:
            cardinalPrint += ""
        anomalyPrint = f"<anomaly detected {cardinalPrint}>"
        print(f"{bold}{green}{anomalyPrint}{reset}")
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')