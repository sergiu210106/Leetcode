'''
976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle
with a non-zero area, formed from three of these lengths. If it is 
impossible to form any triangle of a non-zero area, return 0.
'''

# class Solution:
#     def largestPerimeter(self, nums : list[int]) -> int:
#         n = len(nums)
#
#         def check(a : int, b : int, c : int) -> int:
#             '''
#             returns the perimeter if a,b,c form a triangle else 0
#             '''
#
#             return a + b + c if a < b + c and b < a + c and c < a + b else 0 
#
#         ans = 0
#         for a in range(n):
#             for b in range(a + 1, n):
#                 for c in range(b + 1, n):
#                     value = check(nums[a], nums[b], nums[c])
#
#                     ans = max(value, ans)
#
#         return ans 
#
#

class Solution:
    def largestPerimeter(self, nums : list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

if __name__ == '__main__':
    solution = Solution() 
    print('Expected : 5', solution.largestPerimeter([2, 1, 2]))
    print('Expected: 0', solution.largestPerimeter([1, 2, 1, 10]))

    print('Done')
