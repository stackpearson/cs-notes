    words = list(a.split(' '))
    keys = []
    legend = {}
    
    for i in range(len(pattern)):
        keys.append(pattern[i])
    
    if len(words) != len(pattern):
        return False
        
    for i in range(len(words)):
        if keys[i] in legend:
            pass
        else:
            legend[keys[i]] = words[i]
     
    dupKeys = 0
    dupWords = 0       
    for j in range(1, len(keys)):
        if keys[j-1] == keys[j]:
            dupKeys +=1
        if words[j-1] == words[j]:
            dupWords +=1
    
    if dupKeys != dupWords:
        return False
            
    print('dupKeys', dupKeys)
    print('dupWords', dupWords)
            
    expectedOutput = []
            
    for i in range(len(pattern)):
        if keys[i] in legend:
            expectedOutput.append(legend[keys[i]])
        else:
            return False
    
    if words == expectedOutput:
        return True
    else:
        return False
