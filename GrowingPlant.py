def growingPlant(upSpeed, downSpeed, desiredHeight):
	"""Returns the number of days needed for a plant to reach desired height"""

	# Plant inside seed.
	height = 0

	# Number of days passed.
	dayPassed = 0

	# Grow and count days until you reach or pass the desired height.
	while(height<desiredHeight):

		# Plant height increase by day.
		height+=upSpeed

		# Add a day. the position of this line in the code is important.
		dayPassed = dayPassed + 1

		# If the height is already reached Exit loop.
		if height>=desiredHeight:
			return dayPassed

		# Plant height decreases by night.
		height-=downSpeed

	# Return days passed.
	return dayPassed

# This solution is by andrew_pudge
def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)


