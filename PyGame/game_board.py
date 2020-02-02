'''Defines the gameboard and creates the master game loop'''
import sys
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
CLOCK = pygame.time.Clock()
TICK_RATE = 60
IS_GAME_OVER = False
pygame.init()

GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_SCREEN.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

PLAYER_IMAGE = pygame.image.load(r"C:\Git Repos\python-practice\PyGame\player.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (50, 50))

#Main game loop
while not IS_GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_GAME_OVER = True
    GAME_SCREEN.blit(PLAYER_IMAGE, (375, 375))
    #increment frame
    pygame.display.update()
    CLOCK.tick(TICK_RATE)

pygame.quit()
sys.exit()
