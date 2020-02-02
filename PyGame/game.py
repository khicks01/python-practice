'''Game class uses pygame to set the title, and defines the function of the main game loop'''
import pygame
import character
import enemy
import game_object

pygame.init()
class Game():
    '''Defines main game class - screen parameters'''
    TICK_RATE = 30
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 75)
    def __init__(self, title, fill_color, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.fill_color = (fill_color)
        pygame.display.set_caption(title)
        background_path = r"C:\Git Repos\python-practice\PyGame\background.png"
        background_image = pygame.image.load(background_path)
        self.image = pygame.transform.scale(background_image, (width, height))
    def wipe_screen(self, fill_color):
        '''Simple function to initialize the screen'''
        self.game_screen.fill(fill_color)
    def run_game_loop(self, enemy_speed, level):
        '''defines main game loop'''
        is_game_over = False
        did_win = False
        direction = 0
        self.wipe_screen(self.fill_color)
        text = self.font.render('Level '+ str(level), True, (0, 0, 0, 0))
        self.game_screen.blit(text, (300, 350))
        pygame.display.update()
        pygame.time.Clock().tick(1)
        player = character.PlayerCharacter(375, 700, 50, 50)
        baddie_list = []
        baddie1 = enemy.Enemy(20, 400, 50, 50, enemy_speed)
        baddie2 = enemy.Enemy(self.width-40, 600, 50, 50, enemy_speed*-1)
        baddie3 = enemy.Enemy(80, 200, 50, 50, enemy_speed)
        baddie_list = [baddie1, baddie2, baddie3]
        tresure_path = r"C:\Git Repos\python-practice\PyGame\treasure.png"
        treasure = game_object.GameObject(tresure_path, 375, 50, 50, 50)
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
            self.game_screen.blit(self.image, (0, 0))
            treasure.draw(self.game_screen)
            player.move(direction, self.height)
            baddie1.move(self.width)
            baddie1.draw(self.game_screen)

            if level > 2:
                baddie2.move(self.width)
                baddie2.draw(self.game_screen)
            if level > 4:
                baddie3.move(self.width)
                baddie3.draw(self.game_screen)

            player.draw(self.game_screen)

            for baddie in baddie_list:
                if player.detect_collision(baddie):
                    is_game_over = True
                    text = self.font.render('You Lose!', True, (0, 0, 0, 0))
                    self.game_screen.blit(text, (300, 350))
                    pygame.display.update()
                    pygame.time.Clock().tick(1)
                    pygame.quit()
                    break
            if player.detect_collision(treasure):
                did_win = True
                is_game_over = True
                text = self.font.render('You Win!', True, (0, 0, 0, 0))
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                pygame.time.Clock().tick(1)
                break
            #increment frame
            pygame.display.update()
            pygame.time.Clock().tick(self.TICK_RATE)
        if did_win:
            enemy_speed += 5
            level += 1
            self.run_game_loop(enemy_speed, level)
