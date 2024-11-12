from gomoku_state import terminate_state, winner_found, critical_situation
from gomoku_rules import count_all_three, count_free_three
from LittleGomoku import LittleGomoku

def game_state(gomoku: LittleGomoku) -> int:
	"""
	**********************
	* HEURISTIC FUNCTION *
	**********************
	* EXCEPT TIME < 5MS  *
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

	########################################
	# FREE FOUR
	########################################
	score_black += gomoku.free_four_black * S_FREE_FOUR
	score_white += gomoku.free_four_white * S_FREE_FOUR

	########################################
	# FOUR ALIGNED
	########################################
	score_black += gomoku.four_aligned_black * S_FOUR_ALIGNED
	score_white += gomoku.four_aligned_white * S_FOUR_ALIGNED

	########################################
	# FREE THREE
	########################################
	score_black += gomoku.free_three_black * S_FREE_THREE
	score_white += gomoku.free_three_white * S_FREE_THREE

	########################################
	# THREE ALIGNED
	########################################
	score_black += gomoku.three_aligned_black * S_THREE_ALIGNED
	score_white += gomoku.three_aligned_white * S_THREE_ALIGNED

	########################################
	# PAIRS CATCHED
	########################################
	score_black += gomoku.black_capture * S_PAIRS_CAPTURED
	score_white += gomoku.white_capture * S_PAIRS_CAPTURED


	print(f"Black player scores => {score_black}")
	print(f"White player scores => {score_white}")

	if gomoku.maximizing_player == "B":
		return score_black - score_white
	else:
		return score_white - score_black


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

if __name__ == "2__main__2":
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

	for i in range(7, 11):
		gomoku.place_stone(f"C{i}", "W")

	for i in range(9, 13):
		gomoku.place_stone(f"E{i}", "W")
	gomoku.place_stone(f"E13", "B")

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
	# for i in range(200):
	# 	game_state(littleGomoku)
	# iteration = 361
	iteration = 1000
	print(f"TIMER START FOR {iteration} ITERATIONS")
	for i in range(iteration):
		game_state(littleGomoku)
	# game_state(littleGomoku)
	# game_state(littleGomoku)
	# game_state(littleGomoku)
	mt.stop()
	from gomoku_rules import count_all_three
	print(count_all_three(littleGomoku.board, "W"))



if __name__ == "__main__":
	from Gomoku import Gomoku
	from gomoku_algorithm import minimax
	from MeasureTime import MeasureTime
	gomoku = Gomoku()
	gomoku.place_stone("G6", "B")
	gomoku.place_stone("H7", "W")
	gomoku.place_stone("J3", "B")
	# gomoku.place_stone("H8", "W")
	gomoku.place_stone("J8", "B")
	gomoku.place_stone("H9", "W")
	gomoku.place_stone("J10", "B")
	gomoku.place_stone("R17", "W")
	# gomoku.place_stone("R18", "W")
	gomoku.switch_player_turn()

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

	print(gomoku)
	# gomoku.board[3][1] = "W"
	print(littleGomoku.player_turn)
	print(littleGomoku.maximizing_player)
	print(littleGomoku.minimizing_player)


	measureTime = MeasureTime(start=True)
	actions = littleGomoku.get_actions()
	# littleGomoku.paint_actions(actions)
	print(actions)
	print(minimax(littleGomoku, MAX_DEPTH=1))
	measureTime.stop()
	# littleGomoku.paint_actions(actions)
	# print(is_creating_db_free_three(littleGomoku.board, 3, 1, "W"))
	# littleGomoku.board[7][5] = "W"
	# print(is_free_three(littleGomoku.board, 7, 5, "W"))
	print(littleGomoku)
