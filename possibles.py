# Check if there are numbers with adjacents of the same values
# Aka if the player can play or not
def verifAdjacent(n, curBoard, i, j):
    hasAdjacent = 0
    if((0 <= i < n) and (0 <= j < n)):
        if((j - 1) >= 0):
            if(curBoard[j - 1][i] == curBoard[j][i]):
                hasAdjacent += 1
                return True
        if((i - 1) >= 0):
            if(curBoard[j][i - 1] == curBoard[j][i]):
                hasAdjacent += 1
                return True
        if((i + 1) < n):
            if(curBoard[j][i + 1] == curBoard[j][i]):
                hasAdjacent += 1
                return True
        if((j + 1) < n):
            if(curBoard[j + 1][i] == curBoard[j][i]):
                hasAdjacent += 1
                return True
    if(hasAdjacent == 0):
            return False


# Goes through each cells and check their adjacents
def canStillPlay(n, curBoard):
    status = 0
    for y in range(n):
        for x in range(n):
            status = verifAdjacent(n, curBoard, x, y)
            if status:
                return True
    if not status:
        return False


# Goes through each cells and check the highest value
def checkHighest(n, curBoard):
    highest = 1
    for x in range(n):
        for y in range(n):
            if curBoard[x][y] > highest:
                highest = curBoard[x][y]
    return highest

'''  MEMO VERIF
        [I-1 J-1] [I J-1] [I+1 J-1]
        [I-1 J]   [I J]     [I+1 J]
        [I-1 J+1] [I J+1] [I+1 J+1]

        [Pas Besoin] [I J-1] [Pas Besoin]
        [I-1 J]      [I J]   [I+1 J]
        [Pas Besoin] [I J+1] [Pas Besoin]
'''
