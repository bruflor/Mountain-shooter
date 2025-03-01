import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        # adding a window
        self.window = window
        # uploading to pygame the image
        self.surf = pygame.image.load('./asset/MenuBg.png')
        # Adding a rectangle to display image
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # Adding sounds
        pygame.mixer_music.load('./asset/Menu.mp3')
        # Adding music in a loop with -1
        pygame.mixer_music.play(-1)

        while True:
            # Specifying the image to render inside the rectangle
            self.window.blit(source=self.surf, dest=self.rect)
            # Adding menu texts
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # Updating the screen to render all
            pygame.display.flip()

            # Check all events to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    # Adding method to create text
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
