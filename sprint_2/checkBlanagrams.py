# in this you'll need to reverse word2
# word2 = word2[::-1]
# then iterate over the strings to make sure chars match. Implement a counter to track different chars. If > 1 return False

def checkBlanagrams(word1, word2):
    
    if len(word1 + word2) < 3 and word1 == word2:
        return False
    sort1 = sorted(word1)
    sort2 = sorted(word2)
    print(sort1)
    print(sort2)
    
    count = 0
    startIdx = 0

    for i in range(len(sort1)):
        if sort1[i] != sort2[i]:
            count +=1
            startIdx = i + 1
            break
            
    for j in range(startIdx, len(sort2)):
        if sort2[j] != sort1[j-1]:
            count +=1
 
 
    print(startIdx)
    print(count)
    
    if count > 2:
        return False
    else:
        return True