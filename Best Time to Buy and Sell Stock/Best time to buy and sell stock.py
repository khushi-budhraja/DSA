class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i]-buy > ans:
                ans = prices[i]-buy
        return ans
    
prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))
