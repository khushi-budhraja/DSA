class TwoSum:
    def twoSum(self,nums,target):

        # TC=O(n^2)   SC=O(1)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        #Using Dictionary(HashMap)     TC=O(n)   SC=O(n)
        dct = {}
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [dct[target-nums[i]] , i]
            else:
                dct[nums[i]] = i

        #Two Pointers                  TC=O(n)    SC=O(1)
        nums.sort()
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left] + nums[right] == target:
                return [left,right]
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1

nums = [2,7,11,15]
target = 9
obj = TwoSum()
print(obj.twoSum(nums,target))

