def knapsackLight(value1, weight1, value2, weight2, maxW):
	"""returns maximum value can be obtained without passing maximum weight of the two values."""

	# I can't carry any of these items.
	if maxW<weight1 and maxW<weight2:
		return 0

	# I can carry both items.
	if maxW>=(weight1+weight2):
		return (value1+value2)

	# Return higher value if its weight is easy for me.
	elif weight1<maxW and weight2<maxW:
		return max(value1,value2)

	else:
		if weight1<maxW:
			return value1
		else:
			return value2

# Solution by virgile_f
def knapsackLight(v1, w1, v2, w2, W):
    return max(int(w1<=W)*v1, int(w2<=W)*v2, int(w1+w2<=W)*(v1+v2))
