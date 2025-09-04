'''
1768. Merge Strings Alternately

You are given 2 strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. 

Return the merged string.

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merge the strings like merging arrays
        
        answer_string = ""
        i = 0
        min_len = min(len(word1), len(word2))
        while i < min_len:
            answer_string += word1[i] + word2[i]
            i += 1

        while i < len(word1):
            answer_string += word1[i]
            i += 1

        while i < len(word2):
            answer_string += word2[i]
            i += 1

        return answer_string

