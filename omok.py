import numpy as np

class omok:
    def __init__(self, size=9):
        self.board = np.zeros((size, size))

om = omok()
print(om.board)