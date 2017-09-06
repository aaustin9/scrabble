import models.square as square

class Board:
	squares = []
	column_count = 15
	row_count = 15
	BONUSES = 1
	TILES = 2
	COORDINATES = 3

	def __init__(self):
		for i in range(0, self.column_count):
			column = []
			for j in range(0, self.row_count):
				bonus = None
				if i%7 == 0 and j%7 == 0:
					bonus = "TWS"
				if abs(7-i) == abs(7-j) and abs(7-i) in [0,3,4,5,6]:
					bonus = "DWS"
				elif i%4 == 1 and j%4 == 1 and (i in [5,9] or j in [5,9]):
					bonus = "TLS"
				elif ((i in [0,14] and j in [3, 11]) or (i in [3,11] and j in [0,14]) or 
					(i in [2,6,8,12] and j in [6,8]) or (i in [6,8] and j in [2,12]) or
					(i == 7 and j in [3,11]) or (j == 7 and i in [3,11])):
					bonus = "DLS"
				column.append(square.Square(chr(ord('A')+i), j+1, bonus))
			self.squares.append(column)

	def toString(self, string_option):
		output = ""
		for i in range(0, self.column_count):
			for j in range(0, self.row_count):
				if string_option == self.BONUSES:
					bonus = self.squares[j][i].bonus
					output += (bonus if bonus else "---") + " "
				elif string_option == self.TILES:
					tile = self.squares[j][i].current_tile
					bonus = self.squares[j][i].bonus
					character_representations = {"DLS": "'", "TLS": "\"", "DWS": "+", "TWS": "#"}
					if tile != None:
						output += tile.letter + " "
					elif bonus == None:
						output += "- "
					else:
						output += character_representations[bonus] + " "
				elif string_option == self.COORDINATES:
					coordinates = self.squares[j][i].coordinates
					output += coordinates + (" " if len(coordinates) == 3 else "  ")
			output += "\n"
		return output