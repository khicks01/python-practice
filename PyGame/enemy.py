'''Creates enemy non-playable character '''
from game_object import GameObject

class Enemy(GameObject):
    '''Concrete enemy character object'''
    speed = 10

    def __init__(self, x, y, width, height):
        image_path = (r"C:\Git Repos\python-practice\PyGame\enemy.png")
        super().__init__(image_path, x, y, width, height)
    def move(self, max_width):
        '''Defines automatic movement of the enemy character'''
        if self.x_pos <= 40:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 40:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed
