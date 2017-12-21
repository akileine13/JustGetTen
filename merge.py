import possibles
import random


# Get all adjacent of a cell and stores them in a list (no duplicate)
def getAllAdjacent(n, curBoard, tupleIJ):
    listAllAdjacent = []
    listAllAdjacent.append(tupleIJ)
    index = 0
    i = tupleIJ[0]
    j = tupleIJ[1]
    while(possibles.verifAdjacent(n, curBoard, i, j)):
        if((0 <= i < n) and (0 <= j < n)):
            tupleToAdd = 0
            if((j - 1) >= 0):
                if(curBoard[j - 1][i] == curBoard[j][i]):
                    tupleToAdd = (i, (j - 1))
                    if(tupleToAdd not in listAllAdjacent):
                        listAllAdjacent.append(tupleToAdd)
            if((i - 1) >= 0):
                if(curBoard[j][i - 1] == curBoard[j][i]):
                    tupleToAdd = ((i - 1), j)
                    if(tupleToAdd not in listAllAdjacent):
                        listAllAdjacent.append(tupleToAdd)
            if((i + 1) < n):
                if(curBoard[j][i + 1] == curBoard[j][i]):
                    tupleToAdd = ((i + 1), j)
                    if(tupleToAdd not in listAllAdjacent):
                        listAllAdjacent.append(tupleToAdd)
            if((j + 1) < n):
                if(curBoard[j + 1][i] == curBoard[j][i]):
                    tupleToAdd = (i, (j + 1))
                    if(tupleToAdd not in listAllAdjacent):
                        listAllAdjacent.append(tupleToAdd)
        index += 1
        if(index >= len(listAllAdjacent)):
            print("List sent", listAllAdjacent)
            return listAllAdjacent
        else:
            nextTuple = listAllAdjacent[0 + index]
            i = nextTuple[0]
            j = nextTuple[1]


# Increment the cell selected and set the adjacents to 0
def cellToDelete(n, curBoard, listTuple):
    print(listTuple)
    cellToInc = listTuple[0]
    curBoard[cellToInc[1]][cellToInc[0]] += 1
    for i in range(1, len(listTuple)):
        cellToReset = listTuple[i]
        curBoard[cellToReset[1]][cellToReset[0]] = 0


# gameProba is in bases but can't import it
# It should be here instead
def gameProba(proba):
    randomNum = random.random()
    if(randomNum < proba[0]):
        return 4
    elif(proba[0] < randomNum < proba[1]):
        return 3
    elif(proba[1] < randomNum < proba[2]):
        return 2
    else:
        return 1


# Check for 0  and push the upper cells
# The 0 left are replaced by random numbers (1-4)
def pushToBottom(n, curBoard, proba):
    for y in range((n - 1), 0, -1):
        for x in range((n - 1), -1, -1):
            if(curBoard[y][x] == 0):
                index = (y - 1)
                if(curBoard[index][x] == 0):
                    while(curBoard[index][x] == 0 and index < 0):
                        if(curBoard[index][x] != 0):
                            curBoard[y][x] = curBoard[index][x]
                            curBoard[index][x] =  0
                        index -= 1
                else:
                    curBoard[y][x] = curBoard[y - 1][x]
                    curBoard[y - 1][x] = 0

    for i in range(n):
        for j in range(n):
            if(curBoard[j][i] == 0):
                curBoard[j][i] = gameProba(proba)             
