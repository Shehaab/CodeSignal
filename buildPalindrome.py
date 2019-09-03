# The idea behind the code is inspired from the comment section.
def buildPalindrome(st):
	"""Returns input string as a palindrome."""

	# input string is a palindrome.
	if st == st[::-1]:
		return st

	# Helper variable.	
	stop = 0

	# Strings are immutable.
	listSt = [i for i in st]

	# Remove from string until it becomes palindrome, then add removed characters reversed.
	for i in range(len(st)):

		listSt.remove(st[i])
		
		if "".join(listSt) == "".join(listSt[::-1]):
			stop = i
			break

	return st + st[:stop+1][::-1]