def evenDigitsOnly(n):
    """Function that returns true if all digits in a given number are even."""
    
    # Convert the number to a list.
    divideIt = [int(i) for i in str(n)]
    
    # Check digits even or odd.
    for d in divideIt:
        if (d%2) != 0:
            return False
    
    # No odd digits in n.
    return True

# Solution by keeping_it_leal

def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])

# all() is a function that returns true if all functions in the iterable are true.

