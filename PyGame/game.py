'''Game class uses pygame to set the title, and defines the function of the main game loop'''
import pygame
class Game():
    '''Defines main game class - screen parameters'''
    TICK_RATE = 60

    def __init__(self, title, fill_color, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(fill_color)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        '''defines main game loop'''
        is_game_over = False
        #Main game loop
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
            #game_screen.blit(PLAYER_IMAGE, (375, 375))
            #increment frame
            pygame.display.update()
            pygame.time.Clock().tick(self.TICK_RATE)
