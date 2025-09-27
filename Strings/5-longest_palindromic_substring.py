'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
'''
#
# class Solution:
#     def longestPalindrome(self, s : str) -> str:
#         max_length = 0
#         ans = ""
#
#         def isPalindrome(s : str) -> bool:
#             return s == s[::-1]
#
#         for a in range(len(s)):
#             for b in range(a, len(s)):
#                 if isPalindrome(s[a:b+1]) and b-a+1 > max_length:
#                     max_length = b-a+1
#                     ans = s[a:b+1]
#         return ans 
#

class Solution:
    def longestPalindrome(self, s : str) -> str:
        # check if every element can be the center of a palindromic substring 
        ans = ""
        
        def expand(l : int, r : int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l+1:r]

        for index in range(len(s)):  
            odd = expand(index, index)
            even = expand(index, index + 1)
            
            longer = odd if len(odd) > len(even) else even

            if len(longer) > len(ans):
                ans = longer
            
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad")) # bab / aba
    print(s.longestPalindrome("cbbd")) # bb 

