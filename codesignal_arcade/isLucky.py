def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    # print('right', right)
    # print('left', left)
    return sum(map(int, left)) == sum(map(int, right)