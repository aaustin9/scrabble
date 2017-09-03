import random
import models.tile as tile
import models.values as values

tile_amounts = values.tile_amounts

class TileBag:
	tiles = []
	tile_number = 100

	def __init__(self):
		for letter in tile_amounts.keys():
			for i in range(0, tile_amounts[letter]):
				self.tiles.append(tile.Tile(letter))

	def draw(self):
		if self.tile_number > 0:
			random.shuffle(self.tiles)
			self.tile_number -= 1
			return self.tiles.pop()
		else:
			return None