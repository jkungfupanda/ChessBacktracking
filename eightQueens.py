from board import Board
from position import Position

class EightQueens:
    global SIZE
    SIZE = 4

    def __init__(self, b = None):
        if b == None:
            self.__board = Board()
            
            #[[' ' for i in range(SIZE)] for j in range(SIZE)]
        else:
            self.__board = [[b.__board[i][j] for j in range(SIZE)] for i in range(SIZE)]
        print(self.__board)

    def placeQueens(self, col, b):

        if col==SIZE:    # base case
            return b

        # Attempt to place a queen in each row of the
        # given col.

        for row in range(0, SIZE):
            p = Position (row, col)
            # Make a copy of the given Board
            result = Board (b)
            result.addQueen (p)
            if result.ok():
                result = self.placeQueens(col+1, result)
                if result != None:
                    return result 		# success

        return None
        # failed, time to backtrack

    

q = EightQueens()
print(q)
