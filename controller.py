from models import game

	# def play(self, letter, column, row):

g = game.Game(2)
g.draw(1)
g.draw(2)

for key in g.racks.keys():
	output = ""
	for tile in g.racks[key].tiles:
		output += (tile.letter if tile.letter != 'blank' else '_')
	print output
