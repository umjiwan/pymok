import numpy as np

class omok:
    def __init__(self, size=9):
        if size > 5:
            self.board = np.zeros((size, size))
            self.size = size
        else:
            return "01"

    def errorCheck(self, x, y):
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            return True
        else:
            return False

    def put(self, x, y, stone):
        if self.errorCheck(x, y):
            if self.board[y, x] == 0:
                self.board[y, x] = stone
            else:
                return "02"
        else:
            return "03"

    def endCheck(self, x, y, stone):
        # 가로
        if self.errorCheck(x-2, x+2)
            if np.all(self.board[y, x-2:x+3] == stone):
                return "end"
        else:
            return "03"

if __name__ == "__main__":
    om = omok()
    while True:
        print(om.board)
        x, y = input("x y : ").split(" ")
        print(om.put(int(x), int(y), 1))
