import pygame
import numpy as np
from cell import Cells


class Game:
    pygame.init()

    SCREEN_SIZE = 600
    WHITE = (255, 255, 255)
    CELLCOLOR = (50, 50, 255)
    CELLNUM = 50 # number of cells in row

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((Game.SCREEN_SIZE, Game.SCREEN_SIZE))
        pygame.display.set_caption('GAME OF LIFE')

        self.clock = None
        self.gap = 10
        self.containerSize = Game.SCREEN_SIZE - self.gap * 2

        self.cells = Cells(Game.CELLNUM, Game.CELLCOLOR, self.screen, self.gap, self.containerSize)

        self.cells.draw_first_cells()
        self.loop()

    def update(self):
        # draws frame
        pygame.draw.rect(self.screen, Game.WHITE,
                         pygame.Rect(self.gap, self.gap, self.containerSize, self.containerSize), 2)

        pygame.display.flip()
        self.clock.tick(2)

    def loop(self):
        self.clock = pygame.time.Clock()
        # ----------Program loop -------------
        while self.running:
            # ------------- EXIT ----------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            # -------------------------------------------------

            self.update()

        pygame.quit()
    # -----------------------------------------------------------------------------------

    # # vykresli tabulku
    #
    # cellnum = 5
    # cellSize = (containerSize) / cellnum
    #
    # for x in range(cellnum):
    #     pygame.draw.line(
    #         SCREEN, WHITE,
    #         (gap + (cellSize * x), gap),
    #         (gap + (cellSize * x), containerSize + gap - 1))
    #     # HORIZONTAl DIVISIONS
    #     pygame.draw.line(
    #         SCREEN, WHITE,
    #         (gap + 1, gap + (cellSize * x)),
    #         (gap + containerSize - 1, gap + (cellSize * x)))
