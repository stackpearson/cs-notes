def uncover_spy(n, trust):
    # need to create a set of people
    people = {}
    
    if len(trust) == 1:
        for pair in trust:
            return pair[1]
    
    for pair in trust:
        if pair[1] in people:
            people[pair[1]] += 1
        else:
            people[pair[1]] = 1
    
    possibleSpies = []        
    for key, value in people.items():
        if value == (n-1):
            possibleSpies.append(key)
        else:
            return -1
            
    if len(possibleSpies) < 2:
        return possibleSpies[0]
    else:
        return -1
    
    print('people', people)       
    print('possibleSpies', possibleSpies)
    