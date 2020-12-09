def csIsomorphicStrings(a, b):
    aLen = len(a)
    bLen = len(b)
    
    if aLen != bLen:
        return False
        
    dict_a = {}
    dict_b = {}
    
    for i, value in enumerate(a):
        dict_a[value] = dict_a.get(value, []) + [i]
        
    for j, value in enumerate(b):
        dict_b[value] = dict_b.get(value, []) + [j]
        
    if sorted(dict_a.values()) == sorted(dict_b.values()):
        return True
    else:
        return False