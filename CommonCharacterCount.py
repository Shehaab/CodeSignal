def commonCharacterCount(s1, s2):
	""" Returns the number of similar characters between two strings"""

	# number of similar characters.
	counter = 0

	# mutable lists to hold characters of the two strings.
	ls1 = list()
	ls2 = list()

	# Append characters of strings to the two lists.
	for c in s1:
		ls1.append(c)
	for c in s2:
		ls2.append(c)

	# Compare both Strings
	for indx, value in enumerate(ls1):
		for indx2,value2 in enumerate(ls2):

			# increment counter, and remove character from second string to avoid duplicate characters in both lists.
			if (value == value2):
				counter = counter + 1
				ls2.pop(indx2)
				break
				
	return counter

s1 = "aabcc"
s2 = "adcaa"
c = commonCharacterCount(s1,s2)
print(c)	

#------------------------------------------------------------------------------------------------------------------------------------------------
#Keeping_it_leal Code.

def commonCharacterCount(s1, s2):
	""" Returns the number of similar characters between two strings. """

	""" com is a list, this form sees the count of the letter in both s1 and s2, takes the minimum meaning s1 = 1, s2 = 0. takes
	    s2 then sums it all. it doesn't matter taking set(s1) or taking set(s2)."""
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

# What did you learn from this code?

""" THINK IN AN ABSTRACT WAY, keeping it leal thought, I need to get the minumum count of a character in both strings, so
    he took characters in one string and operated on it, sumed the result. 3abkary yabny olahe """    		
