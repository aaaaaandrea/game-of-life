import pygame
import numpy as np


class Cells:
    def __init__(self, cell_num, color, screen, gap, container_size):
        self.cellMAP = np.random.randint(2, size=(cell_num, cell_num))
        self.helpMAP = np.zeros((cell_num, cell_num), dtype=int)
        self.cell_num = cell_num
        self.color = color
        self.black = (0, 0, 0)
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
                alive = self.check_others(row, column)
                # rules
                self.check_rules(alive, self.cellMAP[row][column], row, column)

        self.cellMAP = self.helpMAP
        self.draw_another_gen()

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

    def check_rules(self, alive, cell, row, column):
        # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        # 2. Any live cell with two or three live neighbours lives on to the next generation.
        # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        # live cell with fewer than two live neighbours dies
        if alive < 2:
            # dies
            self.helpMAP[row, column] = 0
        # live cell with more than three live neighbours dies
        elif alive > 3:
            # dies
            self.helpMAP[row, column] = 0
        elif alive == 3:
            # survives/born
            self.helpMAP[row, column] = 1
        elif alive == 2 and cell == 0:
            # stays dead
            self.helpMAP[row, column] = 0
        elif alive == 2 and cell == 1:
            # survives
            self.helpMAP[row, column] = 1
        else:
            print('wtf stala se chyba')

    def draw_another_gen(self):
        for row in range(self.cell_num):
            for column in range(self.cell_num):
                if self.cellMAP[column][row] == 1:
                    pygame.draw.rect(
                        self.screen, self.color,
                        (self.gap + 1 + (self.cell_size * row) + 1, self.gap + 1 + (self.cell_size * column) + 1,
                         self.cell_size - 1,
                         self.cell_size - 1))
                else:
                    pygame.draw.rect(
                        self.screen, self.black,
                        (self.gap + 1 + (self.cell_size * row) + 1, self.gap + 1 + (self.cell_size * column) + 1,
                         self.cell_size - 1,
                         self.cell_size - 1))
