class Solution:
    def jump(self,nums):
        farthest_jump = 0
        min_jump_count = 0                # Minimum number of jumps to reach nums[n - 1]
        end_of_jump = 0                   # If (i + nums[i]) == 2, end_of_jump = index 2 (farthest_jump)
        for i in range(len(nums)):
            farthest_jump = max(farthest_jump, i + nums[i])

            if farthest_jump >= len(nums) - 1:
                min_jump_count += 1
                return min_jump_count
            
            if i == end_of_jump:
                min_jump_count += 1
                end_of_jump = farthest_jump
        return min_jump_count

nums = [2,3,1,1,4]
obj = Solution()
print(obj.jump(nums))