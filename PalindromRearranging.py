import collections

def palindromeRearranging(inputString):
    """Returns True if characters of inputString can be arranged to form a palindrome."""
    
    # Holds number of occurences of odd characters.
    countOdd = 0
    
    results = collections.Counter(inputString)
    
    # Check if the structure of inputString forms a palindrome or not.
    for key,value in results.items():
        if (value%2 != 0):
            countOdd = countOdd + 1
        else:
            pass
    
    # Return results.
    if countOdd < 2:
        return True
    else:
        return False
    
    
# This solution is by andrew_pudge

def palindromeRearranging(inputString):

    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1