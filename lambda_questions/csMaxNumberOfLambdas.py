def csMaxNumberOfLambdas(text):
    # a = 2
    # b = 1
    # d = 1
    # m = 1
    
    a = 0
    b = 0
    d = 0
    m = 0
    
    for i in range(len(text)):
        if text[i] == 'a':
            a +=1
        elif text[i] == 'b':
            b +=1
        elif text[i] == 'd':
            d +=1
        elif text[i] == 'm':
            m +=1
            
    print('a: ',a)
    print('b: ',b)
    print('d: ',d)
    print('m: ',m)
    
    # need to return the char with the lowest # of occurences since b,d & m are all needed once
    # print('min',min(b,d,m))
    lowest = min(b,d,m)
    
    if (lowest/a) >= .5:
        return lowest
    else:
        return 0