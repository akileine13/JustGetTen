import random
import possibles
import merge
import graphic
from graphic import *
import pygame
from pygame.locals import *

n = 5  # Grid Size
proba = (0.05, 0.30, 0.6)  # Probability for each number


# Return a number using the tuple Proba
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


# Generate a board with random numbers (1-4)
def boardGenerator(n, proba):
    if(0 < proba[0] < proba[1] < proba[2] < 1):
        boardList = [[0 for x in range(n)] for y in range(n)] 
        for y in range(n):
            for x in range(n):
                boardList[y][x] = gameProba(proba)
    return boardList


# Goes through each cells and display them
def display(n, baseBoard):
    for y in range(n):
        for x in range(n):
            print(baseBoard[y][x], end=' ')
            graphic.printCell(baseBoard[y][x], y, x)
            if(x == n - 1):
                print("")
