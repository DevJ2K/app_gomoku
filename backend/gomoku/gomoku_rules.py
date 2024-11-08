def get_all_positions_pairs(board, i, j):
	possibility = ("WBBW", "BWWB")
	try: # F
		if "".join([board[i][j + k] for k in range(4)]) in possibility:
			return [(i, j + 1), (i, j + 2)]
	except:
		pass
	try: # I
		if "".join([board[i][j - k] for k in range(4)]) in possibility:
			return [(i, j - 1), (i, j - 2)]
	except:
		pass
	try: # G
		if "".join([board[i + k][j] for k in range(4)]) in possibility:
			return [(i + 1, j), (i + 2, j)]
	except:
		pass
	try: # E
		if "".join([board[i - k][j] for k in range(4)]) in possibility:
			return [(i - 1, j), (i - 2, j)]
	except:
		pass
	try: # A
		if "".join([board[i - k][j - k] for k in range(4)]) in possibility:
			return [(i - 1, j - 1), (i - 2, j - 2)]
	except:
		pass
	try: # D
		if "".join([board[i + k][j + k] for k in range(4)]) in possibility:
			return [(i + 1, j + 1), (i + 1, j + 2)]
	except:
		pass
	try: # C
		if "".join([board[i - k][j + k] for k in range(4)]) in possibility:
			return [(i - 1, j + 1), (i - 1, j + 2)]
	except:
		pass
	try: # H
		if "".join([board[i + k][j - k] for k in range(4)]) in possibility:
			return [(i + 1, j - 1), (i + 2, j - 2)]
	except:
		pass
	return None

def switch_opponent(string: str) -> str:
	r_str = ""
	for c in string:
		if c == "W":
			r_str += "B"
		elif c == "B":
			r_str += "W"
		else:
			r_str += c
	return r_str

def pair_can_be_capture(board: list[list[str]], i, j, stone) -> list[tuple[int]] | None:
	possibility = ("WBBW", "BWWB")
	try: # F
		if stone + "".join([board[i][j + k] for k in range(1, 4)]) in possibility:
			return [(i, j + 1), (i, j + 2)]
	except:
		pass
	try: # I
		if stone + "".join([board[i][j - k] for k in range(1, 4)]) in possibility:
			return [(i, j - 1), (i, j - 2)]
	except:
		pass
	try: # G
		if stone + "".join([board[i + k][j] for k in range(1, 4)]) in possibility:
			return [(i + 1, j), (i + 2, j)]
	except:
		pass
	try: # E
		if stone + "".join([board[i - k][j] for k in range(1, 4)]) in possibility:
			return [(i - 1, j), (i - 2, j)]
	except:
		pass
	try: # A
		if stone + "".join([board[i - k][j - k] for k in range(1, 4)]) in possibility:
			return [(i - 1, j - 1), (i - 2, j - 2)]
	except:
		pass
	try: # D
		if stone + "".join([board[i + k][j + k] for k in range(1, 4)]) in possibility:
			return [(i + 1, j + 1), (i + 1, j + 2)]
	except:
		pass
	try: # C
		if stone + "".join([board[i - k][j + k] for k in range(1, 4)]) in possibility:
			return [(i - 1, j + 1), (i - 1, j + 2)]
	except:
		pass
	try: # H
		if stone + "".join([board[i + k][j - k] for k in range(1, 4)]) in possibility:
			return [(i + 1, j - 1), (i + 2, j - 2)]
	except:
		pass
	return None

# board = [
# 	[" ", "C", " ", " ", " ", " ", " ", " "],
# 	["W", " ", " ", "W", " ", " ", "W", " "],
# 	[" ", "A", " ", "E", " ", "C", " ", " "],
# 	[" ", " ", "A", "E", "C", " ", " ", " "],
# 	["W", "I", "I", "W", "F", "F", "W", " "],
# 	[" ", " ", "H", "G", "D", " ", " ", " "],
# 	[" ", "H", " ", "G", " ", "D", " ", " "],
# 	["W", " ", " ", "W", " ", " ", "W", " "],
# 	[" ", " ", " ", " ", " ", " ", " ", " "],
# ]

