def fibonacciSimpleSum2(n):
    fib_numbers = generate_fibonacci(n)
    print(fib_numbers)
    fib_numbers = set(fib_numbers) # O(len(fib_numbers)) time and space 
    # loop for all numbers
    for first in fib_numbers:  # This is O(len(fib_numbers)) = O(log n) because fib numbers almost double each iteration
        # # "fix" a first number
        # # loop through the rest
        # for second in fib_numbers:  # O(len(fib_numbers))
        #     # try adding them together and see if the sum == n
        #     if first + second == n: 
        #         return True
        # # Instead of doing a linear search, we could do a binary search, 
        # # where we guess the middle, if the sum of the two numbers is > n, look left,
        # # else if sum < n, look right and repeat until we find a a number 
        diff = n - first
        # does diff exist in fib_numbers? 
        if diff in fib_numbers:  # this is O(1) lookup in a set
            return True
    return False
# helper function to generate fibonacci numbers
# only go up to n
def generate_fibonacci(n): 
    # F(n) = F(n - 1) + F(n - 2)
    # F(0) = 0
    # F(1) = 1
    fib_numbers = [0, 1] # Create a list with two elements, 0 and 1
    cur_fib_number = 1
    # keep generating fib numbers until the next fib number is > n
    while cur_fib_number <= n: 
        fib_numbers.append(cur_fib_number)
        cur_fib_number = fib_numbers[-1] + fib_numbers[-2]
    return fib_numbers

    # MY VERSION AND NOTES

    def fibonacciSimpleSum2(n):
    # need to find a way to generate fib numbers all the way up to end
    # then need to find a way to access each # we've generated so we can determine if they can sum to n
    fibNums = generateFib(n)
    
    fibNums = set(fibNums)
    
    # need to loop over our set and see if we find a combination of numbers that sums to n
    # if we do, then n can be represented by the sum of 2 fib numbers
    for firstNum in fibNums:
        for secondNum in fibNums:
            if firstNum + secondNum == n:
                return True
    
    # if we've made it through the entire set and no numbers sum to n, then return false
    return False

# need to generate our fib numbers to recurse through
def generateFib(n):
    # initiate first fib sequence of 0 and 1, then programatically make the rest of them
    fibNums = [0, 1]
    #set where we're going to start generating the next fib #
    newFibNum = 1
    
    while newFibNum <= n:
        fibNums.append(newFibNum)
        # F(n) = F(n-1) + F(n-2)
        # next fib number = last fib # in the list + 2nd to the last fib # in the list
        # for [0, 1] f = 0 + 1  = 1
        # for [0, 1, 1] f = 1 + 1 or 2
        # for [0, 1, 1, 2] f = 1 + 2 or 3 etc etc
        newFibNum = fibNums[-1] + fibNums[-2]
    return fibNums