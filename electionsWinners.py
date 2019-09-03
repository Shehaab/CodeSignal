def electionsWinners(votes, k):
	"""Returns number of candidates in the votes array that can win based on the number of pending voters <K>"""

	# The people champ.
	maxVoted = max(votes)

	# Counter of pending voters.
	iCanWin = 0

	# Check if candidate can win.
	for i in votes:

		if (i+k)>maxVoted:
			iCanWin+=1

	if iCanWin == 0 and votes.count(max(votes)) == 1:
		return 1
	else:
		return iCanWin

# This solution is by dnl-blkv

def electionsWinners(v, k):
    m = max(v)
    
    return int(v.count(m) == 1) if k == 0 else len([n for n in v if m < n + k])
