'''
744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is in non-decreasing order, and a
character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than 
target. If such a character does not exist, return the first character in letters.
'''

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            m = (left + right) // 2

            if letters[m] <= target:
                left = m + 1
            else:
                right = m - 1
        
        return letters[left] if left < len(letters) else letters[0]


if __name__ == '__main__':
    letters = ["c","f","j"]
    target = 'c'

    solution = Solution()
    print(solution.nextGreatestLetter(letters, target))
