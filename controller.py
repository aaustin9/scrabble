import random
import models.values as values
import models.game as game
import traceback

PLAYER_NUMBER = 2
game = game.Game(PLAYER_NUMBER)
game.startGame()

dictionary_file = "dictionaries/twl06.txt"

def playGame(game):
	current_turn_number = 0
	active_player = 1
	zero_count = 0
	MAX_ZERO_COUNT = 6
	first_play = True
	game.dictionary = loadDictionary(dictionary_file)
	skip_turn = False
	challenged = False

	input("It's your turn, Player " + str(active_player) + "!")

	while zero_count < MAX_ZERO_COUNT:
		try:
			current_turn_number += 1
			print(game.board.toString(game.board.TILES))
			if not first_play and not skip_turn:
				print("It's your turn, Player " + str(active_player) + "!")
				challenge = None
				while challenge not in ["y", "yes", "n", "no", ""]:
					challenge = input("Do you challenge? y/N: " ).lower()
					if challenge in ["y", "yes"]:
						challenge_result = game.challenge(tile_positions, direction)
						print("Challenge was " + challenge_result)
						if challenge_result == "successful":
							game.scores[previous_player] -= play_score
							game.returnTiles(previous_player, tile_positions)
							for player in range(1, PLAYER_NUMBER+1):
								print("Player", player, "score: ", game.scores[player])
							print(game.board.toString(game.board.TILES))
							if game.board.squares[7][7].current_tile == None:
								first_play = True
						elif challenge_result == "unsuccessful":
							skip_turn = True
				game.draw(previous_player)
				if len(game.racks[previous_player].tiles) == 0:
					break
			else:
				skip_turn = False
			if not skip_turn:
				tile_positions = None
				while not tile_positions:
					print("Rack tiles: " + game.racks[active_player].toString(), end='')
					word, position, direction = input("\rEnter move: ").split(" ")
					direction = direction.lower()
					abbreviations = {"d":"down", "r":"right"}
					if direction in abbreviations:
						direction = abbreviations[direction]
					tile_positions = game.placeWord(active_player, word, position, direction, first_play)

				first_play = False
				play_score = game.calculatePlayScore(tile_positions, direction)
				game.scores[active_player] += play_score
				print("Play score:", play_score)
				for player in range(1, PLAYER_NUMBER+1):
					print("Player", player, "score: ", game.scores[player])
			
			previous_player = active_player
			active_player = active_player+1 if active_player < PLAYER_NUMBER else 1

		except Exception as e:
			print(str(e))
			traceback.print_tb(e.__traceback__)
			traceback.clear_frames(e.__traceback__)
			return

	game.board.print_board(game.board.TILES)
	winning_player = 1
	winning_score = 0
	for player in range(1, PLAYER_NUMBER+1):
		if game.scores[player] >= winning_score:
			winning_score = game.scores[player]
			winning_player = player
	print("Game finished! Player", player, "wins!")

def loadDictionary(dictionary_file):
	dictionary = {}
	for letter in range(ord("A"), ord("Z")+1):
		letter = chr(letter)
		dictionary[letter] = {}
		for num in range(2, 16):
			dictionary[letter][num] = set([])

	with open(dictionary_file) as f:
		word_list = [word.strip().upper() for word in f]

	for word in word_list:
		dictionary[word[0]][len(word)].add(word)

	return dictionary

playGame(game)