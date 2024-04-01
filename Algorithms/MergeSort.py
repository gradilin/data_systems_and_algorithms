# nums lists must already be sorted 
def merge(nums1, nums2):
    i = 0 
    j = 0 
    combined = [] 
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            combined.append(nums1[i])
            i += 1 
        else: 
            combined.append(nums2[j])
            j += 1
    while i < len(nums1):
        combined.append(nums1[i])
        i += 1  
    while j < len(nums2): 
        combined.append(nums2[j])
        j += 1
    return combined

#
def isSorted(nums): 
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

# recursive function 
def merge_sort(nums_list): 
    if len(nums_list) == 1 or isSorted(nums_list): 
        return nums_list
    
    # break the list down into multiple lists with single values 
    mid_index = len(nums_list) // 2
    # keep breaking down recursively 
    left = merge_sort(nums_list[:mid_index]) 
    right = merge_sort(nums_list[mid_index:]) 

    #merge em again once they get values returned 
    return merge(left, right)

#Big O: 
# space complexity: new list is created doubling the memory consumption O(n)
# Time complexity: breaking down the list into individual lists O(log n), 
#                    however combining them again is O(n) therefore total is O(n * log n)
# only possible sorting algoithm complexity is O(n^2) and O(n log n)is most efficient for sorting multiple types of data 

nums1 = [1,2,5,7,9]
nums2 = [3,4,5,8,12]

nums_long = [3,4,5,8,12,1,2,5,7,9]
print(merge_sort(nums_long))