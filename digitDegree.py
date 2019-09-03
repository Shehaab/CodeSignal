def digitDegree(n):
    """Returns the number of times we need to sum digits of the number n to make it one number."""
    
    # Sum of digits. Note: n is integer not string.
    digitSum = n
    
    # Number of additions.
    count = 0
    
    # Add until one number remains.
    while(len(str(digitSum))!=1):
        
        # Sum of single digits in the number.
        digitSum = sum([int(i) for i in str(digitSum)])
        
        count+=1
        
    return count    
        

# This solution is by scraphead.

def digitDegree(n):
    
    if n < 10:
        return 0
    
    sumOfDigits = sum([int(i) for i in str(n)])
    
    # The 1 here act as a counter, and the base condition returns zero.
    return digitDegree(sumOfDigits) + 1
    
# This solution is by keeping_it_leal

def digitDegree(n):
    d=0
    while n>=10:
        n=sum([int(i) for i in str(n)])
        d+=1
    return d