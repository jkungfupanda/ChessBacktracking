from position import Position
from board import Board

class EightQueens:

    

    SIZE = 4

    def __init__(self, b):
        # if b == None:
        #     pass
            
        #     #[[' ' for i in range(SIZE)] for j in range(SIZE)]
        # else:
        #     self.b = Board(b)
            
        # print(str(b))
        

        self.b = b
        # print(b)
        print(self.__placeQueens(0,b))
            
#[[b.__board[i][j] for j in range(SIZE)] for i in range(SIZE)]


    def __placeQueens(self, col, b):

        if col==self.SIZE:    # base case
            return b

        # Attempt to place a queen in each row of the
        # given col.

        for row in range(0, self.SIZE):
            p = Position(row, col)
            # Make a copy of the given Board
            result = Board (b)
            result.addQueen(p)
            if result.ok():
                result = self.placeQueens(col+1, result)
                if result != None:
                    return result 		# success

        return None
        # failed, time to backtrack



b = Board()
# b.addQueen(Position(0,0))
# b.addQueen(Position(1,1))
x = EightQueens(b)
print(str(x))
