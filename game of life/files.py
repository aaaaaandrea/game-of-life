import numpy as np


class Files:
    def __init__(self, cellnum):
        self.cellnum = cellnum
        self.patternArray=0

    # --------------------------------------------------------------
    def count_cells(self):
        file = open("table.txt")
        pattern = np.loadtxt(file, delimiter=",")

        self.patternArray=pattern

        # cellnumFile = pattern.size
        cellnumFile = len(pattern)

        return cellnumFile

    def get_array(self):
        return self.patternArray

    # def open_file(self):
    #     with open('table.txt', 'r') as reader:
    #         pattern = np.array(reader.read())
    #     print(pattern)
    #     return pattern

