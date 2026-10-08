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
#functions
def nextFrame(n,e,s,w, player, anomaly, size):
    print(f'\n {bold}ADR {green}ONLINE{reset} ┃ {bold}x: {green}{player["x"]}{reset} {bold}y: {green}{player["y"]}{reset}\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃                          ┃\n┃                          ┃\n┃                          ┃')
    drawRoom(n, e, s, w,"          ","┃")
    print("┃                          ┃\n┃                          ┃\n┃                          ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    #anomaly
    distance = abs(player["x"] - anomaly["x"]) + abs(player["y"] - anomaly["y"])
    anomalyPrint = ""
    if distance <= 2:
        anomalyPrint = "▪▪▪▪▪▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 5:
        anomalyPrint = "▪▪▪▪▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 10:
        anomalyPrint = "▪▪▪▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 15:
        anomalyPrint = "▪▪▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 20:
        anomalyPrint = "▪▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 25:
        anomalyPrint = "▪▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 30:
        anomalyPrint = "▪▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 35:
        anomalyPrint = "▪▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 40:
        anomalyPrint = "▪▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 45:
        anomalyPrint = "▪▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
    elif distance <= 50:
        anomalyPrint = "▪"
        print(f"{bold}ANOMALY-STRENGTH [{green}{anomalyPrint}{reset}]")
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