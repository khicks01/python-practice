'''Creates generic game object interface'''
import pygame
class GameObject:
    '''Main abstract game object'''

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        '''Draws the glyph on top of an image'''
        background.blit(self.image, (self.x_pos, self.y_pos))
        