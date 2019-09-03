import re

def variableName(name):
    """Function returns false if name doesn't consist of letters,digits and underscores only  &
       doesn't start with a number."""
    
    # Check the validity of name variable.
    if re.match("^[A-Za-z0-9_]*$",name) and name[0].isdigit() == False:
        return True
    else:
        return False
    

# This solution is by banach.
def variableName(name):
    return name.isidentifier()
"""A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
   A valid identifier cannot start with a number, or contain any spaces.
   => isidentifier() function returns True if the string is a valid identifier, and False otherwise."""