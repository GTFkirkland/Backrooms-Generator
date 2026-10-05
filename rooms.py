#closed
def generateRoom(topOpen, rightOpen, downOpen, leftOpen):
    room = ("""""")
    if topOpen == True:
        room += "┎----┒"
    room = ["""┎----┒
               |    |
               ┖----┚"""]

generateRoom(True, False, False, False)