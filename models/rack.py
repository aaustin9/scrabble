import tile

class Rack:
	max_tiles = 7
	tiles = []
	id_num = 0

	def __init__(self, number):
		self.id_num = number
		self.tiles = []