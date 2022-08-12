from position import Position

# A Board has a List of Positions, on which there are queens.
# @author (James Peirano and Izhar Ali)

class Board:
    # Positions on which there are queens
    queens = list[Position]

    # Default constructor
    def __init__(self) -> None:
        self.queens = list()

    # Copy Constructor
    def __init__(self, b) -> None:
        self.queens = list(b.queens)

    # """ Place a queen on position p of this Board """
    def addQueen(self, p: Position) -> None:
        self.queens.add(p)
        print(self)

    # """ @return true iff no two queens on this Board
    # * are attacking each other.
    # """
    def ok(self) -> bool:
        p: Position
        other: Position

        for i in range(self.queens.size()-1):
            p = self.queens[i]
            j = i + 1
            for j in range(self.queens.size()):
                other = self.queens[j]
                if (p.isAttacking(other)):
                    return False
        
        return True