def differentSquares(matrix):
	""" Returns number of different 2X2 squares in a list"""

	# convert 2X2 square to a 4-elemented ordered tuple.
	transpose = []

	# Insert 2X2 square into a tuple.
	for r in range(0,len(matrix)-1):
		for c in range(0,len(matrix[0])-1):
			transpose.append((matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1]))

	# Get rid of duplicated, and compute length.
	return len(set(transpose))


print(differentSquares([[2,5,3,4,3,1,3,2], 
 [4,5,4,1,2,4,1,3], 
 [1,1,2,1,4,1,1,5], 
 [1,3,4,2,3,4,2,4], 
 [1,5,5,2,1,3,1,1], 
 [1,2,3,3,5,1,2,4], 
 [3,1,4,4,4,1,5,5], 
 [5,1,3,3,1,5,3,5], 
 [5,4,4,3,5,4,4,4]]))

# This solution is by bandorthild

def differentSquares(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)



# This computes the number of 2X2 squares that has different numbers in the square itself.
def differentSquares(matrix):
	"""Returns the number of 2X2 squares that are different in a matrix."""

	# Number of different squares.
	diffSquareNum = 0

	print("The length of the matrix[row][column]:",len(matrix),len(matrix[0]))

	for r in range(0,len(matrix)-1):
		for c in range(0,len(matrix[0])-1):

			print(f"I'm @ row: {r} and column: {c}")

			# 2x2 square have the same number.
			tempor = matrix[r][c]
			print(f"This is tempor: {tempor}")

			if matrix[r][c+1] != tempor:
				diffSquareNum = diffSquareNum + 1
				continue
			if matrix[r+1][c] != tempor:
				diffSquareNum = diffSquareNum + 1
				continue
			if matrix[r+1][c+1] != tempor:
				diffSquareNum = diffSquareNum + 1
				continue


	return diffSquareNum

print(differentSquares([[3,4,5,6,7,8,9]]))			