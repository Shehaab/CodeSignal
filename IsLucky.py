def isLucky(n):
    """ Returns True for an even number whose first half's sum equal to its second half."""
    
    # List of digits of the number n.
    numList = [int(d) for d in str(n)]
    
    # Extract first half sum, and second half sum using list slicing.
    FSum = sum(numList[0:int((len(numList)/2))])
    SSum = sum(numList[int(len(numList)/2):])    
    
    if FSum == SSum:
        return True
    else:
        return False
    
    

