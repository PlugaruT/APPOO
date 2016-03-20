import pygame
import sys
from pygame.locals import *
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

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
            if checkCell[0] < CELL_SIZE  and checkCell[0] >= 0:
                if checkCell [1] < CELL_SIZE and checkCell[1] >= 0:
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

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life')
    display.fill(WHITE)

    lifeDict = blankGrid()
    lifeDict = startingGridRandom(lifeDict) # Assign random life

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