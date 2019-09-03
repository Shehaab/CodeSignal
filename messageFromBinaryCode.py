"""The code source: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa"""
"""Unicode provides a unique number for every character,
no matter what the platform,
no matter what the program,
no matter what the language."""

def messageFromBinaryCode(code):
    """Converts binary message to ASCII encoding."""
    
    n = int(code,2)
    
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()

