def arrayReplace(inputArray, elemToReplace, substitutionElem):
    """A function that replaces a specific element in a list with other element."""
    
    # Loop through the input array.
    for i in range(0,len(inputArray)):
        
        # Replace element.
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
            
    # Return input array modified.
    return inputArray




# Solution by smirnoval
def arrayReplace(i, e, s):
    return [x if x!=e else s for x in i]
