def isIPv4Address(inputString):
	""" Checks the validity of IPv4 address."""
    
	# Cut numbers as a string datatype from the string into a List.
	ipList = inputString.split(".")
    
	# Hold integers
	ipList2 = []
    
    # Check if numbers are integers.
	for num in ipList:
		try:
			ipList2.append(int(num))
		except:
			return False
    
    # Test 1 for correct form of IPv4.
	if len(ipList2) != 4:
		return False
    
    # Test 2 for correct form of IPv4.
	for num in ipList2:
		if num > 255:
			return False

	return True

# This solution is by dnl-blkv
def isIPv4Address(s):
	
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)