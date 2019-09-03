def deleteDigit(n):
    """Returns Maximum number by only removing one digit from n."""

    # Maximum number.
    maxNum = 0

    # Convert to string so you can iterate though the string.
    strN = str(n)

    # Remove one digit, and choose maximum number.
    for d in strN:
    	tempN = [i for i in strN]

    	# Remove a digit one @ time.
    	tempN.remove(d)

    	# Get maximum digit.
    	if int("".join(tempN)) > maxNum:
    		maxNum = int("".join(tempN))
    	else:
    		pass

    return maxNum


print(deleteDigit(861452))


# This solution is by lucky-seven.
def deleteDigit(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))