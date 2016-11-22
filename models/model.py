# import random
# import values as values

# tile_amounts = values.tile_amounts
# point_values = values.point_values

# class Square:
# 	bonus = ""
# 	row = 0
# 	column = ''
# 	coordinates = ""
# 	current_tile = None

# 	def __init__(self, column, row, bonus=None):
# 		if bonus: self.bonus = bonus
# 		self.row = row
# 		self.column = column
# 		self.coordinates = column + str(row)

# class Tile:
# 	letter = ''
# 	value = 0
# 	def __init__(self, letter):
# 		self.letter = letter
# 		self.value = point_values[letter]

# class Board:
# 	squares = []
# 	column_count = 15
# 	row_count = 15

# 	def __init__(self):
# 		for i in xrange(self.column_count):
# 			column = []
# 			for j in xrange(self.row_count):
# 				column.append(Square(chr(ord('A')+i), j+1))
# 			self.squares.append(column)

# class TileBag:
# 	tiles = []
# 	tile_number = 100

# 	def __init__(self):
# 		for letter in tile_amounts.keys():
# 			for i in xrange(tile_amounts[letter]):
# 				self.tiles.append(Tile(letter))

# 	def draw(self):
# 		if self.tile_number > 0:
# 			random.shuffle(self.tiles)
# 			self.tile_number -= 1
# 			return self.tiles.pop()
# 		else:
# 			return None


# class Rack:
# 	max_tiles = 7
# 	tiles = []
# 	id_num = 0

# 	def __init__(self, number):
# 		self.id_num = number
# 		self.tiles = []

# class Game:
# 	board = Board()
# 	tile_bag = TileBag()
# 	racks = {}
# 	scores = {}
# 	turn_number = 0
# 	turn_player = 0
# 	turn_player_max = 0
	
# 	def __init__(self, players):
# 		for i in xrange(players):
# 			self.racks[i+1] = Rack(i)
# 			self.scores[i+1] = 0
# 		self.turn_player_max = players

# 	def draw(self, player):
# 		while len(self.racks[player].tiles) < self.racks[player].max_tiles:
# 			self.racks[player].tiles.append(self.tile_bag.draw())