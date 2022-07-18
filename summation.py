class Solution:
    result = []
    def sum_2_no(self,nums:list,target:int):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j] == target) & (i != j):
                    part = []
                    part.append(nums[i])
                    part.append(nums[j])
                    if part[::-1] not in self.result:
                        self.result.append(part)
        return self.result

sol = Solution()
print(sol.sum_2_no([-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,0],6))
