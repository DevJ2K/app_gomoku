import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.count_alignment import type_of_alignment

def test_type_of_alignment():
	assert type_of_alignment("  WWW ", "W") == ('free', 3)
	assert type_of_alignment(" WWWW ", "W") == ('free', 4)
	assert type_of_alignment(" WWWW ", "W") == ('free', 4)
	assert type_of_alignment("  WWWW", "W") == ('align', 4)
	assert type_of_alignment("  W WWW ", "W") == ('free', 3)
	assert type_of_alignment("       WWW W ", "W") == ('free', 3)
	assert type_of_alignment("      W WWW        ", "W") == ('free', 3)
	assert type_of_alignment("WWW      ", "W") == ('align', 3)
	assert type_of_alignment("    WW", "W") == ('align', 2)
	assert type_of_alignment("   WWB", "W") == ('align', 2)
