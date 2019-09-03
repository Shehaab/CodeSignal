def validTime(time):
	"""Retruns True if the input string is a correct 24-hour format."""

	# Check the formate of the clock.
	if int(time.split(":")[0]) >= 24:
		return False
	if int(time.split(":")[1]) > 59:
		return False

	return True


print(validTime("25:73"))


# This solution is by keeping_it_leal
def validTime(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60