# Remember to ask your self what is the wildcard to change in this problem. its"("
# Remember to check out Range,len,enumerate, check the bookmark.
# In line 36, if I write SprintList it prints a } in the end of the string for
# "The ((quick (brown) (fox) jumps over the lazy) dog)" String and I don't know why.
def ReverseStringInside(s):
	"""Finds a word inside parenthesis inside a string, reverse the word and returns the whole string."""


	# Holds a copy of s, since s is immutable.
	StringList = list()

	# Convert string into a list.
	for c in s:
		StringList.append(c)
	

	# Extract indices of paranthesis from the string.
	A = [i for i,v in enumerate(s) if v == "("]
	B = [i for i,v in enumerate(s) if v == ")"]

	# For debugging purposes.
	print(A)
	print(B)


	# reach last ( then corresponding ) inverse string inside, and convert them to {} for algorithm purposes.
	for i in reversed(A):
		for k in range(i,len(StringList)):
			if StringList[k] == ")":
				StringList[i], StringList[k] = "{", "}"
				sublist = StringList[i:k+1]
				sublist.reverse()
				StringList[i:k+1] = sublist
				break

	print(StringList)

	# Remove parenthesis from the string.
	for e in StringList[0:]:
		if e == "}" or e == "{":
			StringList.remove(e)

	s = "".join(StringList)		

	print(s)			
	
ReverseStringInside("The ((quick (brown) (fox) jumps over the lazy) dog)")

""" Solution by grey_h """
def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


# props to vanpet90 for his genious idea to use eval in the previous version of this task
def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
