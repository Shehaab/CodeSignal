import re
def sumUpNumbers(inputString):
	"""Return sum of groceries I bought."""

	# Extract number from string, put numbers in a list, and compute sum.
	return sum(map(int,re.findall("[0-9]+",inputString)))


print(sumUpNumbers("2 apples, 12 oranges"))
