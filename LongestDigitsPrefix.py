def longestDigitsPrefix(inputString):
	"""Returns the longest digit prefix in a string."""

	# No digit prefix.
	if not inputString[0].isdigit():
		return ""

    # Stop @ the first not digit character you see.
	for n,c  in enumerate(inputString):
		if not c.isdigit():
			return inputString[:n]

	# Whole string is a number.
	return inputString



# This solution is by thienbui
def longestDigitsPrefix(inputString):

	# ^: Start of the string, \d: Decimal digit, *: 1 or more, re.findall returns a list, [0]: first character which is a string.
    return re.findall('^\d*',inputString)[0]
