def csIsomorphicStrings(a, b):
    aLen = len(a)
    bLen = len(b)
    
    if aLen != bLen:
        return False
        
    aDict = {}
    bDict = {}
    
    for aVal, value in enumerate(a):
        aDict[value] = aDict.get(value, []) + [aVal]
        
    for bVal, value in enumerate(b):
        bDict[value] = bDic.get(value, []) + [aVal]
        
    if sorted(aDict.values()) == sorted(bDict.values()):
        return True
    else:
        return False