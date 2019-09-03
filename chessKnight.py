def checkCell(cellPos):
	"""Returns a list of tuples for the postions the knight can move to."""

	# Knight Current postion.
	cellH = ord(cellPos[0])
	cellV = int(cellPos[1])

	return [(cellH+1,cellV+2),(cellH-1,cellV+2),(cellH+1,cellV-2),(cellH-1,cellV-2),\
	         (cellH+2,cellV+1),(cellH+2,cellV-1),(cellH-2,cellV+1),(cellH-2,cellV-1)]

def chessKnight(cell):
	"""Returns the number of positions the knight can move to."""

	# cells the knight can move to.
	canGo = 0

	# Check the validity of the knight proposed movement.
	for pos in checkCell(cell):

		if (pos[0] >= 97 and pos[0] <= 104) and (pos[1] >= 1 and pos[1] <= 8):
			canGo+=1
		else:
			pass

	return canGo


# Keeping_it_leal solution. shiiiiiiiiiiit.
def chessKnight(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2