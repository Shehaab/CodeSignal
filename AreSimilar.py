def areSimilar(a, b):
    """Return True two input arrays are the same with one interchangable pair, and return False otherwise"""
    
    # Check if the two arrays have the same elements.
    same = sorted(a) == sorted(b)
    
    # Check how many interchangable elements does the arrays have.
    tooMuch = 0
    
    # Count different elements between a and b.
    for indx in range(len(a)):
        if a[indx] != b[indx]:
            tooMuch = tooMuch + 1
        else:
            pass
    
    if (a == b) or (same and tooMuch == 2):
        return True
    else:
        return False
    
    
# This solution is by dnl-blkv

from collections import Counter as C

def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3
