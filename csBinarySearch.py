def csBinarySearch(nums, target):
    min = 0
    max = len(nums) - 1
    
    while not max < min:
        # our guess is the number at the index in the middle of the list rounded to the nearest whole
        guess = (max + min) // 2
        
        # if our number at the guess index is the target, return the guess index
        if nums[guess] == target:
            return guess
        
        # the value at our guess index was less than our target, we add 1 to our min index to move right across the nums list   
        elif nums[guess] < target:
            min = guess + 1
        # otherwise, we move left 
        else:
            max = guess - 1
    # if we've made it through the whole list and not found the target, return -1 
    return -1