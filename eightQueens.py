from position import Position
import copy


class EightQueens:
    # class variable
    outputs = []

    def __init__(self, board):
        """
        Initialize an EightQueens with the given Board.
        """
        self.board = board
        EightQueens.__place_queens(0, board)

    @classmethod
    def __place_queens(cls, col, b):
        """
        Place queens on the board.
        """

        # base case
        if col == b.size:
            return b

        # Attempt to place a queen in each row of the given column.
        for row in range(0, b.size):
            p = Position(row, col)

            # Make a copy of the given Board
            result = copy.deepcopy(b)
            result.add_queen(p)
            EightQueens.outputs.append(result)

            if result.ok():
                result = EightQueens.__place_queens(col + 1, result)
                if result is not None:
                    # success
                    return result

        # failed, time to backtrack
        return None
