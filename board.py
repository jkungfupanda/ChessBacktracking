from position import Position


class Board:
    """
    A Board has a List of Positions, on which there are queens.
    @author (James Peirano and Izhar Ali)  
    """


    def __init__(self, size):
        """
        Initialize a Board with no queens.
        """
        self.size = size
        self.queenPositions = []


    def addQueen(self, p: Position):
        """
        Place a queen on position p of this Board.
        """
        self.queenPositions.append(p)


    def ok(self) -> bool:
        """
        @return true iff no two queens on this Board are attacking each other.
        """

        for i in range(len(self.queenPositions)-1):
            firstQueen = self.queenPositions[i]
            for j in range(i + 1, len(self.queenPositions)):
                otherQueen = self.queenPositions[j]
                if (firstQueen.isAttacking(otherQueen)):
                    return False
        
        return True


    def __str__(self):
        """
        @return a string representation of this Board.
        """

        result = ""
        for row in range(self.size):
            for col in range(self.size):
                p = Position(row,col)
                if(p in self.queenPositions):
                    result += "Q "
                else:
                    result += ". "
                
            result += "\n"
        return result
