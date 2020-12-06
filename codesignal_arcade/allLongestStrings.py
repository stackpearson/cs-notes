def allLongestStrings(inputArray):
    # iterate over the list & count the length of each individual string
    
    max = 0
    
    longestStrings = []
    
    for string in inputArray:
        if len(string) >= max:
            max = len(string)
            
    for string in inputArray:
        if len(string) == max:
            longestStrings.append(string)
            
    return longestStrings