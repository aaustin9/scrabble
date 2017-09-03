import models.board as board
import models.rack as rack
import models.tilebag as tilebag

class Game:
	board = board.Board()
	tile_bag = tilebag.TileBag()
	racks = {}
	scores = {}
	turn_number = 0
	player_number = 0
	player_number_max = 0
	
	def __init__(self, players):
		for i in range(0, players):
			self.racks[i+1] = rack.Rack(i)
			self.scores[i+1] = 0
		self.player_number_max = players

	def start_game(self):
		for player in range(1, self.player_number_max+1):
			self.draw(player)

	def draw(self, player):
		while len(self.racks[player].tiles) < self.racks[player].max_tiles:
			self.racks[player].tiles.append(self.tile_bag.draw())

	def place_word(self, player, word, position, direction):
		player = int(player)
		i = ord(position[0]) - ord('A')
		j = int(position[1:]) - 1
		current_position = (i,j)
		for letter in word:
			if self.board.squares[i][j].current_tile == None:
				self.board.squares[i][j].place_tile(self.racks[player].play_tile(letter))
			if direction == "right":
				i += 1
			elif direction == "down":
				j += 1