def alternatingSums(a):
    """ Sums elements of an array into two teams, and returns an array with sums of two teams."""
    
    # Holds the sums of two teams.
    team1 = 0
    team2 = 0
    
    # Divide two teams, and add their sum.
    for indx, val in enumerate(a):
        if indx % 2 == 0:
            team1 = team1 + val
        else:
            team2 = team2 + val
    
    # Sum of two teams
    b = [team1, team2]
    
    return b


# Solution by andrew_pudge.
def alternatingSums(a):

    return [sum(a[::2]),sum(a[1::2])]