# Important note: if there is an indentation error in this code, just write a new script with this exact code without copying, there is 
# nothin wrong with it.

def boxBlur(image):
     """Returns a list of integer averages of 3x3 matrix chucks"""

    # Number of Columns&Rows of the returned list.
    colNum = len(image[0]) - 2
    rowNum = len(image) - 2
    
    # Indices to compute the average.
    rowInd = [0,3]
    colInd = [0,3]
    
    # Total sum of a 3x3 matrix.
    addIt = 0
    
    # Returned average list.
    list2 = []

    # Number of transitions to another 3x3 matrix of rows.
    for a in range(rowNum):
        
        # Average of the 3x3 row chunk.
	    list1 = []
        
	    print("a is {}".format(a))                          # For debugging.
	    print("rowInd is: {}".format(rowInd))               # For debugging.

	    # Number of transitions to another 3x3 matrix of columns.
	    for b in range(colNum):
            
		    print("b is {}".format(b))                      # For debugging.
		    print("colInd is: {}".format(colInd))           # For debugging.

		    # Compute average.
		    for i in range(rowInd[0],rowInd[1]):
			    print("i is {}".format(i))                  # For debugging
			    addIt = addIt + sum(image[i][colInd[0]:colInd[1]])
                
		    #compute Average.
		    addIt = addIt//9
            
		    # Insert Number in list1 and reset addIt.
		    list1.append(addIt)
		    addIt = 0
            
		    # Transfer to the next 3 columns.
		    colInd = [num+1 for num in colInd]
		    print(list1)

	    # Append list1 to the final list.
	    list2.append(list1)
        
	    # Reset columns for new row average number entry.
	    colInd =[0,3]
        
	    # New row entry.
	    rowInd = [num+1 for num in rowInd]
        
    return list2

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]


print(boxBlur(image))

""" The solution which does not give indentation errors."""

image = [[1,1,1], 
 [1,7,1], 
 [1,1,1]] 

colNum = len(image[0]) - 2
rowNum = len(image) - 2
rowInd = [0,3]
colInd = [0,3]
addIt = 0
list2 = []

# Number of increments for rows
for a in range(rowNum):
	list1 = []
	print("a is {}".format(a))
	print("rowInd is: {}".format(rowInd))

	# Number of increments for columns
	for b in range(colNum):
		print("b is {}".format(b))
		print("colInd is: {}".format(colInd))

		# Compute average of 3x3 matrix row-row in a row.
		for i in range(rowInd[0],rowInd[1]):
			print("i is {}".format(i))
			addIt = addIt + sum(image[i][colInd[0]:colInd[1]])
		#compute Average.
		addIt = addIt//9
		# Insert Number in list1 and reset addIt.
		# Must create new list to carry the new row transition.
		list1.append(addIt)
		addIt = 0
		# Transfer to the next 3 columns.
		colInd = [num+1 for num in colInd]
		print(list1)

	# Append list1 to the final list.
	list2.append(list1)
	# Reset columns for new row average number entry.
	colInd =[0,3]
	# New row entry.
	rowInd = [num+1 for num in rowInd]

print(list2)

