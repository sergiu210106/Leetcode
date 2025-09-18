'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return -1

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    print(solution.search(nums, target))
