def lineEncoding(s):
	"""Returns the number of occurences of a character+character itself in a string if it more than 1."""

	# LineEncodings
	finalList = []

	# Character counter
	sameC = 1

	print(s)
	print()

	# Iterate through s, starting @ the second character
	for c in range(1,len(s)):

		#print(f"I'm @ character {s[c]}")

		# @ last character.
		if c == len(s)-1 and s[c] == s[c-1]:
			#print(f"I'm @ index {c} last character which is {s[c]} and it is equal to previous")
			sameC+=1
			finalList.append(f"{sameC}{s[c-1]}")

		# Different characters.
		if s[c] != s[c-1] and sameC == 1:
			finalList.append(s[c-1])

		# the similar character's streak is over.
		if s[c] != s[c-1] and sameC !=1:
			#print("Character Streak is over")
			finalList.append(f"{sameC}{s[c-1]}")
			sameC = 1

		if s[c] == s[c-1]:
			#print(f"I'm @ the same characters->index: {c}")
			sameC+=1

		# @ last character, and a streak is over
		if c == len(s)-1 and s[c]!= s[c-1]:
			finalList.append(s[c])

	return "".join(finalList)


print(lineEncoding("bbjaadlkjdl"))


# This solution is by jules_b2
from itertools import groupby
def lineEncoding(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x

# Regular expression solution.
def lineEncoding(s):
    counted = re.findall(r'((\w)\2*)', s)
    return "".join([ str(len(count[0])) + count[1] if len(count[0]) > 1 else str(count[0]) for count in counted])