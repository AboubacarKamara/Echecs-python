import copy
import case

def actu(cells):
	width = 8
	functions = [coups_pion, coups_reine, coups_roi,
              coups_tour, coups_fou, coups_cavalier]
	possibleMoves = {}

	for i in range(width**2):
		cell = cells[i]

		if cell == 0:
			continue

		xy = tuple(case.indexToXY(i))
		possibleMoves[xy] = functions[(cell % 10) - 1](cells, i)

		if len(possibleMoves[xy]) == 0:
			del(possibleMoves[xy])

	return possibleMoves


def coups_straight_trajectory(cells, cell, trajectories, loop = True):
	baseCell = case.indexToXY(cell)
	playableCells = []

	for i in trajectories:
		currentCell = copy.copy(baseCell)

		while True:
			currentCell[0] += i[0]
			currentCell[1] += i[1]

			if not case.valid(currentCell):
				break # Hors de portée

			currentCellValue = cells[case.xyToIndex(currentCell)]

			if currentCellValue == 0:
				playableCells.append(copy.copy(currentCell))

				if not loop: # Ne bouge que sur les cellules voisines
					break    # (roi, cavalier)

				continue

			
			if not case.sameTeam(currentCellValue, cells[cell]):
				playableCells.append(copy.copy(currentCell))

			break

	return playableCells


def coups_tour(cells, cell):
	return coups_straight_trajectory(cells, cell, [(1, 0), (-1, 0), (0, 1), (0, -1)])

def coups_fou(cells, cell):
	return coups_straight_trajectory(cells, cell, [(1, 1), (-1, -1), (-1, 1), (1, -1)])

def coups_reine(cells, cell):
	return coups_straight_trajectory(cells, cell, 
	    [(1, 0), (-1, 0), (0, 1), (0, -1)] + [(1, 1), (-1, -1), (-1, 1), (1, -1)])


def coups_roi(cells, cell):
	return coups_straight_trajectory(cells, cell,
        [(1, 0), (-1, 0), (0, 1), (0, -1)] + [(1, 1), (-1, -1), (-1, 1), (1, -1)], False)

def coups_cavalier(cells, cell):
	return coups_straight_trajectory(cells, cell,
        [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)], False)


def coups_pion(cells, cell):
	cellXY = case.indexToXY(cell)
	cellValue = cells[cell]

	possibleMoves = []
	trajectories = []

	if (cellValue < 10 and cellXY[1] == 7) or (cellValue > 10 and cellXY[1] == 2):
		trajectories = [(0, 1), (0, 2)] if (cellValue > 10) else [(0, -1), (0, -2)]

	else:
		trajectories = [(0, 1)] if (cellValue > 10) else [(0, -1)]

	for i in trajectories:
		currentCell = copy.copy(cellXY)

		currentCell[0] += i[0]
		currentCell[1] += i[1]

		if not case.valid(currentCell):
			break
		
		currentCellValue = cells[case.xyToIndex(currentCell)]

		if currentCellValue == 0:
			possibleMoves.append(copy.copy(currentCell))
			continue

		break

	trajectories = [(1, 1), (-1, 1)] if (cellValue > 10) else [(1, -1), (-1, -1)]

	for i in trajectories:
		currentCell = copy.copy(cellXY)

		currentCell[0] += i[0]
		currentCell[1] += i[1]

		if not case.valid(currentCell):
			break

		currentCellValue = cells[case.xyToIndex(currentCell)]

		if currentCellValue != 0 and not case.sameTeam(currentCellValue, cellValue):
			possibleMoves.append(copy.copy(currentCell))

	return possibleMoves
