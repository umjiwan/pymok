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
                end = self.fiveCheck(x, y, stone)
                if not end:
                    pass
                else:
                    return end
            else:
                return "02"
        else:
            return "03"

    def fiveCheck(self, x, y, stone):
        # 가로/세로/우상향 대각선/우하향대각선
        for k in range(4):
            count = 1
            for v in [1, -1]:
                posStone = stone
                while posStone == stone:
                    posStone = -1
                    if k == 0:
                        _x = x + (count * v)
                        _y = y
                    elif k == 1:
                        _x = x
                        _y = y + (count * v)
                    elif k == 2:
                        _x = x + (count * v)
                        _y = y - (count * v)
                    elif k == 3:
                        _x = x + (count * v)
                        _y = y + (count * v)

                    if self.errorCheck(_x, _y): # 자체 예외처리
                        if self.board[_y, _x] == stone: # 자표값이 stone 인지 확인
                            posStone = stone
                            count += 1
            if count == 5:
                return "end"