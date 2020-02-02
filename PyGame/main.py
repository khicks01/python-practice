'''Defines the gameboard and creates the master game loop'''
import sys
import pygame
import game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
CLOCK = pygame.time.Clock()
PLAYER_IMAGE = pygame.image.load(r"C:\Git Repos\python-practice\PyGame\player.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (50, 50))


def main():
    ''' Executes the game code '''
    pygame.init()
    new_game = game.Game(SCREEN_TITLE, WHITE_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT)
    new_game.run_game_loop()
    pygame.quit()
    sys.exit()
main()
