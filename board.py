from position import Position
from eightQueens import EightQueens

# A Board has a List of Positions, on which there are queens.
# @author (James Peirano and Izhar Ali)

class Board:
    # Positions on which there are queens
    
    #queens should really be called queenPositions


    # Default constructor
    def __init__(self):
        self.queens = list()

    # Copy Constructor
    # def __init__(self, b):
    #     self.queens = list(b.queens)

    # """ Place a queen on position p of this Board """
    def addQueen(self, p: Position):
        self.queens.append(p)
        print("i added a queen")

    # """ @return true iff no two queens on this Board
    # * are attacking each other.
    # """
    def ok(self) -> bool:
        p: Position
        other: Position

        for i in range(self.queens.size()-1):
            firstQueen = self.queens[i]
            j = i + 1
            for j in range(self.queens.size()):
                otherQueen = self.queens[j]
                if (firstQueen.isAttacking(otherQueen)):
                    return False
        
        return True

    def __str__(self):
        result = ""
        for row in range(EightQueens.SIZE):
            for col in range(EightQueens.SIZE):
                p = Position(row,col)
                if(p in self.queens):
                    result += "Q "
                else:
                    result += ". "
                
            result += "\n" #newline
        return result



# if(p.row == row and p.col == col)

# p in self.queens
    #     	 public String toString() {
	# 	 String result = "";
	# 	 for (int row=0; row<EightQueens.SIZE; row++) {
	# 		 for (int col=0; col<EightQueens.SIZE; col++) {
				 
	# 			 if (queens.contains (new Position (row, col))) {
	# 				 result += "Q ";
	# 			 } else {
	# 				 result += ". ";
				
	# 			 }
	# 		 }	
	# 		 result += "\n";
	# 			 // newline
	# 	 }
	# 	 return result;
	#  }