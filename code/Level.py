import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):

        self.window = window
        self.name = name
        self.game_mode = game_mode # 1p, 2p cooperative or 2p competitive
        self.entity_list: list[Entity] = []
        self.timeout = 20000

        # Getting all bg
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        # Adding the player
        self.entity_list.append(EntityFactory.get_entity('Player1'))


    def run(self,):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() # FPS

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Texts
            self.level_text(14, f'{self.name} - Timeout {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 25))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)