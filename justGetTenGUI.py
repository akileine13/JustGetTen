import random
import possibles
import merge
import bases
import graphic
from graphic import *
import pygame
from pygame.locals import *

pygame.init()
gameStart = True
windowStatus = True


# The main game loop
def userSelect(n, board):
    while possibles.canStillPlay(n, board):
        tupleIJ = graphic.getClickPos(50, 50, event)
        i = tupleIJ[0]
        j = tupleIJ[1]
        if possibles.verifAdjacent(n, board, i, j):
            colorCell = graphic.getColorCell(tupleIJ)
            bases.display(bases.n, board)
            listTuple = merge.getAllAdjacent(bases.n, board, tupleIJ)
            graphic.colorSelection(listTuple, board)
            if(colorCell == (255,255,255)):
                merge.cellToDelete(bases.n, board, listTuple)
                merge.pushToBottom(bases.n, board, bases.proba)
                bases.display(n, board)
                graphic.printScore(possibles.checkHighest(bases.n, board))
            break
        break


# If player clicks somewhere else than the game board
def userClickButton(rawPosClick):
    rawX = rawPosClick[0]
    rawY = rawPosClick[1]
    if(400 <= rawX <= 625):
        if(140 <= rawY <= 190):
            numInc = 1
            for y in range(bases.n):
                for x in range(bases.n):
                    board[x][y] = numInc
                    numInc += 1
        elif(200 <= rawY <= 250):
            return False
        

# Infinite loop to keep the window open
# Also used to check for events
# Initializes the game  (gameStart)
# If player lost automatically restart the game        
while windowStatus:
    while gameStart:
        board = bases.boardGenerator(bases.n, bases.proba)
        bases.display(bases.n, board)
        graphic.printStaticStuff()
        graphic.printScore(possibles.checkHighest(bases.n, board))
        gameStart = False    

    if(not possibles.canStillPlay(bases.n, board)):
        gameStart = True
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                rawPos = graphic.getClickPosRaw(event)
                if(rawPos[0] > 300):
                    gStatus = userClickButton(rawPos)
                    if(gStatus == False):
                        windowStatus = False
                else:
                    uSelec = userSelect(bases.n, board)
        if event.type == QUIT:
            windowStatus = False