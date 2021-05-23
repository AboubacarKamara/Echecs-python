import case

def saisie_pieces(whitePieces, blackPieces):
	map = [0 for i in range(8*8)]
	prefix = 0

	for piecesStr in whitePieces, blackPieces:
		pieces = piecesStr.split()

		for piece in pieces:
			pieceType = 0

			if len(piece) == 2:
				pieceType = 1

			elif len(piece) == 3:
				typeStr = "pdrtfc" # "Pion dame roi tour fou cavalier"
				pieceType = typeStr.find(piece[0]) + 1

				piece = piece[1:]

			if pieceType == 0:
				print("Format de pièce incorrect:", piece)
				continue

			pieceType += prefix
			index = case.xyToIndex(case.strToXY(piece))

			map[index] = pieceType


		prefix += 10

	return map

def posit():
	return [
            14, 16, 15, 12, 13, 15, 16, 14,
            11, 11, 11, 11, 11, 11, 11, 11,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            4, 6, 5, 2, 3, 5, 6, 4
        ]
