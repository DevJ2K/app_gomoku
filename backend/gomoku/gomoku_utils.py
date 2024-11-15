import string
import re

def convert_coordinate_to_xy(coordinate: str) -> tuple[int] | None:

	# regex = r"([A-Z]:\d+)|(\d+:[A-Z])"
	regex = r"(?:(?:(?P<y>[a-zA-Z])(?P<x>\d+))|(?:(?P<x_alt>\d+)(?P<y_alt>[a-zA-Z])))$"
	match_coordinate = re.match(regex, coordinate)
	if match_coordinate:
		# print(match_coordinate)
		# print(match_coordinate.group("x"))
		# print(match_coordinate.group("y"))
		x = match_coordinate.group("x") or match_coordinate.group("x_alt")
		y = match_coordinate.group("y") or match_coordinate.group("y_alt")
		if y.islower():
			y = string.ascii_lowercase.find(y)
		else:
			y = string.ascii_uppercase.find(y)
		# print(f"x:{x}, y:{y}")
		return (int(x) - 1, int(y))
	else:
		# print("Not found.")
		return (None, None)

def convert_xy_to_coordinate(x: int, y: int): # x = j | y = i
	try:
		y_str = string.ascii_uppercase[y]
		x_str = str(x + 1)
	except:
		return None
	return (f"{y_str}{x_str}")

if __name__ == "__main__":
	# convert_coordinate_to_xy("D3")
	# convert_coordinate_to_xy("D33")
	# convert_coordinate_to_xy("3D")
	# convert_coordinate_to_xy("3:D")
	
	print(convert_xy_to_coordinate(3, 5))