def is_free_three(board: list[list[str]], i, j, stone):
	"""
	Les free_three possibles :
	'  BBB ' => ' BBBB '
	' B BB ' => ' BBBB '
	' BB B ' => ' BBBB '
	' BBB  ' => ' BBBB '
	"""
	count = 0
	if stone == 'B':
		possibility = ("  BBB ", " BBB  ", " B BB ", " BB B ")
		large_double_three = "  BBB  "
	elif stone == 'W':
		possibility = ("  WWW ", " WWW  ", " W WW ", " WW W ")
		large_double_three = "  WWW  "
	else:
		return count
	try: # F
		# print(f"{i}:{j}" ,"{" ,"".join([board[i][j + k] for k in range(0, 6)]), "}")
		if "".join([board[i][j + k] for k in range(0, 6)]) in possibility:
			count += 1
		if "".join([board[i][j + k] for k in range(0, 7)]) == large_double_three:
			count -= 1
	except:
		pass
	try: # G
		if "".join([board[i + k][j] for k in range(0, 6)]) in possibility:
			count += 1
		if "".join([board[i + k][j] for k in range(0, 7)]) == large_double_three:
			count -= 1
	except:
		pass
	try: # D
		if "".join([board[i + k][j + k] for k in range(0, 6)]) in possibility:
			count += 1
		if "".join([board[i + k][j + k] for k in range(0, 7)]) == large_double_three:
			count -= 1
	except:
		pass
	try: # H
		if "".join([board[i + k][j - k] for k in range(0, 6)]) in possibility:
			count += 1
		if "".join([board[i + k][j - k] for k in range(0, 7)]) == large_double_three:
			count -= 1
	except:
		pass
	return count

def count_free_three(board: list[list[str]], stone: str):
	count = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == " ":
				count += is_free_three(board, i, j, stone)
	return count

def remove_pair_capture(board: list[list[str]]) -> dict | None:
	for i in range(len(board)):
		for j in range(len(board[i])):
			value = pair_can_be_capture(board, i, j)
			if value:
				return {'stone_attack': board[i][j], 'coordinate_to_remove': value}
	return None


def main0():
	from Gomoku import Gomoku
	gomoku = Gomoku()
	# HORIZONTAL
	t = 3
	for i in range(9):
		if i % 2 == 0:
			gomoku.place_stone(f"C{t}")
			t += 1
		else:
			gomoku.place_stone(f"I{i + 1}")

	# VERTICAL
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D5", "B")
	gomoku.place_stone(f"E5", "B")
	gomoku.place_stone(f"F5", "B")
	gomoku.place_stone(f"G5", "B")
	for i in range(6, 10):
		gomoku.place_stone(f"I{i}", "W")

	# DIAGONAL
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D6", "B")
	gomoku.place_stone(f"E7", "B")
	gomoku.place_stone(f"F8", "B")
	gomoku.place_stone(f"G9", "B")
	for i in range(6, 10):
		gomoku.place_stone(f"I{i}", "W")

	# TIE
	for i in range(len(gomoku.board)):
		for j in range(len(gomoku.board[i])):
			gomoku.board[i][j] = 'B'

def main1():
	from Gomoku import Gomoku
	gomoku = Gomoku()
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D5", "W")
	gomoku.place_stone(f"E5", "W")
	print(remove_pair_capture(gomoku.board))
	gomoku.place_stone(f"F5", "B")
	print(remove_pair_capture(gomoku.board))

def main_creating_double_three():
	from Gomoku import Gomoku
	gomoku = Gomoku()
	gomoku.place_stone(f"C5", "B")
	gomoku.place_stone(f"D6", "B")
	gomoku.place_stone(f"F9", "B")
	gomoku.place_stone(f"F10", "B")
	# print(is_creating_double_three(gomoku.board, 5, 7, "B"))

	gomoku.place_stone(f"G9", "B")
	gomoku.place_stone(f"H10", "B")
	# gomoku.place_stone(f"I11", "B")


	# gomoku.place_stone(f"F8", "B")
	print(count_free_three(gomoku.board, "B"))
	gomoku.place_stone(f"F8", "B")
	print(count_free_three(gomoku.board, "B"))
	# print(is_creating_double_three(gomoku.board, 5, 7, "B"))
	print(gomoku)
	# print(remove_pair_capture(gomoku.board))

if __name__ == "__main__":
	# print(switch_opponent("WBBW  B"))
	main_creating_double_three()
	# stri = "BB B "
	# print(stri.count("B"))
	# print(stri.count(" "))
	# test2()
	pass



	# print(gomoku)
	# print(terminate_state(gomoku.board))
	pass
