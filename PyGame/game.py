'''Game class uses pygame to set the title, and defines the function of the main game loop'''
import pygame
import character
import enemy

pygame.init()
class Game():
    '''Defines main game class - screen parameters'''
    TICK_RATE = 30

    def __init__(self, title, fill_color, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.fill_color = (fill_color)
        pygame.display.set_caption(title)
    def wipe_screen(self, fill_color):
        '''Simple function to initialize the screen'''
        self.game_screen.fill(fill_color)
    def run_game_loop(self):
        '''defines main game loop'''
        is_game_over = False
        direction = 0
        self.wipe_screen(self.fill_color)
        player = character.PlayerCharacter(375, 700, 50, 50)
        baddie = enemy.Enemy(20, 400, 50, 50)
        #Main game loop
        while not is_game_over:
            #key press logic
            for event in pygame.event.get():
                #Quit action
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    if event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
            #screen update
            self.wipe_screen(self.fill_color)
            player.move(direction, self.height)
            baddie.move(self.width)
            baddie.draw(self.game_screen)
            player.draw(self.game_screen)
            #increment frame
            pygame.display.update()
            pygame.time.Clock().tick(self.TICK_RATE)

        pygame.quit()
