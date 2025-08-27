'''
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should
be kept the same. Then return the number of unique elements
in nums.

Consider the number of unique elements of nums to be k, to get
accepted, you need to do the following things:
    - Change the array nums such that the first k elements of 
    nums contain the unique elements in the order they were 
    present in nums initially. The remaining elements of nums 
    are not important as well as the size of nums.
    
    - Return k.
'''

class Solution:
    def removeDuplicates(self, nums : list[int]) -> int:
        i, j = 0, 0
        
        while j < len(nums):
            if j != 0:
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
                
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
            
            print(i, j)
            
            i += 1
            j += 1

            
        return i
    
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
print(s.removeDuplicates(nums))
print(nums)
