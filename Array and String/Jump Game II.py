from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        boundary = 0
        max_reach = 0
        min_steps = 0
        i = 0
        while boundary<len(nums)-1:
            while i<=boundary:
                max_reach = max(max_reach,i + nums[i])
                i+=1
            min_steps += 1
            boundary = max_reach
        return min_steps
