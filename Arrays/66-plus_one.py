'''
66. Plus One
You are given a large integer represented as an integer array
digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any 
leading 0s. Increment the large integer by one and return the
resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        value, carry = (digits[-1] + 1) % 10, (digits[-1] + 1) // 10
        digits[-1] = value

        for i in range(len(digits) - 2, -1, -1):
            value, carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
            digits[i] = value
            if carry == 0:
                break
            
        return digits if carry == 0 else [1] + digits

if __name__ == '__main__':
    s = Solution()
    
    digits = [9, 9, 9]
    print(s.plusOne(digits))
    