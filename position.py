class Position:


	def __init__(self, r, c):
		self.row = r
		self.col = c
		
	def equals(self, obj):
		other = obj
		
		return self.row == other.row and self.col == other.col


	
	
	#@return true iff a queen on this Position is attaching a queen on the other Position.
	
	def isAttacking(self, other):
		return (
		self.row == other.row or 
		self.col == other.col or 
		self.row + self.col == other.row + other.col or 
		self.row - self.col == other.row - other.col
		)

	def __eq__(self, o: object) -> bool:
		return self.row == o.row and self.col == o.col