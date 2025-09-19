'''
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column
title as it appears in an excel sheet.

For example:
    A -> 1 
    B -> 2
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
'''
class Solution:
    def convertToTitle(self, columnNumber : int) -> str:
        if columnNumber == 0:
            return ""
        
        last_character = chr((columnNumber - 1) % 26 + ord('A'))

        return self.convertToTitle((columnNumber - 1) // 26) + last_character


if __name__ == '__main__':

    solution = Solution()
    print(solution.convertToTitle(701))


