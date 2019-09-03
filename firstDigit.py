def firstDigit(inputString):
    """Returns the Most left number in a string."""
    
    # Loop through each character.
    for c in inputString:
        
        # Check if the character is digit.
        if c.isdigit() == True:
            return c
