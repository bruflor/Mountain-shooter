import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)

    def move(self):
        # On press key
        pressed_key = pygame.key.get_pressed()
        # Top
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        # Bottom
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        # Left
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # Right
        if pressed_key[pygame.K_RIGHT] and self.rect.bottom < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]