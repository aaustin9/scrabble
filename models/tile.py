import values

class Tile:
	letter = ''
	value = 0
	def __init__(self, letter):
		self.letter = letter
		self.value = values.point_values[letter]