'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index 
where it would be inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            m = (left + right) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        
        return left
    
    
if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 6]
    target = 5
    
    print(s.searchInsert(arr, target)) # 2