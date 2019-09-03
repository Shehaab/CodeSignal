def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    """Returns true if two persons have the same total strength, and both have equal strongest arm."""

    # Styling.
	me = yourLeft + yourRight
	you = friendsLeft + friendsRight
    
    # Check Strength of both arms, and the strongest arm.
	if ((me) == (you)) and (max(yourLeft,yourRight) == max(friendsLeft,friendsRight)):
        return True
	else:
		return False

# This solution is by chris_l65
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
