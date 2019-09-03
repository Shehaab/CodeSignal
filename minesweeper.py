def minesweeper(matrix):
    """Returns an same-sized as argument matrix integer matrix, where each element is the sum of elements @ its corners which are 
       equal to the boolean True. Each element has 8 corners."""
    
    # Integer retruned matrix.
    mineMat = list()
    
    # Number of rows and columns of matrix.
    rowNum = len(matrix) - 1
    colNum = len(matrix[0]) - 1
    
    # initialize mineMat to zeros.
    for a in matrix:
        tempList = [x*0 for x in a]
        mineMat.append(tempList)
        
    # Check corners of element in matrix, and put result in mineMat
    for a in range(0,len(mineMat)):
        for b in range(0,len(mineMat[a])):
            if not ((a+1)>rowNum):
                if matrix[a+1][b]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((a-1)<0):
                if matrix[a-1][b]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((b+1)>colNum):
            	if matrix[a][b+1]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((b-1)<0):
                if matrix[a][b-1]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((a+1)>rowNum or (b+1)>colNum):
                if matrix[a+1][b+1]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((a-1)<0 or (b-1)<0):
                if matrix[a-1][b-1]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((a-1)<0 or (b+1)>colNum):
                if matrix[a-1][b+1]:
                    mineMat[a][b]=mineMat[a][b]+1
            if not ((a+1)>rowNum or (b-1)<0):
                if matrix[a+1][b-1]:
                    mineMat[a][b]=mineMat[a][b]+1
                    
    return mineMat

matrix1 = [[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]

print(minesweeper(matrix1))
