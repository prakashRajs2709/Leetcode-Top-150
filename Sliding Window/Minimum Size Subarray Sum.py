from typing import List
class Solution:
    def minSubArrayLen(self, nums: List[int], target) -> int:
        min_len = float('inf')
        left = 0
        cur_sum = 0
        n = len(nums)
        for i in range(n):
            cur_sum += nums[i]
            while cur_sum >=target:
                min_len = min(min_len,i - left+1)
                cur_sum-=nums[left]
                left=left+1

        return 0 if min_len==float('inf') else min_len
    
sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
