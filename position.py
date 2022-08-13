class Position:
	"""
	Position of a queen on the board.
	"""

	def __init__(self, r, c):
		"""
		Initialize a Position with row r and column c.
		"""
		self.row = r
		self.col = c
		

	def isAttacking(self, other):
		"""
		@return true iff a queen on this Position is attaching a queen on the other Position.
		"""
		return (
		self.row == other.row or 
		self.col == other.col or 
		self.row + self.col == other.row + other.col or 
		self.row - self.col == other.row - other.col
		)


	def __eq__(self, o: object) -> bool:
		"""
		@return true iff this Position is equal to the other Position.
		"""
		return self.row == o.row and self.col == o.col
		