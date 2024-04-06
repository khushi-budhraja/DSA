class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_prod = 1
        max_prod = float("-inf")
        for n in nums:
            curr_prod *= n
            if curr_prod > max_prod:
                max_prod = curr_prod
            if curr_prod == 0:
                curr_prod = 1
        curr_prod = 1
        for i in range(len(nums)-1,-1,-1):
            curr_prod *= nums[i]
            if curr_prod > max_prod:
                max_prod = curr_prod
            if curr_prod == 0:
                curr_prod = 1
        return max_prod

obj = Solution()
print(obj.maxProduct([3,-1,4]))
