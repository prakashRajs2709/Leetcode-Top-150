from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fp=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=fp:
                fp=i
        return fp==0