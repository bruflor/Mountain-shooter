from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
import pygame
import sys


class Game:
    def __init__(self):
        # start pygame
        pygame.init()
        # set a window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]: # Players
                player_score = [0,0] # [Player1, Player2]

                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                # if is false we can add a game over screen later

            elif menu_return == MENU_OPTION[4]: # Exit
                pygame.quit()
                sys.exit()

            else:
                pass

