import collections
def isBeautifulString(inputString):
	"""Returns True if lengths of alphabetical characters in the input string exists and it is more than or equal 
	   its preceding one."""

	# Characters in the input string, and there count.
	sampling =  collections.Counter(inputString)

	# Sample each character and each previous alphabetical one.
	for chara,cnt in sampling.items():

		# First Alphabet, no letter before it.
		if chara == "a":
			continue

		# Check if previous alphabetical character exists.
		if chr(ord(chara)-1) in sampling:

			# previous alphabetical character must have a count more that its preceding character.
			if cnt <= sampling[chr(ord(chara)-1)]:
				continue
			else:
				return False
		else:
				return False

	return True


# This solution is by andrew_pudge

import string

def isBeautifulString(inputString):

	# Return a list of count of <ALL> alphabetical characters in the input string.
    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    # if True r must be in descending order, so if inverse(r) equal sorted(r), then the list is in descending order.
    return r[::-1] == sorted(r)