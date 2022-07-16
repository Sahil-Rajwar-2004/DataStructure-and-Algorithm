result = []

class Solution:
    def summation(self,nums:list,target:int):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]+nums[j] == target:
                    part = []
                    part.append(nums[i])
                    part.append(nums[j])
                    result.append(part)
                    part = []
        return result

add = Solution()
print(add.summation([2,7,11,15],9))
