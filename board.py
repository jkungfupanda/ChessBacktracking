from position import Position


class Board:
    """
    A Board has a list of Positions, on which there are queens.
    @authors: James Peirano and Izhar Ali
    """

    def __init__(self, size):
        """
        Initialize a Board with size and no queens.
        """
        self.size = size
        self.queen_positions = []

    def add_queen(self, p: Position):
        """
        Place a queen on position p of this Board.
        """
        self.queen_positions.append(p)

    def ok(self) -> bool:
        """
        @return true iff no two queens on this Board are attacking each other.
        """
        for i in range(len(self.queen_positions)-1):
            first_queen = self.queen_positions[i]
            for j in range(i + 1, len(self.queen_positions)):
                other_queen = self.queen_positions[j]
                if first_queen.is_attacking(other_queen):
                    return False
        
        return True

    def __str__(self):
        """
        @return a string representation of this Board.
        """
        result = ""
        for row in range(self.size):
            for col in range(self.size):
                p = Position(row, col)
                if p in self.queen_positions:
                    result += "Q "
                else:
                    result += ". "
            result += "\n"
        return result
