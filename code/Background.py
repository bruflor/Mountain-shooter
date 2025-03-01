from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        # Speed
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # When the image is on the end of the right corner, put it to restart
        if self.rect.right  <= 0:
            self.rect.left = WIN_WIDTH
