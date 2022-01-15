import pygame
import numpy as np


class Cells:
    def __init__(self, cell_num, color, screen, gap, container_size):
        self.cellMAP = np.random.randint(2, size=(cell_num, cell_num))
        self.cell_num = cell_num
        self.color = color
        self.screen = screen
        self.gap = gap
        self.cell_size = (container_size-2) / cell_num

    def draw_first_cells(self):
        for row in range(self.cell_num):
            # print(row)
            for column in range(self.cell_num):
                # print(column)

                if self.cellMAP[column][row] == 1:
                    pygame.draw.rect(
                        self.screen, self.color,
                        (self.gap+1 + (self.cell_size * row)+1, self.gap+1 + (self.cell_size * column)+1, self.cell_size-1,
                         self.cell_size-1))
