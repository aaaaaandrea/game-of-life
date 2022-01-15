import pygame
import numpy as np


class Cells:
    def __init__(self, cell_num, color, screen, gap, container_size):
        self.cellMAP = np.random.randint(2, size=(cell_num, cell_num))
        self.cell_num = cell_num
        self.color = color
        self.screen = screen
        self.gap = gap
        self.cell_size = (container_size - 2) / cell_num

    def draw_first_cells(self):
        for row in range(self.cell_num):
            # print(row)
            for column in range(self.cell_num):
                # print(column)
                if self.cellMAP[column][row] == 1:
                    pygame.draw.rect(
                        self.screen, self.color,
                        (self.gap + 1 + (self.cell_size * row) + 1, self.gap + 1 + (self.cell_size * column) + 1,
                         self.cell_size - 1,
                         self.cell_size - 1))

    def calc(self):
        for row in range(self.cell_num):
            for column in range(self.cell_num):
                # counts number of living neighbours
                live = self.check_others(row, column)
                #rules
                #change color
            #  print(live)

    def check_others(self, check_row, check_column):
        live = 0

        search_min = -1
        search_max = 2

        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_column:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self.cell_num:
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self.cell_num:
                    valid_neighbour = False

                if valid_neighbour:
                    live += self.cellMAP[neighbour_row][neighbour_column]
        # print(live)
        return live
