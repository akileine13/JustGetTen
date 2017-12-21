import pygame
from pygame.locals import *

backgroundColor = (33,33,33)  #Black
numSelect = (255,255,255) #White
num1 = (246,242,153) #Yellow
num2 = (240,137,137)  #Pink
num2 = (163,180,239)  #Blue
num3 = (134,239,176)  #Green
num4 = (239,146,133) #Salmon
num5 = (233,133,239) #Lavander
num6 = (245,178,107)  #Orange
num7 = (107,245,204) #Turquoise
num8 = (186, 225, 255) #Blue Pastel
num9 = (150, 111, 214) #Purple
num10 = (255, 105, 97) #Red

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont("Consolas", 30)

# Windows's size
windowHeight = 800
windowsWidth = 500

# Creating and showing the window
pygameWindow = pygame.display.set_mode((windowHeight, windowsWidth))
pygameWindow.fill(backgroundColor)
pygame.display.flip()

def printCell(boardValue, y, x):
    xPos = 25 + x * 50
    yPos = 25 + y * 50

    if(boardValue == 1):
        pygame.draw.rect(pygameWindow, num1, (xPos, yPos, 50, 50))
    elif(boardValue == 2):
        pygame.draw.rect(pygameWindow, num2, (xPos, yPos, 50, 50))
    elif(boardValue == 3):
        pygame.draw.rect(pygameWindow, num3, (xPos, yPos, 50, 50))
    elif(boardValue == 4):
        pygame.draw.rect(pygameWindow, num4, (xPos, yPos, 50, 50))
    elif(boardValue == 5):
        pygame.draw.rect(pygameWindow, num5, (xPos, yPos, 50, 50))
    elif(boardValue == 6):
        pygame.draw.rect(pygameWindow, num6, (xPos, yPos, 50, 50))
    elif(boardValue == 7):
        pygame.draw.rect(pygameWindow, num7, (xPos, yPos, 50, 50))
    elif(boardValue == 8):
        pygame.draw.rect(pygameWindow, num8, (xPos, yPos, 50, 50))
    elif(boardValue == 9):
        pygame.draw.rect(pygameWindow, num9, (xPos, yPos, 50, 50))
    elif(boardValue == 10):
        pygame.draw.rect(pygameWindow, num10, (xPos, yPos, 50, 50))
    
    # Render text in cells
    text = myfont.render(str(boardValue), 1, (33, 33, 33))
    pygameWindow.blit(text, (xPos+15, yPos+10))

    pygame.display.flip()

def getColorCell(tupleIJ):
    xPos = 25 + tupleIJ[0] * 50
    yPos = 25 + tupleIJ[1] * 50

    colorCell = pygameWindow.get_at((xPos, yPos))
    return colorCell
        

def colorSelection(tupleList, board):
    for x in range(0, len(tupleList)):
        tupleToColor = tupleList[x]
        xPos = 25 + tupleToColor[0] * 50
        yPos = 25 + tupleToColor[1] * 50

        pygame.draw.rect(pygameWindow, numSelect, (xPos, yPos, 50, 50))
        # Render text in cells
        text = myfont.render(str(board[tupleToColor[1]][tupleToColor[0]]), 1, (33, 33, 33))
        pygameWindow.blit(text, (xPos+15, yPos+10))
    pygame.display.flip()       

def getClickPos(cHeight, cWidth, event):
    clickX = int((event.pos[0] - 25) / cWidth)
    clickY = int((event.pos[1] - 25) / cHeight)
    tuplePosClick = (clickX, clickY)
    return tuplePosClick

def getClickPosRaw(event):
    clickRawX = event.pos[0]
    clickRawY = event.pos[1]
    rawPosClick = (clickRawX, clickRawY)
    return rawPosClick

def printScore(highestNum):
    #Used to "delete" printed number
    pygame.draw.rect(pygameWindow, backgroundColor, (490, 70, 50, 50))

    scoreText = myfont.render(str(highestNum), 1, (255, 255, 255))
    pygameWindow.blit(scoreText, (500, 75))
    pygame.display.flip()

def printStaticStuff():
    scoreTitle = myfont.render("Highest Number", 1, (255, 255, 255))
    pygameWindow.blit(scoreTitle, (400, 25))

    pygame.draw.rect(pygameWindow, num9, (400, 140, 225, 50))
    playAgainTitle = myfont.render("Play Again", 1, (255, 255, 255))
    pygameWindow.blit(playAgainTitle, (425, 150))

    pygame.draw.rect(pygameWindow, num9, (400, 200, 225, 50))
    quitGameTitle = myfont.render("Quit", 1, (255, 255, 255))
    pygameWindow.blit(quitGameTitle, (475, 210))

    pygame.display.flip()

# x ---> event.pos[0]
# y ---> event.pos[1]
