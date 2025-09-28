'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters:

    2 - abc
    3 - def
    4 - ghi
    5 - jkl
    6 - mno
    7 - pqrs
    8 - tuv
    9 - wxyz
'''

class Solution:
    def letterCombinations(self, digits : str) -> list[str]:

        letter_map = {
                '2' : 'abc',
                '3' : 'def',
                '4' : 'ghi',
                '5' : 'jkl',
                '6' : 'mno',
                '7' : 'pqrs',
                '8' : 'tuv',
                '9' : 'wxyz' 
                }
        ans = []
        def backtrack(current_string : str):
            if len(current_string) == len(digits):
                ans.append(current_string)
                return 
            for character in letter_map[digits[len(current_string)]]:
                backtrack(current_string + character)
        
        if digits: # without this, if digits = "" the function returns [""] instead of []
            backtrack("")
        return ans

        


if __name__ == '__main__':
    solution = Solution()

    print(solution.letterCombinations('23'))

