def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    # print('right', right)
    # print('left', left)
    return sum(map(int, left)) == sum(map(int, right)

# this question gives a string of digits, it's asking you to check to see if the # of digits on either side is even or odd. If odd, it's not lucky if even, it is lucky.