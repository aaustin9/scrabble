class Square:
	bonus = ""
	row = 0
	column = ''
	coordinates = ""
	current_tile = None

	def __init__(self, column, row, bonus=None):
		if bonus: self.bonus = bonus
		self.row = row
		self.column = column
		self.coordinates = column + str(row)