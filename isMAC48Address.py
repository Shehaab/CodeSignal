def isMAC48Address(inputString):
	"""Returns true if the input string is a legitimate MAC address."""


	# Check length of MAC address.
	if len(inputString)!=17:
		return False

	# Legitimate characters only.
	if  not set(inputString).issubset("ABCDEF0123456789-"):
		return False

	# MAC address has 5 hyphens.
	if inputString.count("-") != 5:
		return False

	# MAC address is correct.
	return True



print(isMAC48Address("12-34-56-78-9A-BG"))

# This solution is by dnl-blkv
def isMAC48Address(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))

