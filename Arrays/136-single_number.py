'''
136. Single Number
Given a non-empty array of integers, every element appears twice 
except for one. Find that single one.

You must implement a solution with a linear runtime complexity
and only constant extra space.


'''

class Solution:
    def singleNumber(self, nums : list[int]) -> int:
        # idea: xor all elems and use the property that 
        # a ^ a = 0 and 0 ^ x = x 

        ans = 0
        for num in nums:
            ans = ans ^ num

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 1]))
