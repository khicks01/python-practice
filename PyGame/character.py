'''Creates player character '''
from game_object import GameObject

class PlayerCharacter(GameObject):
    '''Concrete playable character object'''
    SPEED = 10

    def __init__(self, x, y, width, height):
        image_path = (r"C:\Git Repos\python-practice\PyGame\player.png")
        super().__init__(image_path, x, y, width, height)
    def move(self, direction):
        '''Defines movement of the player character'''
        if direction > 0:
            self.y_pos -= direction * self.SPEED
        elif direction < 0:
            self.y_pos -= direction * self.SPEED
