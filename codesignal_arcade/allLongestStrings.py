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

    # this problem gave an array of strings and asked you return the string that had the largest length