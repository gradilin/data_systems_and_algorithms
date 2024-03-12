def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i-1 
        while temp < nums[j] and j > -1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1  
    return nums


b_list = [8,4,1,3,6,3,2,9,5,7]
print(insertion_sort(b_list))