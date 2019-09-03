def extractEachKth(inputArray, k):
    """Removes an element after k steps from inputArray and returns a new List."""
    
    # Return a list if its element is not divisible by k.
    return [inputArray[i] for i in range(0,len(inputArray)) if ((i+1)%k)!=0]
    
# This solution by ben_m26
def extractEachKth(inputArray, k):
    del inputArray[k-1::k] # index starts @ zero, k starts @ 1
    return inputArray
