import square

class Board:
	squares = []
	column_count = 15
	row_count = 15

	def __init__(self):
		for i in xrange(self.column_count):
			column = []
			for j in xrange(self.row_count):
				column.append(square.Square(chr(ord('A')+i), j+1))
			self.squares.append(column)