"""What did you learn from this code?
4 Execution time: Sample the code 4 every little detail on a small scale(Model) and on a large scale To get the whole
picture of the code. """

# This code courtesy to: https://github.com/emirot/codesignal/blob/master/intro/arrayMaxConsecutiveSum.py
# Absolutely Amazing: hats off 4 you my friend.
def arrayMaxConsecutiveSum(inputArray, k):
    """Returns the maximum sum of K consecutive elements."""

    # Sum of first K elements.
    i = 0

    # Maximum Sum.
    max = 0

    # Sum of first k elements.
    sum = 0

    n =  len(inputArray)

    # Compute sum of first K elements.
    while i < k:
        sum += inputArray[i]
        i += 1
    if sum > max:
        max = sum

    # Compute sum of the remaining elements
    v = sum

    for j in range(k , n):
        '''New Sum = Old Sum - Previous element + Next element
           ex. [1,2,3,4] => old sum = 1+2+3, new sum = 2+3+4 then, get rid of 1 and add 4 and so forth.
           In this code you save (k-2) addition of elements 4 every addition process, so if get the sum 1000 times you save
           execution time of addition of 1000*(k-2) elements but in my code I add this elements every time I get the sum.
        '''
        v = v - inputArray[j - k] + inputArray[j]  
        if v > max:
            max = v
    return max

# My code, but it has time limit error.
"""
def arrayMaxConsecutiveSum(inputArray, k):
    #Returns Maximum sum of K consecutine elements in an array.
    
    # For time limit purposes.
    lenArrayOnce = len(inputArray)
    
    # Array of sum of K consecutive elements.
    sumArray = [sum(inputArray[i:i+k]) for i in range(0,lenArrayOnce) if (i+k)<=lenArrayOnce]
    
    # Return maximum sum.
    return max(sumArray)

"""