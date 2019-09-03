def bishopAndPawn(bishop, pawn):
	""" Returns True if the bishop can attack the pawn.
		Note: the bishop moves diagonally and the chess board is 8x8 board. A~H horizontally, and 1~8 vertically. """

	# Chess board is a square: bishop and pawn are on the same diagonal if the horizontal and vertical distances are equal.
	return abs(ord(bishop[0]) - ord(pawn[0])) == abs(int(bishop[1]) - int(pawn[1]))

print(bishopAndPawn("a5","c3"))