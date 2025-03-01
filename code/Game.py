from code.Menu import Menu
import pygame
import sys


class Game:
    def __init__(self):
        # iniciando o pygame
        pygame.init()
        # inicia a tela
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        #
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()