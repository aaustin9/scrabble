import random
import models.values as values
import models.game as game

game = game.Game(2)

game.start_game()

while True:
	game.racks[1].print_rack()
	game.racks[2].print_rack()
	game.board.print_board(game.board.TILES)

	player, word, position, direction = input("Enter move: ").split(" ")
	game.place_word(player, word, position, direction)