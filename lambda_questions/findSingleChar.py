def csFindTheSingleNumber(nums):
    # if len(nums) == 0:
    #     return None
    # elif len(nums) == 1:
    #     return nums[0]
    # else:
    #     return (3 * sum(set(nums)) - sum(nums)) / 2
        
    
    
    n = len(nums)
    nums.sort()
    
    unique = []
    
    # need to account for an empty list
    if len(nums) == 0:
        return None
    # need to account for a list with a single element   
    if len(nums) == 1:
        return nums[0]
    
    # check the first character of our sorted list to see if it's unique
    if nums[0] != nums[1]:
        unique.append(nums[0])
    
    # check all our middle chars to see if they're unique   
    for i in range(1, n - 1):
        if (nums[i] != nums[i+1] and nums[i] != nums[i-1]):
            unique.append(nums[i])
    
    # check the last character of our sorted list to see if it's unique    
    if nums[n-2] != nums[n -1]:
        unique.append(nums[n-1])
    
    # since we're guranteed only a single unique char, return the 0 index of unique
    return unique[0]