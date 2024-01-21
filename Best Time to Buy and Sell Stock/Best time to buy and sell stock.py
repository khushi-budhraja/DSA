class Solution:
    def maxProfit(self, prices):
        size=len(prices)
        max_ = 0
        left = 0
        right = 1
        while right<size:
            if prices[left] >= prices[right]:
                left=right
            elif prices[left] < prices[right] :
                if prices[right]-prices[left] > max_:
                    max_ = prices[right]-prices[left]
            right+=1
        return max_
    
prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))