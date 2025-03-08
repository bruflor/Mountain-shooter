import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION


class Score:
    def __init__(self, window):
        # adding a window
        self.window = window
        # uploading to pygame the image
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        # Adding a rectangle to display image
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode:str, player_score:list[int]):
        # Adding sounds
        pygame.mixer_music.load('./asset/Score.mp3')
        # Adding music in a loop with -1
        pygame.mixer_music.play(-1)

        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(48, 'YOU WIN!!', COLOR_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                text = 'Player 1 enter your name (4 characters):'


            pygame.display.flip()
            pass

    def show(self):
        # Adding sounds
        pygame.mixer_music.load('./asset/Score.mp3')
        # Adding music in a loop with -1
        pygame.mixer_music.play(-1)

        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    # Adding method to create text
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)