'''
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to zero.
'''

class Solution:
    def sumZero(self, n : int) -> list[int]:
        return list(range(1, n)) + [-1*(n-1)*n//2]

if __name__ == '__main__':
    solution = Solution()
    print(solution.sumZero(5))
