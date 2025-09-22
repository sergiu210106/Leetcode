'''
3005. Count Elements with maximum frequency

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurences of that element in the array.
'''

class Solution:
    def maxFrequencyElements(self, nums : list[int]) -> int:
        frequency = dict()

        maximum_frequency = 0
        count = 0
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    
        for value in frequency.values():
            if value > maximum_frequency:
                count = 1
                maximum_frequency = value
            elif value == maximum_frequency:
                count += 1
        return count * maximum_frequency



if __name__ == '__main__':
    solution = Solution()
    print(solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
