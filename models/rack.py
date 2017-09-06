import models.tile as tile

class Rack:
	max_tiles = 7
	tiles = []
	id_num = 0

	def __init__(self, number):
		self.id_num = number
		self.tiles = []

	def toString(self):
		output = ""
		for tile in self.tiles:
			output += (tile.letter if tile.letter != "blank" else "_")
		return output

	def playTile(self, letter):
		for tile in range(0, len(self.tiles)):
			if self.tiles[tile].letter == letter:
				return self.tiles.pop(tile)
		if letter.islower():
			for tile in range(0, len(self.tiles)):
				if self.tiles[tile].letter == "blank":
					self.tiles[tile].letter = letter
					return self.tiles.pop(tile)
		print("Error! Invalid play!")
		return None