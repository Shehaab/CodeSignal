def arrayMaximalAdjacentDifference(inputArray):
    """Returns the absolute greatest difference between two adjacent elements in a given array."""
    
    # Temp element, Greatest difference element
    X,Y = 0, 0
    
    # Test adjacent elements.
    for i in range(1,len(inputArray)):
        
        X = abs(inputArray[i] - inputArray[i-1])
        
        if X > Y:
            Y = X
            
    return Y


# This solution is by keeping_it_leal

def arrayMaximalAdjacentDifference(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)