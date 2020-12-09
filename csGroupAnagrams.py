def csGroupAnagrams(strs):
    # need to store anagrams
    
    anagrams = {}
    
    for i in strs:
        sortedWord = ''.join(sorted(i))
        # sorting the anagram as a string
        if sortedWord in anagrams:
            anagrams[sortedWord].append(i)
            # appending the unsorted word
        else:
            anagrams[sortedWord]=[i]
            # adding the anagram as a key if it doesn't exist
    
    results = []
    
    for k, v in anagrams.items():
        results.append(v)
    return results