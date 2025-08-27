'''
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))