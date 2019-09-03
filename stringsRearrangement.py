# This solution is by andrew_pudge: Amazing solution.
"""What did you learn from this problem?
   => Your idea where all your assumption is built on, might be wrong. TroubleShooting will tell you"""
import itertools

def stringsRearrangement(inputArray):

    def f(x,y):
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        if c == 1:
            return True
        return False
    
    
    for k in itertools.permutations(inputArray, len(inputArray)):
        r = True
        for i in range(len(k)-1):
            if not f(k[i], k[i+1]):
                r = False
        if r: 
            return True
        
    return False




# This solution is by: https://github.com/emirot/codesignal/blob/master/intro/stringsRearrangement.py

import itertools


def diff_by_one_charcter(a, b):
    if len(a) != len(b):
        return False
    if a == b:
        return False
    count = 0
    for z, y in zip(a, b):
        if z != y:
            count += 1
    if count == 1:
        return True
    return False


def stringsRearrangement(inputArray):
    all_perm = itertools.permutations(inputArray)
    all_perm = [i for i in all_perm]
    for sub_arr in all_perm:
        i = 0
        good = True
        while i < len(sub_arr)-1:
            if not diff_by_one_charcter(sub_arr[i], sub_arr[i + 1]):
                good = False
                break
            i += 1
        if good:
            return True
    return False

# My solution works fine except for test6, and I don't know why.
""" What did you learn from implementing this code beside the first principle approach.
    . Every code has BULLET processes has to be done for it to work.
    . First Write this BULLET processes, make sure they work, then figure out a way to connect them or scale them
      to the size of the code."""
# Just put the while loop in this code, and it will be complete, just make sure from the website.
# We have a problem with test6, test7 and test3.

def checking(checkThisList):
    """Returns True if preceding elements in a string list differ by one character or less, and returns False otherwise"""

    # Base condition for the while loop.
    startE = checkThisList[0]
    endE = checkThisList[len(checkThisList)-1]
    print(startE,endE)


    # <List validity variable>
    # Equals <len(checkThisList)-1> when input list finishes comparing between all of its elements to return the boolean True.
    checkFinish = 0


    while (True):


        # First for Loop: <for loop> for swapping elements.
        for ee in range(0,len(checkThisList)-1):
            print(f"index of the first loop: {ee}")
            print(checkThisList)

            # Second for loop: Loop Though elements of the list.
            for e in range(0,len(checkThisList)-1):

                # Counter of Different Characters between two perceding elements in the list.
                count = 0

                # For debugging purposes.
                print(f"This is '{checkThisList[e]}' with index: {e}")

                # Compare between sorted characters of each element in order.
                for c1,c2 in zip(checkThisList[e],checkThisList[e+1]):

                    # Check if the two consecutive pair of strings are identical.
                    if checkThisList[e] == checkThisList[e+1]:
                        count = count + len(checkThisList[e]) + 1
                        continue

                    if c1 == c2:
                        pass
                    else:
                        print("different characters")
                        count = count + 1

                # Here: finished comparing between two elements only not all the list.
                if count < 2:
                    checkFinish = checkFinish + 1
                # For debugging purposes.
                else:
                    print("More than one character is different")
                #"Still doing somethin here"

            #Here: I finished comparing the whole list. Result of The check process.
            print(f"this is checkFinish varaiable value: {checkFinish}")
            if checkFinish == len(checkThisList)-1:
                print("This list configuration is OF THE HOOK!")
                return True
            else:
                print("This list SUCKS!")
                print()

            # Reset list validity variable for the next iteration.
            checkFinish = 0

            # Swap elments according to the first for loop control.
            checkThisList[ee], checkThisList[ee+1]= checkThisList[ee+1], checkThisList[ee]
            

        if checkThisList[0]==startE and checkThisList[len(checkThisList)-1]==endE:
            break

    print("We reached the end of the line!")
    return False




# Main list and it copy.
alpha =  ["abc", 
 "bef", 
 "bcc", 
 "bec", 
 "bbc", 
 "bdc"]
beta = alpha
checking(alpha)
"""Why when I do this it doesn't work?
    if alpha == beta:
        do something"""


# This solution is by needmoarcode
from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False

