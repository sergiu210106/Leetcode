'''
1518. Water Bottles
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty water bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
'''

class Solution:
    def numWaterBottles(self, numBottles : int, numExchange : int) -> int:
        numFull = numBottles 
        numEmpty = 0
        
        ans = 0
        while numFull > 0:
            ans += numFull  
            numEmpty += numFull
            numFull = numEmpty // numExchange
            numEmpty = numEmpty % numExchange
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.numWaterBottles(9, 3)) # 13 = 9 + 3 + 1 
