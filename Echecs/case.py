import array

def valid(xy):
	return 1 <= xy[0] <= 8 and 1 <= xy[1] <= 8

def occupied(cases, index):
	return cell(cases, index) == 0

def sameTeam(cellValue1, cellValue2):
	return (cellValue1 < 10) == (cellValue2 < 10)

def cell(cases, index):
	"""
	0: Vide
	1-6:   (Blanc) pawn, queen, king, rook, bishop, knight
	11-16: (Noir)  ^
	"""
	xy = indexToXY(index)
	assert valid(xy)

	return cases[index]


def invertXY(xy):
	width = 8

	column, row = xy

	c = width - column + 1
	r = width - row + 1

	return [c, r]

# Les fonctions suivantes partent du principe que les pièces blanches sont en bas
# et les noires en haut, si ce n'est pas le cas, utiliser invertXY

def xyToStr(xy):
	s = chr(ord('a') + xy[0] - 1)
	s += str(xy[1])

	return s

def strToXY(s):
	column = ord(s[0].lower()) - ord('a') + 1
	row = int(s[1])

	return [column, row]

def xyToIndex(xy):
	width = 8

	return (xy[1] - 1) * width + xy[0] - 1

def indexToXY(index):
	width = 8

	column = (index % width) + 1
	row = (index - column + 1) // width + 1

	return [column, row]
