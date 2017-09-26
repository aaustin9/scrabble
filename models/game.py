import models.board as board
import models.rack as rack
import models.tilebag as tilebag
import models.values as values

class Game:
	board = board.Board()
	tile_bag = tilebag.TileBag()
	racks = {}
	scores = {}
	turn_number = 0
	player_number = 0
	player_number_max = 0
	dictionary = []

	perpendicular = {"right":"down", "down":"right"}
	
	def __init__(self, players):
		for i in range(0, players):
			self.racks[i+1] = rack.Rack(i)
			self.scores[i+1] = 0
		self.player_number_max = players

	def startGame(self):
		for player in range(1, self.player_number_max+1):
			self.draw(player)
			self.scores[player] = 0

	def draw(self, player):
		while len(self.racks[player].tiles) < self.racks[player].max_tiles:
			tile = self.tile_bag.draw()
			if tile:
				self.racks[player].tiles.append(tile)
			else:
				break

	def placeWord(self, player, word, position, direction, first_play=False):
		player = int(player)
		i = ord(position[0]) - ord('A')
		j = int(position[1:]) - 1
		current_position = (i,j)
		played_tiles = []
		valid_play = True
		play_through = False
		for letter in word:
			if self.board.squares[i][j].current_tile == None:
				tile = self.racks[player].playLetter(letter)
				if not tile:
					self.failPlay(player, played_tiles)
					print(1)
					return None
				self.board.squares[i][j].placeTile(tile)
				played_tiles.append((i, j))
			elif self.board.squares[i][j].current_tile.letter != letter:
				self.failPlay(player, played_tiles)
				print(2)
				return None
			else:
				play_through = True
			if direction == "right":
				i += 1
			elif direction == "down":
				j += 1
		if first_play:
			if not self.board.squares[7][7].current_tile:
				self.failPlay(player, played_tiles)
				print(3)
				return None
		elif not play_through:
			adjacent = False
			perp_direction = self.perpendicular[direction]
			for tile_position in played_tiles:
				if self.findStart(tile_position, perp_direction) != self.findEnd(tile_position, perp_direction):
					adjacent = True
			if not adjacent:
				self.failPlay(player, played_tiles)
				print(4)
				return None
		return played_tiles

	def failPlay(self, player, placed_tiles):
		print("Error! Invalid play.")
		self.returnTiles(player, placed_tiles)

	def returnTiles(self, player, placed_tiles):
		for tile_position in placed_tiles:
			i = tile_position[0]
			j = tile_position[1]
			tile = self.board.squares[i][j].current_tile
			if tile.letter.islower():
				tile.letter = "blank"
			self.racks[player].tiles.append(tile)
			self.board.squares[i][j].current_tile = None

	def calculatePlayScore(self, tile_positions, main_direction):
		start = self.findStart(tile_positions[0], main_direction)
		end = self.findEnd(tile_positions[0], main_direction)
		perp_direction = self.perpendicular[main_direction]
		play_score = self.calculateWordScore(start, end, tile_positions, main_direction)
		if(len(tile_positions) == 7):
			play_score += 50
		for position in tile_positions:
			start = self.findStart(position, perp_direction)
			end = self.findEnd(position, perp_direction)
			if start != end:
				play_score += self.calculateWordScore(start, end, [position], perp_direction)
		return play_score
	
	def calculateWordScore(self, start, end, new_tile_positions, direction):
		delta_row = 1 if direction == "down" else 0
		delta_column = 1 if direction == "right" else 0
		i = start[0]
		j = start[1]
		first_tile = True
		multiplier = 1
		total_points = 0
		while (i, j) != end:
			if first_tile:
				first_tile = False
			else:
				i += delta_column
				j += delta_row
			tile_point_value = self.board.squares[i][j].current_tile.value
			if (i, j) in new_tile_positions:
				multiplier, tile_point_value = self.applyBonus(self.board.squares[i][j].bonus, multiplier, tile_point_value)
			total_points += tile_point_value
		return multiplier * total_points

	def applyBonus(self, bonus, multiplier, tile_point_value):
		if not bonus:
			return multiplier, tile_point_value
		elif bonus == "DLS":
			return multiplier, tile_point_value*2
		elif bonus == "TLS":
			return multiplier, tile_point_value*3
		elif bonus == "DWS":
			return multiplier*2, tile_point_value
		elif bonus == "TWS":
			return multiplier*3, tile_point_value

	def findStart(self, position, main_direction):
		if main_direction == "right":
			start_column = position[0]
			active_row = position[1]
			while start_column >= 0 and self.board.squares[start_column-1][active_row].current_tile != None:
				start_column -= 1
			return (start_column, active_row)
		elif main_direction == "down":
			start_row = position[1]
			active_column = position[0]
			while start_row >= 0 and self.board.squares[active_column][start_row-1].current_tile != None:
				start_row -= 1
			return (active_column, start_row)

	def findEnd(self, position, main_direction):
		if main_direction == "right":
			end_column = position[0]
			active_row = position[1]
			while end_column < 15 and self.board.squares[end_column+1][active_row].current_tile != None:
				end_column += 1
			return (end_column, active_row)
		elif main_direction == "down":
			end_row = position[1]
			active_column = position[0]
			while end_row < 15 and self.board.squares[active_column][end_row+1].current_tile != None:
				end_row += 1
			return (active_column, end_row)

	def challenge(self, tile_positions, main_direction):
		word_start = self.findStart(tile_positions[0], main_direction)
		word_end = self.findEnd(tile_positions[0], main_direction)
		word = self.stringTiles(word_start, word_end, main_direction)
		print("Word is " + word)
		if word not in self.dictionary[word[0]][len(word)]:
			return "successful"

		perp_direction = self.perpendicular[main_direction]
		for position in tile_positions:
			word_start = self.findStart(position, perp_direction)
			word_end = self.findEnd(position, perp_direction)
			if word_start != word_end:
				word = self.stringTiles(word_start, word_end, perp_direction)
				print("Word is " + word)
				if word not in self.dictionary[word[0]][len(word)]:
					return "successful"

		return "unsuccessful"

	def stringTiles(self, start, end, direction):
		word = self.board.squares[start[0]][start[1]].current_tile.letter
		i, j = start
		while (i, j) != end:
			if direction == "right":
				i += 1
			elif direction == "down":
				j += 1
			word += self.board.squares[i][j].current_tile.letter
		return word.upper()