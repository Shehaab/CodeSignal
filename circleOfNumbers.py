def circleOfNumbers(n, firstNumber):
    """A function that returns facing numbers equally distributed on a circle connected with a
       line passing though the center of the circle A.K.A radius"""
    
    # Read this solution in the comments section.
    return (firstNumber + n//2) % n

    # The modulus does this for us. If you make the same behaviour around a number, modulus is your guy.
    # it makes you loop around this number, or circle it , like for example circling the alphabets Z back to A.

    hRadius = n//2
    # Move the radius incremently.
    if firstNumber < hRadius:
        return (hRadius + firstNumber)
    
    # Move the radius decremently.
    if firstNumber >= hRadius:
        return (firstNumber - hRadius)