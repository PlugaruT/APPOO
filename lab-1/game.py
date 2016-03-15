import pygame
import sys
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

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


def main():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Game of Life')
    display.fill(WHITE)
    pygame.display.update()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        drawGrid(display)
        pygame.display.update()

if __name__ == '__main__':
    main()