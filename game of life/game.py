import pygame
import numpy as np
from cell import Cells
from files import Files


class Game:
    pygame.init()

    SCREEN_SIZE = 600
    WHITE = (255, 255, 255)
    CELLCOLOR = (255, 255, 255)
    CELLNUM = 50  # number of cells in row
    REFRESH = 4  # speed of changing cells
    READFROMFILE = True  # decides if numbers are read from file or generated

    # ------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.running = True
        self.pause = False
        self.screen = pygame.display.set_mode((Game.SCREEN_SIZE, Game.SCREEN_SIZE))
        pygame.display.set_caption('GAME OF LIFE')

        self.clock = None
        self.gap = 5  # gap between end of screen and frame
        self.containerSize = Game.SCREEN_SIZE - self.gap * 2

        self.files = Files(Game.CELLNUM)
        self.cellnum = self.file_cellnum()
        self.cells = Cells(self.cellnum, Game.CELLCOLOR, self.screen, self.gap, self.containerSize)

        self.file_or_generate()
        self.loop()

        # test = Files.open_file(Game.cellnum)

    # -------------------------------------

    def file_cellnum(self):
        fileCellnum = self.files.count_cells()

        if Game.READFROMFILE:
            return fileCellnum
        else:
            return Game.CELLNUM

    # ------------------------------------------------------------------------------------------------------

    def file_or_generate(self):
        array = self.files.get_array()

        if Game.READFROMFILE:
            # print(array)
            self.cells.draw_file_cells(array)

        else:
            self.cells.draw_first_cells()

    # ------------------------------------------------------------------------------------------------------

    def update(self):
        # draws frame/container
        pygame.draw.rect(self.screen, Game.WHITE,
                         pygame.Rect(self.gap, self.gap, self.containerSize, self.containerSize), 2)

        self.cells.calc()
        pygame.display.flip()
        self.clock.tick(Game.REFRESH)

    # ------------------------------------------------------------------------------------------------------

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

            # pressed = pygame.key.get_pressed()
            # if pressed[pygame.K_SPACE]:
            #     self.pause()

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
