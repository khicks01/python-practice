'''Defines the gameboard and creates the master game loop'''
import sys
import game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)

def main():
    ''' Executes the game code '''
    new_game = game.Game(SCREEN_TITLE, WHITE_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT)
    new_game.run_game_loop(5, 1)
    sys.exit()
main()
