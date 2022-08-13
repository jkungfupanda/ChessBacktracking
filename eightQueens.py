from position import Position
from board import Board
import copy


class EightQueens:

    list_of_outputs = []

    def __init__(self, board):
        """
        Initialize an EightQueens with a given Board.
        """

        self.board = board
        EightQueens.__placeQueens(0, board)
            

    def __placeQueens(col, b):
        """
        Place queens on the board.
        """

        # base case
        if col == b.size:
            return b

        # Attempt to place a queen in each row of the
        # given column.
        for row in range(0, b.size):
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



