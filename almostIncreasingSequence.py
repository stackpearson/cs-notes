def almostIncreasingSequence(sequence):
    # traverse array looking for nums > than num[i+1]
    # if we find one
    
    i = 1
    count = 0
    prev = float('-inf')
    while i < len(sequence):
        print(sequence[i])
        if sequence[i-1] >= sequence[i]:
            count +=1
            if sequence[i] < prev:
                return False
        prev = sequence[i-1]
        i += 1
    
    print('count: ', count)
    if count > 1:
        return False
    else:
        return True