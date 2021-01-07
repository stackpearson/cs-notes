def first_not_repeating_character(s):
    
    # need to keep track of all our characters
    charCount = {}
    
    # need to determine what chars are duplicates, so return all chars where count =1
    for i in s:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1
        # print('charCount', charCount)
            
    uniqueChars = []
    
    
    for key, value in charCount.items():
        if value == 1:
            uniqueChars.append(key)
            
    if uniqueChars:
        return uniqueChars[0]
    else:
        return '_'