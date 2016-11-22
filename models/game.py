import board
import rack
import tilebag

class Game:
	board = board.Board()
	tile_bag = tilebag.TileBag()
	racks = {}
	scores = {}
	turn_number = 0
	turn_player = 0
	turn_player_max = 0
	
	def __init__(self, players):
		for i in xrange(players):
			self.racks[i+1] = rack.Rack(i)
			self.scores[i+1] = 0
		self.turn_player_max = players

	def draw(self, player):
		while len(self.racks[player].tiles) < self.racks[player].max_tiles:
			self.racks[player].tiles.append(self.tile_bag.draw())