import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gomoku_evaluation import *
from Gomoku import Gomoku

def test_terminate_state():
	# HORIZONTAL
	gomoku = Gomoku()
	t = 3
	for i in range(9):
		if i % 2 == 0:
			gomoku.place_stone(f"C{t}")
			t += 1
		else:
			gomoku.place_stone(f"I{i + 1}")

	assert winner_found(gomoku.board)[0] == True

	# VERTICAL
	gomoku = Gomoku()
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D5", "B")
	gomoku.place_stone(f"E5", "B")
	gomoku.place_stone(f"F5", "B")
	gomoku.place_stone(f"G5", "B")
	for i in range(6, 10):
		gomoku.place_stone(f"I{i}", "W")

	assert winner_found(gomoku.board)[0] == True
	assert terminate_state(gomoku.board) == True

	# DIAGONAL
	gomoku = Gomoku()
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D6", "B")
	gomoku.place_stone(f"E7", "B")
	gomoku.place_stone(f"F8", "B")
	gomoku.place_stone(f"G9", "B")
	for i in range(6, 10):
		gomoku.place_stone(f"I{i}", "W")

	assert winner_found(gomoku.board)[0] == True
	assert terminate_state(gomoku.board) == True

	gomoku = Gomoku(board_size=(4, 4))
	for i in range(len(gomoku.board)):
		for j in range(len(gomoku.board[i])):
			gomoku.board[i][j] = 'B'
	assert winner_found(gomoku.board)[0] == False
	assert terminate_state(gomoku.board) == True
