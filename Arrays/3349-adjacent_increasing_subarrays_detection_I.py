'''
Given an array nums of n integers and an integer k, determine wheth
'''

from typing import List 
class Solution:
    def hasIncreasingSubarrays(self, nums : List[int], k : int) -> bool:
        return False 
    
if __name__ == '__main__':
    s = Solution()
    print("Expected: true -> ", s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))
    