'''
3516. Find Closest Person

You are given three integers x, y and z, representing the positions of three people on a number line.
    - x is the position of Person 1
    - y is the position of Person 2
    - z is the position of Person 3 
Both Person 1 and Person 2 move toward Person 3 at the same speed.
Determine which person reaches Person 3 first:
    - Return 1 if Person 1 arrives first.
    - Return 2 if Person 2 arrives first.
    - Return 0 if they arrive at the same time.
'''

class Solution:
    def findClosest(self, x : int, y : int, z : int) -> int:
        def distance(a : int, b : int) -> int:
            return a - b if a > b else b - a
        
        distance_person1 = distance(x, z)
        distance_person2 = distance(y, z)

        if distance_person1 == distance_person2:
            return 0
        elif distance_person1 < distance_person2:
            return 1 
        else:
            return 2

if __name__ == '__main__':
    solution = Solution()
    print(solution.findClosest(2, 7, 4))
