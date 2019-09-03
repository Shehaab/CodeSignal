import re

def findEmailDomain(address):
    """Return the legitimate domain part of an Email address"""
    
    # Find @ sign, then one or more alphanumeric character, then one or more dots.
    return re.search("@[\w].+",address).group()[1:]
