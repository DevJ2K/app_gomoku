class StreaksRegex():
	def __init__(self):
		b_r1 = r"(?:\s?[B]{2,}\s?(?:[B]{1,2}(?:(?:\s+)|(?:[W]))?))$"
		b_r2 = r"(?:\s?[B]{1,2}\s?(?:[B]{2,}(?:(?:\s+)|(?:[W]))?))$"
		b_r3 = r"(?:\s?[B]{2,}\s?(?:[B]{1,2}(?:(?:\s+)|(?:[W]))))"
		b_r4 = r"(?:\s?[B]{1,2}\s?(?:[B]{2,}(?:(?:\s+)|(?:[W]))))"

		w_r1 = r"(?:\s?[W]{2,}\s?(?:[W]{1,2}(?:(?:\s+)|(?:[B]))?))$"
		w_r2 = r"(?:\s?[W]{1,2}\s?(?:[W]{2,}(?:(?:\s+)|(?:[B]))?))$"
		w_r3 = r"(?:\s?[W]{2,}\s?(?:[W]{1,2}(?:(?:\s+)|(?:[B]))))"
		w_r4 = r"(?:\s?[W]{1,2}\s?(?:[W]{2,}(?:(?:\s+)|(?:[B]))))"

		self.black_pattern = rf"{b_r1}|{b_r2}|{b_r3}|{b_r4}"
		self.white_pattern = rf"{w_r1}|{w_r2}|{w_r3}|{w_r4}"