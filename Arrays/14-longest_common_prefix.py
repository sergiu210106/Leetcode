'''
14. Longest Common Prefix

Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # first idea, check on every position from the start of each 
        # word and stop when they dont match
        
        # get stopping point
        min_length = min([len(s) for s in strs])
        ans = ""
        for i in range(min_length):
            ok = True
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    ok = False
                    break
            if ok:         
                ans += strs[0][i]
            else:
                break
        
        return ans
    
