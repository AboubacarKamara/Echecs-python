import os
import colored
import case

def printgame(cells, cells_played, invert = False, clear_scr = True):
	cell_played_a = case.xyToIndex(cells_played[0])
	cell_played_b = case.xyToIndex(cells_played[1])

	characters = " PQKTFCâ™˜"

	print(colored.fg(255), end="")
	print(colored.bg(0), end="")

	if clear_scr:
		clear_screen()
	else:
		print(" ")


	width = 8
	print("   A B C D E F G H")

	for i in range(1, width+1): # Lignes
		print(i, " ", end="")

		for j in range (1, width+1): # Colonnes
			xy = case.invertXY((j, i)) if invert else [j, i]
			index = case.xyToIndex(xy)
			cell = case.cell(cells, index)


			if index == cell_played_a:
				print(colored.bg(5), end="")

			if index == cell_played_b:
				print(colored.attr(5), end="")


			if cell < 10: # Blancs
				print(colored.fg(1), end="")

			else: # Noirs
				print(colored.fg(3), end="")

			print(characters[cell % 10], end="")

			print(colored.attr("reset"), end="")
			print(colored.fg(255), end="")
			print(colored.bg(0), end="")

			print(" ", end="")

		print("", i)
		
	print("   A B C D E F G H")


def clear_screen():
	if os.name == "nt":
		_ = os.system("cls")

	else:
		_ = os.system("clear")
