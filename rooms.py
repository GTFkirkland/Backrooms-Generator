#closed
def drawRoom(topOpen, rightOpen, downOpen, leftOpen, player):
    room = ("""""")
    if topOpen == True:
        room += "┏━ ━┓"
    else:
        room += "┏━━━┓"
    
    if leftOpen == True:
        room += "\n⠀  "
    else:
        room += "\n┃  "
    
    if rightOpen == True:
        room += "  ⠀"
    else:
        room += " ┃"

    if downOpen == True:
        room += "\n┗━ ━┛"
    else:
        room += "\n┗━━━┛"

    #room = ["""┎───┒
    #           ┃   ┃
    #           ┖───┚"""]
    print(room)

drawRoom(True, True, True, True, 1)
drawRoom(False, False, False, False, 1)
