'''
169. Majority Element

Given an array nums, return the majority element.
The majority element is the element that appears more than
[n / 2] times in the array.
'''

from typing import List 

class Solution:
    def majorityElement(self, nums : List[int]) -> int:
        candidate = None 
        count = 0
        
        for number in nums:
            if count == 0:
                candidate = number
                count = 1
            elif number != candidate:
                count -=1
            else:     
                count += 1
        
        return candidate 
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    