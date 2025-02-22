import sys

import pygame

# iniciando o pygame
pygame.init()

# inicia a tela
window = pygame.display.set_mode(size=(600, 480))

# mantém a tela aberta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()