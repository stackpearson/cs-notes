def first_not_repeating_character(s):

    charCount = {}

    for i in s:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1
            
    # need to return all chrs where count = 1
    
    uniqueChars = []
            
    for key, value in charCount.items():
        if value == 1:
            uniqueChars.append(key)
    
    for j in s:
        if j in uniqueChars:
            return j      
    else:
        return '_'