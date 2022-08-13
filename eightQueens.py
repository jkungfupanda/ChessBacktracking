from position import Position
from board import Board
import copy


class EightQueens:

    def __init__(self, board):
        """
        Initialize an EightQueens with a given Board.
        """

        self.board = board
        print(EightQueens.__placeQueens(0, board))
            

    def __placeQueens(col, b):
        """
        Place queens on the board.
        """

        # base case
        if col == Board.SIZE:
            return b

        # Attempt to place a queen in each row of the
        # given column.
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
x = EightQueens(b)
