
def alphabeticShift(inputString):
    """Function that returns a string where each character is bigger by one from the input string"""
    
    # Increment the character, and append it to a list. => Strings are immutable.
    # The if conditional in list comprehension can be written before the loop
    fooL = [chr(ord(i) + 1) if i!="z" else "a" for i in inputString]
    
    # return a string converted from a list.
    return "".join(fooL)


# This solution, and I almost got it but I wasn't in the right mind, is by keeping_it_leal.
# The abstraction of this is do your own data type to suit your needs, then convert it back.
def alphabeticShift(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)