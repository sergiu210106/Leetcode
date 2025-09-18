'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the
value to go outside the signed 32-bit integer range [-2^31, 2^31-1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''
class Solution:
    def reverse(self, x: int) -> int:
        max_value = (1 << 31) - 1
        min_value = -1*(1<<31)

        print(max_value)

        ans = 0
        sign = (x >= 0)
        x = abs(x)
        while x != 0:
            if ans > max_value // 10:
                return 0
            digit = x % 10
            ans = ans * 10 + digit
            x //= 10
        if sign:
            return ans
        else:
            return -1*ans if min_value <= -1*ans <= max_value else 0

# easy solution

class Solution:
    def reverse(self, x : int) -> int:
        max_value = (1<<31) - 1
        min_value = -1*(1<<31)

        x = int(str(x)[::-1]) if x >= 0 else -1*int(str(x)[::-1][:1])
        return x if min_value <= x <= max_value else 0
if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))
