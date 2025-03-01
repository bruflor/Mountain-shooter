import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode # 1p, 2p cooperative or 2p competitive
        self.entity_list: list[Entity] = []

        # Getting all bg
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))


    def run(self,):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
