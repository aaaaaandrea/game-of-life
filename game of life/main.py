import pygame
from grid import Grid


class Main:
    pygame.init()
    running = True

    while running:
        # zavreni okna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()
