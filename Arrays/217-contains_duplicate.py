'''
217. Contains Duplicate 

Given an integer nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
'''

from typing import List 

class Solution:
    def containsDuplicate(self, nums : List[int]) -> bool:
        values = set()
        for number in nums:
            if number in values:
                return True 
            values.add(number)
        
        return False
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))
    print(solution.containsDuplicate([1,2,3,4]))