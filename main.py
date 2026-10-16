#imports
import random as ran
import time as time
import tkinter as tk
from rooms import ranRoom, connectRooms
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
grey = '\033[90m'
magenta = '\033[35m'
lightYellow = '\033[93m'

#variable setups
quit = False
nightmareLock = True
nightmareTiersUnlocked = []
#GAMELOOP START
while quit == False:
    #map choice (START)
    clearTerminal()
    print("{==============Game=Setup==============}")
    sizeChoice = input(f"{bold}Select the game size:\n {bold}1){reset}{blue} Minuscule{reset}\n {bold}2){reset}{cyan} Tiny{reset}\n {bold}3){reset}{green} Small{reset}\n {bold}4){reset}{lightYellow} Large{reset}\n {bold}5){reset}{lightYellow} Huge {reset}\n {bold}6){reset}{red} Massive {reset}\n {bold}7){reset}{red} Colossal {reset}\n {bold}{grey}<Some devices will struggle to generate the sizes below>{reset}\n {bold}8){reset}{magenta} Titanic {reset}\n {bold}9){reset}{magenta} Celestial {reset}\n{bold}{yellow}<Answer>> {reset}")
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
        print(f"{lightYellow}Huge {reset}selected")
    elif sizeChoice == "6":
        size = 270
        print(f"{red}Massive {reset}selected")
    elif sizeChoice == "7":
        size = 400
        print(f"{red}Colossal {reset}selected")
    elif sizeChoice == "8":
        size = 1000
        print(f"{magenta}Titanic {reset}selected")
    elif sizeChoice == "9":
        size = 3000
        print(f"{magenta}Celestial {reset}selected")
    else:
        size = 20
        print(f"{blue}Minuscule {reset}selected")
    time.sleep(1)

    #difficulty
    print("----------------------------------------")
    subSubDifficulty = "0"
    if nightmareLock == False:
        difficulty = input(f"Choose the {bold}{red}Rooms'{reset} difficulty:\n {bold}0){reset} {green}{bold}Peaceful{reset}\n {bold}1){reset} {green}Very Easy{reset}\n {bold}2){reset} {cyan}Easy{reset}\n {bold}3){reset} {blue}Normal{reset}\n {bold}4){reset} {red}Hard{reset}\n {bold}5){reset} {red}{bold}Insane{reset}\n {bold}6){reset} {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n{yellow}{bold}<Answer>> {reset}")
    else:
        if sizeChoice == "3" or sizeChoice == "4" or sizeChoice == "5" or sizeChoice == "6":
            difficulty = input(f"Choose the {bold}{red}Rooms'{reset} difficulty:\n {bold}0){reset} {green}{bold}Peaceful{reset}\n {bold}1){reset} {green}Very Easy{reset}\n {bold}2){reset} {cyan}Easy{reset}\n {bold}3){reset} {blue}Normal{reset}\n {bold}4){reset} {red}Hard{reset}\n {bold}5){reset} {red}{bold}Insane{reset}\n{bold}{grey}🔒︎) <Unlock by escaping on Insane>\n{yellow}{bold}<Answer>> {reset}")
        else:
            difficulty = input(f"Choose the {bold}{red}Rooms'{reset} difficulty:\n {bold}0){reset} {green}{bold}Peaceful{reset}\n {bold}1){reset} {green}Very Easy{reset}\n {bold}2){reset} {cyan}Easy{reset}\n {bold}3){reset} {blue}Normal{reset}\n {bold}4){reset} {red}Hard{reset}\n {bold}5){reset} {red}{bold}Insane{reset}\n{bold}{grey}🔒︎) <Unlock by escaping on Insane, at size Small or larger>\n{yellow}{bold}<Answer>> {reset}")
    
    if difficulty == "1": #very easy
        print(f"{green}{bold}Very Easy {reset}selected")
        difficulty = "hostile"
        subDifficulty = "easy"
    elif difficulty == "2": #easy
        print(f"{cyan}{bold}Easy {reset}selected")
        difficulty = "hostile"
        subDifficulty = "easy"
    elif difficulty == "3": #normal
        print(f"{blue}{bold}Normal {reset}selected")
        difficulty = "hostile"
        subDifficulty = "normal"
    elif difficulty == "4": #hard
        print(f"{red}{bold}Hard {reset}selected")
        difficulty = "hostile"
        subDifficulty = "hard"
    elif difficulty == "5": #insane
        print(f"{red}{bold}Insane {reset}selected")
        difficulty = "hostile"
        subDifficulty = "insane"
    elif difficulty == "6" and nightmareLock == False: #nightmare
        print("----------------------------------------")
        time.sleep(1)
        #extra tiers
        if "5" in nightmareTiersUnlocked:
            subSubDifficulty = input(f"Select the subtier of {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n 1) {magenta}Tier Ⅰ {reset}- {red}35% hunt chance{reset}\n 2) {magenta}Tier ⅠⅠ {reset}- {red}50% hunt chance{reset}\n 3) {magenta}Tier ⅠⅠⅠ {reset}- {red}65% hunt chance & no anomaly signal{reset}\n 4) {magenta}Tier ⅠⅤ {reset}- {red}80% hunt chance & no anomaly signal{reset}\n 5) {magenta}Tier Ⅴ {reset}- {red}100% hunt chance & no anomaly signal{reset}\n{yellow}{bold}<Answer>> {reset}")
        elif "4" in nightmareTiersUnlocked:
            subSubDifficulty = input(f"Select the subtier of {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n 1) {magenta}Tier Ⅰ {reset}- {red}35% hunt chance{reset}\n 2) {magenta}Tier ⅠⅠ {reset}- {red}50% hunt chance{reset}\n 3) {magenta}Tier ⅠⅠⅠ {reset}- {red}65% hunt chance & no anomaly signal{reset}\n 4) {magenta}Tier ⅠⅤ {reset}- {red}80% hunt chance & no anomaly signal{reset}\n{grey}🔒︎) Tier Ⅴ - Unlock by escaping on Tier ⅠⅤ\n{yellow}{bold}<Answer>> {reset}")
        elif "3" in nightmareTiersUnlocked:
            subSubDifficulty = input(f"Select the subtier of {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n 1) {magenta}Tier Ⅰ {reset}- {red}35% hunt chance{reset}\n 2) {magenta}Tier ⅠⅠ {reset}- {red}50% hunt chance{reset}\n 3) {magenta}Tier ⅠⅠⅠ {reset}- {red}65% hunt chance & no anomaly signal{reset}\n{grey}🔒︎) Tier ⅠⅤ - Unlock by escaping on Tier ⅠⅠⅠ\n{grey}🔒︎) Tier Ⅴ - Unlock by escaping on Tier ⅠⅤ\n{yellow}{bold}<Answer>> {reset}")
        elif "2" in nightmareTiersUnlocked:
            subSubDifficulty = input(f"Select the subtier of {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n 1) {magenta}Tier Ⅰ {reset}- {red}35% hunt chance{reset}\n 2) {magenta}Tier ⅠⅠ {reset}- {red}50% hunt chance{reset}\n{grey}🔒︎) Tier ⅠⅠⅠ - Unlock by escaping on Tier ⅠⅠ\n{grey}🔒︎) Tier ⅠⅤ - Unlock by escaping on Tier ⅠⅠⅠ\n{grey}🔒︎) Tier Ⅴ - Unlock by escaping on Tier ⅠⅤ\n{yellow}{bold}<Answer>> {reset}")
        elif "1" in nightmareTiersUnlocked:
            subSubDifficulty = input(f"Select the subtier of {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset}\n 1) {magenta}Tier Ⅰ {reset}- {red}35% hunt chance{reset}\n{grey}🔒︎) Tier ⅠⅠ - Unlock by escaping on Tier Ⅰ\n{grey}🔒︎) Tier ⅠⅠⅠ - Unlock by escaping on Tier ⅠⅠ\n{grey}🔒︎) Tier ⅠⅤ - Unlock by escaping on Tier ⅠⅠⅠ\n{grey}🔒︎) Tier Ⅴ - Unlock by escaping on Tier ⅠⅤ\n{yellow}{bold}<Answer>> {reset}")
        if subSubDifficulty not in nightmareTiersUnlocked:
            subSubDifficulty = "1"
        #prints
        if subSubDifficulty == "1":
            print(f"{magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗EⅠ{reset} selected")
        elif subSubDifficulty == "2":
            print(f"{magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗EⅠⅠ{reset} selected")
        elif subSubDifficulty == "3":
            print(f"{magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗EⅠⅠⅠ{reset} selected")
        elif subSubDifficulty == "4":
            print(f"{magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗EⅠⅤ{reset} selected")
        elif subSubDifficulty == "5":
            print(f"{magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗EⅤ{reset} selected")
        difficulty = "hostile"
        subDifficulty = "nightmare"

    else: #peaceful
        print(f"{green}Peaceful {reset}selected")
        difficulty = "peaceful"
    print("----------------------------------------")
    time.sleep(1)
    #loading
    
    print(f"{bold}{green}Generating map...{reset}")
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
    
    #intro toggle         
    print("----------------------------------------")
    introToggle = input(f"Skip the intro? {bold}{red}y{grey}/{green}n{reset}\n")
    if "y" in introToggle.lower():
        skipIntro = True
    else:
        skipIntro = False
    
    #intro
    clearTerminal()
    if skipIntro == False:
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
            story = input(f"<Choose your {bold}{red}ANOMALY{reset} with care — your {bold}{green}ADR{reset} displays every signal the same>")
    
    #hostile setup
    if difficulty == "hostile":
        #hunt chance based on difficulty
        if subDifficulty == "veryEasy":
            huntChance = [True] + [False] * 63 #1.5625% 1/64
            huntLength = 10
            grace = 30
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
            if subSubDifficulty == "1":
                huntChance = ([True] * 7 + [False] * 13) #35%
            elif subSubDifficulty == "2":
                huntChance = [True, False] #50%
            elif subSubDifficulty == "3":
                huntChance = ([True] * 13) + ([False] * 7) #65%
            elif subSubDifficulty == "4":
                huntChance = [True, True, True, True, False] #80%
            elif subSubDifficulty == "5":
                huntChance = [True] * 10 #100%
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
            if grace <= 0:
                hunt = ran.choice(huntChance)

        clearTerminal()
        nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt if difficulty == "hostile" else False,subSubDifficulty)
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
            nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt if difficulty == "hostile" else False,subSubDifficulty)
            move = input(f"{yellow}{bold}<Move>> {reset}")
        
        #moving the player
        move = move.lower()
        playerPositionBeforeMove = player.copy()
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

        if difficulty == "hostile" and not hunt and grace > 0 and player != playerPositionBeforeMove:
            grace -= 1

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
                hostileD = abs(player["x"] - hostile["x"]) + abs(player["y"] - hostile["y"])
                while hostile == player or hostileD < 7:
                    hostile = {
                        "x": ran.randint(max(0, player["x"] - round(size / 10)), min(size - 1, player["x"] + round(size / 10))),
                        "y": ran.randint(max(0, player["y"] - round(size / 10)), min(size - 1, player["y"] + round(size / 10)))}
                    hostileD = abs(player["x"] - hostile["x"]) + abs(player["y"] - hostile["y"])
                hostilePreviousRoom = None
            

                
    #end
    if difficulty == "hostile" and player == hostile: #death
        clearTerminal()
        nextFrame(map,player,anomaly,size,roomSeen,hostile,hunt, subSubDifficulty, True)
        time.sleep(2)
        story = input(f"{red}{bold}<OBJECTIVE FAILED> {reset}{bold}[ENTER to continue]{reset}")
        num = ran.randint(1000, 9999)
        quit = input(f"{bold}{green}RELOADING GAME...{reset}{bold} [ec:{green}{num}{reset}{bold} to quit][ENTER to reload]{reset}\n")
        if str(num) in quit:
            quit = True
        else:
            quit = False
            print("...")
            time.sleep(1)
    
    elif player == anomaly: #escape
        clearTerminal()
        #unlock nightmare if insane was beaten, and unlock nightmare tiers if nightmare was beaten
        if difficulty == "hostile":
            if subDifficulty == "insane" and sizeChoice in ["3", "4", "5", "6", "7", "8"]:
                nightmareLock = False
                if "1" not in nightmareTiersUnlocked:
                    nightmareTiersUnlocked.append("1")
            
            if subDifficulty == "nightmare":
                if sizeChoice in ["3", "4", "5", "6", "7", "8"]:
                    if subSubDifficulty == "1" and "2" not in nightmareTiersUnlocked:
                        nightmareTiersUnlocked.append("2")
                    elif subSubDifficulty == "2" and "3" not in nightmareTiersUnlocked:
                        nightmareTiersUnlocked.append("3")
                    elif subSubDifficulty == "3" and "4" not in nightmareTiersUnlocked:
                        nightmareTiersUnlocked.append("4") 
                    elif subSubDifficulty == "4" and "5" not in nightmareTiersUnlocked:
                        nightmareTiersUnlocked.append("5")
        
        if subDifficulty == "nightmare":
            story = input(f"{bold}The {magenta}N̸̯͝I̷̞̎G̶̗͒Ȟ̵̭T̵̳̂M̷̨̓Å̶̦R̵̺͗E{reset} ends... {yellow}[ENTER to continue]{reset}")
        else:
            story = input(f"{bold}The Rooms now feel like a bad dream, after the portal took you home... {yellow}[ENTER to continue]{reset}")
        story = input(f"{green}{bold}<OBJECTIVE COMPLETE> {reset}{bold}[ENTER to continue]{reset}")
        num = ran.randint(1000, 9999)
        quit = input(f"{bold}{green}RELOADING GAME...{reset}{bold} [ec:{green}{num}{reset}{bold} to quit][ENTER to reload]{reset}\n")
        if str(num) in quit:
            quit = True
        else:
            quit = False
            print("...")
            time.sleep(1)