def depositProfit(deposit, rate, threshold,year=0):
    """Returns Number of years to bypass Threshold amount of money. """
    
    # Return number of years if threshold is pypassed.
    if deposit >= threshold:
        return year
    
    # Add profit if threshold is not bypassed.
    else:
        return depositProfit(deposit+((rate/100)*deposit), rate, threshold,year+1)

# -> OR

# This is my first recursion totally by myself: 16/3/2019
year = 0
def depositProfit(deposit, rate, threshold):
    
    global year
    print(year)
    
    if deposit >= threshold:
        return year
    else:
        year = year + 1
        return depositProfit(deposit+((rate/100)*deposit), rate, threshold)

print(f"This is the number of years: {depositProfit(50,25,100)}")

# -> OR
# This solution is by andrew_pudge.
def depositProfit(deposit, rate, threshold):

    return math.ceil(math.log(threshold/deposit, 1+rate/100))