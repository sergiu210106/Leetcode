'''
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences
of val in nums in-place. The order of elements may be changed. Then
return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val to 
be k, to get accepted, you need to do the following things:
    - Change the array nums such that the first k elements of nums 
    contain the elements which are not equal to val. The remaining
    elements of nums are not important as well as the size of nums.
    - Return k.
'''

class Solution:
    def removeElement(self, nums : list[int], val : int) -> int:
        # first idea, take two indices from the borders of the array and search for 
        # values equal to val in the beginning of the array and different in the end 
        # of the array, switching them at each step. when the left exceeds the right 
        # index return
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            while left < len(nums) and nums[left] != val:
                left += 1
            while right >= 0 and nums[right] == val:
                right -= 1
                
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                
        k = sum([int(num != val) for num in nums])
        
        return k
        