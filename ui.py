#┏━━━━┓          
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
def nextFrame(map, player, anomaly, size, roomSeen, hostile):
    if hostile == player:
        print(f'\n {bold}{grey}ADR {red}OFFLINE{reset}{grey} ┃ {bold}{grey}x: {red}?{reset} {bold}{grey}y: {red}?{reset}{grey}\n┏━━━━━━━━━━━━━━━━━━━━━━━━┓{reset}')
    else:
        print(f'\n {bold}{grey}ADR {green}ONLINE{reset}{grey} ┃ {bold}{grey}x: {green}{player["x"]}{reset} {bold}{grey}y: {green}{size - player["y"]}{reset}{grey}\n┏━━━━━━━━━━━━━━━━━━━━━━━━┓{reset}')
    drawRoom(map,player,"   ",f"{grey}┃{reset}",roomSeen,anomaly,hostile)
    print(f"{grey}┗━━━━━━━━━━━━━━━━━━━━━━━━┛{reset}")
    #anomaly
    anomalyDistance = abs(player["x"] - anomaly["x"]) + abs(player["y"] - anomaly["y"])
    if hostile != None:
        hostileDistance = abs(player["x"] - hostile["x"]) + abs(player["y"] - hostile["y"])
    else:
        hostileDistance = 9999
    anomalyPrint = ""
    #anomaly detection
    if player != hostile:
        if anomalyDistance <= hostileDistance:
            if anomalyDistance <= 2:
                anomalyPrint = f"{green}{bold}!)▪▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH {green}[{anomalyPrint}{green}]{grey}{reset}")
            elif anomalyDistance <= 5:
                anomalyPrint = f"{green}{bold}10▪▪▪▪▪{grey}▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 10:
                anomalyPrint = f"{green}{bold}09▪▪▪▪▪{grey}▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 15:
                anomalyPrint = f"{green}{bold}08▪▪▪▪{grey}▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 20:
                anomalyPrint = f"{green}{bold}07▪▪▪▪{grey}▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 25:
                anomalyPrint = f"{green}{bold}06▪▪▪{grey}▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 30:
                anomalyPrint = f"{green}{bold}05▪▪▪{grey}▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 35:
                anomalyPrint = f"{green}{bold}04▪▪{grey}▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 40:
                anomalyPrint = f"{green}{bold}03▪▪{grey}▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 45:
                anomalyPrint = f"{green}{bold}02▪{grey}▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
            elif anomalyDistance <= 50:
                anomalyPrint = f"{green}{bold}01▪{grey}▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{anomalyPrint}{grey}]{reset}")
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
        else:
            if hostileDistance <= 2:
                hostilePrint = f"{green}{bold}!)▪▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH {green}[{hostilePrint}{green}]{grey}{reset}")
            elif hostileDistance <= 5:
                hostilePrint = f"{green}{bold}10▪▪▪▪▪{grey}▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 10:
                hostilePrint = f"{green}{bold}09▪▪▪▪▪{grey}▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 15:
                hostilePrint = f"{green}{bold}08▪▪▪▪{grey}▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 20:
                hostilePrint = f"{green}{bold}07▪▪▪▪{grey}▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 25:
                hostilePrint = f"{green}{bold}06▪▪▪{grey}▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 30:
                hostilePrint = f"{green}{bold}05▪▪▪{grey}▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 35:
                hostilePrint = f"{green}{bold}04▪▪{grey}▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 40:
                hostilePrint = f"{green}{bold}03▪▪{grey}▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 45:
                hostilePrint = f"{green}{bold}02▪{grey}▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            elif hostileDistance <= 50:
                hostilePrint = f"{green}{bold}01▪{grey}▪▪▪▪▪{reset}"
                print(f"{bold}{grey}SIGNAL-STRENGTH [{green}{hostilePrint}{grey}]{reset}")
            else:
                if player["y"] < hostile["y"]:
                    cardinalPrint = "South"
                elif player["y"] > hostile["y"]:
                    cardinalPrint = "North"
                else:
                    cardinalPrint = ""
                
                if player["x"] < hostile["x"]:
                    cardinalPrint += "east"
                elif player["x"] > hostile["x"]:
                    cardinalPrint += "west"
                else:
                    cardinalPrint += ""
                hostilePrint = f"<anomaly detected {cardinalPrint}>"
                print(f"{bold}{green}{hostilePrint}{reset}")
    else:
        print(f"{red}{bold}<SIGNAL-NOT-FOUND>")
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')