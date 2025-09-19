'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel spreadsheet, return its corresponding column number.

A -> 1
B -> 2
C -> 3
...
Z -> 26

AA -> 27
AB -> 28
...

'''
# recursive solution
#class Solution
#     def titleToNumber(self, columnTitle: str) -> int:
#         if columnTitle == "":
#             return 0
#
#         return self.titleToNumber(columnTitle[:-1]) * 26 + ord(columnTitle[-1]) - ord('A') + 1
#
# iterative / classical solution
class Solution:
    def titleToNumber(self, columnTitle : str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + ord(ch) - ord('A') + 1
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber("ZY")) # 701
