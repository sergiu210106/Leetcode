'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string
and return it. The vowels are a, e, i, o, u, and they can
appear in both lower and upper cases, more than once. 
Ex. "IceCreAm" -> "AceCreIm"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        # take vowels in a string, reverse the string and 
        # then put them back in the appropriate order
        VOWELS = "aeiouAEIOU"
        
        vowels_string = "".join([v for v in s if v in "aeiouAEIOU"])
        i = len(vowels_string) - 1
        idx = 0
        
        answer_string = ""
        while idx < len(s):
            if s[idx] in VOWELS:
                answer_string += vowels_string[i]
                i -= 1
            else:
                answer_string += s[idx]
            
            idx += 1
            
        return answer_string