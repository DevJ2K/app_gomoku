from rules.gomoku_rules import switch_opponent


def check_alignment(row: str, stone: str, stone_count: int) -> bool:
	return row.count(stone) == stone_count and row.count(" ") == len(row) - stone_count
	pass

# def type_of_alignment(row: str, stone: str):
# 	opponent_stone = switch_opponent(stone)
# 	opponent_count = row.count(opponent_stone)
# 	stone_count = row.count(stone)

# 	if opponent_count > 1:
# 		return 'invalid', 0
# 	if opponent_count == 1:
# 		if row[0] != opponent_stone and row[-1] != opponent_stone:
# 			return 'invalid', 0
# 	if row[0] == " " and row[-1] == " ":
# 		row_split = row.split(" ")
# 		max_align = 0
# 		for item in row_split:
# 			if len(item) > max_align:
# 				max_align = len(item)
# 			if len(item) == stone_count:
# 				if stone_count >= 5:
# 					return 'align', 5
# 				return 'free', stone_count
# 		if max_align == 2 and stone_count == 3:
# 			return 'free', 3
# 		return 'free', max_align
# 	else:
# 		return 'align', stone_count

def type_of_alignment(row: str, stone: str):
	# print(f"'{row}'")
	opponent_stone = switch_opponent(stone)
	stone_count = row.count(stone)
	opponent_count = row.count(opponent_stone)

	# if opponent_count > 1:
	# 	return 'invalid', 0
	if opponent_count >= 1:
		if row[0] != opponent_stone and row[-1] != opponent_stone:
			return 'invalid', 0
		if row[0] == opponent_stone:
			row = row[1:]
		if row[-1] == opponent_stone:
			row = row[:-1]

	if (len(row) < 5):
		return 'invalid', 0

	row_split = row.split(" ")
	max_align = 0
	for item in row_split:
		if item.count(stone) > max_align:
			max_align = item.count(stone)
		if item.count(stone) == stone_count:
			if stone_count >= 5:
				return 'align', 5


	if stone_count == 3:
		if row[0] == " " and row[-1] == " ":
			return "free", stone_count
		return "align", stone_count

	if max_align == 4:
		i_start = row.find(4 * stone)
		i_end = i_start + 3

		i_start = i_start - 1 if i_start - 1 >= 0 else i_start
		i_end = i_end + 1 if i_end + 1 < len(row) - 1 else len(row) - 1

		if row[i_start] == " " and row[i_end] == " ":
			return "free", max_align
	return 'align', 4

def is_three_aligned(board: list[list[str]], i, j, stone):
	count = 0

	try: # F
		if check_alignment("".join([board[i][j + k] for k in range(1, 6)]), stone, 3):
			count += 1
	except:
		pass
	try: # G
		if check_alignment("".join([board[i + k][j] for k in range(1, 6)]), stone, 3):
			count += 1
	except:
		pass
	try: # D
		if check_alignment("".join([board[i + k][j + k] for k in range(1, 6)]), stone, 3):
			count += 1
	except:
		pass
	try: # H
		if check_alignment("".join([board[i + k][j - k] for k in range(1, 6)]), stone, 3):
			count += 1
	except:
		pass
	return count

"""
Si la couleur inverse de la stone (X -> Y) est au bord et unique, c'est un FREE, sinon c'est juste un alignment.
Suffit ensuite de cote la repetition pour savoir si c'est un FOUR, THREE
range(6)
FREE FOUR
- ' XXXX '
- '  XXXX'
FOUR ALIGNED
- ' XXXXY'
- 'YXXXX '
FREE THREE
- ' XX X '
- ' XXX  '
- ...
THREE ALIGNED
- ' XX XY'
- ' XXX Y'
- ...

UNKNOWN THREE
- '  XX X'
- '   XXX'

"""
