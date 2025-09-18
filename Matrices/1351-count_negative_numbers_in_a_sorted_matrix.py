'''
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both 
row-wise and column-wise, return the number of negative numbers in grid.

'''

# easy solution

# class Solution:
#     def countNegatives(self, grid: list[list[int]]) -> int:
#         return sum(num < 0 for row in grid for num in row)

# classic binary search solution

# class Solution:
#     def countNegatives(self, grid: list[list[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])

#         ans = 0            
#         if rows < cols:
#             for i in range(rows):
#                 # search in grid[i] for the biggest index of a positive number
#                 left, right = 0, cols - 1
#                 while left <= right:
#                     m = (left + right) // 2
                    
#                     if grid[i][m] >= 0:
#                         left = m + 1
#                     else:
#                         right = m - 1
#                 print(left)
#                 ans += cols - left
#             return ans

#         for j in range(cols):
#             # search in grid[][j] for the biggest index of a positive number
#             left, right = 0, rows - 1
            
#             while left <= right:
#                 m = (left + right) // 2
                
#                 if grid[m][j] >= 0:
#                     left = m + 1
#                 else:
#                     right = m - 1
            
#             print(left)

#             ans += rows - left
            
#         return ans

# greedy O(n + m)

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # we start from the bottom-left corner and work ourselves up and to the right
        column_index = 0
        ans = 0
        for row_index in range(rows - 1, -1, -1):
            while column_index < cols and grid[row_index][column_index] >= 0:
                column_index += 1
            if column_index < cols:
                ans += cols - column_index
            else:
                break
        return ans
                
        

if __name__ == '__main__':
    solution = Solution()
    arr = [[5,1,0],[-5,-5,-5]]
    print(solution.countNegatives(arr))