def addBorder(picture):
    """Returns Modified list with (*) padding to all elements plus
       (*)*(length of the longest element) padding to the whole list."""
    
    # Add padding to all elements of the list.
    for indx, elem in enumerate(picture):
        picture[indx] = "*" + elem + "*"
        
    # Compute the longest element.
    L = len(max(picture,key=len))
    
    # Add padding to Start and End of the list.
    picture.insert(0, "*"*L)
    picture.insert(len(picture), "*"*L)
    
    return picture

# This was solved by simone_pglr @ 03/Dec/2018
def addBorder(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]