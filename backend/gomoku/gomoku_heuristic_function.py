from gomoku_state import terminate_state, winner_found, critical_situation
from gomoku_rules import count_all_three
from LittleGomoku import LittleGomoku

def game_state(gomoku: LittleGomoku) -> int:
	"""
	**********************
	* HEURISTIC FUNCTION *
	**********************
	C'est uniquement lorsqu'on atteint une terminate state or DEPTH == MAX_DEPTH que cette fonction est appelé. Donc ce n'est pas nécessaire d'appeler les fonctions pour compter constamment à par celle pour les stones capturées.
	Ca renvoie la valeur du tableau.

	End Game Conditions (TERMINATE = TRUE):
	[5] Victory = Max value - 5 stones aligned unbreakable ✅
	[5] Victory = Max value - 5 pairs catched ✅
	[0] Tie = No good- No space left on board

	Good issue (TERMINATE = FALSE):
	[4] - 5 stones aligned
	[3] - Free Four
	[2] - Free Three
	[1] - More stone catch
	# - (?) No Free Three for opponent (?)
	# - No Free Four for opponent


	All possiblities :
	1 Free Three et l'adversaire 0 Free Three
	1 Free Four et l'adversaire 0 Free Four
	+ Free Three que l'adverse
	+ Free Four que l'adverse
	Si rien de tout ça, + de paires capturées que l'adverse
	L'égalité est peut-être une bonne solution ?

	# == ===== ==
	0
	Make substraction of Maximizing Player Score and Minimizing Player Score
	We doesn't need to know you player turn is

	if max_player == BLACK:
		black_score - white_score
	else
		white_score - black_score
	"""


	# Value of thing : (S_ = Score)
	# 5 stones aligned: 100
	# 5 stones aligned: 80
	S_FIVE_ALIGNED = 1000
	# Free Four: 70
	S_FREE_FOUR = 70
	# 4 stones aligned not obstructed: 60
	S_FOUR_ALIGNED = 60
	# Free Three: 50
	S_FREE_THREE = 50
	# 3 stones aligned: 40
	S_THREE_ALIGNED = 20
	# # == PAIRS ==
	# 5 pairs catched: 100
	# 4 pairs catched: 40
	# 3 pairs catched: 30
	# 2 pairs catched: 20
	# 1 pairs catched: 10
	S_PAIRS_CAPTURED = 15



	value = 0
	score_white = 0
	score_black = 0

	########################################
	# FIVE ALIGNED
	########################################
	five_exists, who_critical = critical_situation(gomoku.board)
	if five_exists == True:
		if who_critical == 'B':
			score_black += S_FIVE_ALIGNED
		else:
			score_white += S_FIVE_ALIGNED

		print(who_critical)

	########################################
	# FREE FOUR
	########################################

	########################################
	# FOUR ALIGNED
	########################################

	########################################
	# FREE THREE
	########################################

	# Take in account of the count of three aligned can be more than the real value bc its count 2 times sometimes.
	all_three_black = count_all_three(littleGomoku.board, "B")
	all_three_white = count_all_three(littleGomoku.board, "W")

	score_white += all_three_white['free_three'] * S_FREE_THREE + all_three_white['three_aligned'] * S_THREE_ALIGNED
	score_black += all_three_black['free_three'] * S_FREE_THREE + all_three_black['three_aligned'] * S_THREE_ALIGNED
	########################################
	# THREE ALIGNED
	########################################


	########################################
	# PAIRS CATCHED
	########################################
	score_black += gomoku.black_capture * S_PAIRS_CAPTURED
	score_white += gomoku.white_capture * S_PAIRS_CAPTURED


	print(f"Black player scores => {score_black}")
	print(f"White player scores => {score_white}")
	return


	# print(gomoku_settings)
	if gomoku.settings.allowed_win_by_capture == True and (gomoku.black_capture >= 5 or gomoku.white_capture >= 5):
		value = 5
	if gomoku.settings.allowed_capture == True:
		if winner_found(gomoku.board)[0] == True:
			value = 5
	else:
		if critical_situation(gomoku.board)[0] == True:
			value = 4


	if gomoku.player_turn == gomoku.maximizing_player:
		return random.randint(1, 5)
	else:
		return random.randint(-5, -1)

if __name__ == "__main__":
	from Gomoku import Gomoku
	from gomoku_algorithm import minimax
	from MeasureTime import MeasureTime
	gomoku = Gomoku()
	gomoku.place_stone("H6", "B")
	gomoku.place_stone("J9", "W")
	gomoku.place_stone("H7", "B")
	gomoku.place_stone("J3", "W")
	gomoku.place_stone("H8", "B")
	gomoku.place_stone("J8", "W")
	gomoku.place_stone("H9", "B")
	gomoku.place_stone("J10", "W")

	gomoku.place_stone("H2", "W")
	gomoku.place_stone("H4", "W")
	gomoku.place_stone("H5", "W")

	gomoku.place_stone("H11", "W")
	gomoku.place_stone("H12", "W")
	gomoku.place_stone("H13", "W")

	gomoku.place_stone("H16", "B")
	gomoku.place_stone("H10", "B")

	# gomoku.switch_player_turn()

	littleGomoku = LittleGomoku(
		board=gomoku.board,
		player_turn=gomoku.player_turn,
		gomoku_settings=gomoku.settings,
		max_player=gomoku.maximizing_player,
		min_player=gomoku.minimizing_player,
		black_capture=gomoku.black_capture,
		white_capture=gomoku.white_capture,
		free_three_black=gomoku.free_three_black,
		free_three_white=gomoku.free_three_white,
		board_width=gomoku.get_board_width(),
		board_height=gomoku.get_board_height())

	print(littleGomoku)
	mt = MeasureTime(start=True)
	for i in range(200):
		game_state(littleGomoku)
	# game_state(littleGomoku)
	# game_state(littleGomoku)
	# game_state(littleGomoku)
	# game_state(littleGomoku)
	mt.stop()
	from gomoku_rules import count_all_three
	print(count_all_three(littleGomoku.board, "W"))
