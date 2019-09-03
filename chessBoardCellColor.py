"""If ord(<letter>) is odd, then odd numbers are black, and vice versa."""

def chessBoardCellColor(cell1, cell2):
    """A function that returns boolean true for chess tiles of the same color, and Boolean False otherwise."""
    
    # Extract letter and number from cell names.
    c1 = [i for i in cell1]
    c2 = [j for j in cell2]
    
    # Check tile color for cell1.
    if ord(c1[0])%2 != 0:
        if int(c1[1])%2 !=0:
            color1 = "black"
        else:
            color1 = "white"
    else:
        if int(c1[1])%2 != 0:
            color1 = "white"
        else:
            color1 = "black"
    
    # Check for c2
    if ord(c2[0])%2 != 0:
        if int(c2[1])%2 !=0:
            color2 = "black"
        else:
            color2 = "white"
    else:
        if int(c2[1])%2 != 0:
            color2 = "white"
        else:
            color2 = "black"
            
    # see if tiles have the same color.
    if color1 == color2:
        return True
    else:
        return False
            
# This solution is by andrew_pudge
def chessBoardCellColor(cell1, cell2):
    
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0