""" THe file consists of a base and bracket, and the base may contain brackets."""
def fileNaming(names):
	"""Returns file names without repetition in a (K) fashion"""

	# New file names.
	newNaming = []

	# Debugging.
	print(f"This is the original file names: {names}")

	# Check names O(n).
	for file in names:
		print(f"Now I'm @ '{file}' file")

		# Duplicate order.
		k = 1
		
		# New file name
		if file not in newNaming:
			print(f"{file} is not in newNaming")
			newNaming.append(file)
			print(f"newNaming after '{file}' insertion: {newNaming}")
			continue

		# Engineer the new file name taking into account strings are immutable.
		if file in newNaming:

			# Flag to extract K position in the string.
			foundK = len(file)

			# New file name, and making it mutable.
			file = f"{file}({k})"
			fileM = [c for c in file]

			# making sure that file name is not repeated.
			while(file in newNaming):
				k = k+1
				fileM[foundK+1] = str(int(fileM[foundK+1])+1)
				file = "".join(fileM)

			newNaming.append(file)
	return newNaming
		


	# Debugging
	print(f"This is new naming order: {newNaming}")


fileNaming([])


# This solution is by keeping_it_leal
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names