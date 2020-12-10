def findValueSortedShiftedArray(nums, target):
    
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # else:
    #     return -1
        
# not a binary search, need to revisit

    left = 0
    right = len(nums) -1

    while left < right:
        mid = ((right - left) // 2) + left
        
        if nums[mid] > nums[left]:
            left = mid
        else:
            right = mid
            
            if left + 1 == right:
                return right