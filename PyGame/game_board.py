'''Defines the gameboard and creates the master game loop'''
import sys
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

#Set game render speed
CLOCK = pygame.time.CLOCK()
TICK_RATE = 60
IS_GAME_OVER = False
pygame.init()

GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_SCREEN.fill(WHITE_COLOR)

while not IS_GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_GAME_OVER = True
    pygame.display.update()
    CLOCK.tick(TICK_RATE)


pygame.quit()
sys.exit()
