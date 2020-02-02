'''Creates player character '''
from game_object import GameObject

class PlayerCharacter(GameObject):
    '''Concrete playable character object'''
    SPEED = 10

    def __init__(self, x, y, width, height):
        image_path = (r"C:\Git Repos\python-practice\PyGame\player.png")
        super().__init__(image_path, x, y, width, height)
    def move(self, direction, max_height):
        '''Defines movement of the player character'''
        if direction > 0:
            self.y_pos -= direction * self.SPEED
        elif direction < 0:
            self.y_pos -= direction * self.SPEED
        #Set bottom - prevent character from going off screen
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True
