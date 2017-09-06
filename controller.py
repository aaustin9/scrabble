import random
import models.values as values
import models.game as game

PLAYER_NUMBER = 2
game = game.Game(PLAYER_NUMBER)
game.startGame()

current_turn_number = 0
active_player = 1
zero_count = 0
MAX_ZERO_COUNT = 6

while len(game.racks[active_player].tiles) > 0 and zero_count < MAX_ZERO_COUNT:
	current_turn_number += 1
	active_player = 2 - current_turn_number%2
	print(game.board.toString(game.board.TILES))
	input("It's your turn, Player " + str(active_player) + "!")
	print(game.racks[active_player].toString())
	
	word, position, direction = input("Enter move: ").split(" ")
	direction = direction.lower()
	abbreviations = {"d":"down", "r":"right"}
	if direction in abbreviations:
		direction = abbreviations[direction]

	tile_positions = game.placeWord(active_player, word, position, direction)
	play_score = game.calculatePlayScore(tile_positions, direction)
	game.scores[active_player] += play_score
	print("Play score:", play_score)
	for player in range(1, PLAYER_NUMBER+1):
		print("Player", player, "score: ", game.scores[player])

	game.draw(active_player)

game.board.print_board(game.board.TILES)
winning_player = 1
winning_score = 0
for player in range(1, PLAYER_NUMBER+1):
	if game.scores[player] >= winning_score:
		winning_score = game.scores[player]
		winning_player = player
print("Game finished! Player", player, "wins!")