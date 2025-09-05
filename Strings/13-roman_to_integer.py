'''
13. Roman to Integer
Convert a string from roman to integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        answer = 0
        for i in range(len(s)):
            if i == len(s) - 1 or roman_to_int_dict[s[i]] >= roman_to_int_dict[s[i+1]]:
                answer += roman_to_int_dict[s[i]]
            else:
                answer -= roman_to_int_dict[s[i]]
        
        return answer