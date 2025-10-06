'''
202. Happy Number

Write an algorithm to deetermine if a number 
n is happy. A happy number is a number defined
by the following process:
    - Starting with any positive integer, replace
    the number by the sum of the squares of
    digits. 
    - Repeat the process until the number equals
    1 (where it will stay), or it loops endlessly
    in a cycle which does not include 1.
    - Those numbers for which this process ends in 
    1 are happy.
    - Return true if n is happy, false if not.
'''

class Solution:
    def isHappy (self, n : int) -> bool:
        '''
        function for determining the sum of the squares of a number for easier work.
        '''
        def sum_squares(x : int) -> int:
            ans = 0
            while x != 0:
                ans += (x % 10) * (x % 10)
                x //= 10
            
            return ans
        
        # first idea, keep track of numbers using a set
        # number_set = set()
        # number_set.add(n)
        # current_value = n 
        # while True:
        #     next_value = sum_squares(current_value)
            
        #     if next_value in number_set:
        #         return next_value == 1
            
        #     current_value = next_value
        #     number_set.add(current_value)
        
        # second idea, fast & slow pointers
        # slow = n
        # fast = sum_squares(n)
        
        # while slow != fast:
        #     if fast == 1:
        #         return True 
            
        #     slow = sum_squares(slow)
        #     fast = sum_squares(sum_squares(fast))
            
        # return slow == 1
        
        # third idea : 4 bad cycle
        
        current = n 
        while current != 1 and current != 4:
            current = sum_squares(current)
            
        return current == 1
        
            
if __name__ == '__main__':
    solution = Solution()
    print("Expected : true -> ", solution.isHappy(19))
    print("Expected : false -> ", solution.isHappy(2))
    
