""" This brilliant solution is From this guy:
	https://github.com/dvitsios/codesignal-my-solutions/blob/master/avoidObstacles/avoidObstacles.py
"""
"""
Explaination: If numbers of the list are all divisible by a given number, then I can't use this number to pass them,
			  but using modulus giving me for all numbers of the list a reminder, then this number can pass all these numbers
			  of the list.
"""

def avoidObstacles(inputArray):
    """Return smallest number needed to bypass all elements in an array that represents a number line.
       Note: you start from Zero."""
    
    # Trying i steps from 1 to maximum value of the input array.
    for i in range(1,max(inputArray)):
        
        # Return False for smallest i that returns a reminder for all elements of the array.
        passAllObs = any([x for x in inputArray if not x%i])
        
        # Return the number
        if not passAllObs:
            return i
        
    # Return a number more that the largest element in the array by 1.    
    return max(inputArray)+1    


"""
Elon Musk's First Principle Approach:
	. Musk: Well, I do think there’s a good framework for thinking. It is physics. You know, the sort of first principles
	  reasoning.  Generally I think there are — what I mean by that is, boil things down to their fundamental truths and reason up from there, as opposed to reasoning by analogy.
      Through most of our life, we get through life by reasoning by analogy, which essentially means copying what other people do with slight variations.

      . In layman’s terms, first principles thinking is basically the practice of actively questioning every assumption you think 
        you ‘know’ about a given problem or scenario — and then creating new knowledge and solutions from scratch. Almost like a newborn baby.

      . Remember Avoid obstacles problem you solved on code signal website, The solution using first principle thinking is I need 
        a way to jump a number of steps to pass all numbers without touching them, the best way to use the modulus operator, and list which give a reminder for all numbers is one, choose the smallest number of steps and you've got yourself a solution using first principle thinking.

      . People who reason by analogy tend to make bad decisions, even if they’re smart.

	  STEP 1: Identify and define your current assumptions.
	  STEP 2: Breakdown the problem into its fundamental principles.
	  STEP 3: Create new solutions from scratch.  
"""
