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
		if string_option == self.TILES:
			output += "  "
			for letter in range(ord("A"), ord("O")+1):
				letter = chr(letter)
				output += " " + letter
			output += "\n"
		for i in range(0, self.column_count):
			if string_option == self.TILES:
				output += str(i+1)
				output += "  " if i < 9 else " "
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

	def findActiveRange(self):
		i_range = set([])
		j_range = set([])
		i = 7
		delta_i = -1
		found = True
		for sign_i in [-1, 1]:
			while delta_i <= 7:
				if not found:
					break
				found = False
				delta_i += 1
				j = 7
				sign_j = -1
				i = 7 + delta_i * sign_i
				if i not in i_range:
					for delta_j in range(0, 15):
						sign_j *= -1
						j += delta_j * sign_j
						if self.squares[i][j].current_tile != None:
							found = True
							i_range.add(i)
							j_range.add(j)
							if i > 0:
								i_range.add(i-1)
							if i < 14:
								i_range.add(i+1)
							if j > 0:
								j_range.add(j-1)
							if j < 14:
								j_range.add(j+1)
		for sign_j in [-1, 1]:
			while delta_j <= 7:
				if not found:
					break
				found = False
				delta_j += 1
				i = 7
				sign_i = -1
				j = 7 + delta_j * sign_j
				if j not in j_range:
					for delta_i in range(0, 15):
						sign_i *= -1
						i += delta_i * sign_i
						if self.squares[i][j].current_tile != None:
							found = True
							i_range.add(i)
							j_range.add(j)
							if i > 0:
								i_range.add(i-1)
							if i < 14:
								i_range.add(i+1)
							if j > 0:
								j_range.add(j-1)
							if j < 14:
								j_range.add(j+1)
		return (min(i_range), max(i_range)), (min(j_range), max(j_range))