'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        result = 0

        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            result = max(result, r - l + 1)
        
        return result

