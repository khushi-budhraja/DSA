nums = [1,5,0,2,2,4]

class Solution:
    def canJump(self,nums):
        n = len(nums)
        goal = n-1
        for i in range(n-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

obj = Solution()
print(obj.canJump(nums))