import pygame
import sys
from pygame.locals import *
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 650
CELL_SIZE = 5

FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (50, 50, 50)

assert WINDOW_WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size"
assert WINDOW_HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size"

NR_CELL_WIDTH = WINDOW_WIDTH / CELL_SIZE  # number of cells wide
NR_CELL_HEIGHT = WINDOW_HEIGHT / CELL_SIZE  # Number of cells high


def drawGrid(display):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):  # draw vertical lines
        pygame.draw.line(display, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):  # draw horizontal lines
        pygame.draw.line(display, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

def blankGrid():
    gridDict = {}
    for y in range (NR_CELL_HEIGHT):
        for x in range (NR_CELL_WIDTH):
            gridDict[x,y] = 0
    return gridDict

def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

#Colours the cells black for life and white for no life
def colourGrid(display, item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELL_SIZE # translates array into grid size
    x = x * CELL_SIZE # translates array into grid size
    if lifeDict[item] == 0:
        pygame.draw.rect(display, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(display, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
    return None

#Determines how many alive neighbours there are around each cell
def getNeighbours(item, lifeDict):
    neighbours = 0
    for x in range (-1, 2):
        for y in range (-1, 2):
            checkCell = (item[0] + x, item[1] + y)
            if checkCell[0] < NR_CELL_WIDTH  and checkCell[0] >= 0:
                if checkCell [1] < NR_CELL_HEIGHT and checkCell[1] >= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: # negate the central cell
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

#determines the next generation by running a 'tick'
def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        #get number of neighbours for that item
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1: # For those cells already alive
            if numberNeighbours < 2: # kill under-population
                newTick[item] = 0
            elif numberNeighbours > 3: #kill over-population
                newTick[item] = 0
            else:
                newTick[item] = 1 # keep status quo (life)
        elif lifeDict[item] == 0:
            if numberNeighbours == 3: # cell reproduces
                newTick[item] = 1
            else:
                newTick[item] = 0 # keep status quo (death)
    return newTick

def startingRpentomino(lifeDict):
    #R-pentomino
    lifeDict[48,32] = 1
    lifeDict[49,32] = 1
    lifeDict[47,33] = 1
    lifeDict[48,33] = 1
    lifeDict[48,34] = 1
    return lifeDict

def startingAcorn(lifeDict):
    #Acorn
    lifeDict[105,55] = 1
    lifeDict[106,55] = 1
    lifeDict[109,55] = 1
    lifeDict[110,55] = 1
    lifeDict[111,55] = 1
    lifeDict[106,53] = 1
    lifeDict[108,54] = 1
    return lifeDict

def startingDiehard(lifeDict):
    #Diehard
    lifeDict[45,45] = 1
    lifeDict[46,45] = 1
    lifeDict[46,46] = 1
    lifeDict[50,46] = 1
    lifeDict[51,46] = 1
    lifeDict[52,46] = 1
    lifeDict[51,44] = 1
    return lifeDict

def startingGosperGliderGun(lifeDict):
    #Gosper Glider Gun
    #left square
    lifeDict[5,15] = 1
    lifeDict[5,16] = 1
    lifeDict[6,15] = 1
    lifeDict[6,16] = 1

    #left part of gun
    lifeDict[15,15] = 1
    lifeDict[15,16] = 1
    lifeDict[15,17] = 1
    lifeDict[16,14] = 1
    lifeDict[16,18] = 1
    lifeDict[17,13] = 1
    lifeDict[18,13] = 1
    lifeDict[17,19] = 1
    lifeDict[18,19] = 1
    lifeDict[19,16] = 1
    lifeDict[20,14] = 1
    lifeDict[20,18] = 1
    lifeDict[21,15] = 1
    lifeDict[21,16] = 1
    lifeDict[21,17] = 1
    lifeDict[22,16] = 1

    #right part of gun
    lifeDict[25,13] = 1
    lifeDict[25,14] = 1
    lifeDict[25,15] = 1
    lifeDict[26,13] = 1
    lifeDict[26,14] = 1
    lifeDict[26,15] = 1
    lifeDict[27,12] = 1
    lifeDict[27,16] = 1
    lifeDict[29,11] = 1
    lifeDict[29,12] = 1
    lifeDict[29,16] = 1
    lifeDict[29,17] = 1

    #right square
    lifeDict[39,13] = 1
    lifeDict[39,14] = 1
    lifeDict[40,13] = 1
    lifeDict[40,14] = 1

    return lifeDict

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life')
    display.fill(WHITE)

    lifeDict = blankGrid()
    # lifeDict = startingGridRandom(lifeDict) # Assign random life
    # lifeDict = startingGosperGliderGun(lifeDict)
    lifeDict = startingDiehard(lifeDict)

    #Colours the live cells, blanks the dead
    for item in lifeDict:
        colourGrid(display, item, lifeDict)

    drawGrid(display)
    pygame.display.update()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

         #runs a tick
        lifeDict = tick(lifeDict)

        #Colours the live cells, blanks the dead
        for item in lifeDict:
            colourGrid(display, item, lifeDict)

        drawGrid(display)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()