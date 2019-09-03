
# Try a = [-1, 150, 190, 170, -1, -1, 160, 180] or [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1].
def sortByHeight(a):
    """ Returns Heights of people in ascending orders ignoring the -1s A.K.A trees"""
    
    # Final-result list.
    Lmodified = list()
    
    # trees indices list.
    Ltree = list()
    
    # returns list of indices of tress.
    for indx,elem in enumerate(a):
	    if elem == -1:
		    Ltree.append(indx)
            
    # List of people only.
    for elem in a:
	    if elem != -1:
		    Lmodified.append(elem) 
            
    # Sort people's heights.
    Lmodified.sort()
    
    # put trees in their position again.
    for elem in Ltree:
	    Lmodified.insert(elem,-1)
        
    return Lmodified

""" This is a solution by andrew_pudge. He made a new list with sorted numbers, and used the old list as a map for indices of 
    -1s A.K.A the trees."""

def sortByHeight(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l    