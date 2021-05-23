from time import sleep
import random
import string
import colored
import init
import coups
import affiche
import case

def partie(map, twoPlayers):
	playedCells = [((99, 99), (99, 99))]
	eliminatedPieces = []

	player1turn = False
	whoWon = 0
	quit = False

	def printgame():
		if twoPlayers:
			return affiche.printgame(map, playedCells[len(playedCells) - 1], not player1turn)

		else:
			return affiche.printgame(map, playedCells[len(playedCells) - 1], False)

	while True:
		player1turn = not player1turn

		printgame()
		possibleMoves = coups.actu(map)

		cell1 = []
		cell2 = []
		
		if twoPlayers or player1turn:
			while True:
				if twoPlayers:
					print("Joueur", 1 if player1turn else 2, "- ", end = "")
				action = input("Entrez votre action: ")

				if action == "q":
					quit = True
					break

				if len(action) < 4:
					print("Entrée invalide, veuillez réessayer")
					continue

				cell1 = tuple(case.strToXY(action[:2]))
				cell2 = case.strToXY(action[-2:])

				if not player1turn:
					cell1 = tuple(case.invertXY(cell1))
					cell2 = case.invertXY(cell2)

				if case.valid(cell1) and case.valid(cell2) and cell1 in possibleMoves and cell2 in possibleMoves[cell1]:
					if (player1turn and map[case.xyToIndex(cell1)] < 10) or (not player1turn and map[case.xyToIndex(cell1)] > 10):
						break

					else:
						print("Vous essayez de jouer la pièce de l'adversaire !")

				print("Ce coup n'est pas valide (pour ce type de pièce), veuillez réessayer.")

			if quit:
				break

		else:
			keys = list(possibleMoves.keys())
			piece = random.randint(0, len(keys) - 1)

			cell1 = keys[piece]
			piece = random.randint(0, len(possibleMoves[cell1]) - 1)

			cell2 = possibleMoves[cell1][piece]

		playedCells.append((cell1, cell2))
		destinationValue = map[case.xyToIndex(cell2)]

		if destinationValue != 0:
			eliminatedPieces.append(destinationValue)

			if (destinationValue % 10) == 3:
				whoWon = 1 if player1turn else 2
				break

		map[case.xyToIndex(cell2)] = map[case.xyToIndex(cell1)]
		map[case.xyToIndex(cell1)] = 0

		if (map[case.xyToIndex(cell2)] % 10) == 1 and (cell2[1] == 1 or cell2[1] == 8):
			map[case.xyToIndex(cell2)] += 1


		if twoPlayers or not player1turn:
			printgame()
			s_output = "Coup joué:" if twoPlayers else "L'IA a joué:"

			if player1turn or not twoPlayers:
				print(s_output, case.xyToStr(cell1), "=>", case.xyToStr(cell2))

			else:
				a = case.invertXY(cell1)
				b = case.invertXY(cell2)

				print(s_output, case.xyToStr(a), "=>", case.xyToStr(b))

			sleep(3)


	if quit:
		print("Partie terminée prématurément.")

	else:
		printgame()
		print("Partie terminée, le joueur", whoWon, "a gagné")
	
	print("Merci d'avoir joué !")

# Programme principal
print(colored.fg(255), end="")
print(colored.bg(0), end="")

print(" === Projet Tutoré: Jeu d'échecs ===")
print("Samy BENSAID, Alexis NAIRI")
print("====================================\n")

customGame = (input("Voulez-vous faire une partie normale (n) ou une partie personnalisée (p) ?") == "p")
twoPlayers = (input("Voulez-vous jouer en 1v1 (v) ou contre IA (a) ?") == "v")

map = []

if customGame:
	print("Partie personnalisée. Veuillez donner les pièces et leurs positions (exemple: rg7 f2 g2).")
	whitePieces = input("Blancs: ")
	blackPieces = input("Noirs: ")

	map = init.saisie_pieces(whitePieces, blackPieces)

else:
	print("Partie normale.")
	map = init.posit()

print("Commencement de la partie. 'q' pour quitter.")
sleep(1)
partie(map, twoPlayers)
