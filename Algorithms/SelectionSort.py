def selection_sort(nums): 
    # we dont kneed to evaluate the end 
    for x in range(len(nums) -1): 
        i = x + 1 
        min_index = x
        # iterate through remaining values 
        while i < len(nums):
            # check forlowest value
            if nums[i] < nums[min_index]:
                min_index = i 
            i += 1 
        if nums[x] != nums[min_index]: 
            nums[x], nums[min_index] = nums[min_index], nums[x]
    return nums

b_list = [8,4,1,3,6,3,2,9,5,7]
print(selection_sort(b_list))
