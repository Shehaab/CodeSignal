def sudoku(grid):
    """Returns true if the sudoku sequence is correct, and returns false elsewise."""
    
    # Check rows.
    for a in grid:
        
        if len(a)!=len(set(a)):
            return False
        else:
            pass
    
    # Check columns. 
    for a in range(len(grid)):
        
        # Helper variable.
        temp = []
        
        for b in range(len(grid)):
            
            temp.append(grid[b][a])
                
        if len(temp)!=len(set(temp)):
            return False
        else:
            pass
        
    # Check 3x3 matrices. 
    for i in range(0,7,3):
        for j in range(0,7,3):
            
            # Helper variable.
            temp=[]
            
            for a in grid[i:i+3]:
                for b in a[j:j+3]:
                    temp.append(b)
            
            # Check correct sequence.
            if len(temp)!=len(set(temp)):
                return False
            else:
                pass
    
    # Sudoku sequence is correct.
    return True
            
             
                
        
        
        
        

