def bubble_sort(nums):
    # we want to bubble up the highest value
    # then we want to bubble up the secodn highest value 
    for i in range(len(nums), 1, -1):
        for x in range(i - 1):
            if nums[x] > nums[x + 1]: 
                nums[x], nums[x + 1] = nums[x + 1], nums[x] 
    print(nums)


#Big O: 
# space complexity: sorted in place but scales with size of list  O(n)
# Time complexity: nested loops means O(n^2) 


b_list = [8,4,1,3,6,3,2,9,5,7]

bubble_sort(b_list)