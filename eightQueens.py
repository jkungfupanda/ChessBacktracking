from position import Position
from board import Board
import copy

class EightQueens:

    

    

    def __init__(self, b):
        # if b == None:
        #     pass
            
        #     #[[' ' for i in range(SIZE)] for j in range(SIZE)]
        # else:
        #     self.b = Board(b)
            
        # print(str(b))
        

        self.b = b
        # print(b)
        print(EightQueens.__placeQueens(0,b))
            
#[[b.__board[i][j] for j in range(SIZE)] for i in range(SIZE)]


    def __placeQueens(col, b):

        if col==Board.SIZE:    # base case
            return b

        # Attempt to place a queen in each row of the
        # given col.
        

        for row in range(0, Board.SIZE):
            p = Position(row, col)
            # Make a copy of the given Board
            result = copy.deepcopy(b)
            result.addQueen(p)
            print(result)
            if result.ok():
                result = EightQueens.__placeQueens(col+1, result)
                if result != None:
                    return result 		# success


        return None
        # failed, time to backtrack



b = Board()
# b.addQueen(Position(0,0))
# b.addQueen(Position(1,1))
x = EightQueens(b)
print(str(x))
