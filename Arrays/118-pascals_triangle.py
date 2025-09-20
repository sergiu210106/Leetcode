'''
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's Triangle.
'''

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]

        for _ in range(numRows - 1):
            last_row = ans[-1]
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)
            ans.append(new_row)
        
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
