import pygame


class Grid:
    # rozmerz okna a barva
    SCREEN_SIZE = 600
    COLOR = (255, 255, 255)
    # zobrazeni okna
    SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    gap=10
    containerSize= SCREEN_SIZE -gap*2

    pygame.draw.rect(SCREEN, COLOR, pygame.Rect(gap, gap, containerSize, containerSize), 2)

    # vykresli bunky

    cellnum=5
    cellSize = (containerSize) / cellnum

    for x in range(cellnum):
        pygame.draw.line(
            SCREEN,COLOR,
            (gap + (cellSize * x), gap),
            (gap + (cellSize * x), containerSize + gap -1))
        # HORIZONTAl DIVISIONS
        pygame.draw.line(
            SCREEN, COLOR,
            (gap+1, gap + (cellSize * x)),
            (gap + containerSize -1, gap + (cellSize * x)))





