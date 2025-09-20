'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndex-th (0 - indexed) row of Pascal's Triangle.
'''

class Solution:
    def getRow(self, rowIndex : int) -> list[int]:
        last_row = [1]

        for _ in range(rowIndex):
            new_row = [1]
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)

            last_row = new_row

        return last_row

if __name__ == '__main__':
    solution = Solution()

    print(solution.getRow(3))
