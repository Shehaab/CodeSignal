"""@ first I put r'\w+' instead of r'[a-zA-Z]+ But \w takes Numbers and the underscore into account, so stay away from it.'
   Regular expressions revision -> https://stackoverflow.com/questions/1576789/in-regex-what-does-w-mean
   + sign means 1 or more. note: It does that in a greedy manner(as many characters as possible) """


import re

def longestWord(text):
	"""Returns Longest word in a string."""

	# Extract words to a list.
	words = re.findall(r"[a-zA-Z]+",text)
	print(words)

	# Return the longest word.
	return max(words, key=len)


print(longestWord("You are the best!!!!!!!!!!!! CodeFighter ever!"))

# This solution is by dnl-blkv
def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key=len)