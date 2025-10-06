class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        var = 0
        for i in range(len(nums)):
            if cnt == 0:
                var = nums[i]
    
            if var == nums[i]:
                cnt+=1
            else: 
                cnt-=1
        return var